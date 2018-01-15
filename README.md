## Project2: Classification Analysis
  * Explores different methods for classifying textual data.
  * Dataset used is ["20 Newsgroups"](http://qwone.com/~jason/20Newsgroups/) which is a collection of 20,000 newsgroup documents 
    partitioned evenly across 20 different newsgroups each representing a different topic.
  * Target is to train a classifier to group the documents into two classes _Computer Technology and Recreational activity_ given 
    collection of documents with predefined class types.  
  * Computer Technology and Recreational activity include the following sub-classes:  
    <p align="center">
    <img width="650" alt="screen shot 2018-01-14 at 3 20 32 pm" src ="https://user-images.githubusercontent.com/15849566/34923859-63c76858-f954-11e7-9a45-58749b1223d0.png">
    </p>     

  
  * Steps :  
    * As part of **_understanding the dataset_**, first plot histogram of number of documents per topic or newsgroup to confirm 
      even distribution and calculate number of documents in the two groups above(Computer Technology and Recreational Activity).      
      Number of documents in Recreational activity are 2389 and in Computer Technology are 2343. 
     <p align="center">
     <img width="350" alt="screen shot 2018-01-14 at 3 42 54 pm" src = "https://user-images.githubusercontent.com/15849566/34922219-d2ced988-f941-11e7-82de-6f49509ff76a.png">               
     </p>
     
    * As part of **_feature extraction_**, now transform documents in the dataset into numerical feature vectors by     
      * tokenizing each document.  
      * extracting all words appearing in documents, excluding stop words, punctutations and different stems of word.    
      * creating TFxIDF vector representations where we use it quantify significance of a word to a Document. Similarly we use 
        TFxICF to show siginificance of word to a class. Computed for term t, class c where C is collection of all 20 classes 
        as :  
       <p align="center"> 
       <img width="300" alt="screen shot 2018-01-14 at 4 07 17 pm" src = "https://user-images.githubusercontent.com/15849566/34923633-822f7e36-f952-11e7-8fd4-7dd088df1636.png">
       </p>
       
      * report final number of terms extracted(34792).        
     * Based on the TFxICF scores we get the 10 most significant terms for select set of classes.
        <p align="center">
        <img width="600" alt="screen shot 2018-01-14 at 4 16 50 pm" src = "https://user-images.githubusercontent.com/15849566/34922551-648029a0-f946-11e7-9baf-940be24241c0.png">
       </p>
       
     * As part of  **_feature selection_** we reduce the high dimensionality of data by using Latent Semantic Indexing(LSI)( 
       finds optimal representation of data in a lower dimensional space in mean squared error sense).  
       Applying LSI to TFxICF matrix and selecting k as 50 we map each document to a 50-dimensional vector. These features are 
       used ahead in the **_learning algorithms_**.
     
     * As part of **_learning algorithms_** used to classify documents into Computer Technology vs Recreational Activity groups :    
       * _Linear SVM_ 
         * Receiver Operating Characteristic(ROC) for Linear SVM : 
         <p align="center">
         <img width="400" alt="screen shot 2018-01-14 at 5 30 16 pm" src="https://user-images.githubusercontent.com/15849566/34923449-d0ef369e-f950-11e7-8555-cf35b575bee6.png">
         </p>
            
         * Confusion matrix for Linear SVM :  
         <p align="center">
         <img width="700" alt="screen shot 2018-01-14 at 5 36 40 pm" src="https://user-images.githubusercontent.com/15849566/34923520-9df57c20-f951-11e7-8982-a823583fa20c.png">
         </p>
         
         * Accuracy, Precision and Recall for Linear SVM :  
         <p align="center">
         <img width="400" alt="screen shot 2018-01-14 at 5 39 33 pm" src="https://user-images.githubusercontent.com/15849566/34923591-41a00c50-f952-11e7-958c-9a44aa9f43e8.png">
         </p>

       * _Soft margin SVM_  
         * Receiver Operating Characteristic(ROC) for Soft margin SVM : 
         <p align="center">
         <img width="400" alt="screen shot 2018-01-14 at 8 09 16 pm" src="https://user-images.githubusercontent.com/15849566/34926840-0185ad68-f967-11e7-813f-ae1753370066.png">
         </p>
         
         * Confusion matrix for Soft margin SVM :
         <p align="center">
         <img width="700" alt="screen shot 2018-01-14 at 8 12 00 pm" src="https://user-images.githubusercontent.com/15849566/34926892-560d6f92-f967-11e7-9d10-1357241140e0.png">
         </p>
         
         * Accuracy, Precision and Recall for Soft margin SVM :  
         <p align="center">
         <img width="400" alt="screen shot 2018-01-14 at 8 14 17 pm" src="https://user-images.githubusercontent.com/15849566/34926930-9f2b999c-f967-11e7-8de6-a954e89069bc.png">
         </p>

       * _Naive Bayes_ 
         * Receiver Operating Characteristic(ROC) for Naive Bayes :  
         <p align="center">
         <img width="400" alt="screen shot 2018-01-14 at 8 17 52 pm" src="https://user-images.githubusercontent.com/15849566/34927099-938014dc-f968-11e7-8318-1ef444e4cfc7.png">
         </p>
         
         * Confusion matrix for Naive Bayes :  
         <p align="center">
         <img width="700" alt="screen shot 2018-01-14 at 8 23 15 pm" src="https://user-images.githubusercontent.com/15849566/34927155-f7cc4ad2-f968-11e7-9976-74bc2e7a7143.png">
         </p>
         
         * Accuracy, Precision and Recall for Naive Bayes :
         <p align="center">
         <img width="400" alt="screen shot 2018-01-14 at 8 23 31 pm" src="https://user-images.githubusercontent.com/15849566/34927179-28725bb8-f969-11e7-8b55-77da1593ef12.png">
         </p>
         
       * _Logistic Regression_
         * Receiver Operating Characteristic(ROC) for Logistic Regression : 
         <p align="center">
         <img width="400" alt="screen shot 2018-01-14 at 8 35 12 pm" src="https://user-images.githubusercontent.com/15849566/34927373-8bb35b7c-f96a-11e7-93f7-c5b8eb1295d0.png">
         </p>
         
         * Confusion matrix for Logistic Regression :
         <p align="center">
         <img width="700" alt="screen shot 2018-01-14 at 8 35 26 pm" src="https://user-images.githubusercontent.com/15849566/34927400-becc7ab6-f96a-11e7-81ac-ac6ce933fa75.png">
         </p>
         
         * Accuracy, Precision and Recall for Logistic Regression :
           <p align="center">
           <img width="400" alt="screen shot 2018-01-14 at 8 35 34 pm" src="https://user-images.githubusercontent.com/15849566/34927426-e5bbfdc2-f96a-11e7-8de6-e988a36243b3.png">
           </p>
        
        * Comparision 
        <p align="center">
        <img width="400" alt="screen shot 2018-01-14 at 8 39 52 pm" src="https://user-images.githubusercontent.com/15849566/34927459-38b8eada-f96b-11e7-82c0-4160915223c2.png">
        </p>

     * As part of **_multi-class classification_** we compare Naive Bayes vs Linear SVM to classify documents mentioned in step 3 
       above :  
       * Accuracy, Precision and Recall for Naive Bayes and SVM for _One vs Rest_ method:
       <p align="center">
       <img width="400" alt="screen shot 2018-01-14 at 9 01 01 pm" src="https://user-images.githubusercontent.com/15849566/34927842-18142d6e-f96e-11e7-8d4c-201c40803c18.png">
       </p>
       
       * Accuracy, Precision and Recall for Naive Bayes and SVM for _One vs One_ method:
       <p align="center">
       <img width="400" alt="screen shot 2018-01-14 at 9 02 42 pm" src="https://user-images.githubusercontent.com/15849566/34927867-58c7398c-f96e-11e7-8bab-1b46ea63de21.png">
       </p>
       
       * Confusion matrix for Naive Bayes and SVM for _One vs Rest_ method:
       <p align="center">
       <img width="700" alt="screen shot 2018-01-14 at 10 53 47 pm" src="https://user-images.githubusercontent.com/15849566/34930343-e81d2164-f97d-11e7-980f-0411d5867825.png">
       </p>
       
       * Confusion matrix for Naive Bayes and SVM for _One vs One_ method:
       <p align="center">
       <img width="700" alt="screen shot 2018-01-14 at 10 51 34 pm" src="https://user-images.githubusercontent.com/15849566/34930282-a8604c9a-f97d-11e7-8a7d-f0edcf007c26.png">
       </p>
       
       
## Project4: Popularity prediction Twitter
  * Here we know the current and previous tweet activity for a hashtag and need to predict its tweet activity in the future. The 
    prediction should help us determine whether the tweet will become more popular and if so then by how much.  
  * Available Twitter data is collected by querying popular hashtags related to 2015 Super Bowl spanning a period starting 2 
    weeks before game to a week after the game.  
  * Steps :  
    * We calculate statistics associated with each hashtag that includes 
      * Average number of tweets per hour, average number of followers of users posting tweets and average number of retweets.    
        These statistics helps us conclude that as hashtags become more generic, like #superbowl being more generic than 
        #gopatriots, number of tweets per hour increases.     
      * Further we plot and compare for #SuperBowl and #NFL, a histogram with 1-hour bins based on number of tweets in one hour 
        over time. 
        
        <p align="center">
        <img width="500" alt="screen shot 2018-01-15 at 12 01 07 am" src="https://user-images.githubusercontent.com/15849566/34932339-46c74b64-f987-11e7-88e3-ba52182ab275.png">
        </p>

       <p align="center">
       <img width="500" alt="screen shot 2018-01-15 at 12 03 50 am" src="https://user-images.githubusercontent.com/15849566/34932462-b25ddb22-f987-11e7-8592-cad5cc202014.png">
       </p>
       
       
       * The above graphs conclude that number of tweets in an hour were high near the super-bowl event compared to days other  
         than the super-bowl event.

    * Next we fit a linear regression model using 5 features to predict number of tweets in next hour with features extracted 
      from tweet data in previous hour. The features used are :
      * x1 - number of tweets,  
      * x2 - total number of retweets,
      * x3 - sum of the number of followers of the users posting the hashtag,
      * x4 - maximum number of followers of the users posting the hashtag,
      * x5 - time of the day
      We then discuss the models training accuracy and significance of each feature using t-test and P-value results of fitting 
      the model.      
      An example for the same is demonstrated by showing the P, t and R^2 values for #gopatriots.
      
      <p align="center">
      <img width="550" alt="screen shot 2018-01-15 at 7 11 57 am" src="https://user-images.githubusercontent.com/15849566/34948945-75db006c-f9c3-11e7-8571-012efe3048fa.png">
      </p>
      
         * Here x1,x2 and x5 are significant as they have very low P values and high t-value.   
           R^2 value is reported to be 0.614.  
    
    * Then we design a regression model using the following features :
      * _Network features_:
        * Network indicates connectivity of users posting the tweets. The connectivity is indicative of how well the tweet can 
          diffuse in the network. 
          * Number of retweets: Sum of number of retweets in an hour(x1).
          * Number of max followers: Here we count a list of followers for the users who tweeted in last hour and take the 
            maximum (x3).
          * Sum of number of people following the hashtag: As people following the tweets are the likely
            users to tweet, we take the number of people following that hashtag as a feature(x2). 
          * Number of mentions: Sum of number of tweets in a given hour containing '@' mentions(x5).
          * Number of unique users: We also take the number of unique users which posted in last hours
            as a feature(x6).
      * _Time Series Features_:
        * These indicate the trend of tweets in a given time interval. Since the past number of tweets values are extremely 
          important, through these features we try to extract the tweet variation with time.  
          * Moving Average: Averaging number of tweets in last five hours with reference to presentvalue(x7).    
          * Moving Standard Deviation:Standard deviation of tweets in last ve hours with reference to present value(x8).  
          * Derivative:Taking number of tweets to be a time-series,the Derivative indicates Slope value at present time(x9).  
          * Derivative mean: Mean of past five derivative values. The derivate gives the trend for past values
            which is a very good indicator for prediction(x10).  
          * Past value: We take the past five values of number of tweets. This ensures we have enough past  
            information to predict the values in next hour. This is similar to the linear prediction model used  
            in many cases(x10-x15).    
          * Time of day: Represent hours of the day with respect to a given time reference(x4).  
          
      * Using these Network and Time Series features we built a Linear Regression model. From that we get the significant 
        features and then we do a scatter plot of Predictant values(number of tweets for next hour) vs significant features.   
        Sample is shown for #gopatriots.  
        
        <p align="center">
        <img width="650" alt="screen shot 2018-01-15 at 7 27 37 am" src="https://user-images.githubusercontent.com/15849566/34949691-ae8b30ba-f9c5-11e7-82a6-6d6f26264c58.png">
        </p>
        
      * After doing several more scatter plots we concluded that the scatter plots indicate linear relation between significant 
        variable and predictant value which was expected and in line with theoretical explanation of p and t values.  
              
    *  Average Prediction Error obtained from 10 fold cross validation over full dataset is :  
       <p align="center">
       <img width="300" alt="screen shot 2018-01-15 at 7 33 21 am" src="https://user-images.githubusercontent.com/15849566/34950006-acc6174e-f9c6-11e7-8581-89a9345ee178.png">
       </p>
       
       * Then the dataset is divided for each hashtag into three periods:  
         Period 1: Before  Feb 1, 8:00 AM    
         Period 2: Between Feb 1, 8:00 AM and 8:00 PM    
         Period 3: After Feb 1, 8:00 PM    
         Cross validation results were calculated for each hashtag in these periods and the cross validation error tabulated.  
         
         <p align="center">
         <img width="250" alt="screen shot 2018-01-15 at 7 39 05 am" src="https://user-images.githubusercontent.com/15849566/34950170-3e4d5114-f9c7-11e7-8cca-9fdf540cfffe.png">
         </p>
         
    * After reading the time periods from the file we computed the hashtag occuring the maximum number of times in a given test 
      file. The file along with their corresponding tweet prediction for next hour are as :
      <p align="center">
      <img width="700" alt="screen shot 2018-01-15 at 8 21 59 am" src="https://user-images.githubusercontent.com/15849566/34952073-4428de72-f9cd-11e7-9e79-630bd75b2d4f.png">
      </p>
      
   
        
    
      
