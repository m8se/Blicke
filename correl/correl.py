#! /usr/bin/env python
from pylab import show, plot, xlabel, ylabel, rand, scatter
import pickle
from scipy import zeros, corrcoef
from numpy.random import random
from numpy import ones
from pylab import figure,hist,mean,text
import sys
import numpy
sys.path.append(".")
from hierarchische_clusterung import gruppen_erzeugen 
sys.path.append("../")
from DAO import DAO
import tkMessageBox


dao=DAO();
reqs=DAO.convertToList(sys.argv[1])
zeitreihen=dao.req_zeitreihen(reqs,DAO.STRESS|DAO.NOT_STRESS)
dyade_num=len(reqs)

# Entferne alle Zustaende mit 0
zeitreihen_trimmed=zeros([dyade_num,2,6000])
lens=zeros([dyade_num,3])

# Erstelle getrimmte Zeitreihe ohne 0 ( keine Daten) Zustaende
print "Trimming start"
for d in range(dyade_num):
	for m in range(2):
		a=0
		for i in zeitreihen[d,m]:
			if(i>0 and i<17):
				zeitreihen_trimmed[d,m,a]=i-1
				a+=1
		lens[d,m]=a
print "Trimming end"



cors=zeros([dyade_num,2])
for i in range(dyade_num):
	#if(i!=3):	#Schliesse ungeeignete Dyadn aus
		tmp_state=zeitreihen_trimmed[i,0]
		length=lens[i,0]
		cors[i,0]=corrcoef(tmp_state[:length]//4,tmp_state[:length]%4)[0,1] #vor Stress
		
		tmp_state=zeitreihen_trimmed[i,1]
		length=lens[i,1]
		print length,
		cors[i,1]=corrcoef(tmp_state[:length]//4,tmp_state[:length]%4)[0,1] #nach Stress

# Generate N random values
xmax=0.6
ymax=0.6
N=50
X=random(N)*xmax
Y=random(N)*ymax

for c in range(dyade_num):
	i=cors[:,1][c]
	if(numpy.isnan(i)):
		tkMessageBox.showinfo("Dyaden","Dyade "+str(reqs[c])+" kann zu fehlerhaften Darstellungen fuehren wegen nicht definiertem CorrCoeff.")
		print "contains Errors"

print str(cors[:,1])

plot(cors[:,0],cors[:,1],'o')
plot(X,Y,'x')
xlabel("Korr.koeff. vor Stress")
ylabel("Korr.koeff. nach Stress")

for i in range(dyade_num):
	if(reqs[i]!=247):	# Scliesse ungeeignet Dyaden aus
		text(cors[i,0],cors[i,1],str(reqs[i]))


vector_list=zeros([len(cors),2])

for k in range(len(cors)):
	vector_list[k]=cors[k][:1]

groups=gruppen_erzeugen(vector_list)

trimmed_groups=[]


# Erstelle richtige Gruppen, d.h. eliminiere hinten stehende -1
for g in groups:
    g_list=list(g)
    try:
        ind=g_list.index(-1)
        trimmed_groups+=[g[:ind]]
    except:
        trimmed_groups+=[g]

# Ordne die Gruppen alphabetisch
ordered_groups = sorted(trimmed_groups, key=len)
ordered_groups.reverse()

print "Gruppen:",groups
print "Trimmed Gruppen:",trimmed_groups
print "Sorted Gruppen:",trimmed_groups

# Zeige die 10 groessten Gruppen an
N_max=10 # maximal anzuzeigende Gruppen
if(N_max>len(ordered_groups)):
    N_max=len(ordered_groups)
for g in range(N_max):
    color=rand(3,1)
    for i in ordered_groups[g]:
        scatter(cors[int(i),0], cors[int(i),1], s=g*80,edgecolors=color, facecolors='none', linewidths=2, label='Class 2')

for i in range(len(cors)):
    text(cors[i,0], cors[i,1],reqs[i])


		
figure(2)
hist(cors[:,0])
xlabel("Korr.koeff. vor Stress")
ylabel("Absolute Haeufigkeit")

figure(3)
diff=cors[:,1]-cors[:,0]
for i in range(len(diff)):
	print str(reqs[i])+":"+str(cors[i,1])

hist(diff)
xlabel("Aenderung des Korr.koeff.")
ylabel("Absolute Haeufigkeit")
print mean(diff)



figure(4)
hist(cors[:,0])
ylabel("Absolute Haeufigkeit")
xlabel("Korr.koeff. vor Stress")



show()