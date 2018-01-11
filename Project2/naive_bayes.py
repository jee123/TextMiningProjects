import cPickle,gzip
import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt

with gzip.open("train_data.pkl.gz",'rb') as g:
  train_data=cPickle.load(g)
g.close() 

with gzip.open("test_data.pkl.gz",'rb') as g:
  test_data=cPickle.load(g)
g.close() 
print len(train_data[0])
clf = GaussianNB()
clf.fit(train_data[0],train_data[1])
#y_score=clf.fit(train_data[0],train_data[1]).decision_function(test_data[0])
predicted = clf.predict(test_data[0])
label_test=test_data[1]
print np.mean(predicted == label_test) 
print confusion_matrix(label_test, predicted)
print precision_score(label_test, predicted)
print recall_score(label_test, predicted)

fpr,tpr,threshold=roc_curve(label_test,predicted)
plt.plot(fpr,tpr)
plt.xlabel('false positive rate')
plt.ylabel('true positive rate')
plt.title('ROC curve for Naive Bayes')
plt.savefig('ROC_NaiveBayes.png')
