import json
import datetime, time

import math
import pickle
import tweet_class as tc

# ref_dict = {'n_retweets':0'sum_following':1,'max_follower':2,'time':3,'num_mentions':4,'n_unique_user':5
#             'moving_av':6, 'moving_std':7, 'derivative':8, 'derivative_mean':9, past_vals':10,11,12,13,14}


# ref_dict = {'n_tweets':0,'n_retweets':1,'sum_following':2,'max_follower':3,'time':4,'num_mentions':5,'n_unique_user':6}

def get_vector(tweet,n_bin):
    user = tweet['tweet']['user']
    user_id = user['id_str']
    n_tweet = 1
    n_retweets = tweet['tweet']['retweet_count']

    sum_user = {user_id : user['followers_count']}
    max_num_follower = user['followers_count']

    num_mentions = len(tweet['tweet']['entities']['user_mentions'])
    time_of_day = n_bin%24
    res = [n_tweet,n_retweets,sum_user,max_num_follower,time_of_day,num_mentions]
    return res

def update_vector(n, o):
    o[0] += n[0]
    o[1] += n[1]
    for u_id in n[2]:
        if u_id not in o[2]:
            o[2][u_id] = n[2][u_id]
    o[3] = max(o[3],n[3])
    o[5] += n[5]
    return o

def min_time(f):
    
    line = f.readline()
    tweet = json.loads(line)

    min_time = 10000000000    
    
    start_date = datetime.datetime(2015,01,01, 12,0,0)
    mintime = int(time.mktime(start_date.timetuple()))

    while len(line)!=0:
        tweet = json.loads(line)
        line = f.readline()
        tweet_time = tweet['firstpost_date']
        if tweet_time >= mintime:
            # max_time=max(max_time,tweet['firstpost_date'])
            min_time=min(min_time,tweet['firstpost_date'])
    return min_time
        

def extract_data(f,min_time):
    x = {}
    #f=open('tweets_#nfl.txt')
    line = f.readline()
    
    tweet = json.loads(line)
    
    while len(line)!=0:
        tweet = json.loads(line)
        line = f.readline()
        bin_num = (tweet['firstpost_date'] - min_time)/3600
        if bin_num >= 0:
            cur_tweet = get_vector(tweet,bin_num)
            if bin_num not in x:
                x[bin_num] = cur_tweet
            else:
                temp = update_vector(cur_tweet,x[bin_num])
                x[bin_num] = temp
    
    for key in x:
        x[key].append(len(x[key][2].keys()))     
        x[key][2] = sum(x[key][2].values())
    return x,min_time

def modify(sample,period):
    
    
    f_name = 'pickled/original/sample'+sample+'_period'+period+'.pickle'
    with open(f_name) as f:
        data = pickle.load(f)

    k_m = max(data.keys())
    all_vals = [0]*(k_m + 1)

    for i in range(k_m+1):
        if i in data:
            all_vals[i] = data[i][0]

    k = 6
    mod = tc.ts_data(all_vals)
    moving_av = mod.moving_average(k,mean = True)
    moving_std = mod.moving_average(k,mean = False)
    d_mean = mod.moving_average(k,mean = True, d = True)
    d = mod.get_d()


    for i in range(k_m+1):
        if i in data:
            temp = data[i][1:]
            feats = [moving_av[i], moving_std[i], d[i], d_mean[i]]
            if i >= 5:
                past_vals = all_vals[i-4:i+1]
            else:
                past_vals = [0]*(4-i) + all_vals[:i+1]
            data[i] = temp+feats+past_vals
    
    store_location = 'pickled/modified/sample'+sample+'_period'+period+'.pickle'
    
    with open(store_location,'wb') as f:
        data = pickle.dump(data,f)
    print 'Saving data'


def store(sample,period, time = False):
    f_name = 'sample'+sample+'_period'+period+'.txt'
    print f_name
    with open(f_name) as f:
        mintime = min_time(f)
        if time:
            return mintime
    with open(f_name) as f:    
        print 'Mintime found'
        res,min_time1 = extract_data(f,mintime)

    store_location = 'pickled/original/sample'+sample+'_period'+period+'.pickle'
    print 'Storing data'
    with open(store_location,'wb') as f:
       pickle.dump(res,f)
