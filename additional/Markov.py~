import pickle
from pylab import *
import random


# Zufaellige Wahl einea Zustandes, gewichtet durch die Zustandswahrsch.
def choose_randomly(vector):
	SUM=0
	r=random.random()
	for b in range(len(vector)):
		SUM+=vector[b]
		if(SUM>r):
			return b;
		
		if(b==len(vector)-1):
			return random.randint(0,16)

# Darstellung einer Matrix
def print_ueb_matrix(matrix):
	for a in range(16):
		print "\n"
		for b in range(16):
			print matrix[a,b],

f=open("../Daten/id_lst.data");
ids=pickle.load(f)
#print ids;

f2=open("../Daten/zeitreihen.data");
zeitreihen=pickle.load(f2)
#print zeitreihen


# Einlesen der Zeitreihendaten
#	zeitreihen[Dyade][Stresslevel][Zeitschritt]



#print len(zeitreihen)

# Erstelle fuer Dyade eine Uebergangsmatrix 

num_dyade=len(zeitreihen)
ueb_matrix=zeros([num_dyade,16,16])
for d in range(num_dyade):
	num_steps=len(zeitreihen[d][0])
	old_status=zeitreihen[d][0][0]
	for i in range(1,num_steps):
		new_status=zeitreihen[d][0][i]
		#print new_status
		ueb_matrix[d,old_status,new_status]+=1
		old_status=new_status;	
	ueb_matrix[d,:,0]=0

	
# Normiere die Spalten
	for d in range(num_dyade):
		for a in range(16):		
			SUM=sum(ueb_matrix[d,a])
			if(SUM!=0):
				ueb_matrix[d,a]/=SUM

print ""
print_ueb_matrix(ueb_matrix[10])
""" Plot Uebergangsmatrizen
for i in range(10,15):
	pcolor(ueb_matrix[i])
	figure(i)
show()
"""



#
# Model the Markov Process
#

# Einlesen der Aufenthaltswahrscheinlichkeiten

dyade=10
f=open("../Daten/rel_aufenthalt.data")
start_vectors=pickle.load(f)



# Waehle Anfangszustand

state=choose_randomly(start_vectors[dyade,0])

res=[]
N=4500
for i in range(N):
	if(state is None):
		print "Warning"
	state=choose_randomly(ueb_matrix[dyade,state])
	#print state
	res.append(state);

#print res
plot(res)
ylim([0,16])
xlim([0,5000])
title("Simulierte Dyade")

figure(2)
title("Gemessene Dyade")
plot(zeitreihen[dyade][0])
xlim([0,5000])
ylim([0,16])
show()
