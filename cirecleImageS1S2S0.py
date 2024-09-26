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
import cirecleImageS3 as CP

os.chdir("C:/Users/Laboratorio/StokeMatix/CaptureHub/27.05big image")
imName=[0,16,32,48,64,80,96,112,128,144,160,176,192,208,224,240,255] #,[0,16,32,48,64,80,96,112,128,144,160,176,192,208,224,240,255]
i=0
s0_group=[]
s1_group=[]
s2_group=[]
for i in range(len(imName)):
    
    openName=str(imName[i]) #"g"+
    saveName="new_"
    im=cv2.imread(openName+".tif")
    print(openName+".tif")
    im1=im[:,:,1] # green channel
    
    mpl.rcParams['font.size'] = 20
    # im_45=im_45withlabel[120:620,100:600] # adjust these arraies to make the light in the center
    leftP=im1[0:2048,0:1223]
    rightP=im1[0:2048,1224:2448]
    
    im_0=leftP[380:960,350:930] #(611-100/612+100) (654-200/655+200)
    im_45=leftP[1380:1960,350:930] #(1636-100/1637+100) (654-200/655+200)
    
    im_n45=rightP[380:960,350:930]
    im_90=rightP[1380:1960,350:930]
    
    x0,y0=280,290 # center
    r=200
    
    lenx_0,leny_0=im_0.shape
    # print(lenx_0,leny_0)       
    newcircle_0=im_0.copy()
    
    for i0 in range(lenx_0):  
        for j0 in range(leny_0):
            distance_squared = (i0 - x0) ** 2 + (j0 - y0) ** 2
            if distance_squared > r ** 2:             
                newcircle_0[i0,j0]=0  # To avoid the inf 
            
                
    lenx_90,leny_90=im_90.shape
    # print(lenx_90,leny_90)       
    newcircle_90=im_90.copy()
    for i1 in range(lenx_90):  
        for j1 in range(leny_90):
            distance_squared = (i1 - x0) ** 2 + (j1 - y0) ** 2
            if distance_squared > r ** 2:             
                newcircle_90[i1][j1]=0
                
    lenx_45,leny_45=im_45.shape
    # print(lenx_45,leny_45)       
    newcircle_45=im_45.copy()
    for i2 in range(lenx_45):  
        for j2 in range(leny_45):
            distance_squared = (i2 - x0) ** 2 + (j2 - y0) ** 2
            if distance_squared > r ** 2:             
                newcircle_45[i2][j2]=0
                
    lenx_n45,leny_n45=im_n45.shape
    # print(lenx_n45,leny_n45)       
    newcircle_n45=im_n45.copy()
    for i3 in range(lenx_n45):  
        for j3 in range(leny_n45):
            distance_squared = (i3 - x0) ** 2 + (j3 - y0) ** 2
            if distance_squared > r ** 2:             
                newcircle_n45[i3][j3]=0
    
    
    norm_0=newcircle_0/255
    norm_n45=newcircle_n45/255
    norm_45=newcircle_45/255
    norm_90=newcircle_90/255
    
    S0_H=norm_0+norm_90
    S0_45=norm_45+norm_n45
    S_avg=(S0_H+S0_45)/2
    epsilon = 1e-30
    S_avg_safe = np.where(S_avg == 0, epsilon, S_avg)
    S0_norm=S_avg_safe/S_avg_safe
    
    sum_pixels_0 = 0
    count_pixels_0 = 0
    for i00 in range(lenx_0):  
        for j00 in range(leny_0):
            distance_squared = (i00 - x0) ** 2 + (j00 - y0) ** 2
            if distance_squared < r ** 2:             
                sum_pixels_0 += S0_norm[i00,j00]
                count_pixels_0 += 1
           
                
    
    S1=norm_0-norm_90
    S1_norm=S1/S_avg_safe
    sum_pixels_1 = 0
    count_pixels_1 = 0
    for i01 in range(lenx_0):  
        for j01 in range(leny_0):
            distance_squared = (i01 - x0) ** 2 + (j01 - y0) ** 2
            if distance_squared < r ** 2:             
                sum_pixels_1 += S1_norm[i01,j01]
                count_pixels_1 += 1
    
    S2=norm_45-norm_n45
    S2_norm=S2/S_avg_safe
    sum_pixels_2 = 0
    count_pixels_2 = 0
    for i02 in range(lenx_0):  
        for j02 in range(leny_0):
            distance_squared = (i02 - x0) ** 2 + (j02 - y0) ** 2
            if distance_squared < r ** 2:             
                sum_pixels_2 += S2_norm[i02,j02]
                count_pixels_2 += 1
    
    
    plt.figure(1,figsize=(12, 10))
    plt.subplot(2, 2, 1)
    plt.imshow(S0_H,vmin=-1,vmax=1,cmap='seismic')
    plt.title('S0_H',loc='left')
    plt.colorbar()
    plt.minorticks_on()
    plt.grid(which='minor',linestyle=':', linewidth='0.1', color='gray')
    
    plt.subplot(2, 2, 2)
    plt.imshow(S0_norm,vmin=-1,vmax=1,cmap='seismic')
    plt.title('S0_norm',loc='left')
    plt.colorbar()
    plt.minorticks_on()
    plt.grid(which='minor',linestyle=':', linewidth='0.1', color='gray')
    # plt.Axes(im, im.axis.Tick==10)
    plt.subplot(2, 2, 3)
    plt.imshow(S1_norm,vmin=-1,vmax=1,cmap='seismic')
    plt.minorticks_on()
    plt.grid(which='minor',linestyle=':', linewidth='0.1', color='gray')
    plt.title('S1_norm',loc='left')
    plt.colorbar()
    # plt.Axes(im, im.axis.Tick==10)
    plt.subplot(2, 2, 4)
    plt.imshow(S2_norm,vmin=-1,vmax=1,cmap='seismic')
    plt.minorticks_on()
    plt.grid(which='minor',linestyle=':', linewidth='0.1', color='gray')
    plt.title('S2_norm',loc='left')
    plt.colorbar()
    plt.savefig(f"{saveName} {imName[i]}_norm_stokes.jpg")
    plt.clf()
    
    plt.figure(2,figsize=(10, 10))
    plt.subplot(2, 2, 1)
    plt.imshow(norm_0,vmin=0,vmax=1,cmap='hot')
    plt.title('0',loc='left')
    plt.colorbar()
    plt.minorticks_on()
    plt.grid(which='minor',linestyle=':', linewidth='0.1', color='gray')
    plt.subplot(2, 2, 4)
    plt.imshow(norm_90,vmin=0,vmax=1,cmap='hot')
    plt.title('90',loc='left')
    plt.colorbar()
    plt.minorticks_on()
    plt.grid(which='minor',linestyle=':', linewidth='0.1', color='gray')
    # plt.Axes(im, im.axis.Tick==10)
    plt.subplot(2, 2, 3)
    plt.imshow(norm_45,vmin=0,vmax=1,cmap='hot')
    plt.minorticks_on()
    plt.grid(which='minor',linestyle=':', linewidth='0.1', color='gray')
    plt.title('45',loc='left')
    plt.colorbar()
    # plt.Axes(im, im.axis.Tick==10)
    plt.subplot(2, 2, 2)
    plt.imshow(norm_n45,vmin=0,vmax=1,cmap='hot')
    plt.minorticks_on()
    plt.grid(which='minor',linestyle=':', linewidth='0.1', color='gray')
    plt.title('-45',loc='left')
    plt.colorbar()
    
    plt.savefig(f"{saveName} {imName[i]}_norm_Original.jpg")
    plt.clf()
    
    s0_average=sum_pixels_0 / (count_pixels_0 +1)
    s1_average=sum_pixels_1 / (count_pixels_1 +1)
    s2_average=sum_pixels_2 / (count_pixels_2+1)
    s0_group.append(s0_average)
    s1_group.append(s1_average)
    s2_group.append(s2_average)
