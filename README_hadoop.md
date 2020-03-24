# Installation de Hadoop

Nous avons installé Hadoop sur un cluster de raspberry pi 4. Ici, on prendra un exemple de 3 noeuds.

# Installation et configuration d'Hadoop 

On commence par télécharger la version 2.9.2 d'hadoop 

       wget https://downloads.apache.org/hadoop/common/hadoop-2.9.2/hadoop-2.9.2.tar.gz
       tar zxvf hadoop-2.9.2.tar.gz
       sudo mv hadoop-2.9.2 /opt/hadoop
       
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
       

 # Configuration des fichiers de configuration de hadoop
 
 
 
 
