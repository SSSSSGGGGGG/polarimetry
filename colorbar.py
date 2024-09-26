# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 11:28:11 2024

@author: SG
"""
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
data = np.zeros((10, 10))

plt.figure(1)
plt.imshow(data, cmap='viridis')  # Display an empty image
plt.colorbar()  # Show color bar
plt.axis('off')  # Turn off axis
plt.show()