import json
import csv
from textblob import TextBlob

## Methods
# method to get a converted star value based off sentiment
def getSentStar(sent):
    return 2.2338*sent + 3
# method that returns sentiment of a given json object / dictionary's text key
def getSent(n):
    blob = TextBlob(data[n]['text'])
    return float(blob.sentiment.polarity)

## Main Method
data = []
# read the entire file into a python list
with open('yelp_academic_dataset_review.json','r') as json_file:
    for line in json_file:
        data.append(json.loads(line))

# create csv writer object
csv_file = open('majortest1.csv', 'w')
csv_writer = csv.writer(csv_file, lineterminator = '\n')
csv_writer.writerow(['ReviewID','Sentiment','Stars','SentStart','Residual','Original Review'])

# Loop through each json object, get the sentiment, and add to that particular json object as a dictionary item
for n in range(0,len(data)-1): #range(0,len(data))
    review_id = data[n]['review_id']
    sentiment = getSent(n)
    stars = data[n]['stars']
    sentStar = getSentStar(sentiment)
    residual = stars - sentStar
    text = data[n]['text']
    csv_writer.writerow([review_id, sentiment, stars, sentStar, residual, text])

csv_file.close()
