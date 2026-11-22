# CultureGSite

Site de culture générale : 9 vignettes thématiques (santé, géopolitique, économie, physique, informatique, mathématiques, études, philosophie et sagesse, langue française). Chaque vignette ouvre une page de thème qui liste et résume les documents, pages web et vidéos associés, avec le statut de lecture de chaque source.

## Fichiers

- `index.html` : le site complet (HTML, CSS et JavaScript dans un seul fichier, sans dépendance à installer). La navigation entre thèmes et fiches repose sur le fragment d'URL (`#sante`, `#etudes-salaires`, etc.). La zone de recherche couvre aussi les pages HTML liées depuis les fiches (`fiches-ses/`, `fiches-informatique/`, `fiches-geopolitique/`, quiz compris) : elles sont lues à la première recherche, et chaque résultat ouvre la page à la bonne fiche. Cette partie demande que le site soit servi en HTTP (GitHub Pages) ; en ouvrant `index.html` directement depuis le disque, seules les fiches de `index.html` sont cherchées.
- `fiches-ses/` : six cours interactifs pour lycéens (fiches et quiz) sur les SES, la finance personnelle, l'entreprise et les marchés, avec une page d'accueil `accueil-ses.html`. Pages autonomes (HTML, CSS et JavaScript dans chaque fichier), ouvertes depuis le thème « Économie et finance ».
- `fiches-informatique/` : cours interactif pour lycéens (9 fiches et 25 questions de quiz) sur les satellites quantiques, `satellites-quantiques.html`. Page autonome (HTML, CSS et JavaScript dans le fichier), ouverte depuis le thème « Informatique et technologies », sur le même modèle que `fiches-ses/`.
- `fiches-geopolitique/` : fiches vidéo en frise, ouvertes depuis le thème « Géopolitique ». Pour chaque vidéo : une page parcours (`<sujet>.html`), une planche animée par étape (`<sujet>-NN-*.html`, flèches du clavier pour passer de l'une à l'autre), une fiche explicative (`<sujet>-fiche.html`), une feuille de style commune `frise.css` et les SVG dans `images/<sujet>/`. Cinq sujets : `aron-europe-*` (Aron, 1973), `aron-politique-*` (Aron, 1975), `aron-histoire-*` (cours d'Aron à la Sorbonne, 1963-1964), `aron-crise-*` (extrait de 1974) et `aron-portrait-*` (émission complète de 1974). Ces pages sont générées par `outils/aron_europe.py`, `outils/aron_politique.py`, `outils/aron_histoire.py`, `outils/aron_crise.py` et `outils/aron_portrait.py` (`python3 -I outils/<script>.py` depuis la racine).
- `images/` : illustrations des fiches (SVG réalisés pour le site).

## Utilisation

Ouvrir `index.html` dans un navigateur, ou publier le dépôt avec GitHub Pages (branche `main`, dossier racine).
