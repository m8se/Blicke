from pylab import *
import pickle

def find_len(liste):
	len=0
	for i in liste:
		if(i==0):
			break;
		len+=1
	return len
		

f2=open("../../Daten/zeitreihen.data");
zeitreihen=pickle.load(f2)
#print zeitreihen

dyade_num=len(zeitreihen)

f=open("../../Daten/id_lst.data");
ids=pickle.load(f)
print ids;

dyaden_ids=[]
for i in range(dyade_num):
	dyaden_ids+=[ids[i]]

# Entferne alle Zustaende mit 0
zeitreihen_trimmed=zeros([dyade_num,3,6000])
lens=zeros([dyade_num,3])
print "Trimming start"
for d in range(dyade_num):
	for m in range(3):
		a=0
		for i in zeitreihen[d,m]:
			if(i>0 and i<17):
				zeitreihen_trimmed[d,m,a]=i-1
				a+=1
		lens[d,m]=a
print "Trimming end"

cors=zeros([dyade_num,2])
for i in range(dyade_num):
	if(i!=3):
		tmp_state=zeitreihen_trimmed[i,0]
		length=lens[i,0]
	
		cors[i,0]=corrcoef(tmp_state[:length]//4,tmp_state[:length]%4)[0,1] #vor Stress
		
		tmp_state=zeitreihen_trimmed[i,2]
		length=lens[i,2]
		print length,
		cors[i,1]=corrcoef(tmp_state[:length]//4,tmp_state[:length]%4)[0,1] #nach Stress

# Generate N random values
xmax=0.6
ymax=0.6
N=50

X=random(N)*xmax
Y=random(N)*ymax


print cors[:,1]
#hist(cors[:,0])
plot(cors[:,0],ones(len(cors[:,0])),'o')
xlabel("Korr.koeff. vor Stress")

figure(2)
#hist(cors[:,1])
plot(cors[:,1],ones(len(cors[:,1])),'o')
xlabel("Korr.koeff. nach Stress")


figure(3)
diff=cors[:,1]-cors[:,0]
hist(diff)
xlabel("Aenderung des Korr.koeff.")
ylabel("Absolute Haeufigkeit")
print mean(diff)



figure(5)
plot(cors[:,0],cors[:,1],'o')
plot(X,Y,'x')
xlabel("Korr.koeff. vor Stress")
ylabel("Korr.koeff. nach Stress")


for i in range(55):
	text(cors[i,0],cors[i,1],dyaden_ids[i])

show()
