from osgeo import gdal
from rest_framework.serializers import ModelSerializer

from indexes.models import NDVIIndex


class NDVISerializer(ModelSerializer):
    class Meta:
        model = NDVIIndex
        fields = '__all__'

    def ndvi_calculator(self, B04, B8A):
        import matplotlib.pyplot as plt
        import numpy
        from io import BytesIO
        import rasterio
        from django.core.files.base import ContentFile

        with rasterio.open(f'./media/{B04}') as src:
            band_red = src.read(1)

        with rasterio.open(f'./media/{B8A}') as f:
            band_nir = f.read(1)

        # Allow division by zero
        numpy.seterr(divide='ignore', invalid='ignore')

        # # Calculate NDVI
        ndvi = (band_nir.astype(float) - band_red.astype(float)) / (band_nir + band_red)

        min_value = numpy.nanmin(ndvi)
        max_value = numpy.nanmax(ndvi)
        mid = 0.1

        fig = plt.figure(figsize=(20, 10))
        ax = fig.add_subplot(111)

        cmap = plt.cm.YlGn
        cax = ax.imshow(ndvi, cmap=cmap, clim=(min_value, max_value), vmin=min_value, vmax=max_value)

        ax.axis('off')

        f = BytesIO()

        plt.savefig(f, format='png', transparent=True)
        content_file = ContentFile(f.getvalue())
        return content_file

    def remove_file(self, deleting_path):
        import os
        if os.path.isfile(deleting_path):
            os.remove(deleting_path)

    def create(self, validated_data):
        obj = NDVIIndex.objects.create(
            coordinates=validated_data['coordinates']
        )
        geo = NDVIIndex.objects.get(id=obj.id)
        my_file = geo.coordinates.name
        B04 = my_file.replace('coordinates_geojson/', 'B04')
        B04 = B04.replace('geojson', 'tiff')
        B8A = my_file.replace('coordinates_geojson/', 'B8A')
        B8A = B8A.replace('geojson', 'tiff')

        with open(f'./media/{geo.coordinates}', 'r') as file:
            my_coordinates = file.read()

        inputpath_B8A = "./B8A.tiff"
        outputpath_B8A = f"./media/{B8A}"

        cropped_file_B8A = gdal.Warp(destNameOrDestDS=f'{outputpath_B8A}',  # TODO fix the saving place
                                     srcDSOrSrcDSTab=inputpath_B8A,  # TODO fix the input file place
                                     cutlineDSName=f'{my_coordinates}',  # TODO input have to be json
                                     cropToCutline=True,
                                     copyMetadata=True,
                                     dstNodata=0)
        inputpath_B04 = "./B04.tiff"
        outputpath_B04 = f"./media/{B04}"

        cropped_file = gdal.Warp(destNameOrDestDS=f'{outputpath_B04}',  # TODO fix the saving place
                                 srcDSOrSrcDSTab=inputpath_B04,  # TODO fix the input file place
                                 cutlineDSName=f'{my_coordinates}',  # TODO input have to be json
                                 cropToCutline=True,
                                 copyMetadata=True,
                                 dstNodata=0)
        obj.ndvi_image.save('ndvi.png', self.ndvi_calculator(B04=B04, B8A=B8A))

        self.remove_file(outputpath_B04)
        self.remove_file(outputpath_B8A)

        return obj
