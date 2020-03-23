'''
# demarrage du serveur zookerper (de kafka) utilisable en mode local
/opt/kafka/bin/zookeeper-server-start.sh /opt/kafka/config/zookeeper.properties &

# demarrage de kafka
/opt/kafka/bin/kafka-server-start.sh /opt/kafka/config/server.properties &

# lancer du script de connection 
python /opt/kafka/bin/topic_kafka_keyword.py
'''

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from kafka import KafkaProducer, KafkaClient

import json

access_token = "WWWWWW"
access_token_secret =  "XXXXXX"
consumer_key =  "YYYYY"
consumer_secret =  "ZZZZZZ"

class MyStreamListener(StreamListener):
    def on_data(self, data):
        # producer.send("coronavirus", data.encode('utf-8'))
        # recuperation et envoi tex
        full_tweet = json.loads(data)
        # transmet uniquement si  les champs text, id_str et id existent
        if full_tweet.get('text') and full_tweet.get('id_str') and full_tweet.get('id'):
            # exemple de transmission uniquement du champs text
            # il faut en tenir compte a la reception
            # tweet_text = full_tweet['text']
            # print("Tweet Text: " + tweet_text)
            # print ("------------------------------------------")
            # producer.send("coronavirus", tweet_text.encode('utf-8'))
            producer.send("coronavirus", data.encode('utf-8'))
            #print (data)
        return True
    def on_error(self, status):
        print (status)

# définition du producer
producer = KafkaProducer(bootstrap_servers="localhost:9092")
# mise en place du listener
l = MyStreamListener()
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
stream = Stream(auth, l)

# doit contenir coronavirus
stream.filter(track=["coronavirus"])
