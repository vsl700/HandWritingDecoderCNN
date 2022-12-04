import numpy as np

import img_to_text
import image_to_grayscale

import cnn

import os

words = ["Hello", "Yes", "Well", "Library", "Welcome", "Hi", "No", "Apple", "Nope", "So", "High", "Fox", "Box"]
words_for_imgs = []
for word in words:
    words_for_imgs.append(word)
    words_for_imgs.append(word.upper())
    words_for_imgs.append(word.lower())

print(words)
print(words_for_imgs)

dir_list = os.listdir("fonts")
print(dir_list)

images = [img_to_text.convert(words_for_imgs[i], "fonts/" + dir_list[j]) for i in range(len(words_for_imgs)) for j in range(len(dir_list))]
maxWidth = 0
maxHeight = 0
for image in images:
    if image.width > maxWidth:
        maxWidth = image.width

    if image.height > maxHeight:
        maxHeight = image.height

print(maxWidth, maxHeight)

# With each font, each word, according to the data in the 'images' array
word_results = np.array([int(i / 3) for i in range(len(words_for_imgs)) for j in range(len(dir_list))])

grayscale_imgs = np.array(
    [image_to_grayscale.convert(images[i], maxWidth, maxHeight)
     for i in range(len(images))])

print(len(grayscale_imgs))
cnn.begin(grayscale_imgs, word_results)
print(len(grayscale_imgs), "pics")
