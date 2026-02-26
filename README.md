# Détection d’objets en temps réel avec YOLO

## Description

Ce projet consiste à détecter des objets en temps réel à l’aide de la webcam.
C’était la première fois que j’utilisais **OpenCV** et **YOLO**, donc l’objectif était surtout d’apprendre les bases de la vision par ordinateur : capturer un flux vidéo, charger un modèle pré-entraîné et afficher les prédictions à l’écran.

Le programme affiche le nom des objets détectés ainsi que leur score de confiance. Les personnes sont ignorés car ici le but est de détectés uniquement les objets.

---

## Fonctionnement

* Capture vidéo en direct via la webcam
* Analyse de chaque image par le modèle YOLO
* Récupération des boîtes de détection 
* Affichage du label et du pourcentage de confiance
* Fermeture du programme avec la touche **q**

---

## Technologies utilisées

* Python — langage principal
* OpenCV — gestion de la caméra et affichage vidéo
* YOLO (Ultralytics) — modèle de détection d’objets
* Modèle pré-entraîné : `yolo11n.pt`

---

## Installation

Installer les dépendances :

```
pip install opencv-python ultralytics
```

Puis exécuter le script Python.

---

## Objectif du projet

* Découvrir OpenCV
* Comprendre le fonctionnement de YOLO
* Manipuler un modèle de deep learning pré-entraîné
* Travailler avec de la détection d’objets en temps réel

---

## Améliorations possibles

/ 
