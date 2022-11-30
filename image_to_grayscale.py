import numpy as np
import matplotlib.pyplot as plt

from PIL import Image


def rgb2gray(rgb):
    return np.dot(rgb[...], [0.2989, 0.5870, 0.1140])


def convert(img: Image, size: int):
    pixels = np.array([[[img.getpixel((x, y))[i] for i in range(3)] for x in range(img.width)] for y in range(img.height)])
    temp = rgb2gray(pixels)
    gray = np.zeros((size, size))
    for i in range(len(temp)):
        for j in range(len(temp[0])):
            gray[i][j] = temp[i][j]

    # plt.imshow(gray, cmap=plt.get_cmap('gray'), vmin=0, vmax=1)
    # plt.show()

    gray /= 255  # I need the data pixels between 0 and 1
    return gray
