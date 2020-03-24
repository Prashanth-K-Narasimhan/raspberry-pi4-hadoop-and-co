# Utilsation Spark Streaming

## Example avec twitter

Lançons les trois applications dans l’ordre suivant :
 
- Twitter App Client.

        python spark_streaming_twitter_client.py


- Soumission du script Spark.

On commence par démarrer les services spark, puis on soumet le script 

        python$SPARK_HOME/sbin/start-all.sh
        /opt/spark/bin/spark-submit spark_stream_twitter.py

- Tableau de bord Web App.

On commence par lancer app.py qui va définir la page html si dessous

       python app.py
       
puis on lance un browser internet : ip_defini_app_py:port_defini_app_py
