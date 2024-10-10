Instructions pour Exécuter le Projet Django Social
Prérequis
Avant de commencer, assurez-vous que les éléments suivants sont installés sur votre machine :
Python (version 3.6 ou supérieure)
pip (gestionnaire de paquets Python)

Étape 1 : Cloner le Dépôt
Ouvrez votre terminal ou invite de commande et exécutez la commande suivante pour cloner le dépôt :
git clone https://github.com/Aaronia09/asitech_social.git

Étape 2 : Naviguer vers le Répertoire du Projet
Accédez au répertoire du projet cloné :
cd asitech_social

Étape 3 : Configurer la Base de Données
Avant d'exécuter le projet, vous devez appliquer les migrations de la base de données. Exécutez les commandes suivantes :

python manage.py makemigrations
python manage.py migrate

Étape 4 : Créer un Superutilisateur (Facultatif)
Si vous souhaitez accéder à l'interface d'administration de Django, créez un superutilisateur :

python manage.py createsuperuser
Suivez les instructions pour définir un nom d'utilisateur, une adresse e-mail et un mot de passe.

Étape 5 : Exécuter le Serveur de Développement
Pour démarrer le serveur de développement, exécutez la commande suivante :
python manage.py runserver
Le serveur sera accessible à l'adresse suivante : http://127.0.0.1:8000/

Liens de l'Application
Voici une liste des liens  :
-Page d'accueil
URL : http://127.0.0.1:8000/
Lien : Accueil
-Page d'enregistrement
URL : http://127.0.0.1:8000/social/register/
Lien : S'inscrire
- Page de connexion
URL : http://127.0.0.1:8000/social/login/
Lien : Se connecter
-Créer une publication
URL : http://127.0.0.1:8000/social/post/create/
Lien : Créer une Publication
-Détails d'une publication
URL : http://127.0.0.1:8000/social/post/<post_id>/ 
Lien : Détails de la Publication 
-Ajouter un commentaire à une publication
URL : http://127.0.0.1:8000/social/post/<post_id>/comment/ 
Lien : Ajouter un Commentaire 
-Aimer une publication
URL : http://127.0.0.1:8000/social/post/<post_id>/like/
Lien : Aimer la Publication (Il faut cliquer sur Voir les commentaires)
-Profil de l'utilisateur
URL : http://127.0.0.1:8000/social/profile/
Lien : Mon Profil
-Notifications
URL : http://127.0.0.1:8000/social/notifications/
Lien : Notifications
