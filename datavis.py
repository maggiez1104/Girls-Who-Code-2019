import json
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud


polarity = []
subjectivity = []

#Get the JSON data
tweetFile = open("tweets_small.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

# Continue your program below!
bigtweet = ""
for tweet in tweetData:
    text = tweet["text"]
    tb = TextBlob(text)


    polaritynumber = tb.polarity
    polarity.append(polaritynumber)
    subjectivitynumber = tb.subjectivity
    subjectivity.append(subjectivitynumber)

    bigtweet += text

bigblob = TextBlob(bigtweet)
filterd = {}
allfrequencies = []
wordsList = bigblob.words
badwords = ["then", "where", "however", "when", "take"]
for word in wordsList:
    #filters HEREDITARY
    if len(word) < 3:
        continue
    elif word in badwords:
        continue
    elif not word.isalpha():
        continue
    if word == "DevOps":
        continue    
    filterd[word] = bigblob.word_counts[word]
print(filterd)
allfrequencies.append(filterd)

with open("dictdump.json") as f:
    try:
        olddata = json.load(f)
    except ValueError:
        olddata = []
allfrequencies.extend(olddata)
f.close()

f = open("dictdump.json", "w")
json.dump(allfrequencies, f)
f.close()



#create world cloud


averagepolarity = sum(polarity)/len(polarity)
#print(averagepolarity)
averagesubjectivity = sum(subjectivity)/len(subjectivity)
#print(averagesubjectivity)

#part 2
#polarity
#plt.xlabel('Polarity')
#plt.ylabel('Number of Tweets')
#plt.title('Tweet Polarity')
#plt.axis([-1, 1, 0, 60])
#plt.grid(True)
#plt.hist(polarity, bins = [-1.1, -.75, -.5, -.25, 0, .25, .5, .75, 1.1])
#plt.show()

#subjectivity
#plt.xlabel('subjectivity')
#plt.ylabel('Number of Tweets')
#plt.title('Tweet Subjectivity')
#plt.axis([0, 1, 0, 60])
#plt.grid(True)
#plt.hist(polarity, bins = [0, .25, .5, .75, 1.1])
#plt.show()f

#part 3
