# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 11:28:11 2024

@author: SG
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import stokesFigCP as CP
import matplotlib as mpl

os.chdir("C:/Users/Laboratorio/StokeMatix/CaptureHub/old/5.28cun")
imName=[0,16,32,48,64,80,96,112,128,144,160,176,192,208,224,240,255] #,[0,16,32,48,64,80,96,112,128,144,160,176,192,208,224,240,255]
i=0
s0_group=[]
s1_group=[]
s2_group=[]
s3_group=[]
for i in range(len(imName)):
    
    openName="g"+str(imName[i]) #"green"+ #"green"+
    saveName="new_"
    im=cv2.imread(openName+".tif")
    print(openName+".tif")
    im1=im[:,:,1] # green channel
    
    mpl.rcParams['font.size'] = 20
    # im_45=im_45withlabel[120:620,100:600] # adjust these arraies to make the light in the center
    leftP=im1[0:2048,0:1223]
    rightP=im1[0:2048,1224:2448]

    im_0=leftP[500:600,520:620] #(611-100/612+100) (654-200/655+200)
    im_45=leftP[1500:1600,520:620] #(1636-100/1637+100) (654-200/655+200)

    im_n45=rightP[500:600,520:620]
    im_90=rightP[1500:1600,520:620]
 
    norm_0=im_0/255.0    
    norm_90=im_90/255.0
    norm_45=im_45/255.0 
    norm_n45=im_n45/255.0
    s0_H_V=norm_0+norm_90  
    s0_D_A=norm_45+norm_n45
    
    
    S0_avg=(norm_0+norm_90+norm_45+norm_n45)/2
    s0=S0_avg/S0_avg
    s1=(norm_0-norm_90)/S0_avg
    s2=(norm_45-norm_n45)/S0_avg
    s3=CP.CalS3(imName[i])
   
    
    s0_group.append(s0)
    s1_group.append(s1)
    s2_group.append(s2)
    s3_group.append(s3)
length=len(s1_group)   
# print(length) 
fig, axs = plt.subplots(ncols=length, nrows=3, figsize=(30, 3),
                     layout="constrained")
for i in range(length):
  
    axs[0, i].imshow(s1_group[i], vmin=-1, vmax=1, cmap='seismic')
    axs[0, i].set_title(imName[i])
    
    axs[1, i].imshow(s2_group[i], vmin=-1, vmax=1, cmap='seismic')
    
    axs[2, i].imshow(s3_group[i], vmin=-1, vmax=1, cmap='seismic')
    
cbar = fig.colorbar(axs[0, 0].images[0], ax=axs.ravel().tolist(), orientation='vertical',shrink=1)
fig.text(0.93, 0.75, "S1", ha='center', va='center', fontsize='large')
fig.text(0.93, 0.45, "S2", ha='center', va='center', fontsize='large')
fig.text(0.93, 0.15, "S3", ha='center', va='center', fontsize='large')
for ax_row in axs:
    for ax in ax_row:
        ax.axis('off')

plt.minorticks_on()
# # Adjust subplot layout
# plt.show()
