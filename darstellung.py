#! /usr/bin/env python
from numpy import zeros, corrcoef
import pickle
from pylab import *
daten=open("Daten/rel_aufenthalt.data", "r")
rel_aufenthalt=pickle.load(daten)
daten.close
daten=open("Daten/kor_koefs.data", "r")
kor_koefs=pickle.load(daten)
daten.close
#daten=open("Daten/gruppen_opt.data", "r")
#gruppen=pickle.load(daten)
#daten.close
daten=open("Daten/gruppen_norm.data", "r")
gruppen=pickle.load(daten)
daten.close
daten=open("Daten/gruppen_norm_str.data", "r")
gruppen_str=pickle.load(daten)
daten.close


dyaden_gruppen=zeros(55)
for i in range(len(gruppen)):
	break
	for l in range(70):
		if gruppen[i][l]==-1:
			break
		tmp=gruppen[i][l]
		dyaden_gruppen[tmp]+=1
print dyaden_gruppen

bild=0
for k in ([15,49]):
	figure(bild)
	bild+=1
	for i in range(4):
		for l in range(4):
			plot(i,l,'o', ms=100*sqrt(rel_aufenthalt[k,0,4*i+l]), lw=20, mfc='green')
	axis([-1,5,-1,5])
	title("Gruppe")
	xlabel("Kind")
	ylabel("Mutter")


figure(bild)
bild+=1
k=0
kor_koefs_vec=zeros(len(kor_koefs)*(len(kor_koefs)-1)/2)
for i in range(len(kor_koefs)-1):
	break
	for l in range(1,len(kor_koefs)):
		if i<=l:
			continue
		kor_koefs_vec[k]=kor_koefs[i,l]
		k+=1
bins=20
hist(kor_koefs_vec,bins=bins)
show()

