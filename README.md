# Orchestration d'une Stack Hybride - Activité 2

Ce projet déploie une architecture multi-services orchestrée avec **Docker Compose**, pilotant simultanément une base de données SQL (MySQL) et NoSQL (MongoDB) via une API FastAPI.

## Architecture
Le projet se compose de 5 services interconnectés :
- **api** : Application FastAPI (Python) faisant le pont entre MySQL et MongoDB.
- **db_mysql** : Base de données SQL (Image officielle).
- **db_mongo** : Base de données NoSQL (Image personnalisée non-root).
- **admin_mysql** : Interface Adminer pour la gestion SQL.
- **admin_mongo** : Interface Mongo-Express pour la gestion NoSQL.

## Contraintes Techniques Respectées
- **Orchestration & Résilience** : Utilisation de `depends_on` avec `service_healthy` pour garantir l'ordre de démarrage.
- **Healthchecks "Métiers"** : Vérification réelle de l'intégrité des données (4 utilisateurs en SQL, 5 articles en NoSQL).
- **Sécurité** : 
    - Isolation des bases de données du monde extérieur (pas de ports exposés sur les DB).
    - Gestion des secrets via un fichier `.env` (non versionné).
    - Image MongoDB exécutée en mode **non-root**.
- **Volumes** : Initialisation des données via des scripts montés en volume.

## Démarrage
1. Cloner le dépôt.
2. Créer un fichier `.env` à partir du modèle `.env.example`.
3. Lancer la stack :
   ```bash
   docker compose up --build -d
   
## Liens d'accès
Une fois la stack saine (healthy), les services sont accessibles aux adresses suivantes :

API (Users) : http://localhost:8000/users

API (Posts) : http://localhost:8000/posts

Adminer : http://localhost:8080

Mongo-Express : http://localhost:8081