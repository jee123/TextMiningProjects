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

tweet_data = ['tweets_#superbowl.txt']
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

tweets=[]
def extract_data():
    f = open('tweet_data/tweets_#superbowl.txt')
    print 'Data Loaded'
    count = 0
    for line in f:
        print count
        tweet = json.loads(line)
        count = count + 1
        tweets.append(tweet)

extract_data()
print len(tweets)