s3_group=CP.CalS3(imName) 
plt.figure(3,figsize=(12, 6))  
plt.plot(imName,s0_group,label="S0",marker="o")
plt.plot(imName,s1_group,label="S1",marker="o")
plt.plot(imName,s2_group,label="S2",marker="o")
plt.plot(imName,s3_group,label="S3",marker="o")
plt.xticks(ticks=imName)
plt.ylim(-1, 1.1)
plt.minorticks_on()
plt.axhline(0, color='black', linestyle='--')
# Manually set the minor ticks for the x-axis to an empty list
plt.gca().xaxis.set_minor_locator(plt.NullLocator())
plt.legend()

plt.figure(4,figsize=(12, 5))  
plt.plot(imName,[np.sqrt(s1_group[i]**2+s2_group[i]**2+s3_group[i]**2) for i in range(len(s1_group))],label="DOP",marker="o")
plt.xticks(ticks=imName)
plt.yticks()
plt.minorticks_on()
plt.gca().xaxis.set_minor_locator(plt.NullLocator())
plt.legend()

DOP=[np.sqrt(s1_group[i]**2+s2_group[i]**2+s3_group[i]**2) for i in range(len(s1_group))]
print(DOP)
    # plt.figure(figsize=(10, 10))
    # plt.subplot(2, 2, 1)
    # plt.imshow(newcircle_0/255)
    # plt.title('0',loc='left')
    # plt.colorbar()
    # plt.minorticks_on()
    # plt.grid(which='minor',linestyle=':', linewidth='0.1', color='gray')
    # plt.subplot(2, 2, 4)
    # plt.imshow(newcircle_90/255)
    # plt.title('90',loc='left')
    # plt.colorbar()
    # plt.minorticks_on()
    # plt.grid(which='minor',linestyle=':', linewidth='0.1', color='gray')
    # # plt.Axes(im, im.axis.Tick==10)
    # plt.subplot(2, 2, 3)
    # plt.imshow(newcircle_45/255)
    # plt.minorticks_on()
    # plt.grid(which='minor',linestyle=':', linewidth='0.1', color='gray')
    # plt.title('45',loc='left')
    # plt.colorbar()
    # # plt.Axes(im, im.axis.Tick==10)
    # plt.subplot(2, 2, 2)
    # plt.imshow(newcircle_n45/255)
    # plt.minorticks_on()
    # plt.grid(which='minor',linestyle=':', linewidth='0.1', color='gray')
    # plt.title('-45',loc='left')
    # plt.colorbar()