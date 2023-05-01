# MIAHOOT DEPLOY
Ce dépôt sert à lancer l'application Miahoot, sur une machine locale ou sur Google Cloud.

## Déploiement sur machine locale

pour cela, vous pouvez utiliser cette commande :
```sh
docker compose up
```

L'application sera disponible sur http://localhost:8080

## Déploiement sur Google Cloud

tout d'abord, il vous faut une clé Google cloud. Pour cela :
- Accédez à la console Google Cloud du projet (console.cloud.google.com) et sélectionnez le projet Miahoot.
Dans le menu de gauche, sélectionnez "IAM et administration" > "Comptes de service".
- Trouvez votre compte de service sur la page "Comptes de service" et cliquez sur le bouton "Modifier" dans la colonne "Actions".
- Cliquez sur le bouton "+ Créer une clé" et sélectionnez le type de clé "JSON".
- Enregistrez le fichier de clé téléchargé dans le dossier keys, à la racine de ce projet.

ATTENTION : Ces clés permettent de lancer des ressources payantes Google Cloud. Si cette clé est exposée sur internet (via un git push malencontreux notamment), un utilisateur malveillant pourrait utiliser cette clé à ses propres fins. Si cela devait arriver, supprimez la clé au plus vite des accès Google Cloud. Dans l'état actuel du .gitignore, tout fihcier présent dans keys ne figurera pas dans les commits

Une fois la clé téléchargée dans le dossier keys, renommez-la en keys.json. 

Une fois cela fait, créez les fichiers de configuration kubernetes avec la commande suivante :
```sh
kompose convert --file docker-compose.yaml --out ./kube-scripts/
```
Si vous n'avez pas kompose installé sur votre machine, vous pouvez suivre le [tutoriel à cette adresse.](https://github.com/kubernetes/kompose#binary-installation)

Ensuite, exécutez cette commande pour avoir toutes les dépendances pour le bon fonctionnement du script python :

```sh
pip install google-auth google-auth-oauthlib google-auth-httplib2 google-cloud-container kubernetes
```

Enfin, exécutez cette commande :

```sh
python deployment_script.py
```

L'application sera disponible à cette addresse : 