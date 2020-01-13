# Comment créer un simulateur de marché à l'aide de chaînes de Markov et de Python ?

# Traitement de l'information 
Pour cette analyse, on utiliserai les données analytiques de n'importe quel site web 
le dataset devrait suivre une structure similaire à celle ci-dessous. 

| USER ID | ACTION 1 | ACTION 2 | PAGE VIEWS |
|---------|----------|----------|------------|
| 1101    | 1        | 0        | 11         | 
| 1102    | 0        | 0        | 54         |
| 1103    | 1        | 1        | 3          |
          
Des exemples d'action peuvent être «offre / annonce cliquée», «abonnement cliqué», etc.

# Segmentation de la clientèle
Sélectionnez un jour particulier dans votre dataset et obtenez des données sur les nouveaux utilisateurs
pour un jour particulier. Par exemple :

| USER ID | JOUR     | STATUS   | ACTION 1   |
|---------|----------|----------|------------|
| 1101    | 1        | NEW USER | 1          | 
| 1102    | 1        | NEW USER | 0          |
| 1103    | 1        | NEW USER | 1          |

Vous pouvez ensuite diviser la distribution en 3 segments (inactif, actif et très actif)
en fonction de votre heuristique.

| USER ID | JOUR     | STATUS   | ACTION 1   | SEGMENTS |
|---------|----------|----------|------------|----------| 
| 1101    | 1        | NEW USER | 1          | 1        |
| 1102    | 1        | NEW USER | 0          | 3        | 
| 1103    | 1        | NEW USER | 1          | 2        |

après segmentation sur les données du premier jour:
 - 1 = utilisateur inactif
 - 2 = utilisateur actif 
 - 3 = utilisateur très actif
 
 Appliquer la segmentation à ces données après 30 jours. Assurez-vous de tenir compte du délai 
(par exemple, faites la moyenne de votre score d'engagement pour les 30 jours).
 
| USER ID | JOUR     | ACTION 1 | ACTION 2   | SEGMENTS |
|---------|----------|----------|------------|----------| 
| 1101    | 2-30     | 2        | 1          | 1        |
| 1102    | 2-30     | 32       | 28         | 3        | 
| 1103    | 2-30     | 9        | 10         | 2        |

# Preparation de la chaine de Markov
Voyons d'abord si notre système satisfait les hypothèses d'un modèle de Markov:
 - Il existe un ensemble fini d'états. Dans notre système, seuls 3 segments de clients peuvent entrer et sortir.
 - Les probabilités de se déplacer entre les états sont fixes. Donc Recurrent non nul.
 - Accessibilité de l'État. Les utilisateurs de n'importe quel segment peuvent passer à un autre segment sans aucune restriction externe. Donc Irreductible .
 - Non cyclique. Le mouvement de segment à segment n’est en aucun cas «automatique» dans notre système, Donc Aperiodique.
 
Notre système fonctionne bien contre la plupart des hypothèses de la chaîne de Markov. 
Cela nous donne une certaine confiance dans nos estimations de modèle, que nous obtiendrons
une fois que nous aurons construit le modèle.

# Construire la chaîne de Markov
De nos mouvements de segments enregistrés. Nous examinons comment les utilisateurs de chaque segment
le jour 1 sont passés à divers segments après 30 jours et calculons les probabilités en conséquence.
  
 
 
 
 
