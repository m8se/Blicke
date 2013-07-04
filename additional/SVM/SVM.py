print __doc__ 

from pylab import *
from sklearn import svm, datasets
import pickle


dyads=[272,223,243,15,282,312,325,340,245,204,357,299,240,310,347,242,288,304,318,319,327,328,254,256,344,372,375,378,381,274,284,300,303,307,343,363,257,277,302,314,315,320,338,348,349,365]
classes=[1,1,1,2,2,2,2,2,2,3,3,4,4,5,5,6,6,6,6,6,6,6,6,6,6,6,6,6,6,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7]

f=open("../../Daten/rel_aufenthalt.data")
start_vectors=pickle.load(f)

f=open("../../Daten/id_lst.data");
ids=pickle.load(f)
print ids; 	

X=[]
# convert dyad nums to list entries
for dyad in dyads:
	i=ids.index(str(dyad))
	X+=[start_vectors[i,0]]

print X
print len(X)
Y=classes
print len(Y)

clf=svm.LinearSVC(C=1.0)
clf.fit(X,Y)
Z = clf.predict(X)

print Z
