# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 11:28:11 2024

@author: SG
"""
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
mpl.rcParams['font.size'] = 8
# im_45=im_45withlabel[120:620,100:600] # adjust these arraies to make the light in the center
leftP=im1[0:2048,0:1223]
rightP=im1[0:2048,1224:2448]

im_0=leftP[500:800,500:800] #(611-100/612+100) (654-200/655+200)
im_45=leftP[1500:1800,500:800] #(1636-100/1637+100) (654-200/655+200)

im_n45=rightP[480:580,520:620]
im_90=rightP[1480:1580,520:620]

plt.subplot(1, 2, 1)
plt.imshow(im_0)
plt.title('original',loc='left')
plt.minorticks_on()
plt.grid(which='minor',linestyle=':', linewidth='0.1', color='gray')
# plt.Axes(im, im.axis.Tick==10)
plt.subplot(1, 2, 2)
plt.imshow(im_45)
plt.minorticks_on()
plt.grid(which='minor',linestyle=':', linewidth='0.1', color='gray')
plt.title('GreenChannel',loc='left')


# plt.subplot(4, 2, 1)

# plt.minorticks_on()
# plt.grid(which='minor',linestyle=':', linewidth='0.1', color='gray')
# plt.title('0',loc='left')
# norm_0=im_0/255.0
# plt.imshow(norm_0)

# plt.subplot(4, 2, 2)
# norm_n45=im_n45/255.0
# plt.imshow(norm_n45)
# plt.title('-45',loc='left')
# plt.minorticks_on()
# plt.grid(which='minor',linestyle=':', linewidth='0.1', color='gray')

# plt.subplot(4, 2, 3)
# norm_45=im_45/255.0
# plt.imshow(norm_45)
# plt.title('45',loc='left')
# plt.minorticks_on()
# plt.grid(which='minor',linestyle=':', linewidth='0.1', color='gray')

# plt.subplot(4, 2, 4)
# norm_90=im_90/255.0
# plt.imshow(norm_90)
# plt.title('90',loc='left')
# plt.minorticks_on()
# plt.grid(which='minor',linestyle=':', linewidth='0.1', color='gray')


# sum_0_90=norm_0+norm_90
# plt.subplot(4, 2, 5)
# plt.imshow(sum_0_90)
# plt.title('S0=I0+I90',loc='left')
# plt.minorticks_on()
# plt.grid(which='minor',linestyle=':', linewidth='0.1', color='gray')

# sub_0_90=norm_0-norm_90
# plt.subplot(4, 2, 6)
# plt.imshow(sub_0_90)
# plt.title('S1=I0-I90',loc='left')
# plt.minorticks_on()
# plt.grid(which='minor',linestyle=':', linewidth='0.1', color='gray')

# sub_45_n45=norm_45-norm_n45
# plt.subplot(4, 2, 7)
# plt.imshow(sub_45_n45)
# plt.title('S2=ID-IA',loc='left')
# plt.minorticks_on()
# plt.grid(which='minor',linestyle=':', linewidth='0.1', color='gray')
# plt.colorbar(spacing='proportional')
# plt.subplots_adjust(hspace=1)
# plt.savefig("S2.tif")

# print(np.max(np.max(norm_0)),np.max(np.max(norm_90)),np.max(np.max(norm_45)),np.max(np.max(norm_n45)))
# print(np.max(np.min(norm_0)),np.min(np.min(norm_90)),np.min(np.min(norm_45)),np.min(np.max(norm_n45)))
# print(np.max(np.max(sum_0_90)),np.max(np.max(sub_0_90)),np.max(np.max(sub_45_n45)))
# print(np.max(np.min(sum_0_90)),np.min(np.min(sub_0_90)),np.min(np.min(sub_45_n45)))
# # def calIntensity(row, col,x,y,r,pol):
# #     count=0
# #     sumintensity=0 # for sum work here it should be 0
# #     for i in range(rows):  
# #         for j in range(cols):
# #             distance_squared = (i - x0) ** 2 + (j - y0) ** 2
# #             if distance_squared < r ** 2:
# #                 if pol=="45":
# #                     sumintensity += im_45[i, j]
                    
# #                 else:
# #                     sumintensity += im_n45[i, j]
# #                 count+=1
                    
# #     print(f"The sum of the intensity id {sumintensity} and the number of the pixel is {count} ")
# #     print(f"Then the average of the intensity is {sumintensity/count:.2f}")
    
# # print("For +45")
# # rows, cols = np.shape(im_45)
# # x0,y0=rows/2,cols/2 
# # r=20
# # cal45=calIntensity(rows, cols, x0, y0, r,"45")
# # print("For -45")
# # rows_45, cols_45 = np.shape(im_n45)
# # x0_45,y0_45=rows_45/2,cols_45/2 
# # cal_45=calIntensity(rows_45, cols_45, x0_45, y0_45, r,"-45")
