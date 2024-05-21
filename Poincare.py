# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 11:28:11 2024

@author: SG
"""



import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# If using Jupyter Notebook, uncomment the following line:
# %matplotlib notebook

def poincare_sphere(S1, S2, S3):
    x = S1
    y = S2
    z = S3

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Plot the sphere
    u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
    sphere_x = np.cos(u) * np.sin(v)
    sphere_y = np.sin(u) * np.sin(v)
    sphere_z = np.cos(v)
    ax.plot_surface(sphere_x, sphere_y, sphere_z, color='0.5', alpha=0.1, edgecolors='0.65')

    # Plot the axes
    ax.plot([-1.5, 1.5], [0, 0], [0, 0], 'k-', linewidth=0.5)
    ax.plot([0, 0], [-1.5, 1.5], [0, 0], 'k-', linewidth=0.5)
    ax.plot([0, 0], [0, 0], [-1.5, 1.5], 'k-', linewidth=0.5)

    ax.text(1.75, 0, 0, '+S1', fontweight='bold', fontsize=12)
    ax.text(0.1, 1.6, 0, '+S2', fontweight='bold', fontsize=12)
    ax.text(-0.05, 0, 1.35, '+S3', fontweight='bold', fontsize=12)

    # Plot the equator and prime meridian
    t = np.linspace(-1, 1, 100)
    equator_y = np.sqrt(1 - t**2)
    ax.plot(t, equator_y, np.zeros_like(t), 'k-', linewidth=0.5)
    ax.plot(t, -equator_y, np.zeros_like(t), 'k-', linewidth=0.5)

    prime_meridian_z = np.sqrt(1 - t**2)
    ax.plot(np.zeros_like(t), t, prime_meridian_z, 'k-', linewidth=1)
    ax.plot(np.zeros_like(t), t, -prime_meridian_z, 'k-', linewidth=1)

    # Plot the data points
    ax.scatter(x[0], y[0], z[0], color='k', s=16)  # Adjusted marker size (4^2)
    ax.scatter(x[1:4], y[1:4], z[1:4], edgecolors='k', facecolors=(0.7, 0.7, 1), s=16)
    ax.scatter(x[4:8], y[4:8], z[4:8], edgecolors='k', facecolors=(0.35, 0.35, 1), s=16)
    ax.scatter(x[8:10], y[8:10], z[8:10], edgecolors='k', facecolors=(0, 0, 1), s=16)
    ax.scatter(x[10:14], y[10:14], z[10:14], edgecolors='k', facecolors=(1, 0.7, 0.7), s=16)
    ax.scatter(x[14:17], y[14:17], z[14:17], edgecolors='k', facecolors=(1, 0.4, 0.4), s=16)

    ax.view_init(elev=20, azim=-135)
    ax.set_axis_off()
    plt.show()

# Provided data
S1 = [0.052678622, 0.057043128, 0.051607531, 0.026610903, -0.024018592, -0.113552192, -0.212786257, -0.297516853, -0.37344744, -0.451327763, -0.527621065, -0.600779531, -0.658937899, -0.66505057, -0.498724741, -0.377489577, -0.378305462]
S2 = [0.945565331, 0.946514496, 0.945829129, 0.946154634, 0.937401469, 0.904185381, 0.846021329, 0.779859999, 0.703951433, 0.606402539, 0.484236263, 0.328932123, 0.12739057, -0.210526674, -0.59129189, -0.698180875, -0.698798966]
S3 = [0.115858577, 0.116600466, 0.109331863, 0.089064757, 0.055155716, 0.00360812, -0.050291432, -0.094232168, -0.132968784, -0.174170551, -0.217499175, -0.258231438, -0.300907227, -0.336885768, -0.334729973, -0.302779043, -0.302842309]

poincare_sphere(S1, S2, S3)

