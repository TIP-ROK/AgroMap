import json
import random
import time
from datetime import datetime

from django.db import connection
from osgeo import gdal, osr
import os

from gip.views.handbook_contour import contour_test_for_ai
from indexes.models.satelliteimage import SciHubImageDate
import rasterio
import numpy as np
from ai.models import Contour_AI, Images_AI, Yolo
from ultralytics import YOLO
from PIL import Image
from pyproj import Proj, Transformer
from pyproj.transformer import transform as trnsfrm
from django.contrib.gis.geos import Polygon, GEOSGeometry
import matplotlib.pyplot as plt
import pandas as pd


def merge_bands():
    # Фильтруем объекты SciHubImageDate по ID и загружаем изображения
    satellite_images = SciHubImageDate.objects.filter(id__in=[154, 155])

    for image in satellite_images:
        time.sleep(2)
        path = 'media/'
        files = [
            path + f"{image.B02}",  # Синий
            path + f"{image.B03}",  # Зеленый
            path + f"{image.B04}",  # Красный
        ]

        # Открываем первый файл из списка для получения метаданных
        with rasterio.open(files[0]) as src:
            meta = src.meta
            meta.update(count=len(files))  # Устанавливаем количество каналов в метаданных
            meta.update(driver="GTiff")  # Устанавливаем тип драйвера в метаданных

        # Создаем выходной файл с помощью метаданных и записываем в него данные из всех файлов
        output_file = f"media/Merge_Bands/ID={image.pk}_DATE={datetime.fromisoformat(str(image.date)).strftime('%Y-%m-%d')}.tif"
        with rasterio.open(output_file, "w", **meta) as dst:
            for id, layer in enumerate(files, start=1):
                with rasterio.open(layer) as src:
                    dst.write(src.read(1), id)


def create_rgb():
    time.sleep(8)
    merge_bands_list = os.listdir('media/Merge_Bands')

    for band_rgb in merge_bands_list:
        # Открываем входной файл с помощью Rasterio
        with rasterio.open(f'media/Merge_Bands/{band_rgb}') as src:
            # Читаем каналы красного, зеленого и синего цветов
            red = src.read(3)
            green = src.read(2)
            blue = src.read(1)

            # Масштабируем значения пикселей до диапазона от 0 до 255
            red = np.interp(red, (red.min(), red.max()), (0, 255)).astype('uint8')
            green = np.interp(green, (green.min(), green.max()), (0, 255)).astype('uint8')
            blue = np.interp(blue, (blue.min(), blue.max()), (0, 255)).astype('uint8')

            # Создаем RGB изображение, объединив каналы в одно изображение
            rgb = np.dstack((red, green, blue))

            # Получаем метаданные из исходного файла и обновляем количество каналов и тип данных
            meta = src.meta.copy()
            meta.update(count=3, dtype='uint8')

            # Записываем RGB изображение в новый файл в формате GeoTIFF
            with rasterio.open(f"media/RGB/RGB_{band_rgb}", 'w', **meta) as dst:
                dst.write(rgb.transpose(2, 0, 1))


def cut_rgb_tif():
    time.sleep(8)
    rgb_tif_list = os.listdir('media/RGB')
    for rgb_tif in rgb_tif_list:
        input_file = os.path.join('media/RGB', rgb_tif)

        # Открываем входной файл с помощью GDAL
        ds = gdal.Open(input_file)
        if ds is not None:
            band = ds.GetRasterBand(1)
            xsize = band.XSize
            ysize = band.YSize

            out_path = 'media/cutted_tiff/'
            output_filename = f"tile_"

            tile_size_x = 256
            tile_size_y = 256

            # Обрезаем изображение на тайлы
            for i in range(0, xsize, tile_size_x):
                for j in range(0, ysize, tile_size_y):
                    output_file = os.path.join(out_path,
                                               output_filename + str(i) + "_" + f"{random.randint(1, 10000)}" + str(
                                                   j) + f"{random.randint(1, 10000)}" + ".tif")
                    com_string = f"gdal_translate -of GTIFF -srcwin {i}, {j}, {tile_size_x}, {tile_size_y} {input_file} {output_file}"
                    os.system(com_string)

        else:
            print(f"Не удалось открыть файл: {rgb_tif}")


