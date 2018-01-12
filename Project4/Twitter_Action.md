### Description :  
 * The test data consists of tweets containing a hashtag in a specified time window. 
 * We use our model to predict number of tweets containing the hashtag posted within one hour immediately following the given 
   time window.

### Steps :    
#### 1.  Average number of tweets , followers and retweets per hour:  
  * avg_tweets = float(num_tweets)*3600/(maxtime - min_time)),      
  * average number of followers of users posting the tweets(used user['followers_count']),      
  * average number of retweets for each hashtag in training tweet data(used tweet['tweet']['retweet_count']).    

Tweets are stored in separate files for different hashtags and files are named as tweet[#hashtag].txt.
The tweet file contains one tweet in each line and tweets are sorted with respect to their posting time. 
Each tweet is a JSON string that you can load in Python as a dictionary.

#### 2.  Fit Linear Regression model using 5 features to predict number of tweets in the next hour:
  * Features extracted from tweet data from previous hour include :  
      * number of tweets(n_tweet=1),   
      * total number of retweets(tweet['tweet']['retweet_count']),   
      * sum of number of followers of the users posting the hashtag({user_id : user['followers_count']} so we take sum of 
      'followers_count'),   
      * maximum number of followers of the users posting the hashtag(user['followers_count']), and  
      * time of the day(n_bin%24 where n_bin=bin_num = (tweet['firstpost_date'] - min_time)/3600)  

  * The significance of each feature is determined using the t-test and P-value results of fitting the model.

#### 3.  Regression model using any features
  * Fit your model on the data and report fitting accuracy and significance of variables. 
  * For the top 3 features in your measurements, draw a scatter plot of number of tweets for next hour vs feature value, 
    using all the samples you have extracted and analyze it.

#### 4.  Creating different regression models for different periods of time.
  * Different periods of time include 
     * First, when the hashtags haven't become very active,   
     * Second, their active period,   
     * Third, after they pass their high-activity time.
  * Train 3 regression models for these time periods (The times are all in PST):
     * Before Feb. 1, 8:00 a.m.
     * Between Feb. 1, 8:00 a.m. and 8:00 p.m. 
     * After Feb. 1, 8:00 p.m.
  * Report cross-validation errors for the 3 different models.

#### 5.   Run your model on test data to make predictions for the next hour in each case. 
   * Each file in the test data contains a hashtag's tweets for a 6-hour window.
   * A file named sample5_period2.txt contains tweets for a 6-hour window that lies in the second time period.
   * Report your predicted number of tweets for the next hour of each sample window.
