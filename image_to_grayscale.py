import numpy as np
# import matplotlib.pyplot as plt

from PIL import Image


def rgb2gray(rgb):
    return np.dot(rgb[...], [0.2989, 0.5870, 0.1140])


def convert(img: Image, width: int, height: int):
    pixels = np.array([[np.dot(img.getpixel((x, y)), [0.2989, 0.5870, 0.1140, 1])
                        for x in range(img.width)]
                       for y in range(img.height)])
    # temp = rgb2gray(pixels)
    gray = np.zeros((height, width))
    for i in range(len(pixels)):
        for j in range(len(pixels[0])):
            gray[i][j] = pixels[i][j]

    # plt.imshow(gray, cmap=plt.get_cmap('gray'), vmin=0, vmax=1)
    # plt.show()

    gray /= 510  # I need the data pixels between 0 and 1
    return gray
