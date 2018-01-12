The test data consists of tweets containing a hashtag in a specified time window, and you will use your model to predict number of tweets containing the hashtag posted within one hour immediately following the given time window.

1.average number of tweets per hour(avg_tweets = float(num_tweets)*3600/(maxtime - min_time)), 
average number of followers of users posting the tweets(used user['followers_count']), and 
average number of retweets for each hashtag in training tweet data(used tweet['tweet']['retweet_count']).

Tweets are stored in separate files for different hashtags and files are named as tweet_[#hashtag].txt.
The tweet file contains one tweet in each line and tweets are sorted with respect to their posting time. 
Each tweet is a JSON string that you can load in Python as a dictionary.

2.Fit a Linear Regression model using 5 features to predict number of tweets in the next hour, with
features extracted from tweet data in the previous hour. 
The features you should use are: 

•number of tweets(n_tweet=1), 
•total number of retweets(tweet['tweet']['retweet_count']), 
•sum of the number of followers of the users posting the hashtag({user_id : user['followers_count']} so we take sum of 'followers_count'), 
•maximum number of followers of the users posting the hashtag(user['followers_count']), and
•time of the day(n_bin%24 where n_bin=bin_num = (tweet['firstpost_date'] - min_time)/3600)

significance of each feature using the t-test and P-value results of fitting the model.

3.regression model using any features.Fit your model on the data and report fitting accuracy and significance of variables. 
For the top 3 features in your measurements, draw a scatter plot of predictant (number of tweets for next hour) versus feature value, 
using all the samples you have extracted and analyze it.

4.create different regression models for different periods of time. First, when the hashtags haven't become very active, second, their active period, and third, after they pass their high-activity time.
 Train 3 regression models for these time periods (The times are all in PST):
1. Before Feb. 1, 8:00 a.m.
2. Between Feb. 1, 8:00 a.m. and 8:00 p.m. 
3. After Feb. 1, 8:00 p.m.
Report cross-validation errors for the 3 different models.

5.Run your model on test data to make predictions for the next hour in each case. 
Each file in the test data contains a hashtag's tweets for a 6-hour window.a file named sample5_period2.txt contains tweets for a 6-hour window 
that lies in the 2nd time period.Report your predicted number of tweets for the next hour of each sample window.

6. stock price prediction using sentiment from twitter data.