import tweepy
import goose
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import json
import pandas as pd
import matplotlib.pyplot as plt

con_key = "......write your own consumer key..."
con_secret = "...."
acc_token = "..."
acc_secret = "..."

class StdOutListener(StreamListener):
    def on_data(self, data):
        try:
            print data
            saveFile = open('academia1.txt','a')
            saveFile.write(data)
            saveFile.write('\n')
            saveFile.close()          
            return True
        except BaseException, e:
            print 'failed ondata,',str(e)
            time.sleep(5)
        

    def on_error(self, status):
        print status

        
l = StdOutListener()
auth = OAuthHandler(con_key, con_secret)
auth.set_access_token(acc_token, acc_secret)
stream = Stream(auth, l)
stream.filter(track=['trump india'])
