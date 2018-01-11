import json
import datetime, time


f = open('/Users/tjee/Documents/Project4_EE239/tweet_data/tweets_#superbowl.txt')

lines = f.readlines()
print 'data loaded'

tweets = []
# count = 0
for line in lines:    
    tweet = json.loads(line)
    tweets.append(tweet)
    line = f.readline()
    break
print tweets


start_date = datetime.datetime(2015,01,01, 12,0,0)
end_date = datetime.datetime(2015,02,01, 15,0,0)
mintime = int(time.mktime(start_date.timetuple()))
maxtime = int(time.mktime(end_date.timetuple()))


#num_tweets = len(tweets)
#num_tweets = 10
num_window = 0

max_followers = 0
for i in range(0, 10):
    tweet = tweets[i]
    tweet_time = tweet['firstpost_date']
    if tweet_time >= mintime:
        if tweet_time >= maxtime:
            break;
        num_window += 1
        max_followers = max(max_followers, tweet['tweet']['user']['followers_count'])
    







