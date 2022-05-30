# -*- coding: utf-8 -*-
"""GalexyEye.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/197CTSLQsreXHfGbkWV8ms44Fqnrj-nCW

- We know in black and white images (night images, true for most cases), the difference between pixels' RGB values is near to zero.
- Therefore, calculate the differences between channels for all pixels (R-G, G-B, B-R).
- Afterwards, consider the square of the differences avoiding negative values.
-  And then we find the mean values for all differences.
- If this mean value is near to zero then the image is taken at night, otherwise it is taken in day light.
"""

import PIL

img = PIL.Image.open('night_sample.png')

img

from numpy import *
from matplotlib.pyplot import *

im = imread('night_sample_03.jpeg')

# im_norm =  (im.max()/255.0)
# im  = im.astype('float32')

# im /= 255.0

# calculate the differences between channels
r_g = subtract(im[:,:,0], im[:,:, 1])
g_b = subtract(im[:,:,1], im[:,:, 2])
b_r = subtract(im[:,:,2], im[:,:, 0])

# square of the differences to avoid negative values 
# find the mean values for all differences
r_g = mean(square(r_g))
g_b = mean(square(g_b))
b_r = mean(square(b_r))

print( r_g, g_b, b_r)
sum_rgb = r_g + g_b + b_r

if sum_rgb < 100:  # set the threshold manually 
  print('Night')
else:
  print('Day')

imshow(im)

im.shape

r = im[:, :, 0]

imshow(r, cmap=cm.gray)

imshow(im[:,:,2], cmap=cm.gray)

