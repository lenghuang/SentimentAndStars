import json
import csv
from textblob import TextBlob

## Methods
def getWordCount(text_reference):
    blob = TextBlob(text_reference)
    return len(blob.words)

## Main Method
under100 = []

# read the entire file into a python list
with open('DummyData.json','r') as file:
    for line in file:
        line = json.loads(line)
        if (getWordCount(line['text']) < 20):
            under100.append(line)

for n in range(0,len(under100)):
    print(under100[n]["text"])
