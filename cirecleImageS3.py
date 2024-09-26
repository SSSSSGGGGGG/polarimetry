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

def CalS3(imName):
    os.chdir("C:/Users/Laboratorio/StokeMatix/CaptureHub/27.05big image")
    # imName=[0,32,64,128,160,192,224,255] #,64,128,192,255
    # print(imName)
    # i=0
    s0_group=[]
    s3_group=[]
    for i in range(len(imName)):
        
        
        openName="h"+str(imName[i])
        # print(imName[i])
        saveName="new_h"
        im=plt.imread(openName+".tif")
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
        
        x0,y0=280,290
        r=200
        
        lenx_0,leny_0=im_0.shape
        # print(lenx_0,leny_0)       
        newcircle_0=im_0.copy()
        
        for i0 in range(lenx_0):  
            for j0 in range(leny_0):
                distance_squared = (i0 - x0) ** 2 + (j0 - y0) ** 2
                if distance_squared > r ** 2:             
                    newcircle_0[i0,j0]=0
                
                    
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
        for i000 in range(lenx_0):  
            for j000 in range(leny_0):
                distance_squared = (i000 - x0) ** 2 + (j000 - y0) ** 2
                if distance_squared < r ** 2:             
                    sum_pixels_0 += S0_norm[i000,j000]
                    count_pixels_0 += 1
        S1=norm_0-norm_90
        S1_norm=S1/S_avg_safe
        sum_pixels_3 = 0
        count_pixels_3 = 0
        for i03 in range(lenx_0):  
            for j03 in range(leny_0):
                distance_squared = (i03 - x0) ** 2 + (j03 - y0) ** 2
                if distance_squared < r ** 2:             
                    sum_pixels_3 += S1_norm[i03,j03]
                    count_pixels_3 += 1       
        
        
        
        plt.figure(1,figsize=(10, 5))
        plt.subplot(1, 2, 1)
        plt.imshow(S0_norm,vmin=-1,vmax=1,cmap='seismic')
        plt.title('S0_norm',loc='left')
        plt.colorbar(shrink=0.5)
        plt.minorticks_on()
        plt.grid(which='minor',linestyle=':', linewidth='0.1', color='gray')
        # plt.Axes(im, im.axis.Tick==10)
        plt.subplot(1, 2, 2)
        plt.imshow(S1_norm,vmin=-1,vmax=1,cmap='seismic')
        plt.minorticks_on()
        plt.grid(which='minor',linestyle=':', linewidth='0.1', color='gray')
        plt.title('S3_norm',loc='left')
        plt.colorbar(shrink=0.5)
     
        plt.savefig(f"{saveName} {imName[i]}_norm_stoke3.jpg")
        
        plt.clf()
        # plt.Axes(im, im.axis.Tick==10)
        # plt.subplot(2, 2, 4)
        # plt.imshow(S2_norm,vmin=-1,vmax=1,cmap='seismic')
        # plt.minorticks_on()
        # plt.grid(which='minor',linestyle=':', linewidth='0.1', color='gray')
        # plt.title('S2_norm',loc='left')
        # plt.colorbar()
        # plt.savefig(f"{saveName} {imName[i]}_norm_stokes.jpg")
        # plt.clf()
        
        plt.figure(2,figsize=(12, 10))
        plt.subplot(2, 2, 1)
        plt.imshow(norm_0,vmin=0,vmax=1,cmap='hot')
        plt.title('0',loc='left')
        plt.colorbar()
        plt.minorticks_on()
        plt.grid(which='minor',linestyle=':', linewidth='0.1', color='gray')
        
        plt.subplot(2, 2, 2)
        plt.imshow(norm_n45,vmin=0,vmax=1,cmap='hot')
        plt.title('-45',loc='left')
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
        plt.subplot(2, 2, 4)
        plt.imshow(norm_90,vmin=0,vmax=1,cmap='hot')
        plt.minorticks_on()
        plt.grid(which='minor',linestyle=':', linewidth='0.1', color='gray')
        plt.title('90',loc='left')
        plt.colorbar()
        plt.savefig(f"{saveName} {imName[i]}_norm_Original.jpg")
        plt.clf()
        
        s0_average=sum_pixels_0 / count_pixels_0 
        s3_average=sum_pixels_3 / (count_pixels_3+1)
        # print(count_pixels_0,count_pixels_3)
        s0_group.append(s0_average)
        s3_group.append(s3_average)
    return s3_group
        
    
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