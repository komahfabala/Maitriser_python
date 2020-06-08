# Maitriser_python
## le debut avec quelques exercices de debutant
>#### calcule de la moyenne a partir d'un fichier
>#### nombre***mystere
>#### trier des listes sans utiliser la fonction sort() de python
>#### calcule des surface de rectangle , triangle 
>#### produire des nombres aleatoires
>#### parcourir une chaine de caractere
le projet compte bancaire en python:
=================================== 
Objectif : 
========= 

    Définir les propriétés et méthodes d’une classe
    Définir des constructeurs
    Créer une instance de classe
    Accéder par les accesseurs aux propriétés en lecture et écriture d’un objet
    Appliquer des méthodes
    Définir des attributs et méthodes statiques

Travail à faire:
===============

    Définir une classe Client avec les attributs suivants : CIN, Nom, Prénom, Tél.
    Définir à l’aide des propriétés les méthodes d’accès aux différents attributs de la classe.
    Définir un constructeur permettant d’initialiser tous les attributs.
    Définir un constructeur permettant d’initialiser le CIN, le nom et le prénom.
    Définir la méthode Afficher ( ) permettant d’afficher les informations du Client en cours.
    Créer Une classe Compte caractérisée par son solde et un code qui est incrémenté lors de sa création ainsi que son propriétaire qui représente un client.
    Définir à l’aide des propriétés les méthodes d’accès aux différents attributs de la classe (le numéro de compte et le solde sont en lecture seule)
    Définir un constructeur permettant de créer un compte en indiquant son propriétaire.
    Ajouter à la classe Compte les méthodes suivantes :
        Une méthode permettant de Crediter() le compte, prenant une somme en paramètre.
        Une méthode permettant de Crediter() le compte, prenant une somme et un compte en paramètres, créditant le compte et débitant le compte passé en paramètres.
        Une méthode permettant de Debiter() le compte, prenant une somme en paramètre
        Une méthode permettant de Débiter() le compte, prenant une somme et un compte bancaire en paramètres, débitant le compte et créditant le compte passé en paramètres
        Une méthode qui permet d’afficher le résumé d’un compte.
        Une méthode qui permet d’afficher le nombre des comptes crées.
        une methode qui permet de rechercher un compte a partir en donnant son nom en paramètre.
        une methode qui permet de rechercher un compte en donnant son numero en paramètre.
    Créer une classe compteur d'objet qui permet de compter tous les objets instancier dans l'application.
    Créer un programme de test pour la classe Compte.
le projet Cercle en python:
==========================
Objectif : 
=========

    Définir les propriétés et méthodes d’une classe
    Définir des constructeurs
    Créer une instance de classe
    Accéder par les accesseurs aux propriétés en lecture et écriture d’un objet
    Appliquer des méthodes

Travail à faire:
===============

### Un cercle est défini par :

    Un point qui représente son centre 
    Son rayon r

On peut créer un cercle en précisant son centre et son rayon.

Dans ce problème, nous allons commencer tout d’abord par définir la classe Point définie par :

    Les attributs: x et y de type réel
    Un constructeur qui permet de définir les valeurs de x et de y.
    Une méthode Afficher () qui affiche une chaîne de caractères POINT(x,y).

### Les opérations que l’on souhaite exécuter sur un cercle sont :

    getPerimetre(): retourne le périmètre du cercle.
    getSurface(): retourne la surface du cercle.
    appartient (Point p): retourne si le point p appartient ou non au cercle.
    Afficher (): Affiche une chaîne de caractères de type CERCLE(x,y,R)
Le projet article en python:
===========================
Objectif :
=========  

    Définir les propriétés et méthodes d’une classe
    Définir des propriétés statiques
    Définir des constructeurs
    Créer une instance de classe
    Accéder par les accesseurs aux propriétés en lecture et écriture d’un objet
    Appliquer des méthodes

Travail à faire:
===============

    Créer la classe Article caractérisée par les attributs : Référence, Désignation, PrixHT, TauxTVA.

      Ces attributs doivent seulement être accessibles par le biais des accesseurs (get / set) en lecture/écriture mis en œuvre par les propriétés.

    Ajouter les constructeurs suivants :

    Un constructeur par défaut
    Un constructeur initialisant tous les attributs.
    Un Constructeur qui permet de renseigner la référence et la désignation lors de l’instanciation
    Un constructeur de recopie

    Implémentez la méthode CalculerPrixTTC() ;

        Cette méthode doit calculer le prix TTC d’un article qui équivaut à : PrixHT + (PrixHT*TauxTVA/100) et retournera la     valeur calculée.

    Ajouter la méthode AfficherArticle() qui affiche les informations de l’article.

    Créer un programme de test où il faut créer des objets (en utilisant les différents constructeurs) et leur calculer le prix TTC.

    Le taux de TVA est en fait commun à tous les articles. Pour éviter toute redondance de cet attribut, vous devriez donc la déclarer comme partagéeau niveau de la classe Article et non comme un attribut spécifique des objets instanciés à partir de la classe. Proposer une solution et tester de nouveau.
Debut Machine Learning:
=======================
    Les conceptes cités ci-dessous sont très importants dans la comprehension du machine learning:
    1. Mean: la moyenne des valeurs
    2. Median : la valeure au milieu
    3. Mode : la valeur qui apparait de plus dans la donnée 
