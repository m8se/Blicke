#! /usr/bin/env python
from numpy import zeros, corrcoef
import pickle
from math import sqrt
daten=open("Daten/rel_aufenthalt.data", "r")
rel_aufenthalt=pickle.load(daten)
daten.close
zahl=1
norm=zeros([55,55])
gruppen=zeros([2000,70])-1
for i in range(55):
	print i
	for l in range(55):
		summe=0
		for k in range(16):
			summe+=(rel_aufenthalt[i,0,k]-rel_aufenthalt[l,0,k])**2
		norm[i,l]=sqrt(summe)
print norm
speicher=open("Daten/norm.data", "w")
pickle.dump(norm[:],speicher)
speicher.flush()
speicher.close
krit=0.3
for i in range(55):
	break 
	print i
	for l in range(55):
		if l<=i:
			continue
		if norm[i,l]<krit:
			finish=0
			doppel=0
			for m in range(2000):
				for n in range(70):
					if (gruppen[m,n]==i)&(doppel==0):
						for k in range(70):
							if (gruppen[m,k]!=-1):
								if (norm[l,gruppen[m,k]]>krit):
									break
								if(norm[l,gruppen[m,k]]==1):
									break
							else:
								gruppen[m,k]=l
								break
					elif (gruppen[m,n]==l)&(doppel==0):
						for k in range(70):
							if gruppen[m,k]!=-1:
								if (norm[i,gruppen[m,k]]<krit):
									break
								if (norm[i,gruppen[m,k]]==1):
									break
							else:
								gruppen[m,k]=i
								break
					elif (n==0)&(gruppen[m,n]==-1):
						gruppen[m,n]=i
						gruppen[m,n+1]=l
						finish=1
						break
				if finish==1:
					break	
speicher=open("Daten/gruppen_norm.data", "w")
pickle.dump(gruppen[:],speicher)
speicher.flush()
speicher.close
