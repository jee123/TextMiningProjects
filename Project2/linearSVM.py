# -*- coding: utf-8 -*-

import cPickle,gzip
import numpy as np
from sklearn import svm
from sklearn import cross_validation
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import roc_curve
import matplotlib.pyplot as plt

with gzip.open("train_data.pkl.gz",'rb') as g:
  train_data=cPickle.load(g)
g.close() 

with gzip.open("test_data.pkl.gz",'rb') as g:
  test_data=cPickle.load(g)
g.close() 
label_test=test_data[1]

clf = svm.SVC(kernel = 'linear')
scores = cross_validation.cross_val_score(clf, train_data[0], train_data[1], cv=5)

print '\n'
clf.fit(train_data[0],train_data[1])
predicted = clf.predict(test_data[0])
print np.mean(predicted == label_test) 
print confusion_matrix(label_test, predicted)
print precision_score(label_test, predicted)
print recall_score(label_test, predicted)
fpr,tpr,threshold=roc_curve(label_test,predicted)
plt.plot(fpr,tpr)
plt.xlabel('false positive rate')
plt.ylabel('true positive rate')
plt.title('ROC curve for linear SVM')
plt.savefig('ROC_SVM')
