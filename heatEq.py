# soleve the Heat equation 1dim
# u_t = u_xx x in [0, pi]

import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation

D = 1.
dim = 33
dx = 1. / (dim-1)
dt = (1. / (2. * D)) * dx * dx
INTV = 3000

def initFunc(x):
    a = 1./2
    return math.exp( - 100 * (x - a) * (x - a))

def nextStep(u):
    uNext = [0] * dim
    for i in range(1, dim-1):
        uNext[i] = u[i] + dt * D * (u[i-1] - 2.*u[i] + u[i+1])
    return uNext

# initial condition

fig = plt.figure()
ims = []

u = [0] * dim
for i in range(0, dim):
    u[i] = initFunc(i * dx)

# time loop
t = 0.
i = 0

while t < 100.:
    u = nextStep(u)
    t = t + dt;
    if i % INTV == 0:
        im = plt.plot(u,"b")
        ims.append(im)
    i = i + 1;

ani = animation.ArtistAnimation(fig, ims)
ani.save("heat.gif", writer = "imagemagick")
plt.show()
