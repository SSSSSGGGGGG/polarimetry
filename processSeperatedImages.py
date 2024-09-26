# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 11:28:11 2024

@author: SG
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import processSeperatedImagesCP as CP
import matplotlib as mpl

os.chdir("C:/Users/Laboratorio/StokeMatix/CaptureHub/old/5.28cun")
imName=[0,16,32,48,64,80,96,112,128,144,160,176,192,208,224,240,255] #,[0,16,32,48,64,80,96,112,128,144,160,176,192,208,224,240,255]
i=0
s0_group=[]
s1_group=[]
s2_group=[]
for i in range(len(imName)):
    
    openName="g"+str(imName[i]) #"green"+
    saveName="new_"
    im=cv2.imread(openName+".tif")
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
    plt.imshow(s0,vmin=-1,vmax=1,cmap='seismic')
    plt.colorbar() 
    plt.title(str(imName[i])+'norm_S0',loc='left')
    plt.minorticks_on()
    plt.grid(which='minor',linestyle=':', linewidth='0.1', color='gray')  
    plt.savefig(f"{saveName} {imName[i]}_norm_S0.jpg")
    plt.clf()
    
    # plt.figure(10)
    plt.imshow(s1,vmin=-1,vmax=1,cmap='seismic')
    plt.colorbar()
    plt.title(str(imName[i])+'norm_S1',loc='left')
    plt.minorticks_on()
    plt.grid(which='minor',linestyle=':', linewidth='0.1', color='gray')  
    plt.savefig(f"{saveName} {imName[i]}_norm_S1.jpg")
    plt.clf()
    
    # plt.figure(11)
    plt.imshow(s2,vmin=-1,vmax=1,cmap='seismic')
    plt.colorbar()
    plt.title(str(imName[i])+'norm_S2',loc='left')
    plt.minorticks_on()
    plt.grid(which='minor',linestyle=':', linewidth='0.1', color='gray')  
    plt.savefig(f"{saveName} {imName[i]}_norm_S2.jpg")
    plt.clf()
    
    s0_average=np.average(np.average(s0)) 
    s1_average=np.average(np.average(s1))
    s2_average=np.average(np.average(s2))
    s0_group.append(s0_average)
    s1_group.append(s1_average)
    s2_group.append(s2_average)
    # print(np.array(imName[0]))
s3_group=CP.CalS3(imName)  
plt.figure(1,figsize=(9, 5))  
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
cmap=mpl.colormaps['seismic']
print(cmap)
# def StokeParameters():
#     print("Stokesparameter")
#     return s1_group, s2_group,s3_group
