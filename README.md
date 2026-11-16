# Mini-projet 1 – Conteneuriser et publier une application web

## 1. Présentation

Ce projet consiste à conteneuriser une application web Flask avec Docker.

L'application retourne un message de bienvenue au format JSON, indique l'environnement d'exécution et le nom d'hôte du conteneur.

## 2. Technologies utilisées

- Python 3.11
- Flask 3.1.0
- Docker
- Docker Hub
- Git

## 3. Fonctionnalités

L'application expose une route HTTP :

- GET / : retourne un message JSON.
- ENV : permet de configurer l'environnement d'exécution.
- Valeur par défaut de ENV : development.
- Port d'écoute : 5000.

## 4. Construction de l'image

```bash
docker build -t mini-projet-docker:1.0.1 .
```

## 5. Image Docker Hub

Dépôt : https://hub.docker.com/r/sihem93/mini-projet-docker

| Tag | Description |
|---|---|
| 1.0.0 | Première version |
| 1.0.1 | Deuxième version |
| 1.0 | Alias de 1.0.1 |

## 6. Télécharger l'image

```bash
docker pull sihem93/mini-projet-docker:1.0.1
```

## 7. Lancer l'application

```bash
docker run -d \
  --name mini-projet-docker \
  -p 8080:5000 \
  -e ENV=production \
  --memory=256m \
  --cpus=0.5 \
  sihem93/mini-projet-docker:1.0.1
```

Application accessible sur http://localhost:8080

## 8. Variables d'environnement

| Variable | Description | Valeur par défaut |
|---|---|---|
| ENV | Environnement d'exécution | development |

## 9. Vérification et diagnostic

```bash
docker ps -a
docker logs mini-projet-docker
docker inspect mini-projet-docker
docker history sihem93/mini-projet-docker:1.0.1
curl http://localhost:8080/
```

## 10. Arrêter et supprimer le conteneur

```bash
docker stop mini-projet-docker
docker rm mini-projet-docker
```

## 11. Organisation du projet

```text
mini-project-docker/
├── app.py
├── Dockerfile
├── requirements.txt
├── .dockerignore
├── .gitignore
└── README.md
```

## 12. Conclusion

Ce mini-projet permet de mettre en pratique les notions fondamentales de Docker : création d'une image, configuration par variables d'environnement, gestion des ressources, diagnostic, exploitation du cache, versionnage et publication sur Docker Hub.
