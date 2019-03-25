from rake_nltk import Rake
r = Rake()
tweet = "After more than two years of Presidential Harassment, the only things that have been proven is that Democrats and other broke the law. The hostile Cohen testimony, given by a liar to reduce his prison time, proved no Collusion! His just written book manuscript showed what he"
r.extract_keywords_from_text(tweet)
print(r.get_ranked_phrases())
