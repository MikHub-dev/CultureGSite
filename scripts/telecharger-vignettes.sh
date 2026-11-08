#!/bin/sh
# Télécharge en local les vignettes (timbre.jpg) de J.-F. Colonna utilisées par les fiches de rubriques.
# À lancer depuis la racine du dépôt (Codespace ou machine avec accès à internet) : sh scripts/telecharger-vignettes.sh
# Tant que les fichiers locaux n'existent pas, le site charge les vignettes directement depuis lactamme.polytechnique.fr.
while IFS="$(printf '\t')" read -r local remote; do
  [ -f "$local" ] && continue
  mkdir -p "$(dirname "$local")"
  curl -fsS "$remote" -o "$local" || echo "échec : $remote"
  sleep 0.3
done < scripts/vignettes-colonna.tsv
