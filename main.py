import numpy as np

import img_to_text
import image_to_grayscale

import cnn

import os

words = ["Hello", "Yes", "Well", "Library", "Welcome", "Hi", "No", "Apple", "Nope", "So", "High", "Fox", "Box"]

dir_list = os.listdir("fonts")
print(dir_list)

images = [img_to_text.convert(words[j], "fonts/" + dir_list[i]) for j in range(len(words)) for i in range(len(dir_list))]
# With each font, each word, according to the data in the 'images' array
word_results = np.array([i for i in range(len(words)) for j in range(len(dir_list))])

grayscale_imgs = np.array(
    [image_to_grayscale.convert(images[i], 200)
     for i in range(len(images))])

print(len(grayscale_imgs))
cnn.begin(grayscale_imgs, word_results)
print(len(grayscale_imgs), "pics")
