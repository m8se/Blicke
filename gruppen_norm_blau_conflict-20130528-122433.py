#! /usr/bin/env python
from numpy import zeros, corrcoef
import pickle
from math import sqrt
from pylab import show, plot, figure, subplot, axis, title, xlabel, ylabel, hist
daten=open("Daten/gruppen_norm.data", "r")
gruppen=pickle.load(daten)
daten.close
daten=open("Daten/gruppen_norm_str.data", "r")
gruppen_str=pickle.load(daten)
daten.close

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
laenge=zeros(len(gruppen[:][0]))
for i in range(len(gruppen[:])):
	zahl=0
	for l in range(len(gruppen[0][:])):
		zahl=l
		print zahl
		if gruppen[i][l]==-1:
			break
	laenge[i]=zahl
#########plot

daten=open("Daten/rel_aufenthalt.data", "r")
rel_aufenthalt=pickle.load(daten)
daten.close		
print len(gruppen)
bild=0
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
#speicher=open("Daten/gruppen_opt.data", "w")
#pickle.dump(gruppen[:],speicher)
#speicher.flush()
#speicher.close

