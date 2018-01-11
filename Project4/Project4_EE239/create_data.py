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

def get_selected(all_elem, selected):
    result = []
    for i in selected:
        result.append(all_elem[i])
    return result


def get_vector(tweet,n_bin):
    user = tweet['tweet']['user']
    user_id = user['id_str']
    n_tweet = 1
    n_retweets = tweet['tweet']['retweet_count']
    # sum_of_followers[(tweet['firstpost_date']-mintime)/3600]+=user['followers_count']  #remove the follower count of users posting again in the same hour
    sum_user = {user_id : user['followers_count']}
    max_num_follower = user['followers_count']
    #time_of_day[(tweet['firstpost_date']-mintime)/3600]=int(tweet['tweet']['created_at'].split()[3].split(':')[0]) 
    time_of_day = n_bin%24
    res = [n_tweet,n_retweets,sum_user,max_num_follower,time_of_day]
    return res

def update_vector(n, o):
    o[0] += n[0]
    o[1] += n[1]
    for u_id in n[2]:
        if u_id not in o[2]:
            o[2][u_id] = n[2][u_id]
    o[3] = max(o[3],n[3])
    return o

def extract_data(file_name):
    f = open(file_name)
    print 'Data Loaded'    
    #f=open('tweets_#nfl.txt')
    line = f.readline()
    
    tweet = json.loads(line)
    
    tweets = []
    while len(line)!=0:
        tweet = json.loads(line)
        tweets.append(tweet)
        line = f.readline()
        
        
    start_date = datetime.datetime(2015,01,01, 12,0,0)
#	end_date = datetime.datetime(2015,02,01, 15,0,0)

    mintime = int(time.mktime(start_date.timetuple()))
#	maxtime = int(time.mktime(end_date.timetuple()))

    min_time = 10000000000
    for tweet in tweets:
        tweet_time = tweet['firstpost_date']
        if tweet_time >= mintime:
            # max_time=max(max_time,tweet['firstpost_date'])
            min_time=min(min_time,tweet['firstpost_date'])
    x = {}
    for tweet in tweets:
        bin_num = (tweet['firstpost_date'] - min_time)/3600
        cur_tweet = get_vector(tweet,bin_num)
        if bin_num not in x:
            x[bin_num] = cur_tweet
        else:
            temp = update_vector(cur_tweet,x[bin_num])
            x[bin_num] = temp
    f.close()
    for key in x:
        x[key][2] = sum(x[key][2].values())     
    return x,min_time

f_name = '/Users/tjee/Documents/Project4_EE239/tweet_data/tweets_#superbowl'
res,min_time = extract_data(f_name+'.txt')
import pickle
with open(f_name+'.pickle','wb') as f:
    pickle.dump(res,f)
