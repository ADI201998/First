import matplotlib.pyplot as plt
import numpy as np
import math as m

x = 2
y = 2
n = 0
while True:
	i=int(input())
	angle = (i*np.pi)/180
	axes = plt.gca()
	axes.set_xlim([0,4])
	axes.set_ylim([0,4])
	dist = 1

	dy1 = np.sin(angle) + 2
	dx1 = (1 - (dy1-2)**2)**0.5 + 2

	dy2 = np.sin(angle) + 2
	dx2 = 2 - (1 - (dy2-2)**2)**0.5

	dy3 = 2 - m.fabs(np.sin(angle))
	dx3 = 2 - (1 - (dy3-2)**2)**0.5

	dy4 = 2 - m.fabs(np.sin(angle))
	dx4 = 2 + (1 - (dy4-2)**2)**0.5

	if i<=90 and i>=0:
		
		plt.arrow(dx3-x, dy3-y, dx1-x, dy1-y, width = 0.1, shape = 'full')
		plt.draw()
		plt.pause(0.005)
		plt.clf()

	elif i<=180 and i>90:
		
		plt.arrow(x, y, dx2-x, dy2-y, width = 0.1, shape = 'full')
		plt.draw()
		plt.pause(0.005)
		plt.clf()

	if i<=270 and i>180:
		
		plt.arrow(x, y, dx3-x, dy3-y, width = 0.1, shape = 'full')
		plt.draw()
		plt.pause(0.005)
		plt.clf()

	elif i<360 and i>270:
		
		plt.arrow(x, y, dx4-x, dy4-y, width = 0.1, shape = 'full')
		plt.draw()
		plt.pause(0.005)
		plt.clf()

plt.show()
