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


#LC is at 45 degree to camera, the panels of 0 degree and 90 degree are for circular polarizations.
def CalS3(imName):
    os.chdir("C:/Users/Laboratorio/StokeMatix/CaptureHub/old/5.28cun")
    # imName=[0,32,64,128,160,192,224,255] #,64,128,192,255
    # print(imName)
    # i=0
    s3_group=[]
    for i in range(len(imName)):
        
        
        openName="h"+str(imName[i]) #"green"+
        # print(imName[i])
        saveName="new_h"
        im=plt.imread(openName+".tif")
        print(openName+".tif")
        im1=im[:,:,1] # green channel
        
        mpl.rcParams['font.size'] = 15
        # im_45=im_45withlabel[120:620,100:600] # adjust these arraies to make the light in the center
        leftP=im1[0:2048,0:1223]
        rightP=im1[0:2048,1224:2448]
    
        im_0=leftP[500:600,520:620] #(611-100/612+100) (654-200/655+200)
        im_45=leftP[1500:1600,520:620] #(1636-100/1637+100) (654-200/655+200)

        im_n45=rightP[500:600,520:620]
        im_90=rightP[1500:1600,520:620]
    
        
        norm_0=im_0/255.0
        # plt.figure(1)
        
        # plt.imshow(norm_0,vmin=-1,vmax=1)
        # plt.title(str(imName[i])+'0',loc='left')
        # plt.minorticks_on()
        # plt.grid(which='minor',linestyle=':', linewidth='0.1', color='gray')
        # plt.colorbar()   
        # plt.savefig(f"{saveName} {imName[i]}_0.jpg")
        # plt.clf()
        
        norm_90=im_90/255.0
        # plt.figure(2)
        
        # plt.imshow(norm_90,vmin=-1,vmax=1)
        # plt.title(str(imName[i])+'90',loc='left')
        # plt.minorticks_on()
        # plt.grid(which='minor',linestyle=':', linewidth='0.1', color='gray')
        # plt.colorbar()
        # plt.savefig(f"{saveName} {imName[i]}_90.jpg")
        # plt.clf()
        
        norm_45=im_45/255.0
        # plt.figure(3)
        
        # plt.imshow(norm_45,vmin=-1,vmax=1)
        # plt.title(str(imName[i])+'45',loc='left')
        # plt.minorticks_on()
        # plt.grid(which='minor',linestyle=':', linewidth='0.1', color='gray')
        # plt.colorbar() #ticks=np.arange(0,255,50)
        # plt.savefig(f"{saveName} {imName[i]}_45.jpg")
        # plt.clf()
        
        norm_n45=im_n45/255.0
        # plt.figure(4)
        
        # plt.imshow(norm_n45,vmin=-1,vmax=1)
        # plt.title(str(imName[i])+'-45',loc='left')
        # plt.minorticks_on()
        # plt.grid(which='minor',linestyle=':', linewidth='0.1', color='gray')
        # plt.colorbar()
        # plt.savefig(f"{saveName} {imName[i]}_-45.jpg")
        # plt.clf()
        
        s0_H_V=norm_0+norm_90
        # plt.figure(5)
        # plt.imshow(s0_H_V,vmin=-1,vmax=1)
        # plt.title(str(imName[i])+'S0 of H+V',loc='left')
        # plt.minorticks_on()
        # plt.grid(which='minor',linestyle=':', linewidth='0.1', color='gray') 
        # plt.colorbar()
        # plt.savefig(f"{saveName} {imName[i]}_S0_H+V.jpg")
        # plt.clf()
        
        # plt.figure(6)
        # plt.imshow(norm_0-norm_90,vmin=-1,vmax=1)
        # plt.title(str(imName[i])+'S1',loc='left')
        # plt.minorticks_on()
        # plt.grid(which='minor',linestyle=':', linewidth='0.1', color='gray') 
        # plt.colorbar()
        # plt.savefig(f"{saveName} {imName[i]}_S1.jpg")
        # plt.clf()
        
        # plt.figure(7)
        # plt.imshow(norm_45-norm_n45,vmin=-1,vmax=1)
        # plt.colorbar()
        # plt.title(str(imName[i])+'S2',loc='left')
        # plt.minorticks_on()
        # plt.grid(which='minor',linestyle=':', linewidth='0.1', color='gray')  
        # plt.savefig(f"{saveName} {imName[i]}_S2.jpg")
        # plt.clf()
        
        s0_D_A=norm_45+norm_n45
        # plt.figure(8)
        # plt.imshow(s0_D_A,vmin=-1,vmax=1)
        # plt.colorbar() 
        # plt.title(str(imName[i])+'S0 of D+A',loc='left')
        # plt.minorticks_on()
        # plt.grid(which='minor',linestyle=':', linewidth='0.1', color='gray')  
        # plt.savefig(f"{saveName} {imName[i]}_S0_D+A.jpg")
        # plt.clf()
        
        # diff=norm_0+norm_90-norm_45-norm_n45   
        # plt.imshow(diff)
        # plt.colorbar()
        
        S0_avg=(norm_0+norm_90+norm_45+norm_n45)/2
        s0=S0_avg/S0_avg
        s1=(norm_0-norm_90)/S0_avg
        s2=(norm_45-norm_n45)/S0_avg
        
        # plt.figure(9)
        # plt.imshow(s0,vmin=-1,vmax=1)
        # plt.colorbar() 
        # plt.title(str(imName[i])+'norm_S0',loc='left')
        # plt.minorticks_on()
        # plt.grid(which='minor',linestyle=':', linewidth='0.1', color='gray')  
        # plt.savefig(f"{saveName} {imName[i]}_norm_S0.jpg")
        # plt.clf()
        
        # plt.figure(10)
        plt.imshow(s1,vmin=-1,vmax=1,cmap='seismic')
        plt.colorbar()
        plt.title(str(imName[i])+'norm_S3',loc='left')
        plt.minorticks_on()
        plt.grid(which='minor',linestyle=':', linewidth='0.1', color='gray')  
        plt.savefig(f"{saveName} {imName[i]}_norm_S3.jpg")
        plt.clf()
        
        # plt.figure(11)
        # plt.imshow(s2,vmin=-1,vmax=1)
        # plt.colorbar()
        # plt.title(str(imName[i])+'norm_S2',loc='left')
        # plt.minorticks_on()
        # plt.grid(which='minor',linestyle=':', linewidth='0.1', color='gray')  
        # plt.savefig(f"{saveName} {imName[i]}_norm_S2.jpg")
        # plt.clf()
        
        s3_average=np.average(np.average(s1))
        s3_group.append(s3_average)
    return s3_group
     