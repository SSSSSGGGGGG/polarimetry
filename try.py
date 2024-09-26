# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 11:28:11 2024

@author: SG
"""

import numpy as np
import matplotlib.pyplot as plt

import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import matplotlib as mpl
import matplotlib.colors as mcolors

os.chdir("C:/Users/Laboratorio/StokeMatix/CaptureHub/27.05big image")
im=plt.imread("0.tif")
im1=im[:,:,1] # green channel
# plt.imshow(im1)
# im45withlabel=im1[1000:2000,0:1050]
# im_45withlabel=im1[0:950,1220:2170]

# im45=im45withlabel[110:610,100:600]
mpl.rcParams['font.size'] = 15
# im_45=im_45withlabel[120:620,100:600] # adjust these arraies to make the light in the center
leftP=im1[0:2048,0:1223]
rightP=im1[0:2048,1224:2448]

im_0=leftP[380:960,350:930] #(611-100/612+100) (654-200/655+200)
im_45=leftP[1380:1960,350:930] #(1636-100/1637+100) (654-200/655+200)

im_n45=rightP[380:960,350:930]
im_90=rightP[1380:1960,350:930]

# Assuming im_45 is already defined as a NumPy array
# For example, im_45 = np.array(Image.open('path_to_image_file'))

# Define the center and radius
x0,y0=290,290
r=200
count = 0

# Get the dimensions of the image
lenx, leny = im_45.shape[:2]  # Assuming im_45 is a 2D or 3D array (for grayscale or RGB images)
print(lenx, leny)

# Initialize newcircle as a copy of im_45
newcircle = im_45.copy()

# Process the image to create a circular mask
for i in range(lenx):  
    for j in range(leny):
        distance_squared = (i - x0) ** 2 + (j - y0) ** 2
        if distance_squared > r ** 2:
            newcircle[i, j] = 0  # Set the value to 0 if outside the circle
        count += 1
verify=im_45-newcircle
# Display the modified image
plt.figure(figsize=(10, 10))
plt.subplot(1, 2, 1)
plt.imshow(newcircle)
plt.title('Cropped',loc='left')
plt.minorticks_on()
plt.grid(which='minor',linestyle=':', linewidth='0.1', color='gray')
# plt.Axes(im, im.axis.Tick==10)
plt.subplot(1, 2, 2)
plt.imshow(verify)
plt.minorticks_on()
plt.grid(which='minor',linestyle=':', linewidth='0.1', color='gray')
plt.title('Subtraction with original',loc='left')
