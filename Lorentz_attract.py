import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation
plt.rcParams['animation.ffmpeg_path'] = 'D:\\FFmpeg\\bin\\ffmpeg.exe'

def lorenz(x, y, z, s=10, r=26, b=8/3):
    """
    Given:
       x, y, z: a point of interest in three dimensional space
       s, r, b: parameters defining the lorenz attractor
    Returns:
       x_dot, y_dot, z_dot: values of the lorenz attractor's partial
           derivatives at the point x, y, z
    """
    x_dot = s*(y - x)
    y_dot = r*x - y - x*z
    z_dot = x*y - b*z
    return x_dot, y_dot, z_dot


def sample_spherical(npoints, ndim=3):
    vec = np.random.randn(ndim, npoints)
    return vec


dt = 0.001
num_points = 25000
num_steps = 10000

xl = np.empty((num_steps+1, num_points))
yl = np.empty((num_steps+1, num_points))
zl = np.empty((num_steps+1, num_points))

radius = 200
points = sample_spherical(num_points) * radius

xl[0, :] = points[0]
yl[0, :] = points[1]
zl[0, :] = points[2]

for i in range(num_steps):
    for j in range(num_points):
        xl[i+1, j] = xl[i, j] + lorenz(xl[i, j], yl[i, j], zl[i, j])[0]*dt
        yl[i+1, j] = yl[i, j] + lorenz(xl[i, j], yl[i, j], zl[i, j])[1]*dt
        zl[i+1, j] = zl[i, j] + lorenz(xl[i, j], yl[i, j], zl[i, j])[2]*dt

fig = plt.figure(figsize=(12, 12), dpi=300)
ax = fig.add_subplot(projection='3d')
line, = ax.plot([], [], [], lw=0.2, marker='o', ls='', markersize=0.2)
ax.set_xlim(-radius, radius)
ax.set_ylim(-radius, radius)
ax.set_zlim(-radius, radius)


def animate(i):
    line.set_data(xl[i], yl[i])
    line.set_3d_properties(zl[i])
    xlim = max(np.abs(np.min(xl[i])), np.abs(np.max(xl[i])))
    ylim = max(np.abs(np.min(yl[i])), np.abs(np.max(yl[i])))
    zlim = max(np.abs(np.min(zl[i])), np.abs(np.max(zl[i])))
    lim = max(xlim, ylim, zlim)
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)
    ax.set_zlim(-lim, lim)
    fig.canvas.draw()
    return line,


#ax.plot(xs, ys, zs, lw=0.4, color='blue')
anim = FuncAnimation(fig, animate, frames=num_steps, interval=20, blit=False)
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title("Lorenz Attractor")
writervideo = animation.FFMpegWriter(fps=60)
anim.save("Lorentz.mp4", writer=writervideo)
#plt.show()