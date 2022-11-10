# Cryptosystème d'ElGamal

## Objectifs du TIPE
— Modélisation : Le protocole RSA est fondé sur l’arithmétique. Nous défini-
rons tout d’abord les notions importantes sur les nombres entiers et pre-
miers. Nous démontrerons ensuite les théorèmes utilisés dans ce protocole.

— Simulation numérique : Nous modéliserons l’algorithme du système RSA
en python. L’objectif est de créer 4 fonctions : une première fonction ”cle”
qui génère une clé publique et privée. Une deuxième fonction ”chiffrer”
qui prend en entrée la clé publique et le message et qui renvoie un mes-
sage crypté. Une troisième fonction ”dechiffrer” qui prend en entrée la
clé privée et le message crypté et renvoie le message recherché. Enfin, une
quatrième fonction ”pirate” qui représente un élément intérmédiaire entre
l’émetteur et le récepteur, c’est-à-dire susceptible d’intercepter le message
transmis sans posséder la clé de décriptage. La fonction prendrait donc en
entrée la sortie de la fonction ”chiffrer” et tenterait de décrypter le message sans la clé.

— Synthèse : Nous ferons alors un bilan des données récoltées et de ce fait,
nous étudierons la sécurité du sytème RSA en le comparant aux autres
systèmes de cryptographie.
