#! /usr/bin/env python
from numpy import zeros, corrcoef
import pickle
daten=open("Daten/zeitreihen.data", "r")
zeitreihen=pickle.load(daten)
daten.close
rel_aufenthalt=zeros([55,3,16])
#Berechnung der relativen Aufenthaltsw.keiten
for i in range(55):
	for l in range(3):
		zahl=0
		for k in range(4510):
			if (zeitreihen[i,l,k]<=0)|(zeitreihen[i,l,k]>16):
				continue
			zahl+=1
			rel_aufenthalt[i,l,zeitreihen[i,l,k]-1]+=1
		for k in range(16):
			if rel_aufenthalt[i,l,k]!=0:
				rel_aufenthalt[i,l,k]/=float(zahl)
speicher=open("Daten/rel_aufenthalt.data", "w")
pickle.dump(rel_aufenthalt[:],speicher)
speicher.flush()
speicher.close

