#! /usr/bin/env python
from numpy import zeros, corrcoef
import pickle
from math import sqrt
import matplotlib
import matplotlib.pyplot as plt
from pylab import show, plot, figure, subplot, axis,ylim,xlim , title, xlabel, ylabel, hist, text
daten=open("Daten/gruppen_norm.data", "r")
gruppen_n=pickle.load(daten)
daten.close
daten=open("Daten/gruppen_norm_str.data", "r")
gruppen=pickle.load(daten)
daten.close

daten = open("Daten/id_lst.data", "r")
id_lst=pickle.load(daten)
daten.close

#gruppen=gruppen_str

for i in range(len(gruppen[0,:])):
	for l in range(len(gruppen[0,:])):
		if gruppen[i,l]==-1:
			break
		for k in range(1,len(gruppen[0,:])-l):
			if gruppen[i,l+k]==-1:
				break	
			if gruppen[i,l]>gruppen[i,l+k]:
				tmp=gruppen[i,l]
				gruppen[i,l]=gruppen[i,l+k]
				gruppen[i,l+k]=tmp
gruppen=list(gruppen)
i=0
while i<(len(gruppen)-1):
	l=i+1
	while l<(len(gruppen)):
		if (gruppen[i]==gruppen[l]).all():
			del(gruppen[l])
		else:
			l+=1
	i+=1
print len(gruppen)
i=0
while i<len(gruppen):	
	if gruppen[i][len(gruppen[0][:])-1]==-1:
		i+=1
	else:
		del gruppen[i]
		print "hey"
def kuerzen():
	i=0
	while i<len(gruppen):
		break
		if gruppen[i][3]==-1:
			del gruppen[i]
		else:
			i+=1
	i=0
	while i<len(gruppen):
		break
		if gruppen[i][5]!=-1:
			del gruppen[i]
		else:
			i+=1
gruppen.append(range(len(gruppen[0][:])))
def laengen(gruppen):
	laenge=zeros(len(gruppen))
	for i in range(len(gruppen)):
		zahl=0
		for l in range(len(gruppen[0][:])):
			zahl=l
			if gruppen[i][l]==-1:
				break
		laenge[i]=zahl
	return laenge
laenge=laengen(gruppen)
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
ytiles=15

dx=xlen/xtiles
dy=ylen/ytiles



frame1=plt.gca()
frame1.axes.get_xaxis().set_visible(False)
frame1.axes.get_yaxis().set_visible(False)






###############
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
a=zuordnen(gruppen)
def diagramm(ref,gruppen,laenge):
	stelle=zeros([len(laenge),2])-1
	#text(0,0,"0")
	stelle[0,:]=([0,1])
	draw_dyade(0,0,id_lst)
	for i in range(len(laenge)):
		for l in range(6):
			if ref[i,l]==-1:
				break
			uebergabe=zeros([laenge[int(ref[i,l])]])
			for z in range(int(laenge[int(ref[i,l])])):
				uebergabe[z]=id_lst[int(gruppen[int(ref[i,l])][z])]
			#uebergabe=gruppen[int(ref[i,l])][:laenge[int(ref[i,l])]]
			print str(uebergabe[0])
			draw_dyade(int(stelle[i,0]),int(stelle[i,1]),uebergabe)
			stelle[ref[i,l],0]=stelle[i,0]
			stelle[ref[i,l],1]=stelle[i,1]+1
			stelle[i,0]+=laenge[ref[i,l]]
	#ylim([0,15])
	#xlim([0,57])
	#plt.axis([0,54,0,9])
	plt.show()
diagramm(a,gruppen,laenge)
#a_l=laengen(a[0])

#################




#########plot
def daten_pl():
	daten=open("Daten/rel_aufenthalt.data", "r")
	rel_aufenthalt=pickle.load(daten)
	daten.close		
	for h in range(len(gruppen)):
		break
		figure(bild)
		for j in range(4):
			k=gruppen[h][j]
			subplot(220+j)
			for i in range(4):
				for l in range(4):
					plot(i,l,'o', ms=100*sqrt(rel_aufenthalt[k,0,4*i+l]), lw=20, mfc='green')
			axis([-1,5,-1,5])
			title("Gruppe")
			xlabel("Kind")
			ylabel("Mutter")
		bild+=1
	figure(bild)
	bins=20
	hist(laenge,bins=bins)
	show()

def gruppen_pl():
	boxplot([1,2,3,4])
	show()

#speicher=open("Daten/gruppen_opt.data", "w")
#pickle.dump(gruppen[:],speicher)
#speicher.flush()
#speicher.close

