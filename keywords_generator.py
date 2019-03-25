##A separate class for implementing keyword generation. This allows us to change how we implement keyword generation
##in the furture, without changing fundamentally how our code operates

#Right now, it's just a basic Rake implementation, courtesy of Tanner Fry

from rake import Rake

class Keyword_Generator():
    def __init__():
        self.model = Rake()
    def get_keywords(tweet)
        self.model.get_keywords_from_text(tweet)
        return self.model.get_ranked_phrases();
