#!/usr/bin/env python3
from sys import argv
import os
import cv2
import numpy as np

#60 120 5

def dissimilarity(image, char_images):
    return np.sum(np.sum(np.abs(image.astype(int)-char_images.astype(int)), axis=-1), axis=-1)

try:
    image_path = argv[1]
except IndexError:
    print("You need to provide the path of an image, no path provided.")
    raise

#Final height and width
height = int(argv[2])#60
width = int(argv[3])#120

image = cv2.imread(image_path,cv2.IMREAD_GRAYSCALE)
cv2.imshow('Original Image',image)
cv2.waitKey(0)

image = cv2.resize(image, (14*width,28*height))
cv2.imshow('Resized Image',image)
cv2.waitKey(0)
"""image = 255-cv2.Canny(image,50,200)
cv2.namedWindow("After Canny", cv2.WINDOW_NORMAL)
cv2.imshow('After Canny',image)
cv2.waitKey(0)
image = cv2.erode(image, cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(int(argv[4]),int(argv[4]))))
cv2.namedWindow("Eroded Image", cv2.WINDOW_NORMAL)
cv2.imshow('Eroded Image',image)
cv2.waitKey(0)"""
cv2.destroyAllWindows()

cell_height = image.shape[0]//height
cell_width = image.shape[1]//width

#char_image_shape = (14,7)

char_images = []
image_ascii = []
for filename in os.listdir("character-images"):
    img = cv2.imread(os.path.join("character-images",filename),0)
    if img is not None:
        img = cv2.resize(img, (cell_width,cell_height))
        char_images.append(img)
        image_ascii.append(filename[:-4])
char_images = np.array(char_images)

for r in range(height):
    for c in range(width):
        cell_image = image[cell_height*r:cell_height*(r+1),cell_width*c:cell_width*(c+1)]
        diss = dissimilarity(cell_image,char_images)
        min_in = np.argmin(diss)
        print(chr(int(image_ascii[min_in])), end="", flush=True)
        #cv2.imshow('cell_image', cell_image)
        #cv2.imshow('char_image', char_images[min_in])
        """if(r==2 and c==2):
            for x in range(char_images.shape[0]):
                print(dissimilarity(cell_image,char_images[x]), end=" ", flush=True)
                cv2.imshow('specific_char_image', char_images[x])
                cv2.imshow('difference', np.abs(np.maximum(char_images[x], cell_image) - np.minimum(char_images[x], cell_image)))
                cv2.waitKey(0)"""
        #cv2.waitKey(0)
    print()
