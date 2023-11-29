# Utilisation de Nice Piges Radio


## ETAPE 1 : Installation

Assurez-vous que python soit installé sur votre PC. Ouvrez le CMD et tapez :
```python
python --version
```
Si la version de python s'affiche vous avez python !

Sinon, installez Python depuis la page officielle de python (https://www.python.org/downloads/)

Lancez le fichier <code>"setup_nicepiges"</code>

Une fois l'installation terminée, fermez la fenêtre d'installation.

<br>


## ETAPE 2 : Ajouter votre radio

Déplacez vous dans le dossier de l'une des instances (ex: <code>insance-1</code>)

Pour ajouter votre radio, ouvrez avec un éditeur de texte (bloc notes, vscode...) 
le fichier <code>"soft_nice_piges.py"</code> et modifier les valeurs entre " " des lignes indiquées au début.
A savoir :
- Le nom de votre radio 
- l'url du flux de diffusion de votre radio
- le type d'encodage du flux de votre radio (aac, mp3, flac, ogg...)

<span style="color:violet;">De préférence, ne modifiez pas le code du logiciel à part ces trois éléments listés ci-dessus. Celà évitera tout problème.</span>

<br>

## ETAPE 3 : Démarrer le logiciel

Lancez le logiciel en double cliquant sur <code>"START Nice Piges Radio"</code> dans le répertoire du logiciel.

Vous verrez un dossier <code>"Piges nom_de_votre_radio"</code> créé dans le répertoire du logiciel, les piges sont 
rangées par jour de la semaine et les fichiers sont créés heure par heure.

<span style="color:violet;">Attention, le logiciel fonctionne sur un enregistrement d'une semaine, chaque heure d'une semaine passée
est remplacée par la semaine courante !</span>

<br>

## ETAPE 4 : Piger plusieurs radios

Pour faire les piges de plusieurs flux (plusieurs radios), il suffit de copier le contenu du dossier de <code>instance-1</code> vers un nouveau dossier à côté de celui-ci (par exemple <code>instance-2</code>) <span style="color:violet;"> mais ne copiez pas le sous-dossier "Piges nom_de_radio"</span>, de toute façon les piges seront recréées par le logiciel.

Mettez les paramètres de la radio que vous souhaitez.

Lancez la deuxième instance du logiciel avec le fichier START !

<br>
<br>

<span style="color:white; font-size:18px; border:solid white 1px; padding:8px; text-align:center; background-color:rgb(13,255,251,0.2); "> Bonne utilisation de "Nice Piges Radio"
by @valuthringer </span>