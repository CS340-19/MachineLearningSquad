from newsapi import NewsApiClient
class Search_Handler():
    def __init__(self):
        self.key = "1e0c8264ce8f4c4bb4a007b0e7bad782"
        self.newsapi = NewsApiClient(api_key = self.key)
    def do_search(self, query):
        self.stories = self.newsapi.get_top_headlines(q=query, language="en", country="us");
        print("".join(str(x) for x in self.stories)
        return self.stories
