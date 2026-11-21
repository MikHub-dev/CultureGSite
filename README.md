# CultureGSite

Site de culture générale : 9 vignettes thématiques (santé, géopolitique, économie, physique, informatique, mathématiques, études, philosophie et sagesse, langue française). Chaque vignette ouvre une page de thème qui liste et résume les documents, pages web et vidéos associés, avec le statut de lecture de chaque source.

## Fichiers

- `index.html` : le site complet (HTML, CSS et JavaScript dans un seul fichier, sans dépendance à installer). La navigation entre thèmes et fiches repose sur le fragment d'URL (`#sante`, `#etudes-salaires`, etc.).
- `fiches-ses/` : six cours interactifs pour lycéens (fiches et quiz) sur les SES, la finance personnelle, l'entreprise et les marchés, avec une page d'accueil `accueil-ses.html`. Pages autonomes (HTML, CSS et JavaScript dans chaque fichier), ouvertes depuis le thème « Économie et finance ».
- `fiches-informatique/` : cours interactif pour lycéens (9 fiches et 25 questions de quiz) sur les satellites quantiques, `satellites-quantiques.html`. Page autonome (HTML, CSS et JavaScript dans le fichier), ouverte depuis le thème « Informatique et technologies », sur le même modèle que `fiches-ses/`.
- `images/` : illustrations des fiches (SVG réalisés pour le site).

## Utilisation

Ouvrir `index.html` dans un navigateur, ou publier le dépôt avec GitHub Pages (branche `main`, dossier racine).
