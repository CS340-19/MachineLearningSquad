from rake_nltk import Rake
import tweepy
#Twitter verifcation
consumer_key = '6rhHP477gI9xV4Yfq61dBc1bW'
consumer_secret = 'ZJIcQdLKyFTXqq2wYNk8VuwbIbjVX7VBXnmRl1KNCxPuuctHhN'
access_token = '1086272151907454976-szO2NJn3e5qnXj3SeDgnJKB3sQ8OqU'
access_token_secret = 'sl4scvVPoQqsge0tQnpYMtyrGFy8ettiNvz7sBULxKHQZ'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#grab tweet based on tweet ID given
tweetid = input("Tweet ID: ")

#grab all characters of tweet and print it out
tweet = api.get_status(tweetid,tweet_mode='extended')
print(tweet.full_text)

#rake is used as a basic word extraction
r = Rake();
r.extract_keywords_from_text(tweet.full_text)
words = r.get_ranked_phrases();
string = " ".join(str(x) for x in words)

#print what words rake extracts
print(string)

#make sure google search is imported
try:
    from googlesearch import search
except ImportError:
    print("No module name 'google' found")

#prinout top 3 seach results from google search on the keywords rake extracted
for j in search(string, tld='com', num=3 ,stop = 1, pause=2):
    print(j)
