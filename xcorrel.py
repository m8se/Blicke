# Skript zur Auswertung von Dyaden
#	Darstellung des Cross Correlation Maximums


import pickle
from pylab import *# plot, ylim, show, title
import sys
from scipy.signal import argrelextrema
dat_loc='Daten/'
def moving_average(a, n=3) :
    ret = np.cumsum(a, dtype=float)
    return (ret[n - 1:] - ret[:1 - n]) / n

def find_maximum(cor):
	N=4
	#noch evt. Rauschen beruecksichtigen
	avg=moving_average(cor,N)
	avg=avg[:len(avg)-N]
	ylim([0,max(avg)])
	plot(avg)

	maxs=argrelextrema(avg,np.greater)[0]
	for m in maxs:
		plot(m,avg[m],'o')

	# Check for saddle points
	saddles=[]
	saddle=0
	for i in range(len(avg)-1):
		if(avg[i]==avg[i+1]):
			saddle+=1
		else:
			if(saddle!=0):
				saddles+=[i-saddle/2]
				saddle=0

	#check if saddles should be maxima
	maxs=list(maxs)
	for s in saddles:
		print "Current saddle:"+str(s)
		index=s
		neg=True
		while(abs(avg[index]-avg[s])<1E-3):
			index-=1
		if(avg[index]>avg[s]):
			neg=False
		index=s
		while(abs(avg[index]-avg[s])<1E-3):
			index+=1
		print s,index,avg[index],avg[s]

		if(avg[index]<avg[s] and neg):
			maxs+=[s]
			print "yep"
			print "New Maximum"+str(s)


	for m in maxs:
		plot(m,avg[m],'o')
	for s in saddles:
		plot(s,avg[s],'x')
	
	
	#Grenze bei len(avg)/2
	left=[]
	right=[]
	print "Saddles:"+str(saddles)
	print "Maxima:"+str(maxs)
	show()
		
	for i in array(maxs):
		print i
		if(i>len(avg)/2):
			right+=[i]
		else:
			left+=[i]
	res=[min(array(right)-len(avg)/2),-max(array(left)-len(avg)/2)]
	print res
	if(res[0]<res[1]):
		print res[0]
	else:
		print -res[1]

	

dyade_in=sys.argv[1]

f=open(dat_loc+"zeitreihen.data");
zeitreihen=pickle.load(f)
f.close()
dyade_num=len(zeitreihen)
#print zeitreihen

f=open(dat_loc+"id_lst.data");
ids=pickle.load(f)
f.close()

print ids;

# Bestimme die Indexnummer fuer die uebergebene Dyade
dyaden_ids=[]
for i in range(dyade_num):
	dyaden_ids+=[ids[i]]
ind=dyaden_ids.index(str(dyade_in))


#Entferne alle Zustaende mit z<=0 und z>16
zeitreihen_trimmed_m0=[]
zeitreihen_trimmed_m2=[]

for i in zeitreihen[ind,0]:
	if(i>0 and i<17): # wenn gueltiger Dyadenwert
		zeitreihen_trimmed_m0+=[i-1]

for i in zeitreihen[ind,2]:
	if(i>0 and i<17): # wenn gueltiger Dyadenwert
		zeitreihen_trimmed_m2+=[i-1]


# Berechnung der Kreuzkorrelation:
figure(5)
cor=list(xcorr(array(zeitreihen_trimmed_m0)//4,array(zeitreihen_trimmed_m0)%4,maxlags=100)[1])
title("Cross Correlation von KuM vor Stress")

# Finde das naechstliegende lokale Maximum
print len(cor)





figure(2)
find_maximum(cor)

"""
# Finde lokales Maximum, rechts von 0
for i in range(start,2*start):
	if((avg[i+1]-avg[i])*(avg[i+2]-avg[i+1])<0 and avg[i+1]>avg[i+2]):
		resr=i+1
		break	
		
#Finde lokales Maximum links von 0
rg=range(0,start)
rg.reverse()
resl=0
for i in rg:
	if((avg[i]-avg[i-1])*(avg[i-1]-avg[i-2])<0 and avg[i-1]>avg[i]):
		resl=i-1
		break	
print resl
print min([resr-100,resl-100])
"""

#resr=min(maxs[:])
#resl=min(maxs[:97])
#print resr,resl


