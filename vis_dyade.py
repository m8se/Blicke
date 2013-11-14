# Skript zur Auswertung von Dyaden
#	Darstellung von Mutter Kind Zeitreihen
# 	Cross Correlation


from DAO import DAO
import pickle
from pylab import *
import sys

from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
## for Palatino and other serif fonts use:
#rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)

dat_loc='Daten/'
if(len(sys.argv)!=2):
	print "Falscher Programmaufruf:\npython vis_dyade.py <dyaden_nr>"
	#print sys.argv
	exit()

dyade_in=sys.argv[1]

dao=DAO()
zeitreihen_ungestresst=dao.req_rel_auf([dyade_in],DAO.NOT_STRESS)
zeitreihen_gestresst=dao.req_rel_auf([dyade_in],DAO.STRESS)

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
subplot(211)
plot(zeitreihen_trimmed[0]//4)
title("Kind")
ylabel("Zustand")
yticks([0,1,2,3])
subplot(212)
plot(zeitreihen_trimmed[0]%4)
xlabel("t")
ylabel("Zustand")
yticks([0,1,2,3])
title("Mutter")

figure(2)
title("Zustandsaenderungen nach Stress")
subplot(211)
plot(zeitreihen_trimmed[2]//4)
title("Kind")
ylabel("Zustand")
yticks([0,1,2,3])
subplot(212)
plot(zeitreihen_trimmed[2]%4)
ylabel("Zustand")
xlabel("t")
yticks([0,1,2,3])
title("Mutter")

# Berechnung der Kreuzkorrelation:
figure(5)
a=list(xcorr(zeitreihen_trimmed[0]//4,zeitreihen_trimmed[0]%4,maxlags=100)[1])
title("Cross Correlation von KuM vor Stress")
ylabel(r"K($\tau)")
xlabel(r"$\tau")
print a.index(max(a))-100

show()
