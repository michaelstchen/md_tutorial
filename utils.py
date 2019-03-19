import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
from matplotlib.animation import FuncAnimation


def setup_plot(num_dims, boxl, ms):
    # set up figure and animation
    fig = plt.figure(figsize=(8,8))
    if num_dims == 2:
        ax = fig.add_subplot(111, aspect='equal', autoscale_on=False,
                             xlim=(-0.5*boxl, 0.5*boxl), ylim=(-0.5*boxl, 0.5*boxl))
        particles, = ax.plot([], [], 'bo', ms=ms)
    elif num_dims == 3:
        ax = p3.Axes3D(fig)
        ax.set_xlim3d([-0.5*boxl, 0.5*boxl])
        ax.set_ylim3d([-0.5*boxl, 0.5*boxl])
        ax.set_zlim3d([-0.5*boxl, 0.5*boxl])
        particles, = ax.plot([], [], [], 'ro', ms=ms)

    return fig, ax, particles
