# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 11:28:11 2024

@author: SG
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Cursor

# Generate some random data
num_points = 10
x_values = np.linspace(0, 10, num_points)
y_values = np.sin(x_values)

# Create the figure and axis
fig, ax = plt.subplots()

# Plot the data
ax.plot(x_values, y_values, label='sin(x)')

# Initialize an empty list to store fixed points
fixed_points = []

def on_click(event):
    if event.xdata is not None and event.ydata is not None:
        # Add the clicked point to the list
        fixed_points.append((event.xdata, event.ydata))
        # Annotate the point
        ax.annotate(f'({event.xdata:.2f}, {event.ydata:.2f})', xy=(event.xdata, event.ydata),
                    xytext=(event.xdata + 0.5, event.ydata + 0.5),
                    arrowprops=dict(arrowstyle='->', color='red'))
        # Redraw the figure
        fig.canvas.draw()

# Connect the click event to the function
fig.canvas.mpl_connect('button_press_event', on_click)
# Create a cursor (green lines)
cursor = Cursor(ax, color='green', linewidth=2)

def on_move(event):
    if event.xdata is not None and event.ydata is not None:
        ax.set_title(f"Cursor: ({event.xdata:.2f}, {event.ydata:.2f})")

fig.canvas.mpl_connect('motion_notify_event', on_move)

plt.show()
# Customize the plot
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Click to Fix Points')
ax.legend()

plt.show()
