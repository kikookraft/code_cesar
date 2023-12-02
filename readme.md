# Code & chiffrage
Tomy Besson & Lenny Bay
## Table des matières
- [Code Inverse](#code-inverse)
    - [Exemples](#exemples) 
- [Code César](#code-césar)
    - [Exemples](#exemples-1)
- [Code Vigenère](#code-vigenère)
    - [Exemples](#exemples-2)   
- [Code César affine](#code-césar-affine)
    - [Génération des clés](#génération-des-clés)
    - [Chiffrement](#chiffrement)
    - [Déchiffrement](#déchiffrement)
    - [Exemples](#exemples-3)   

## Général
Le programme est composé de 4 fonctions principales qui sont appelées dans le `__main__` en fonction du choix de l'utilisateur.

Il est d'abord demandé a l'utilisateur de choisir un message a chiffrer ou déchiffrer.  

Les differents moyen de chiffrer sont accessibles via un menu qui demande a l'utilisateur de choisir entre 4[*](#note) choix qui sont les suivants:
- Code Inverse
- Code César
- Code Vigenère 
- Code César affine

Le programme demande ensuite a l'utilisateur un mode (chiffrage ou déchiffrage) et une clé (si besoin) puis affiche le résultat du chiffrage ou du déchiffrage.

## Code Inverse
> Fonction `optimized_crypt` ligne `64`

Le code inverse est un code très simple qui consiste à inverser l'ordre des lettres d'un message.  
Au lieu de la fonction donné dans l'énnoncé, nous avons utilisé un manière plus simple de faire la fonction grace a python (en inversant directement la liste).  
### Exemples
- `Bonjour` > `ruojnoB`
- `Bonjour, comment allez-vous?` > `?uov-zeulla tnemmoc ,ruojnoB`
- `Je suis un code` > `edoc nu sius eJ`

## Code César
> Fonction `cesar` ligne `70`

Le code César est un code qui consiste à décaler les lettres d'un message d'un certain nombre de lettres. Pour le déchiffrer il suffit de décaler les lettres dans l'autre sens.  
Dans le code on utilise la clé pour décaler les lettres en permuation circulaire.

### Exemples
- Clé: 3, Message: `Bonjour`  
Resultat: `e#Ç.#p_`
- Clé: -3, Message: `e#Ç.#p_`  
Resultat: `Bonjour`  
- Clé: 42, Message: `Il a mangé des camions a la lavande?`  
Resultat: `+Vxùx2ùèI$x,vaxGù2NPèaxùxVùxVùâùè,vL`
- Clé: -42, Message: `+Vxùx2ùèI$x,vaxGù2NPèaxùxVùxVùâùè,vL`
Resultat: `Il a mangé des camions a la lavande?`

## Code Vigenère
> Fonction `code_vigenere` ligne `79`

Le code Vigenère est un code qui consiste à décaler les lettres d'un message d'un certain nombre de lettres en fonction de la clé qui est un mot. Pour le déchiffrer il suffit de décaler les lettres dans l'autre sens.

### Exemples
- Clé: `bonjour`, Message: `Bonjour`, Mode: `chiffrer`  
Resultat: `Âf]ÔfOû`
- Clé: `bonjour`, Message: `Âf]ÔfOû`, Mode: `déchiffrer`  
Resultat: `Bonjour`
- Clé: `Muzik4`, Message: `La 3ème touche FA# du piano ne fonctionne plus!!`, Mode: `chiffrer`  
Resultat: `dtM^?(LDgDZ9+=M[aGÉN10SzÂÊ00RoÉE0:@BûÙE:lb8[1kcm`
- Clé: `Muzik4`, Message: `dtM^?(LDgDZ9+=M[aGÉN10SzÂÊ00RoÉE0:@BûÙE:lb8[1kcm`, Mode: `déchiffrer`  
Resultat: `La 3ème touche FA# du piano ne fonctionne plus!!`

## Code César affine
Le code césar affine utilise deux clés pour décaler les lettres d'un message. La première clé est un nombre premier avec la taille de l'alphabet utilisé. La deuxième clé est un nombre aléatoire.

Le programme utilise des nombres aléatoire a chaque utilisation pour générer les clés.

### Génération des clés
> Fonction `genere_cle` ligne `28`

Deux nombres `a` et `b` sont généré aléatoirement entre 0 et 1000.
La fonction verifie ensuite que `a` est premier avec la taille de l'alphabet utilisé (109) grâce a la fonction `verif_cle` ligne `39` . Si ce n'est pas le cas, `a` reprend une nouvelle valeur aléatoire et la fonction recommence.

La fonction `verif_cle` utilise la fonction `pgcd` ligne `23` pour calculer le pgcd de `a` et de la taille de l'alphabet.

### Chiffrement
> Fonction `affine` ligne `95`

Le chiffrement utilise la formule suivante: `y = (a * x + b) % (taille alphabet)`
- `y` est la lettre chiffré
- `x` est la lettre à chiffrer
- `a` est la première clé
- `b` est la deuxième clé
- `taille alphabet` est la taille de l'alphabet utilisé (109 dans notre cas)

### Déchiffrement
> Utilise la même fonction que le chiffrement avec le paramètre `decrypt`

Pour déchiffer le message, on a besoin de la clé `a` et de la clé `b` pour créer la clé inverse. Pour cela on appelle la fonction `prime` ligne `45` qui est une implémentation de l'algorithme d'Euclide étendu. Cette fonction nous permet de trouver `a'` et `b'` tel que `a * a' + b * b' = 1`.

On utilise ensuite la formule suivante pour déchiffrer le message: `x = (a' * y + b') % (taille alphabet)`
- `y` est la lettre chiffré
- `x` est la lettre à chiffrer
- `a'` est la clé inverse de `a`
- `b'` est la clé inverse de `b`
- `taille alphabet` est la taille de l'alphabet utilisé (109 dans notre cas)

### Exemples
- Clé: `a = 7`, `b = 42`, Message: `Bonjour`, Mode: `chiffrer`  
Resultat: `ùK_-K9k`
- Clé: `a = 7`, `b = 42`, Message: `ùK_-K9k`, Mode: `déchiffrer`  
Resultat: `Bonjour`
- Clé: `a = 871`, `b = 60`, Message: `Lorem Ipsum Dolor Sit Amet`, Mode: `chiffrer`  
Resultat: `PJ'ejk.G08jkWJRJ'kC9#kîje#`
- Clé: `a = 871`, `b = 60`, Message: `PJ'ejk.G08jkWJRJ'kC9#kîje#`, Mode: `déchiffrer`  
Resultat: `Lorem Ipsum Dolor Sit Amet`
---
#### Note
Il existe un 5ème choix dans le menu (activable en ecrivant `5`), cela permet d'activer un fonction qui teste automatiquement la validité du code césar affine en chiffrant et déchiffrant plusieures phrases avec des clés aléatoires et en comparant le résultat avec le message de départ.
Cette fonction permettait le debugage du code césar affine de manière plus rapide.
