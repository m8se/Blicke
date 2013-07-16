#! /usr/bin/env python
from numpy import zeros, corrcoef
import pickle
daten=open("Daten/rel_aufenthalt.data", "r")
rel_aufenthalt=pickle.load(daten)
daten.close
zahl=1
kor_koefs=zeros([55,55])
gruppen=zeros([2000,70])-1
for i in range(55):
	for l in range(55):
		kor=corrcoef(rel_aufenthalt[i,0,:],rel_aufenthalt[l,0,:])
		kor_koefs[i,l]=kor[0,1]
speicher=open("Daten/kor_koefs.data", "w")
pickle.dump(kor_koefs[:],speicher)
speicher.flush()
speicher.close
for i in range(55):
	for l in range(55):
		if l<=i:
			continue
		if kor_koefs[i,l]>0.95:
			finish=0
			doppel=0
			for m in range(2000):
				for n in range(70):
					if (gruppen[m,n]==i)&(doppel==0):
						for k in range(70):
							if (gruppen[m,k]!=-1):
								if (kor_koefs[l,gruppen[m,k]]<0.95):
									break
								if(kor_koefs[l,gruppen[m,k]]==1):
									break
							else:
								gruppen[m,k]=l
								break
					elif (gruppen[m,n]==l)&(doppel==0):
						for k in range(70):
							if gruppen[m,k]!=-1:
								if (kor_koefs[i,gruppen[m,k]]<0.95):
									break
								if (kor_koefs[i,gruppen[m,k]]==1):
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
speicher=open("Daten/gruppen.data", "w")
pickle.dump(gruppen[:],speicher)
speicher.flush()
speicher.close
