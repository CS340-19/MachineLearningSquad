import pprint
import json
from newsapi import NewsApiClient
from googleapiclient.discovery import build
class Search_Handler():
    def __init__(self):
        self.service = build("customsearch", "v1", developerKey="AIzaSyBJrI3DsXAEvFoZnT4xaJJxmoVGIfO3jmw")
    def do_search(self, query):
        self.stories = self.service.cse().list(
                q=query, cx="012957021449082369818:uml3rkdclnk", num=3).execute()
        #print((self.stories))
        self.stories_json = json.dumps(self.stories)
        self.decoded_stories = json.loads(self.stories_json)
        #self.items = json.dumps(self.decoded_stories[u'items'])
        #self.decoded_items = json.loads(self.items)
        self.return_value = list()
        for key in self.decoded_stories[u'items']:
            '''
            print("STORY--------------------------------------------------------")
            for item, value in key.iteritems():
                print(item,value)
                print("\n")
            '''
            self.return_value.append({"title":key[u'title'], "description":key[u'snippet'], "link":key[u'link']})
        return json.dumps(self.return_value)
