# Readme Kafka et raspberry pi 4


- Mise en place des librairies python (twitter et kafka)
- Démarrage des servers zookeeper et kafka en mode local
- Création d'un topic (ici coronavirus)
- Lancement d'un producer de tweets à l'aide d'un script python



Hypothèse : kafka est installé sous le répertoire /opt/kafka

## Commandes qui seront lancés

## Installation (déjà effectué ou non) de librairies python

La première librairie fait la connection avec Kafka, les deux dernières avec twitter.

- pip install kafka-python
- pip install python-twitter
- pip install tweepy


## Démarrage du serveur zookerper (de kafka) utilisable en mode local
- /opt/kafka/bin/zookeeper-server-start.sh /opt/kafka/config/zookeeper.properties &

## Démarrage des serveurs kafka
- /opt/kafka/bin/kafka-server-start.sh /opt/kafka/config/server.properties &

## Création d'un topic, ici le topic a comme nom coronavirus
- /opt/kafka/bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic coronavirus

## Lancement du script producer 
(le sript a été placé dans le répertoire fichier)
- python ~/fichier/topic_kafka_keyword_v1.py


##  test de  reception coronavirus
Sur un autre terminal : 
- bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic coronavirus --from-beginning

## Arrêt des serveurs
- /opt/kafka/bin/zookeeper-server-stop.sh &
- /opt/kafka/bin/kafka-server-stop.sh  &



##  test de  reception coronavirus
- bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic coronavirus --from-beginning