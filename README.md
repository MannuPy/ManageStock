# ManageStock

Ce projet est une API de gestion de stock professionnelle développée en utilisant Django REST Framework. Il permet de gérer efficacement vos articles, leurs quantités, leurs prix et bien plus encore.

## Configuration de l'Environnement Virtuel

1. Assurez-vous d'avoir Python installé sur votre système.

2. Clonez ce dépôt sur votre machine :

git clone(https://github.com/MannuPy/ManageStock.git

bash


3. Accédez au répertoire du projet :

cd ManageStock




4. Créez un environnement virtuel nommé `venvstage` :

python -m venv venvstage



5. Activez l'environnement virtuel :

- Sur Windows :

  ```
  venvstage\Scripts\activate
  ```



6. Installez les dépendances requises :

pip install -r requirements.txt




## Configuration de la Base de Données

Ce projet utilise la base de données SQLite par défaut de Django. Assurez-vous d'avoir correctement configuré votre base de données dans le fichier `settings.py` de l'application "Stock".

## Migration de la Base de Données

Appliquez les migrations pour créer la base de données et les tables requises :

python manage.py makemigrations
python manage.py migrate



## Démarrage du Serveur de Développement

Lancez le serveur de développement Django :

python manage.py runserver

 


Le serveur sera accessible à l'adresse [http://127.0.0.1:8000/]

## API Endpoints

- **Créer un nouvel utilisateur** (Inscription) :
  - URL : [http://127.0.0.1:8000/signup]
  - Méthode : POST
  - Exemple de Données JSON :
    ```json
    {
      "username": "VotreNomUtilisateur",
      "password": "VotreMotDePasse",
      "email": "votre@email.com"
    }
    ```

- **Connecter un utilisateur** (Connexion) :
  - URL : [http://127.0.0.1:8000/login](http://127.0.0.1:8000/login)
  - Méthode : POST
  - Exemple de Données JSON :
    ```json
    {
      "username": "VotreNomUtilisateur",
      "password": "VotreMotDePasse"
    }
    ```

- **Tester un Token d'Authentification** :
  - URL : [http://127.0.0.1:8000/test_token]
  - Méthode : GET
  - Exemple : Vous devez inclure un en-tête d'autorisation (Authorization) avec un token valide.

## Opérations CRUD pour les Articles

Vous pouvez effectuer les opérations CRUD (Create, Read, Update, Delete) pour les articles en utilisant les points de terminaison de l'API :

- **Créer un Article** :
  - URL : http://127.0.0.1:8000/api/articles/
  - Méthode : POST
  - Exemple de Données JSON : Consultez les champs du modèle Article.

- **Récupérer la Liste des Articles** :
  - URL : [http://127.0.0.1:8000/api/articles/]
  - Méthode : GET

- **Récupérer un Article par ID** :
  - URL : [http://127.0.0.1:8000/api/articles/1/
  - Méthode : GET

- **Mettre à Jour un Article par ID** :
  - URL : [http://127.0.0.1:8000/api/articles/1/](http://127.0.0.1:8000/articles/1/)
  - Méthode : PUT
  - Exemple de Données JSON : Consultez les champs du modèle Article.

- **Supprimer un Article par ID** :
  - URL : [http://127.0.0.1:8000/api/articles/1/](http://127.0.0.1:8000/articles/1/)
  - Méthode : DELETE
