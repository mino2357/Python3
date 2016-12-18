# soleve the Heat equation 1dim
# u_t = u_xx x in [0, pi]

import math

D = 1.
dim = 10
dx = 1. / (dim-1)
dt = (1. / (2. * D)) * dx * dx

def initFunc(x):
	return math.sin(x)

def nextStep(u):
	uNext = [0] * dim
	for i in range(1, dim-1):
		uNext[i] = u[i] + dt * D * (u[i-1] - 2.*u[i] + u[i+1])
	return uNext

# initial condition

u = [0] * dim
for i in range(0, dim):
	u[i] = initFunc(i * dx * math.pi)

# time loop
t = 0.

while t < 10.:
	u = nextStep(u)
	t = t + dt;
	print(u)

