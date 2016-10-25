from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

alpha = 0

def getTemp(alpha, L=1, tMax=0.1):
    dt = 0.00005
    dx = 0.01
    Nx = int(L / dx)
    dx = L / Nx
    Nt = int(tMax / dt)
    dt = tMax / Nt

    dx = L / Nx
    dt = tMax / Nt

    assert dt * alpha / dx ** 2 <= 0.5, 'Parameters are not numerically stable'

    temp = np.zeros(Nx)
    temp[0] = 1

    for i in range(Nt):
        temp[1:-1] += dt * alpha / dx ** 2 * (temp[0:-2] - 2 * temp[1:-1] + temp[2:])
    return temp, np.linspace(0, L, Nx)
    
T, x = getTemp(alpha)

fig = plt.figure()
ax = fig.add_subplot(111)
line, = ax.plot(x, T)
#plt.plot(x, T)

def update(*args):
    global alpha
    if alpha >= 0.99:
        alpha = 0
    else:
        alpha += 0.01
    T, x = getTemp(alpha)
    X = np.append(line.get_xdata(), x)
    Y = np.append(line.get_xdata(), T)
    time_text.set_text(time_template%(alpha))
    line.set_xdata(X)
    line.set_ydata(Y)
    fig.canvas.draw()
    return line, time_text

plt.gcf().subplots_adjust(bottom=0.15)
plt.xlabel('Distance', fontsize=18)
plt.ylabel('Temperature', fontsize=16)
time_template = 'alpha = %.1f'    # prints running simulation time
time_text = ax.text(0.2, 0.9, '', transform=ax.transAxes)
ani = animation.FuncAnimation(fig, update, frames = 100, interval=10, blit=True)
#ani.save('pfeifer_hw7p2.mp4', writer='avconv')
plt.show()

