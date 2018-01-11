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


def min__time(file_name):
    f = open(file_name)   
    #f=open('tweets_#nfl.txt')
    line = f.readline()
    
    tweet = json.loads(line)
    num_tweets=1

    start_date = datetime.datetime(2015,01,01, 12,0,0)
#   end_date = datetime.datetime(2015,02,01, 15,0,0)

    mintime = int(time.mktime(start_date.timetuple()))
#   maxtime = int(time.mktime(end_date.timetuple()))
    num_tweets=1
    min_time = 10000000000  
    max_time=0  
    while len(line)!=0:
        tweet = json.loads(line)
        line = f.readline()
        tweet_time = tweet['firstpost_date']
        num_tweets=num_tweets+1
        if tweet_time >= mintime:
            max_time=max(max_time,tweet['firstpost_date'])
            min_time=min(min_time,tweet['firstpost_date'])
    return min_time,max_time,num_tweets


all_files=['tweets_#gopatriots.txt','tweets_#gohawks.txt','tweets_#patriots.txt','tweets_#sb49.txt','tweets_#nfl.txt','tweets_#superbowl.txt']

for fname in all_files:
    f = open(fname)
    line = f.readline()
    tweet = json.loads(line)
    min_time,maxtime,num_tweets=min__time(fname)

    start_date = datetime.datetime(2015,01,01, 12,0,0)
    #end_date = datetime.datetime(2015,02,01, 15,0,0)

    mintime = int(time.mktime(start_date.timetuple()))
    #maxtime = int(time.mktime(end_date.timetuple()))


    #num_tweets = len(tweets)
    num_window = 0
    avg_tweets = float(num_tweets)*3600/(maxtime - min_time)    
    
    number_of_samples=(maxtime-min_time)/3600


    his=[]
    users = {}
    num_retweets = 0
    num_followers = 0
    number_of_tweets_hour=[0]*number_of_samples
    total_number_retweets=[0]*number_of_samples
    sum_of_followers=[0]*number_of_samples
    max_num_follower=[0]*number_of_samples
    #time_of_day=[0]*747
    time_of_day=np.zeros((number_of_samples,24))


    while len(line)!=0:
        tweet = json.loads(line)
        #tweets.append(tweet)
        line = f.readline()

    #for tweet in tweets:
        tweet_time = tweet['firstpost_date']
        user = tweet['tweet']['user']
        user_id = user['id_str']
        if tweet_time >= mintime:
            #if tweet_time >= maxtime:
            #   break
            if user_id not in users:
                users[user_id] = user['followers_count']
                num_followers += users[user_id]

            num_retweets += tweet['tweet']['retweet_count']
            

    
    print 'For ',fname,' file'
    print 'Average number of tweets = ', (avg_tweets)
    print 'Average number of followers =',num_followers/len(users)
    print 'Average number of retweets =',num_retweets/float(number_of_samples)


