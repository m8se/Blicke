import pickle
from pylab import plot, figure, show, scatter, xlabel, ylabel, zeros, random, subplot, ones, text, hist, rand	

import sys
sys.path.append("../")
from hierarchische_clusterung import gruppen_erzeugen
from DAO import DAO
data_path=''

dao=DAO();
dyaden_ids=dao.convertToList(sys.argv[1])
zeitreihen=dao.req_zeitreihen(dyaden_ids,DAO.NOT_STRESS|DAO.STRESS)

dyade_num=len(dyaden_ids)

# Bestimme fuer eine bestimmte Dyade die Staytime im ungestressten und gestressten Zustand
# Fuer die Auswertung interessiert lediglich das Verhalten der Mutter
#
# Die Zustaende sind von 1-16. Der Zustand 0 steht fuer "Keine Daten"
# Deswegen wird vor dem Einlesen jeder zust. -1 gerechnet
#
# Frage: Welche Zeitreihe ist M --> die 2., deswegen Mod.
# 
# Klassifikation nach relativer Aenderung der Zustandsaenderg.rate
"""
Auswertung:
	- Fig. 1, ziemlich gleichverteilt im Intervall 0-0,6
	- im Mittel nimmt die Rate nur geringfuegig ab
	- Klass. moeglich nach Abnahme und Zunahme
"""
#


freqs=zeros([dyade_num,3])
dt=0.04
for d in range(dyade_num):
	max=2
	for mode in range(max):
		data_len=len(zeitreihen[d,mode])
		old_status=(zeitreihen[d,mode,0]-1)%4	# Mutter ist 2. eingelesener Wert
		num_changes=0
		steps=0
		for i in range(1,data_len):
			if(zeitreihen[d,mode,i]>0 and zeitreihen[d,mode,i]<17):
				new_status=(zeitreihen[d,mode,i]-1)%4
				steps+=1	
				if(new_status!=old_status):
					num_changes+=1
				old_status=new_status
		freqs[d,mode]=num_changes/(steps*dt);

# Generate N random values
xmax=0.8
ymax=0.8
N=50

X=random(N)*xmax
Y=random(N)*ymax

# Plot big freqs
figure(1)
plot(freqs[:,0],freqs[:,1],'o')
plot(X,Y,'x')
xlabel("Durchschnittliche Zustandsaenderungsrate vor Stress")
ylabel("Durchschnittliche Zustandsaenderungsrate nach Stress")

# Plot the freqs
figure(2)
#print freqs
subplot(221)
plot(X,Y,'x')
plot(freqs[:,0],freqs[:,1],'o')
xlabel("Durchschnittliche Zustandsaenderungsrate vor Stress")
ylabel("Durchschnittliche Zustandsaenderungsrate nach Stress")
subplot(223)
plot(freqs[:,0],ones(len(freqs[:,0])),'o')
subplot(222)	
plot(ones(len(freqs[:,1])),freqs[:,1],'o')	
subplot(221)
#xlim([0,1])
#ylim([0,1])
for i in range(dyade_num):
	text(freqs[i,0],freqs[i,1],dyaden_ids[i])
	

# Aenderungen
figure(4)

hist((freqs[:,1]-freqs[:,0]))
xlabel("Aenderung der durchschnittlichen Zustandsaenderungsrate")
ylabel("Absolute Haeufigkeit")
#print(mean(freqs[:,2]-freqs[:,0]))


figure(5)
#plot((freqs[:,1]-freqs[:,0])/freqs[:,0],ones(len(freqs[:,1])),'o')
hist((freqs[:,1]-freqs[:,0])/freqs[:,0])
xlabel("relative Aenderung der durchschnittlichen Zustandsaenderungsrate")
ylabel("Absolute Haeufigkeit")


data=[freqs[:,0],freqs[:,2]]
vector_list=zeros([len(freqs[:,2]),2])
for k in range(len(freqs[:,2])):
	vector_list[k]=[freqs[:,0][k],freqs[:,1][k]]

#print data
#print vector_list

# use hierarchic clustering

groups=gruppen_erzeugen(vector_list)

print "Groups: "+str(groups)
trimmed_groups=[]

for g in groups:
    g_list=list(g)
    try:
        ind=g_list.index(-1)
        trimmed_groups+=[g[:ind]]
    except:
        trimmed_groups+=[g]

print "Trimmed groups: "+str(trimmed_groups)



sorted_groups = sorted(trimmed_groups, key=len)
sorted_groups.reverse()

print "Sorted groups: "


# print groups
for g in sorted_groups:
	print "[",
	for el in g:
		print dyaden_ids[int(el)],
	print "]"

# draw the ten biggest groups

figure(1)

N_max=5 # maximal anzuzeigende Gruppen
if(N_max>len(sorted_groups)):
    N_max=len(sorted_groups)
    
for g in range(N_max):
	color=rand(3,1)
	for i in sorted_groups[g]:
		scatter(freqs[:,0][i], freqs[:,1][i], s=g*80,edgecolors=color, facecolors='none', linewidths=2, label='Class 2')
for i in range(dyade_num):
	text(freqs[i,0],freqs[i,1],dyaden_ids[i])
show()	
