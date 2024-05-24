# Scrappi - Outil de scraping de données Web

Scrappi est un outil Python avec une interface graphique Tkinter qui permet de récupérer des données à partir d'un site Web en utilisant Selenium et de les enregistrer dans un fichier JSON. Il offre également des fonctionnalités pour afficher, modifier et supprimer les fichiers JSON générés.

### Prérequis

Avant d'exécuter le script, assurez-vous d'avoir installé les bibliothèques Python suivantes :

- selenium

- tkinter

- Vous devez également avoir installé le pilote WebDriver approprié pour votre navigateur (par exemple, ChromeDriver pour Google Chrome).

 ## Utilisation

### Saisir les informations de scraping

- Entrez l'URL du site Web à scraper dans le champ "Entrez Url du site".

- Entrez le XPath de l'élément à cliquer (par exemple, un bouton d'acceptation des cookies) dans le champ "Xpath cookie".

- Entrez les noms des classes CSS à scraper, séparés par des virgules, dans la zone de texte "Class a scrap".

### Lancer le scraping

- Cliquez sur le bouton "Valider" pour lancer le processus de scraping.

- Le script ouvrira le navigateur, naviguera vers l'URL spécifiée, cliquera sur l'élément XPath fourni (s'il existe), et récupérera les données des éléments correspondant aux classes CSS spécifiées.

- Les données seront enregistrées dans un fichier JSON dans le dossier "data" du répertoire courant.

### Afficher un fichier JSON

- Cliquez sur le bouton "Sélectionner un fichier JSON".

- Naviguez jusqu'au fichier JSON que vous souhaitez afficher et sélectionnez-le.

- Le contenu du fichier JSON sera affiché dans la zone de texte.

- Modifier un fichier JSON

- Après avoir affiché un fichier JSON, vous pouvez modifier son contenu dans la zone de texte.

- Cliquez sur le bouton "Enregistrer" pour enregistrer les modifications apportées au fichier JSON.

### Supprimer un fichier JSON

- Après avoir affiché un fichier JSON, vous pouvez le supprimer en cliquant sur le bouton "Supprimer".

## Remarques

- Assurez-vous que le pilote WebDriver approprié pour votre navigateur est installé et accessible depuis votre système.

- Le script crée un dossier "data" dans le répertoire courant pour stocker les fichiers JSON générés.

- Vous pouvez personnaliser le script selon vos besoins, par exemple en modifiant les éléments à scraper ou en ajoutant des fonctionnalités supplémentaires.Scrappi - Outil de scraping de données Web

