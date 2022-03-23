import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

M = 10e13 #5.972e24
G = 6.6743e-11
num_step = 1000
num_particles = 8
factor = 100
dt = 0.001

def gravity(x):
    p = x[:3]
    v = x[3:]
    distance = np.linalg.norm(p)
    a = -(p/distance) * G*M/(distance**2)
    return np.concatenate((v,a), axis=None)

x = np.zeros((num_step+1, num_particles, 6))
x[0,0] = np.array([50, 0, np.sqrt(100**2-50**2), 0, np.sqrt(G*M/100), 0])
x[0,1] = np.array([90, 0, 0, 0, np.sqrt(G*M/90), 0])
x[0,2] = np.array([80, 0, 0, 0, np.sqrt(G*M/80), 0])
x[0,3] = np.array([70, 0, 0, 0, np.sqrt(G*M/70), 0])
x[0,4] = np.array([60, 0, 0, 0, np.sqrt(G*M/60), 0])
x[0,5] = np.array([50, 0, 0, 0, np.sqrt(G*M/50), 0])
x[0,6] = np.array([40, 0, 0, 0, np.sqrt(G*M/40), 0])
x[0,7] = np.array([30, 0, 0, 0, np.sqrt(G*M/100), 0])
for i in range(num_step):
    for n in range(num_particles):
        if np.linalg.norm(x[i,n]) < 1:
            break
        curr = x[i,n]
        next = None
        for j in range(i, i+factor):
            next = dt*gravity(curr) + curr
            curr = next
        x[i+1,n] = curr


# Plot
fig = plt.figure(figsize=(12, 12), dpi=300)
ax = fig.add_subplot(projection='3d')
colors = plt.cm.jet(np.linspace(0, 1, num_particles))
lines = sum([ax.plot([], [], [], lw=0.4, c=c)
             for c in colors], [])
pts = sum([ax.plot([], [], [], 'o', c=c, markersize=0.5)
           for c in colors], [])
ax.set_xlim(-100, 100)
ax.set_ylim(-100, 100)
ax.set_zlim(-100, 100)

def animate(i):
    for n, (line, pt) in enumerate(zip(lines, pts)):
        line.set_data(x[0:i,n,0], x[0:i,n,1])
        line.set_3d_properties(x[0:i,n,2])
        pt.set_data(x[i,n,0], x[i,n,1])
        pt.set_3d_properties(x[i,n,2])
    return lines + pts


#ax.plot(x[:,0], x[:,1], x[:,2], lw=0.4, color='blue')
anim = FuncAnimation(fig, animate, frames=num_step, interval=10, blit=True)
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title("Gravity")
ax.plot(0,0,0, marker='o', markersize=2, color='black')
plt.show()