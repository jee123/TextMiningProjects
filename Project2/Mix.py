# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 20:39:04 2016

@author: shubham
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 16:11:36 2016

@author: shubham
"""

import cPickle,gzip
import numpy as np

from sklearn.svm import SVC 
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression as lr

from sklearn.metrics import roc_curve
import matplotlib.pyplot as plt

with gzip.open("train_data.pkl.gz",'rb') as g:
  train_data=cPickle.load(g)
g.close() 

with gzip.open("test_data.pkl.gz",'rb') as g:
  test_data=cPickle.load(g)
g.close() 
label_test=test_data[1]

clf_list = [SVC(kernel='linear',C=10**(-1)), SVC(kernel = 'linear'), 
            GaussianNB(), lr()]

clf_name = ['Soft Margin SVM', 'Linear SVM','Naive Bayes', 'Logistic Regression']

colors = ['b','r','g','y']
plt.figure()

for i in range(len(clf_name)):
    print 'Currently using',clf_name[i]    
    clf = clf_list[i]
    clf.fit(train_data[0],train_data[1])
    y_pred = clf.predict(test_data[0])
    
    fpr,tpr,threshold=roc_curve(label_test,y_pred)
    plt.plot(fpr,tpr,colors[i])

plt.xlabel('false positive rate')
plt.ylabel('true positive rate')
plt.title('ROC curves')
plt.legend(clf_name,loc = 4)
plt.savefig('ROC_combined.png')