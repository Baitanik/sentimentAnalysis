
from textblob import TextBlob
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import sys
import argparse

#Variables that contains the user credentials to access Twitter API 
consumer_key='xxxxxxxxxxxxxxxxxxxxxxx'
consumer_secret='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
access_token_key='xxxxxxxx-xxxxxxxxxxxxxxxxx'
access_token_secret='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'



class StdOutListener(StreamListener):

    def on_data(self, data):
        jsondata = json.loads(data)
#         print(jsondata) # will print whole json data with very detailed informations
        if "text" in jsondata:
            self.print_sentiment(jsondata['text'])
        return True

    def on_error(self, status):
        print(status)
        
    def print_sentiment(self,text):
        sentimentData = TextBlob(text)
        print(text.encode("utf-8"))
        sentimentVal="";
        if  sentimentData.sentiment.polarity > 0 :
            sentimentVal = "positive"
        elif sentimentData.sentiment.polarity < 0 :
            sentimentVal = "negative"
        else :
            sentimentVal = "neutral"
            
        print("Sentiment : {} , Polarity Value :{}".format(sentimentVal, sentimentData.sentiment.polarity));
        sys.stdout.flush()


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='twitter sentiment analysis')
    parser.add_argument("keyword", help="Please provide the keyword for which tweets will be received")
    args = parser.parse_args()
#     print(args.keyword)
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token_key, access_token_secret)
    stream = Stream(auth, l)
    stream.filter(track=[args.keyword])