from nltk.tokenize import TweetTokenizer
from nltk.corpus import twitter_samples
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import re

def raw_string(s):
    if isinstance(s, str):
        s = s.encode('string-escape')
    elif isinstance(s, unicode):
        s = s.encode('unicode-escape')
    return s;

def re_buf(string):
    string = re.sub(r'http\S+', '', string)
    return string
##print(twitter_samples)

corpus = twitter_samples.strings();

train = corpus[:len(corpus)/2]
tweet  = TweetTokenizer(strip_handles = True, reduce_len = True)
train2 = list()
map(re_buf, train)
#regex = re.compile(r"^@.* ")
for x in train:
    train2.append(tweet.tokenize(x))
#train2 = {tweet.tokenize(x) for x in train}
test = corpus[len(corpus)/2:]
vect = TfidfVectorizer(analyzer = "word", tokenizer = tweet.tokenize, stop_words = 'english')
X = vect.fit_transform(train)
indices = np.argsort(vect.idf_)[::-1]
features = vect.get_feature_names()
top_n = 1000
top_features = [features[i] for i in indices[:top_n]]
print top_features
print(X.shape)
#feature_Array = np.array(tfidf.get_feature_names())
#tfidf_sorting = np.argsort(response.toarray()).flatten()[::-1]

#n = 3
#top_n = feature_array[tfidf_sorting][:n]
#print(train2, "\n")
#print("\n\nFN:\n\n")
#print(X.get_feature_names())
#print(train)
#classifier = nl.NaiveBayesClassifier.train(train)
#print("Classifier accuracy percent:",(nltk.classify.accuracy(classifier, test))*100)


'''from datetime import date
from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key = '1e0c8264ce8f4c4bb4a007b0e7bad782')
d = date.today()
today = "%04d-%02d-%02d" % (d.year, d.month, d.day)
print(today)
##all_articles = newsapi.get_everything(language = 'en', from_param = today)

try:
    all_articles = newsapi.top_headlines(q='bitcoin',
                                      sources='bbc-news,the-verge',
                                      domains='bbc.co.uk,techcrunch.com',
                                      from_param='2017-12-01',
                                      to='2017-12-12',
                                      language='en',
                                      sort_by='relevancy',
                                      page=2)
except:
    print("error\n")
for x in all_articles:
    print(x)
'''


