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
