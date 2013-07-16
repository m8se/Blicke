#! /usr/bin/env python
from numpy import zeros, corrcoef, linspace
import pickle
from math import sqrt
from pylab import plot, show, figure
daten=open("Daten/rel_aufenthalt.data", "r")
rel_aufenthalt=pickle.load(daten)
daten.close
zahl=1
norm=zeros([55,55])
stress=0
for i in range(55):
	print i
	for l in range(55):
		summe=0
		for k in range(16):
			summe+=(rel_aufenthalt[i,stress,k]-rel_aufenthalt[l,stress,k])**2
		norm[i,l]=sqrt(summe)
def komp_abgl(krit,matrix):
	komp=zeros([len(matrix),len(matrix)])
	for i in range(len(matrix)):
		for l in range(len(matrix)):
			if matrix[i,l]<krit:
				komp[i,l]+=1
	return komp
###################################Abstaende sortieren
nachbar=zeros([len(norm[:,0]),len(norm[:,0])-1,2])
for i in range(len(norm[:,0])):
	print i
	stelle=range(len(norm[:,0]))
	del(stelle[i])
	for l in range(len(norm[0,:])-1):
		tmp=[2,0,0]
		point=0
		for k in stelle:
			if tmp[0]>norm[i,k]:
				tmp[0]=norm[i,k]
				tmp[1]=k
				tmp[2]=point
			point+=1
		else:
			nachbar[i,l,0]=tmp[1]
			nachbar[i,l,1]=tmp[0]
			del(stelle[tmp[2]])
print nachbar				
###########
gruppen=zeros([len(norm[:,0]),len(norm[0,:])])-1
for i in range(len(norm[:,0])):
	print i
	stelle=zeros(len(norm[:,0]))
	gruppen[i,0]=i
	gruppen[i,1]=nachbar[i,0,0]
	abstand=nachbar[i,0,1]
	stelle[i]+=1
	for l in range(2,len(norm[:,0])):
		for k in range(l):
			h=0
			while h!=l:
				if nachbar[gruppen[i,k],stelle[gruppen[i,k]],0]==gruppen[i,h]:
					stelle[gruppen[i,k]]+=1
					h=0
				else:
					h+=1
		tmp=0
		for k in range(1,l):
			if nachbar[gruppen[i,tmp],stelle[gruppen[i,tmp]],1]>nachbar[gruppen[i,k],stelle[gruppen[i,k]],1]:
				tmp=k
		if nachbar[gruppen[i,tmp],stelle[gruppen[i,tmp]],1]>abstand:
			print 'raus'
			break
		print tmp
		gruppen[i,l]=nachbar[gruppen[i,tmp],stelle[gruppen[i,tmp]],0]
		stelle[gruppen[i,tmp]]+=1
if stress==0:		
	speicher=open("Daten/gruppen_norm.data", "w")
	pickle.dump(gruppen[:],speicher)
	speicher.flush()
	speicher.close
	
if stress==2:		
	gruppen_str=gruppen
	speicher=open("Daten/gruppen_norm_str.data", "w")
	pickle.dump(gruppen_str[:],speicher)
	speicher.flush()
	speicher.close
