import os
import sys
import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import socket
import json

# definition des clefs fournies par Twitter
ACCESS_TOKEN = "WWWWWW"
ACCESS_SECRET =  "XXXXXX"
CONSUMER_KEY =  "YYYYYY"
CONSUMER_SECRET =  "ZZZZZZ"

# Definition du listener
class TweetsListener(StreamListener):
    def __init__(self, csocket):
        self.client_socket = csocket
    def on_data(self, data):
        try:
            msg = json.loads(data)
            if msg.get('text'):
                # exemple de transmission uniquement du champs text
                # il faut en tenir compte a la reception
                # recuperation et codage en utf8 du text du tweet
                tweet_text = msg['text'].encode('utf-8')
                # print("Tweet Text: " + tweet_text)
                # print ("------------------------------------------")
                  
                # envoie du champ text vers l'ip et port définis
                self.client_socket.send((tweet_text + '\n'))
            return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
    def on_error(self, status):
        print(status)
        return True

s = socket.socket()
# indiquer l'ip et le port qui connectent
host = "192.168.0.129"
port = 15555
c = None
s.bind((host, port))
s.listen(5)
c, addr = s.accept()
print("Connected... Starting getting tweets.")

# lancement du listener
l = TweetsListener(c)

# autorisation et accès aux tweets
auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
stream = Stream(auth, l)

# filtrage des tweets ayant coronavirus
stream.filter(track="coronavirus")

