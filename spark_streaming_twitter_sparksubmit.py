# base sur https://www.toptal.com/apache/apache-spark-streaming-twitter
# de Hanee Medhat Shousha
import sys
# pour forcer utf-8
reload(sys)
sys.setdefaultencoding('utf-8')
import time
import json

import requests

# From within pyspark or send to spark-submit:
from pyspark import SparkConf, SparkContext

from pyspark.streaming import StreamingContext
from pyspark.sql import Row,SQLContext

# envoi vers dashboard
def send_df_to_dashboard(df):
    # extract the hashtags from dataframe and convert them into array
    top_tags = [str(t.hashtag) for t in df.select("hashtag").collect()]
    # extract the counts from dataframe and convert them into array
    tags_count = [p.hashtag_count for p in df.select("hashtag_count").collect()]
    # initialize and send the data through REST API
    url = 'http://192.168.0.129:15002/updateData'
    request_data = {'label': str(top_tags), 'data': str(tags_count)}
    response = requests.post(url, data=request_data)


def aggregate_tags_count(new_values, total_sum):
    return sum(new_values) + (total_sum or 0)

def get_sql_context_instance(spark_context):
    if ('sqlContextSingletonInstance' not in globals()):
        globals()['sqlContextSingletonInstance'] = SQLContext(spark_context)
    return globals()['sqlContextSingletonInstance']

def process_rdd(time, rdd):
    print("rdd----------- %s -----------" % str(time))
    try:
        # Get spark sql singleton context from the current context
        sql_context = get_sql_context_instance(rdd.context)
        # convert the RDD to Row RDD
        row_rdd = rdd.map(lambda w: Row(hashtag=w[0], hashtag_count=w[1]))
        # create a DF from the Row RDD
        hashtags_df = sql_context.createDataFrame(row_rdd)
        # Register the dataframe as table
        hashtags_df.registerTempTable("hashtags")
        # get the top 10 hashtags from the table using SQL and print them
        hashtag_counts_df = sql_context.sql("select hashtag, hashtag_count from hashtags order by hashtag_count desc limit 10")
        hashtag_counts_df.show()
        # call this method to prepare top 10 hashtags DF and send them
        send_df_to_dashboard(hashtag_counts_df)
    except:
        e = sys.exc_info()[0]
        print("Error: %s" % e)


# Creer une configuration spark
conf = SparkConf()
conf.setAppName("TwitterStreamApp")

sc = SparkContext(conf=conf)
sc.setLogLevel("ERROR")

sc.setCheckpointDir("/tmp/TwitterStreamApp")

ssc = StreamingContext(sc, 10) # 60 second batch interval

# mise en commentaire car apparition d'une erreur
ssc.checkpoint("/tmp/TwitterStreamApp")

IP = "192.168.0.129"	# Replace with your stream IP
Port = 15555	        # Replace with your stream port

# recuperation du stream
# dans le cas de notre exemple, un texte en utf-8 est emis
lines = ssc.socketTextStream(IP, Port)

# cherche a compter les  hashtags

# chaque texte est splitte en mots
words = lines.flatMap(lambda line: line.split(" "))
# filtrage des mots en ne conservant que le  hashtags, puis map de chaque hashtag vers une paire (hashtag,1)
hashtags = words.filter(lambda w: '#' in w).map(lambda x: (x, 1))
# hashtags.pprint()
# reduction et comptage des hashtags
tags_totals  = hashtags.reduceByKey(lambda x, y: x + y)
# tags_totals.pprint()

tags_totals = hashtags.updateStateByKey(aggregate_tags_count)
tags_totals.pprint()
# do processing for each RDD generated in each interval
tags_totals.foreachRDD(process_rdd)


ssc.start() # Start reading the stream
ssc.awaitTermination() # Wait for the process to terminate

