from io import BytesIO

import matplotlib.pyplot as plt
import numpy
import numpy as np
import rasterio


def get_region_of_interest(ndre, multiplier=1/2):

    # undo the background adjustment
    region = np.where(ndre == -255, 0, ndre)

    # mean of center rows
    center_row1 = np.mean(region[int(multiplier * len(region))])
    center_row2 = np.mean(region[int(multiplier * len(region)) + 1])

    # mean of both rows
    mean = (center_row1 + center_row2) / 2
    return round(mean, 3)


def get_ndre(red_file, nir_file):
    with rasterio.open(red_file) as band_red:
        red = band_red.read(1).astype('float64')

    with rasterio.open(nir_file) as band_nir:
        nir = band_nir.read(1).astype('float64')

    np.seterr(divide='ignore', invalid='ignore')
    # ndre calculation, empty cells or nodata cells are reported as 0
    ndre = np.where((nir == 0.) | (red == 0.), -255, np.where((nir + red) == 0., 0, (nir-red) / (nir+red)))

    return ndre


def ndre_calculator(B07, B8A, saving_file_name):

    with rasterio.open(f'{B07}') as src:
        band_red = src.read(1)

    with rasterio.open(f'{B8A}') as f:
        band_nir = f.read(1)

    # Allow division by zero
    numpy.seterr(divide='ignore', invalid='ignore')

    # # Calculate ndre
    ndre = (band_nir.astype(float) - band_red.astype(float)) / (band_nir + band_red)

    min_value = numpy.nanmin(ndre)
    max_value = numpy.nanmax(ndre)
    mid = 0.1

    fig = plt.figure(figsize=(75, 25))
    ax = fig.add_subplot(111)

    cmap = 'BrBG'
    cax = ax.imshow(ndre, cmap=cmap, clim=(min_value, max_value), vmin=min_value, vmax=max_value)

    ax.axis('off')

    f = BytesIO()

    plt.savefig(f'./media/{saving_file_name}.png', format='png', transparent=True, bbox_inches='tight')
    plt.close()


def average_ndre(red_file, nir_file):
    return get_region_of_interest(get_ndre(red_file=red_file, nir_file=nir_file))
