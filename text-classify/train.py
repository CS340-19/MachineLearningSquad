from nltk.corpus import twitter_samples
import random

tweets = twitter_samples.strings()
selected = random.sample(tweets, 10);
infoedTweets = list()

f = open("keywords.train", "a")
for t in selected:
    print(t, "\n");

    f.write(t.encode("ascii", "ignore"))
    f.write("\t")
    #i = raw_input("Keywords: ");
    #print(i);
    f.write(raw_input("Keywords: ").lower())
    f.write("\n")

    
