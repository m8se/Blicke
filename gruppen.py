#! /usr/bin/env python
from numpy import zeros, corrcoef
import pickle
daten=open("Daten/gruppen.data", "r")
gruppen=pickle.load(daten)
daten.close
for i in range(2000):
	for l in range(70):
		if gruppen[i,l]==-1:
			break
		for k in range(1,70-l):
			if gruppen[i,l+k]==-1:
				break	
			if gruppen[i,l]>gruppen[i,l+k]:
				tmp=gruppen[i,l]
				gruppen[i,l]=gruppen[i,l+k]
				gruppen[i,l+k]=tmp
gruppen=list(gruppen)
for i in range(len(gruppen)):
	if gruppen[i][0]==-1:
		del(gruppen[i:])
		break
print len(gruppen)
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
	for l in range(6):
		if gruppen[i][l]==-1:
			del gruppen[i]
			break
	else:
		i+=1
i=0
while i<len(gruppen):
	l=0
	while l<len(gruppen):
		if l==i:
			l+=1
			continue
		for m in range(70):
			if gruppen[i][m]==-1:
				continue
			for n in range(70):
				if gruppen[l][n]==-1:
					continue
				if gruppen[i][m]==gruppen[l][n]:
					break
			else:
				break
		
		else:
			del(gruppen[i])
			break
		l+=1	
	else:
		i+=1

for z in range(1):
	i=0
	while i<len(gruppen):
		l=0
		while l<len(gruppen):
			fehlt=([0,-1,-1])
			if l==i:
				l+=1
				continue
			for m in range(70):
				if gruppen[i][m]==-1:
					continue
				fehlt[0]+=1
				fehlt[2-fehlt[0]%2]=m
				for n in range(70):
					if gruppen[l][n]==-1:
						continue
					if gruppen[i][m]==gruppen[l][n]:
						fehlt[0]-=1
						break
				else:
					if fehlt[0]>1:
						break
			else:
				for n in range(fehlt[0]):
					m=fehlt[1+n]
					while gruppen[i][m]!=-1:
						gruppen[i][m]=gruppen[i][m+1]
						m+=1
				if l<i:
					i-=1
				del(gruppen[l])
				continue
			l+=1	
		else:
			i+=1
print len(gruppen)
speicher=open("Daten/gruppen_opt.data", "w")
pickle.dump(gruppen[:],speicher)
speicher.flush()
speicher.close

