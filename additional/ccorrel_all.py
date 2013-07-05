# Skript zur Auswertung von Dyaden
#	Darstellung des Cross Correlation Maximums


import pickle
from pylab import *
import sys
from scipy.signal import argrelextrema
sys.path.append("../")
from hierarchische_clusterung import gruppen_erzeugen

def moving_average(a, n=3) :
    ret = np.cumsum(a, dtype=float)
    return (ret[n - 1:] - ret[:1 - n]) / n

def find_maximum(cor):
	N=2
	avg=moving_average(cor,N)
	avg=avg[:len(avg)-N]
	plot(avg)
	#noch evt. Rauschen beruecksichtigen
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
		while(index>0 and avg[index]==avg[s]):
			index-=1
		if(avg[index]>avg[s]):
			neg=False
		index=s
		while(index<len(avg)-1 and avg[index]==avg[s]):
			index+=1
		print s,index,avg[index],avg[s]

		if(avg[index]<avg[s] and neg):
			maxs+=[s]
			print "yep"
			print "New Maximum"+str(s)



	
	#Grenze bei len(avg)/2
	left=[]
	right=[]
	print "Maxima:"+str(maxs)
	for i in array(maxs):
		print i
		if(i>len(avg)/2):
			right+=[i]
		else:
			left+=[i]
	if(len(right)>0 and len(left)>0):
		nleft=-max(array(left)-len(avg)/2)
		nright=min(array(right)-len(avg)/2)
		if(nright<nleft):
			res=nright
		else:	
			res=-nleft
	else:
		if(len(right)>0):	
			res=min(array(right)-len(avg)/2)
		elif(len(left)>0):
			res=max(array(left)-len(avg)/2)
		else:
			res=100
	print res
	return res


f2=open("../Daten/zeitreihen.data");
zeitreihen=pickle.load(f2)
dyade_num=len(zeitreihen)
#print zeitreihen

f=open("../Daten/id_lst.data");
ids=pickle.load(f)
print ids;

maxs0=[];
maxs2=[]
tau=100
for ind in range(len(zeitreihen)):
 	if(ids[ind]!='299' and ids[ind]!='363'):
		figure(1)
		#Entferne alle Zustaende mit z<0 und z>16
		print "Dyade:"+ids[ind]
	
		zeitreihen_trimmed_m0=[]
		zeitreihen_trimmed_m2=[]
	
		for i in zeitreihen[ind,0]:
			if(i>0 and i<17): # wenn gueltiger Dyadenwert
				zeitreihen_trimmed_m0+=[i-1]
		
		for i in zeitreihen[ind,2]:
			if(i>0 and i<17): # wenn gueltiger Dyadenwert
				zeitreihen_trimmed_m2+=[i-1]
	
		# Berechnung der Kreuzkorrelation:

		if(len(zeitreihen_trimmed_m0)<tau*2+1):
			tau=len(zeitreihen_trimmed_m0)/2-1			
		cor0=list(xcorr(array(zeitreihen_trimmed_m0)//4,array(zeitreihen_trimmed_m0)%4,maxlags=tau)[1])
		tau=100

		if(len(zeitreihen_trimmed_m2)<tau*2+1):
			tau=len(zeitreihen_trimmed_m2)/2			
		cor2=list(xcorr(array(zeitreihen_trimmed_m2)//4,array(zeitreihen_trimmed_m2)%4,maxlags=tau)[1])

		title("Cross Correlation von KuM vor Stress")
	
		# Finde das naechstliegende lokale Maximum
		print len(cor0)
		figure(2)
		maxs0+=[find_maximum(cor0)]
		maxs2+=[find_maximum(cor2)]
	
figure(3)
plot(maxs0,maxs2,'o')

#Klassifiziere die Daten mit der HC Methode

print "Laber:",maxs0[3],maxs2[3]
Maxs0=array(maxs0)
Maxs2=array(maxs2)
vector_list=zeros([len(Maxs0),2])
for k in range(len(Maxs0)):
	vector_list[k]=[Maxs0[k],Maxs2[k]]
print vector_list
groups=gruppen_erzeugen(vector_list)

trimmed_groups=[]

for g in groups:
    for i in range(len(g)):
        if(g[i]==-1):
            trimmed_groups+=[g[:i-1]]
            break


 
N_max=10 # maximal anzuzeigende Gruppen
for g in range(N_max):
    color=rand(3,1)
    for i in ordered_groups[g]:
        scatter(maxs0[int(i)], maxs2[int(i)], s=g*80,edgecolors=color, facecolors='none', linewidths=2, label='Class 2')

#h
show()
