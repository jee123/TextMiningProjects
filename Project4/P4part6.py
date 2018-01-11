import re
import numpy as np
import json
import datetime, time
# Read in the sentiment/valence files

#valenceFile = os.path.join(dataFilePath, "EmotionLookupTable.txt")
valenceFile="AFINN-111.txt"
#emoticonFile = os.path.join(dataFilePath, "EmoticonLookupTable.txt")

valenceList = []

# Open the valence file and read in each word/valence pair
for line in open(valenceFile, "r"):
    # Split the line based on tabs and select the first two elements
    (word, valence) = line.split("\t")[:2]
    
    wordRegex = re.compile(word)
    valencePair = (wordRegex, int(valence))
    valenceList.append(valencePair)
    
# Open the emoticon file and read in the valence for each emoticon
'''for line in codecs.open(emoticonFile, "r", "utf-8"):
    # Split the line based on tabs and select the first two elements
    (emoticon, valence) = line.split("\t")[:2]
    
    emoticonRegex = re.compile(re.escape(emoticon))
    valencePair = (emoticonRegex, int(valence))
    valenceList.append(valencePair)
'''

#print ("Number of Sentiment Keywords:", len(valenceList))

'''for i in np.random.random_integers(0, len(valenceList)-1, 10):
    print(valenceList[i][0].pattern, "\t", valenceList[i][1])
'''

f_name = 'tweets_#gohawks.txt'
before=datetime.datetime(2015,01,28, 0,0,0)
after=datetime.datetime(2015,02,07,0,0,0)
before_time=int(time.mktime(before.timetuple()))
after_time=int(time.mktime(after.timetuple()))

sortedTimes=[1,2,3,4,5,6,7,8,9]
companies={'dorito':{},'makeithappy':{},'budweiser':{},'mcdonald':{},'mercedes':{},'lexus':{},'audi':{},'minion':{}}
#companies={'dorito':{}}
for key in companies.keys():
	print "Calculating sentiment scores for ", key
	timeSentiments = {}
	for t in sortedTimes:
		print 'day ', t
		sentimentList = []
		thisMinuteSentiment = None
		f = open(f_name)
		line = f.readline()
		while len(line)!=0:
			tweet = json.loads(line)
			line=f.readline()
			if tweet['firstpost_date']>=(before_time+86400*(t-1)) and tweet['firstpost_date']<=(before_time+86400*t):
				tweetText = tweet['tweet']["text"].lower()
				temp=tweet['tweet']['entities']['hashtags']
				h=[]
				param=False
				for hh in temp:
					p=hh['text']
					p=p.lower()
					if key in p:
						param=True
						break

					

				if param:
				# skip retweets
				    if ( tweetText.startswith("rt ") ):
				        continue

				    valCount = 0
				    valSum = 0.0
				    valAvg = 0.0
				    for valencePair in valenceList:
				        if ( valencePair[0].search(tweetText) is not None ):
				            valCount += 1
				            valSum += valencePair[1]

				    if ( valCount > 0 ):
				        valAvg = valSum / valCount
				        sentimentList.append(valAvg)
		if(len(sentimentList)>0):
			thisMinuteSentiment=np.array(sentimentList).mean()
		else:
			thisMinuteSentiment = 0.0
		#print t ,'two'
		timeSentiments[t]=thisMinuteSentiment	
	companies[key]=timeSentiments				    
		

			    

print  'Final scores of the companies is ' ,companies

#{1: 2.0440939441861952, 2: 1.9779034961685824, 3: 1.737713466700642, 4: 1.7300995445526697, 5: 1.8024238077230097,
# 6: 1.8318799433096069, 7: 1.8088680290528358, 8: 1.8076435722892887, 9: 1.7105997850911381, 10: 1.7728034420099912, 11: 1.643302626064834, 12: 0.90667655114940726}