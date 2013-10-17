#! /usr/bin/env python
from numpy import zeros, corrcoef
import pickle
from math import sqrt
import matplotlib
import matplotlib.pyplot as plt
from pylab import show, plot, figure, subplot, axis,ylim,xlim , title, xlabel, ylabel, hist, text
from hierarchische_clusterung import gruppen_erzeugen
from DAO import DAO
import sys
id_lst=sys.argv[1]
stress=sys.argv[2]
print stress
Titel='Normal'

gruppen=gruppen_erzeugen(daten.req_rel_auf([299,240,325,245],DAO.STRESS))

#Doppelte Gruppen werden entfernt

#	for i in range(len(gruppen[0,:])):
#		for l in range(len(gruppen[0,:])):
#			if gruppen[i,l]==-1:
#				break
#			for k in range(1,len(gruppen[0,:])-l):
#				if gruppen[i,l+k]==-1:
#					break	
#				if gruppen[i,l]>gruppen[i,l+k]:
#					tmp=gruppen[i,l]
#					gruppen[i,l]=gruppen[i,l+k]
#					gruppen[i,l+k]=tmp
gruppen=list(gruppen)
def gruppen_doppelt(gruppen):
	i=0
	while i<(len(gruppen)-1):
		l=i+1
		while l<(len(gruppen)):
			if (gruppen[i]==gruppen[l]).all():
				del(gruppen[l])
			else:
				l+=1
		i+=1
	i=0
	while i<len(gruppen):	
		if gruppen[i][len(gruppen[0][:])-1]==-1:
			i+=1
		else:
			del gruppen[i]
	print gruppen
	gruppen.append(range(len(gruppen[0][:])))
	print gruppen

gruppen_doppelt(gruppen)
#Die Laengen der Arrays werden ermittelt
def laengen(gruppen):
	laenge=zeros(len(gruppen))
	for i in range(len(gruppen)):
		zahl=0
		for l in range(len(gruppen[0][:])):
			print "hep", gruppen[i][l]
			if gruppen[i][l]==-1:
				print "break"
				break
			zahl=l
		laenge[i]=zahl
	return laenge
laenge=laengen(gruppen)
print "l:",laenge
#gruppe werden der Laenge nach sortiert
def sortieren(gruppen,laenge):
	for i in range(len(laenge)):
		for l in range(i+1,len(laenge)):
			if laenge[i]<laenge[l]:
				tmp=gruppen[l]
				gruppen[l]=gruppen[i]
				gruppen[i]=tmp
				tmp=laenge[l]
				laenge[l]=laenge[i]
				laenge[i]=tmp
sortieren(gruppen,laenge)
##############
#Der Plot von Kaesten mit Textfuellung an einer bestimmten Position
font_size=6
fig = plt.figure()
ax = fig.add_subplot(111)

ylen=400	
xlen=400
xtiles=54
ytiles=10


def draw_dyade(x,y,dyads):
	dyade_len=len(dyads)
	rect1 = matplotlib.patches.Rectangle((x*dx,y*dy), dx*dyade_len, dy, facecolor='white',edgecolor='black')
	ax.add_patch(rect1)
	plt.xlim([0,xlen])
	plt.ylim([0,ylen])
	for i in range(dyade_len):
		if(i!=(dyade_len-1)):
        		plt.text((x+i)*dx,(y+0.5)*dy,str(int(dyads[i]))+",",size=font_size)
		else:
			plt.text((x+i)*dx,(y+0.5)*dy,str(int(dyads[i])),size=font_size)

xlen=400
ylen=400
xtiles=55
ytiles=25
dx=xlen/xtiles
dy=ylen/ytiles
frame1=plt.gca()
frame1.axes.get_xaxis().set_visible(False)
frame1.axes.get_yaxis().set_visible(False)






###############
#Die Gruppen werden fuer die Darstellung sortiert
def zuordnen(gruppen):
	ref=zeros([len(gruppen),6])-1
	for i in range(len(gruppen)-1):
		l=0
		while True:
			l+=1
			if gruppen[-1-i][0] in gruppen[-1-l-i]:
				k=0
				while True:
					if ref[-1-l-i][k]==-1:
						ref[-1-l-i][k]=len(gruppen)-1-i
						break
					k+=1
				break

	return ref
print gruppen
a=zuordnen(gruppen)
#
#Diagramm mit den Gruppen wird erstellt
def diagramm(ref,gruppen,laenge):
	stelle=zeros([len(laenge),2])-1
	stelle[0,:]=([0,1])
	draw_dyade(0,0,id_lst)
	for i in range(len(laenge)):
		for l in range(6):
			if ref[i,l]==-1:
				break
			uebergabe=zeros([laenge[int(ref[i,l])]])
			for z in range(int(laenge[int(ref[i,l])])):
				uebergabe[z]=id_lst[int(gruppen[int(ref[i,l])][z])]
			print str(uebergabe[0])
			draw_dyade(int(stelle[i,0]),int(stelle[i,1]),uebergabe)
			stelle[ref[i,l],0]=stelle[i,0]
			stelle[ref[i,l],1]=stelle[i,1]+1
			stelle[i,0]+=laenge[ref[i,l]]
	plt.title(Titel)
	plt.show()
diagramm(a,gruppen,laenge)

#################

