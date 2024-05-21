# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 11:28:11 2024

@author: SG
"""
import numpy as np
import matplotlib.pyplot as plt
import os


os.chdir("C:/Users/Laboratorio/StokeMatix/spectrum")
color=["r","g","b","c","m","y","w"]
for j in range (len(color)):
    filename="n45"+color[j]+".SSM"
    with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
    x=[]
    y=[]
    def text_to_2d_array(text):
        try:
            rows_ori = text.strip().split('\n')
            rows=rows_ori[2:len(rows_ori)]
            for i in range (len(rows)):
                col1=rows[i].strip().split(' ')
                x.append(float(col1[0]))
                y.append(float(col1[2]))
 
            return rows
    
            
        except Exception as e:
            print(f"An error occurred: {e}")
    text_array=text_to_2d_array(text)
    # text_float=float(text_array.value)
    # print(text_float)
    # print(f"text_array: {text_array}")
    # Show the plot
    # plt.figure()
    plt.plot(x[421:1221], y[421:1221], linestyle='-', marker='o', color='b', label='Data')
    plt.xticks([400,500,600,700,800])
    plt.minorticks_on()
    max_value = max(y)
    max_index = y.index(max_value)

# Annotating the maximum point
    plt.annotate(f'(  {x[max_index]}, {y[max_index]})',
    xy=(x[max_index], y[max_index]),
    xytext=(x[max_index] +20, y[max_index] + 15),
    arrowprops=dict(facecolor='black', arrowstyle='->'),fontsize=10) #
    # plt.show()
    plt.savefig(f"{filename}.jpg")
    plt.clf()