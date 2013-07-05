# Skript zur Auswertung von Dyaden
#	Darstellung von Mutter Kind Zeitreihen
# 	Cross Correlation


import pickle
from pylab import *
import sys

if(len(sys.argv)!=2):
	print "Falscher Programmaufruf:\npython vis_dyade.py <dyaden_nr>"
	#print sys.argv
	exit()

dyade_in=sys.argv[1]


f2=open("../Daten/zeitreihen.data");
zeitreihen=pickle.load(f2)
dyade_num=len(zeitreihen)
#print zeitreihen

f=open("../Daten/id_lst.data");
ids=pickle.load(f)
print ids;

# Bestimme die Indxnummer fuer die uebergebene Dyade
dyaden_ids=[]
for i in range(dyade_num):
	dyaden_ids+=[ids[i]]
ind=dyaden_ids.index(str(dyade_in))


#Entferne alle Zustaende mit z<0 und z>16
zeitreihen_trimmed=zeros([3,6000])
for m in range(3):
	a=0
	for i in zeitreihen[ind,m]:
		if(i>0 and i<17): # wenn gueltiger Dyadenwert
			zeitreihen_trimmed[m,a]=i-1
			a+=1

#print zeitreihen_trimmed[0]
title("Zustandsaenderungen vor Stress")
plot(zeitreihen_trimmed[0]//4)
plot(zeitreihen_trimmed[0]%4+6)
legend(["Kind","Mutter"])

figure(2)
title("Zustandsaenderungen nach Stress")
plot(zeitreihen_trimmed[2]//4)
plot(zeitreihen_trimmed[2]%4+6)
legend(["Kind","Mutter"])

# Berechnung der Kreuzkorrelation:
figure(5)
a=list(xcorr(zeitreihen_trimmed[0]//4,zeitreihen_trimmed[0]%4,maxlags=100)[1])
title("Cross Correlation von KuM vor Stress")
print a.index(max(a))-100

show()
