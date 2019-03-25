import json
from pycorenlp import StanfordCoreNLP

def getAvgSent(sent):
    total = 0
    count = 0
    for s in sent["sentences"]:
        total += float(s["sentimentValue"])
        count += 1
    return (total / count)

# Sets up server
nlp = StanfordCoreNLP('http://localhost:9000')

text = "I love this pizza place, it has the best cheese slice in town. But, it is a bit expensive, so I'm not sure if it is worth it."

sent = nlp.annotate(text, properties={'annotators':'sentiment','outputFormat':'json', 'timeout':1000})

print(getAvgSent(sent))
