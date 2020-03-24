# Raspberry pi 4 - hadoop and Co

L'objectif de github est de montrer qu'on peut utiliser quelques modules de l'écosystème Hadoop avec des raspberry pi 4.

- Présentation du cluster Hadoop [cf. Description_cluster_raspberry.md]

- Installation des modules suivants :
    - Hadoop (README_hadoop.md)
    - Spark
    - Kafka  (README_kafka.md)
    - Zookeeper
    - Cassandra
    
- Utilisation par le biais d'un fil rouge : amusons avec des tweets

- On commencera par :
  - utilisation de spark streaming (cf. README_spark-streaming-twitter.md)
  - tranfert de tweets dans kafka
  - intégration à spark
  - utilisation de cassandra
  - intégration de cassandra
