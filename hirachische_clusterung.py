#! /usr/bin/env python
from numpy import zeros
from math import sqrt
from pylab import plot, show, axis, Circle, figure,text
import matplotlib.pyplot as plt

p=([1,2.5,2,5],[2,1,3,1.5])
d=zeros([4,4])
for i in range(4):
	for l in range(4):
		d[i,l]=sqrt((p[0][i]-p[0][l])**2+(p[1][i]-p[1][l])**2)



fig = figure(0)
ax = fig.add_subplot(1, 1, 1)
ax.plot(p[0][:],p[1][:],'x',color='blue')
ax.axis([0,6,0,4])
for i in range(4):
	ax.text(p[0][i],p[1][i],str(i+1),color='b')

fig = figure(1)
ax = fig.add_subplot(1, 1, 1)
ax.plot(p[0][:],p[1][:],'x',color='blue')
ax.plot(p[0][1],p[1][1],'x',color='red')
ax.plot(p[0][:2],p[1][:2],color='red')

kreis=plt.Circle((p[0][1], p[1][1]), radius=d[1,0], color='r',fill=False)
ax.axis([0,6,0,4])
#ax.text(p[0][],p[1][:2],zahlen[:],color='red')
ax.add_patch(kreis)
for i in range(4):
	ax.text(p[0][i],p[1][i],str(i+1),color='b')
ax.text(p[0][1],p[1][1],str(2),color='r')


fig = figure(2)
ax = fig.add_subplot(1, 1, 1)
ax.plot(p[0][:],p[1][:],'x',color='b')
ax.plot(p[0][:2],p[1][:2],'x',color='red')
kreis=plt.Circle((p[0][0], p[1][0]), radius=d[1,0], color='r',fill=False)
ax.axis([0,6,0,4])
ax.add_patch(kreis)
for i in range(4):
	ax.text(p[0][i],p[1][i],str(i+1),color='b')
for i in range(2):
	ax.text(p[0][i],p[1][i],str(i+1),color='r')

fig = figure(3)
ax = fig.add_subplot(1, 1, 1)
ax.plot(p[0][:],p[1][:],'x',color='b')
ax.plot(p[0][:3],p[1][:3],'x',color='red')
kreis=plt.Circle((p[0][2], p[1][2]), radius=d[1,0], color='r',fill=False)
ax.axis([0,6,0,4])
ax.add_patch(kreis)
for i in range(4):
	ax.text(p[0][i],p[1][i],str(i+1),color='b')
for i in range(3):
	ax.text(p[0][i],p[1][i],str(i+1),color='r')
show()
