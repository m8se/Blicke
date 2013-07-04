import pickle
from pylab import *
import random


def choose_randomly(vector):
	sum=0
	r=random.random()
	for b in range(len(vector)):
		sum+=vector[b]
		if(sum>r):
			return b;

def print_ueb_matrix(matrix):
	for a in range(16):
		print "\n"
		for b in range(16):
			print matrix[a,b],

f=open("../Daten/id_lst.data");
ids=pickle.load(f)
print ids;

f2=open("../Daten/zeitreihen.data");
zeitreihen=pickle.load(f2)
print zeitreihen


# Einlesen der Zeitreihendaten
#	zeitreihen[Dyade][Stresslevel][Zeitschritt]



print len(zeitreihen)

# Erstelle fuer Dyade eine Uebergangsmatrix 

num_dyade=len(zeitreihen)
ueb_matrix=zeros([num_dyade,16,16])
for d in range(num_dyade):
	num_steps=4500
	old_status=zeitreihen[d][0][0]
	for i in range(1,num_steps):
		N=0
		new_status=zeitreihen[d][0][i]
		#print new_status
		ueb_matrix[d,old_status,new_status]+=1
		N+=1
		old_status=new_status;	
	
# Normiere die Spalten
	for d in range(num_dyade):
		for a in range(16):		
			SUM=sum(ueb_matrix[d,a])
			if(SUM!=0):
				ueb_matrix[d,a]/=sum(ueb_matrix[d,a])

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

dyade=20
f=open("../Daten/rel_aufenthalt.data")
start_vectors=pickle.load(f)

# Nehme alle uebergebenen Dyaden und finde die entsprechenden Indizes
in_indizes=['3','6']

# Mittle die Aufenthaltswahrscheinlichkeiten
aufenthalts_vector_sum=zeros(17)
ueberg_matrix_sum=zeros([16,16])
N=len(in_indizes)

for i in in_indizes:
	print start_vectors[i,0]
	aufenthalts_vector_sum+=start_vectors[i,0]
	ueberg_matrix_sum+=ueb_matrix[i]

aufenthalts_vector_sum/=N
ueberg_matrix_sum/=N

print "Gemittelte Aufenthaltswahrscheinlichkeit:"
print aufenthalts_vector_sum
print "Gemittelte Uebergangsmatrix:"
print ueberg_matrix_sum
