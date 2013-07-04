#! /usr/bin/env python
from numpy import zeros, corrcoef, linspace
import pickle
from math import sqrt
from pylab import plot, show, figure

#################
# Ein Array mit der den Abstand von jedem zu jedem Punkt enthaelt wird erzeugt. 
def abstand_matrix(array): # Der array sollte die Aufenthaltswahrscheinlichkeiten enthalten	
	laenge=len(array[:,0])
	breite=len(array[0,:])
	print breite, laenge
	norm=zeros([laenge,laenge])
	for i in range(laenge):
		for l in range(laenge):
			summe=0
			for k in range(breite):
				summe+=(array[i,k]-array[l,k])**2
			#print i,summe
			norm[i,l]=sqrt(summe)
	return norm

def komp_abgl(krit,matrix):
	komp=zeros([len(matrix),len(matrix)])
	for i in range(len(matrix)):
		for l in range(len(matrix)):
			if matrix[i,l]<krit:
				komp[i,l]+=1
	return komp
###################################Abstaende sortieren

# erzeugen eines arrays mit den naechsten nachbarn
def nnachbar(array):# Der array sollte die Aufenthaltswahrscheinlichkeiten enthalten	
	norm=abstand_matrix(array)
	nachbar=zeros([len(norm[:,0]),len(norm[:,0])-1,2])
	for i in range(len(norm[:,0])):
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
	return nachbar				
###########
#Durchfuehrung der hierarchischen clusterung
def gruppen_erzeugen(array):# Der array sollte die Aufenthaltswahrscheinlichkeiten enthalten	
	norm=abstand_matrix(array)
	nachbar=nnachbar(array)
	gruppen=zeros([len(norm[:,0]),len(norm[0,:])])-1
	for i in range(len(norm[:,0])):
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
				break
			gruppen[i,l]=nachbar[gruppen[i,tmp],stelle[gruppen[i,tmp]],0]
			stelle[gruppen[i,tmp]]+=1
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
	return gruppen
#daten=open("Daten/rel_aufenthalt.data", "r")
#aufenthalt_wk=pickle.load(daten)
#daten.close
#aufenthalt_wk_comb=zeros([55,32])
#aufenthalt_wk_comb[:,:16]=aufenthalt_wk[:,0,:]
#aufenthalt_wk_comb[:,16:]=aufenthalt_wk[:,2,:]
#gruppen=gruppen_erzeugen(aufenthalt_wk_comb)
#speicher=open("Daten/gruppen_comb.data", "w")
#pickle.dump(gruppen[:],speicher)
#speicher.flush()
#speicher.close
