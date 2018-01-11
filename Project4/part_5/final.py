import create_data as cd
import results
import pickle
import json
import datetime, time
import matplotlib.pyplot as plt
import math
import numpy as np
from sklearn import linear_model
from sklearn.feature_selection import chi2
import statsmodels.formula.api as sm
import scipy, scipy.stats
from sklearn import cross_validation
import sklearn.preprocessing as pp
import pickle


files = {'10,3':'#nfl','1,1':'#nfl','2,2':'#patriots','3,3':'#patriots','4,1':'#nfl','5,1':'#nfl','6,2':'#superbowl','7,3':'#superbowl','8,1':'#nfl','9,2':'#superbowl'}

with open('times.pickle') as f:
	times = pickle.load(f)

for i in files:
	q = i.split(',')
	t = times[files[i]]
	print 'For Sample',q[0],'Prediction of 7th hour is'
	results.three_part_split(files[i],t,q[0],q[1])
	print '-'*50
	# print i,files[i]