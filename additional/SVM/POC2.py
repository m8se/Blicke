print __doc__ 

from pylab import *
from sklearn import svm, datasets

iris=datasets.load_iris()

X=iris.data[:,:2]
Y=iris.target

clf=svm.SVC(C=1.,kernel='rbf',probability=True)
clf.fit(X,Y)

h=.02
x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
Z = clf.predict_proba(np.c_[xx.ravel(), yy.ravel()])
print Z
