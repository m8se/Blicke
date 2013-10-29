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
	gruppen.append(range(len(gruppen[0][:])))


#Die Laengen der Arrays werden ermittelt
def laengen(gruppen):
	laenge=zeros(len(gruppen))
	for i in range(len(gruppen)):
		zahl=0
		for l in range(len(gruppen[0][:])):
			if gruppen[i][l]==-1:
				break
			zahl=l+1
		laenge[i]=zahl
	return laenge

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
	ref=zeros([len(gruppen),12])-1 #Jede Gruppe wird der groesseren Gruppe zugeordnet mit der sie die groesst moegliche Ueberschneidung hat  
	for i in range(len(gruppen)-1):
		l=0
		while True:
			l+=1
			if gruppen[-1-i][0] in gruppen[-1-l-i]:
				k=0
				while True:
					if ref[-1-l-i][k]==-1: #freien Platz suchen 
						ref[-1-l-i][k]=len(gruppen)-i-1
						break
					k+=1
				break

	return ref

#
#Diagramm mit den Gruppen wird erstellt
def diagramm(ref,gruppen,laenge):
	stelle=zeros([len(laenge),2])-1
	stelle[0,:]=([0,1])
	draw_dyade(0,0,id_lst)
	for i in range(len(laenge)-1):
		for l in range(6):	
			if ref[i,l]!=-1:
				uebergabe=zeros([laenge[int(ref[i,l])]])
				for z in range(int(laenge[int(ref[i,l])])):
					uebergabe[z]=id_lst[int(gruppen[int(ref[i,l])][z])]
				draw_dyade(int(stelle[i,0]),int(stelle[i,1]),uebergabe)
				stelle[ref[i,l],0]=stelle[i,0]
				stelle[ref[i,l],1]=stelle[i,1]+1
				stelle[i,0]+=laenge[ref[i,l]]
	plt.title(Titel)
	plt.show()


#################
daten=DAO()
id_lst_c=sys.argv[1][1:-1].split(',')
stress=int(sys.argv[2])
if stress==1:
	Titel='Stressfrei'
elif stress==4:
	Titel='Gestresst'
elif stress==5:
	Titel='Stressfrei & Gestresst'
elif stress==8:
	Titel='Stressfrei & Gestresst'
id_lst=[]
for i in id_lst_c:
	id_lst.append(int(i))
daten_roh=daten.req_rel_auf(id_lst,stress)
if stress==5:
	for i in id_lst_c:
		id_lst.append(int(i))
st_number=len(daten_roh[0,:,0])
dyad_number=len(daten_roh[:,0,0])
dim_number=len(daten_roh[0,0,:])
daten_ready=[]
daten_ready=zeros([st_number*dyad_number,dim_number])
for i in range(st_number):
	daten_ready[i*dyad_number:(i+1)*dyad_number][:]=daten_roh[:,i,:]
#daten_ready=daten.req_rel_auf(id_lst,DAO.STRESS)[:,0,:]
print "ready", daten_ready, "\n"

#gruppen=list(gruppen_erzeugen(daten.req_rel_auf(id_lst,DAO.STRESS)[:,0,:]))
gruppen=list(gruppen_erzeugen(daten_ready))
print gruppen
gruppen_doppelt(gruppen)
laenge=laengen(gruppen)
sortieren(gruppen,laenge)
a=zuordnen(gruppen)
diagramm(a,gruppen,laenge)

