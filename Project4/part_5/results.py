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

def get_selected(all_elem, selected):
    result = []
    for i in selected:
        result.append(all_elem[i])
    return result

def get_pval(tag):

    f_name = tag+'_train_test.pickle'
    with open(f_name) as f:
        data = pickle.load(f)
    x = data['x']
    y = data['y']

    mean = y.mean()
    std = y.std()

    y = (y - mean)/std
    
    results = sm.OLS(y,x).fit()
    print results.summary()


def cross_val(tag):
    # load data
    f_name = tag+'_train_test.pickle'
    with open(f_name) as f:
        data = pickle.load(f)
    x = data['x']
    y = data['y']

    mean = y.mean()
    std = y.std()

    y = (y - mean)/std
    avg_error=[]
    kf=cross_validation.KFold(len(x),10,True)
    for train_index,test_index in kf:
        X_train = get_selected(x, train_index)
        X_test = get_selected(x, test_index)
        Y_train = get_selected(y, train_index)
        Y_test = get_selected(y, test_index)
        
        regr=linear_model.LinearRegression()
        regr.fit(X_train,Y_train)
        Y_pred=regr.predict(X_test)
        a_e = np.mean(abs(Y_pred-Y_test))
        a_e = a_e*std + mean
        avg_error.append(a_e)
    
    print 'Average error in prediction from cross-validation =',np.mean(avg_error)    

# res,min_time = extract_data('tweets_#gopatriots.txt')
def three_part_split(tag,min_time,sample,period):
    #Splitting the data in three time periods
    f_name = 'modified/'+tag+'.pickle'
    with open(f_name) as f:
        res = pickle.load(f)

    f_name = tag+'_train_test.pickle'
    with open(f_name) as f:
        data = pickle.load(f)
    y = data['y']

    before=datetime.datetime(2015,02,01, 8,0,0)
    after=datetime.datetime(2015,02,01,20,0,0)
    before_time=int(time.mktime(before.timetuple()))
    after_time=int(time.mktime(after.timetuple()))

    #Splitting the dataset according to the time period given 
    before_index=(before_time-min_time)/3600
    after_index=(after_time-min_time)/3600
    x_before=[]
    y_before=[]
    x_active=[]
    y_active=[]
    x_after=[]
    y_after=[]

    for index,key in enumerate(res):
        cur = res[key]
        if key<before_index:
            x_before.append(cur)
            y_before.append(y[index])
        elif key>before_index and key<=after_index:
            x_active.append(cur)
            y_active.append(y[index])
        else:
            x_after.append(cur)
            y_after.append(y[index])       

    # pp.normalize(x,axis = 0)
    x_before=np.asarray(x_before)
    y_before=np.asarray(y_before)
    x_active=np.asarray(x_active)
    y_active=np.asarray(y_active)
    x_after=np.asarray(x_after)
    y_after=np.asarray(y_after)  

    x_before=pp.normalize(x_before, axis = 0)
    x_active=pp.normalize(x_active, axis = 0)
    x_after=pp.normalize(x_after, axis = 0)

    store_location = 'pickled/modified/sample'+sample+'_period'+period+'.pickle'
    
    with open(store_location) as f:
        data = pickle.load(f)

    
    x_test = []
    for i in data:
        x_test.append(data[i])
    # print len(x_test)
    x_test = np.array(x_test)
    
    if period == '1':
        regr_before = linear_model.LinearRegression()
        regr_before.fit(x_before, y_before)
        print abs(regr_before.predict(x_test)[-1])

    elif period == '2':
        regr_active = linear_model.LinearRegression()
        regr_active.fit(x_active, y_active)
        print abs(regr_active.predict(x_test)[-1])

    elif period == '3':    
        regr_after = linear_model.LinearRegression()
        regr_after.fit(x_after,y_after)
        print abs(regr_after.predict(x_test)[-1])