def yolo():
    file = Yolo.objects.get(id=1)
    model = YOLO(f'media/{file.ai}')
    cutted_files = os.listdir('media/cutted_tiff')

    for file in cutted_files:
        ds = gdal.Open(f"media/cutted_tiff/{file}", gdal.GA_ReadOnly)

        proj = osr.SpatialReference(wkt=ds.GetProjection())
        proj_wgs84 = osr.SpatialReference()
        proj_wgs84.ImportFromEPSG(4326)
        transform = osr.CoordinateTransformation(proj, proj_wgs84)

        ulx, xres, xskew, uly, yskew, yres = ds.GetGeoTransform()
        lrx = ulx + (ds.RasterXSize * xres)
        lry = uly + (ds.RasterYSize * yres)

        ul_lon, ul_lat, _ = transform.TransformPoint(ulx, uly)
        lr_lon, lr_lat, _ = transform.TransformPoint(lrx, lry)

        coords = [
            [[ul_lat, ul_lon, ], [ul_lat, lr_lon], [lr_lat, lr_lon], [lr_lat, ul_lon],
             [ul_lat, ul_lon]]]
        geojson = {
            "type": "Polygon",
            "coordinates": coords
        }

        with connection.cursor() as cursor:
            cursor.execute(f"""
                SELECT ST_Intersects('{contour_test_for_ai}'::geography::geometry, '{GEOSGeometry(f"{geojson}")}'::geography::geometry);
            """)
            inside = cursor.fetchall()
        if inside[0][0] == True:
            image = Image.open(f'media/cutted_tiff/{file}')
            results = model.predict(source=image, save=False, conf=0.5, hide_labels=True, line_thickness=1)
            try:
                arrays = results[0].masks.segments
                confs = results[0].boxes.conf
                w, h = image.size
                x = 1 / w
                y = 1 / h
                img = Image.fromarray(results[0].orig_img)
                # plt.imshow(img)
                for i in arrays:
                    df = pd.DataFrame(i)
                    df.loc[len(df)] = ([i[0][0], i[0][1]])
                    plt.plot(df[0] / x, df[1] / y, c="red")
                plt.axis('off')
                plt.savefig(f'media/images/{file[:-4]}.png', transparent=True, bbox_inches='tight', pad_inches=0)
                images = Images_AI.objects.create()
                images.image.save(os.listdir('media/images/')[0],
                                  open(f"media/images/{os.listdir('media/images')[0]}", 'rb'))
                with rasterio.open(f'media/cutted_tiff/{file}') as src:
                    for n in range(0, len(arrays)):
                        coordinates = []
                        for i in arrays[n]:
                            coordinates.append(src.xy(i[1] / x, i[0] / y))
                        coordinates.append(coordinates[0])
                        geojsons = []
                        for i in range(0, len(coordinates)):
                            inProj = Proj(init=f'epsg:{src.crs.to_epsg()}')
                            outProj = Proj(init='epsg:4326')
                            x1, y1 = coordinates[i][0], coordinates[i][1]
                            x2, y2 = trnsfrm(inProj, outProj, x1, y1)
                            geojsons.append([x2, y2])
                        conf = confs[n]
                        geojson = {
                            "type": "Polygon",
                            "coordinates": [geojsons]
                        }
                        poly = GEOSGeometry(f"{geojson}")
                        with connection.cursor() as cursor:
                            cursor.execute(f"""
                            SELECT dst.id FROM gip_district AS dst WHERE ST_Contains(dst.polygon::geography::geometry,
                            '{poly}'::geography::geometry);
                            """)
                            district = cursor.fetchall()[0][0]
                        Contour_AI.objects.create(polygon=poly, percent=conf, district_id=district)

                        # with connection.cursor() as cursor:
                        #
                        #     cursor.execute(f"""
                        #     SELECT SUM(subquery.percent) as total_percent
                        #     FROM (
                        #         SELECT ST_Area(ST_Intersection(scm.polygon::geometry,
                        #         '{poly}'::geography::geometry)) / ST_Area(scm.polygon::geometry) * 100 as percent
                        #         FROM ai_contour_ai as scm
                        #     ) as subquery;
                        #     """)
                        #     # percent = cursor.fetchall()[0][0]
                        #     percent = cursor.fetchall()[0][0]
                        # if round(percent) < 30:
                        #     with connection.cursor() as cursor:
                        #         cursor.execute(f"""
                        #         SELECT dst.id FROM gip_district AS dst WHERE ST_Contains(dst.polygon::geography::geometry,
                        #         '{poly}'::geography::geometry);
                        #         """)
                        #         # district = cursor.fetchall()[0][0]
                        #         district = cursor.fetchall()
                        #         # print(district)
                        #     # Contour_AI.objects.create(polygon=poly, percent=conf, district_id=district)
            except Exception as e:
                print(e)


def deleted_files():
    time.sleep(8)
    merge_bands_dir = "media/Merge_Bands"
    rgb_dir = "media/RGB"

    # Удаление файлов в директории Merge_bands
    for file_name in os.listdir(merge_bands_dir):
        file_path = os.path.join(merge_bands_dir, file_name)
        if os.path.isfile(file_path):
            os.remove(file_path)

    # Удаление файлов в директории RGB
    for file_name in os.listdir(rgb_dir):
        file_path = os.path.join(rgb_dir, file_name)
        if os.path.isfile(file_path):
            os.remove(file_path)
