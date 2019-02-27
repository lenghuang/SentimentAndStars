import json
import csv
from textblob import TextBlob

## Methods
def getWordCount(text_reference):
    blob = TextBlob(text_reference)
    return len(blob.words)
def getSentStar(sent):
    return 2.5*sent + 3
def getSent(n, list):
    blob = TextBlob(list[n]['text'])
    return float(blob.sentiment.polarity)
def generateCSV(list, filename):
        csv_file = open(filename, 'w')
        csv_writer = csv.writer(csv_file, lineterminator = '\n')
        csv_writer.writerow(['ReviewID','Sentiment','Stars','SentStart','Residual','Word Count', 'Original Review'])
        for n in range(0,len(list)):
            review_id = list[n]['review_id']
            sentiment = getSent(n, list)
            stars = list[n]['stars']
            sentStar = getSentStar(sentiment)
            residual = stars - sentStar
            text = list[n]['text']
            wordCount = getWordCount(text)
            csv_writer.writerow([review_id, sentiment, stars, sentStar, residual, wordCount, text])
        csv_file.close()

## Main Method
under50 = []
under100 = []
under200 = []
under300 = []
under400 = []
under500 = []
under600 = []
under700 = []
under800 = []
under900 = []
under1000 = []
over1000 = []

# read the entire file into a python list
with open('yelp_academic_dataset_review.json','r') as file:
    for line in file:
        line = json.loads(line)
        if getWordCount(line['text']) < 50:
            under50.append(line)
        elif 50 <= getWordCount(line['text']) < 100:
            under100.append(line)
        elif 100 <= getWordCount(line['text']) < 200:
            under200.append(line)
        elif 50 <= getWordCount(line['text']) < 300:
            under300.append(line)
        elif 50 <= getWordCount(line['text']) < 400:
            under400.append(line)
        elif 50 <= getWordCount(line['text']) < 500:
            under500.append(line)
        elif 50 <= getWordCount(line['text']) < 600:
            under600.append(line)
        elif 50 <= getWordCount(line['text']) < 700:
            under700.append(line)
        elif 50 <= getWordCount(line['text']) < 800:
            under800.append(line)
        elif 50 <= getWordCount(line['text']) < 900:
            under900.append(line)
        elif 50 <= getWordCount(line['text']) < 1000:
            under1000.append(line)
        elif 1000 <= getWordCount(line['text']):
            over1000.append(line)

generateCSV(under50, 'Under50.csv')
generateCSV(under100, 'Under100.csv')
generateCSV(under200, 'Under200.csv')
generateCSV(under300, 'Under300.csv')
generateCSV(under400, 'Under400.csv')
generateCSV(under500, 'Under500.csv')
generateCSV(under600, 'Under600.csv')
generateCSV(under700, 'Under700.csv')
generateCSV(under800, 'Under800.csv')
generateCSV(under900, 'Under900.csv')
generateCSV(under1000, 'Under1000.csv')
generateCSV(over1000, 'Over1000.csv')
