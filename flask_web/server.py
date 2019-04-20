import sys
sys.path.insert(0, './code_src/')

from flask import Flask, request
from flask_cors import CORS
from tweet_handler import Tweet_Handler

app = Flask(__name__)
CORS(app)

t = Tweet_Handler()
@app.route("/")
def return_stories():
    tweet_id = request.args.get('tweetid')
    return t.Generate_Twitter_Stories(tweet_id)

