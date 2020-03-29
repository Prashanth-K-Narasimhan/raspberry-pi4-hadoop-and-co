# Installation de Hadoop

Nous avons installé Hadoop sur un cluster de raspberry pi 4. Ici, on prendra un exemple de 3 noeuds.

# Installation et configuration d'Hadoop 

On commence par télécharger la version 2.9.2 d'hadoop 

       wget https://downloads.apache.org/hadoop/common/hadoop-2.9.2/hadoop-2.9.2.tar.gz
       tar zxvf hadoop-2.9.2.tar.gz
       sudo mv hadoop-2.9.2 /opt/hadoop
       sudo chown pi:pi -R /opt/hadoop
       
# Modification du .bashrc

      nano ~/.bashrc
       
 puis ajouter les lignes suivantes :
 
    export HADOOP_HOME=/opt/hadoop
    export HADOOP_INSTALL=/opt/hadoop
    export PATH=$PATH:$HADOOP_INSTALL/bin
    export PATH=$PATH:$HADOOP_INSTALL/sbin
    export HADOOP_MAPRED_HOME=$HADOOP_INSTALL
    export HADOOP_COMMON_HOME=$HADOOP_INSTALL
    export HADOOP_HDFS_HOME=$HADOOP_INSTALL
    export YARN_HOME=$HADOOP_INSTALL
    export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-armhf
 
 concernant Java (je conseille d'installer la version 8)
 
    sudo apt-get install openjdk-8-jdk openjdk-8-jre
    sudo update-alternatives --config java
    
 vérification avec
 
    java -version
       
 # Préparation du répertoire hdfs
 
 Sur chaque noeud du cluster, effectuer les opérations suivantes :
 
    sudo mkdir /hdfs
    sudo mkdir /hdfs/tmp
    chown pi:pi -R /hdfs
    
    # si le répertoire doit être réinitialisé
    rm -rf /hdfs/tmp/*
    
    $HADOOP_HOME/bin/hdfs namenode -format
        

 # Configuration des fichiers de configuration de hadoop
 
 Dans le répertoire $HADOOP_HOME/etc/hadoop
 
 fichiers : core-site.xml, hdfs-site.xml, mapred-site.xml, yarn-site.xml, hadoop-env.sh, master et slaves
 
 (cf. répertoire hadoop)
 
 Attention aux configurations : remplacer pi-nodeXX par les noms des noeuds de votre cluster.
 
 # Lancer hadoop
 
    $HADOOP_HOME/sbin/start-dfs.sh
    $HADOOP_HOME/sbin/star-yarn.sh
    
 # vérification d'un démarrage correct
 
 - noeud maître
 
       pi@pi-node29:~ $ jps
       19920 ResourceManager
       7250 NameNode
       7539 SecondaryNameNode
       7350 DataNode
       20282 Jps
       20012 NodeManager

- noeud esclave

       pi@pi-node30:~ $ jps
       22643 Jps
       22473 NodeManager
       5341 DataNode
 
 • Pages web à regarder
 
 Concernant les nodes et les applications
 
 http://pi-node16:8088/cluster
 
 Concernant les datanodes
 
 http://pi-node16:9870/dfshealth.html#tab-overview
 
 (dans cet exemple, c'est pi-node16 qui gère)
 
