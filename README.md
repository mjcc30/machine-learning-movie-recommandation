# machine-learning-movie-recommandation

## groupe 2
Hicham ECHARIF CHEFCHAOUNI 
Maxime CORDEIRO
Louis POULIN
Nicolas DENIS
Ivan BRAGA FERNANDES

## description
Dans ce projet, nous allons construire un système de recommandation de films de base en utilisant le jeu de données TMDB 5000 Movie.

https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset

## Livrables attendus 

1. Une organisation DevOps Azure qui contient :  
  - Un board où vous répartissiez les tâches entre les membres de votre groupe suivant votre méthode de travail Agile, Scrum  
  - Les pipelines pour le CI/CD 

2. Un repo Github contenant : 
  - Un fichier README (où vous expliquez comment lancer les scripts, …),
  - Un notebook Python (non cleané, pour comprendre votre démarche :  
    - Les problèmes rencontrés sur le jeu de données  
    - Comment vous avez nettoyé les données 
    - Votre modélisation (du preprocessing à la prédiction). 
    - Le code générant le dashboard et permettant de déployer le modèle sous forme d’API 

3. L’URL de la WebApp mise en ligne et répondant au cahier des charges précisé ci-dessus.  
  - Un support de présentation (environ 10 slides) :  
  - De La démarche de modélisation et la méthodologie d’entraînement du modèle  
  - De La fonction coût, l’algorithme d’optimisation et la métrique d’évaluation
  - L’interprétabilité du modèle est explicitée (1 page max). N’oubliez pas : la façon d'interpréter l'importance des variables n'est pas la même pour une régression logistique que pour un random forest (par exemple). Préciser les limites éventuelles ?  
  - Les limites et les améliorations possibles pour gagner en performance et en interprétabilité (1 page max) 
 

## Modalités de présentation du travail 

Votre présentation pourra prendre cette forme : 

- 5 min. Présentation de la problématique, de l'exploration des données, du cleaning effectué, du feature engineering 
- 10 min Présentation des différentes pistes de modélisation effectuées 
- 10 min Présentation du dashboard 
- 10 min Séance de questions-réponses

## How to

lancement des scripts pour le front

```
cd front
npm install
npm start
```

lancement des scripts pour l'api

```
pipenv install
cd api
gunicorn --bind 127.0.0.1:5050 wsgi:app
```
