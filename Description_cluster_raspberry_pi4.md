# Description du cluster Raspberry pi 4

## MATÉRIELS

- 20 raspberry pi 4 
- 20 cartes micro SD Noobs 32Gb
- 20 alimentations officielles 15.3W usb-c
- 5 hubs NetGear GS 205 (5 ports)
- 1 hub NetGear GS 316 (16 ports)
- 8 multiprises
- 5 MakerFun pour Raspberry Pi 4 Model B & Raspberry Pi 3 B + Boîtier avec Ventilateur et radiateur, Boîtier en Acrylique 4 Couches superposable Boîtier Cluster pour Raspberry Pi 3/2 modèle B
- 20 cables éthernet 0,25cm
- 5 cables ethernet 50 cm
- 1 grand cable ethernet vers la prise réseau

## Mise en place

- 4 raspeberry pi sont connectés à un GS 205 lui même connecté au GS 316.

## Utilisation d'un NAS synology pour gérer le DHCP

## IP
- Les raspberry ont été nommés pi-node13 à pi-node32
- Les ip 192.168.0.113 à 192.168.0.132

- Les (ip nom_noeuds) ont été intégrés à chaque fichier /etc/hosts.
- cf le fichier hosts

        192.168.0.113 pi-node13
        192.168.0.114 pi-node14
        192.168.0.115 pi-node15
        192.168.0.116 pi-node16
        192.168.0.117 pi-node17
        192.168.0.118 pi-node18
        192.168.0.119 pi-node19
        192.168.0.120 pi-node20
        192.168.0.121 pi-node21
        192.168.0.122 pi-node22
        192.168.0.123 pi-node23
        192.168.0.124 pi-node24
        192.168.0.125 pi-node25
        192.168.0.126 pi-node26
        192.168.0.127 pi-node27
        192.168.0.128 pi-node28
        192.168.0.129 pi-node29
        192.168.0.130 pi-node30
        192.168.0.131 pi-node31
        192.168.0.132 pi-node32


