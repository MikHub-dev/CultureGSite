# Quiz du thème Santé (5 questions chacun) : (question, choix, index de la bonne réponse, explication)
QUIZ = [
("sante-aliments", "Quiz 1 : les aliments écartés", [
 ("Pourquoi le cardiologue écarte-t-il les céréales sucrées du petit-déjeuner ?", ["Elles provoquent un pic de sucre et d'insuline", "Elles contiennent trop de protéines", "Elles sont trop riches en fibres"], 0, "Il leur reproche le pic de sucre et d'insuline, qui fatigue le métabolisme ; il propose des flocons d'avoine."),
 ("Que reproche-t-il à la charcuterie transformée ?", ["Le manque de vitamines", "Les nitrates et nitrites, mauvais pour la tension et les artères", "Le prix"], 1, "Il conseille plutôt de la dinde ou du poulet rôtis maison."),
 ("Que propose-t-il à la place de la margarine ?", ["Du beurre ou de l'huile d'olive extra-vierge", "De l'huile de friture", "Rien du tout"], 0, "La margarine contient souvent des acides gras trans, qui font monter le mauvais cholestérol."),
 ("Une tasse de soupe en conserve peut apporter…", ["5 % du sel autorisé par jour", "Jusqu'à 100 % de la limite quotidienne de sodium", "Aucun sel"], 1, "D'où son conseil : une soupe maison de légumes et d'herbes."),
 ("Que pense-t-il des viandes végétales ultra-transformées ?", ["Elles sont toujours meilleures que la viande", "Elles contiennent sodium, huiles inflammatoires et additifs", "Elles n'ont aucun défaut"], 1, "Il préfère les lentilles, les haricots ou le tofu peu transformé."),
]),
("sante-aliments", "Quiz 2 : lire les étiquettes", [
 ("Une mention « bon pour le cœur » sur un paquet…", ["garantit un produit sain", "ne garantit rien : il faut lire les ingrédients", "est interdite en France"], 1, "« Light », « végétal » ou « bon pour le cœur » ne suffisent pas."),
 ("Lequel de ces « adversaires » revient souvent dans la liste ?", ["Les sucres ajoutés", "L'eau", "Les légumes frais"], 0, "Avec le sodium, les graisses trans, les huiles industrielles et les additifs."),
 ("Pourquoi les sodas « light » posent-ils aussi problème selon lui ?", ["Ils perturbent le microbiome", "Ils sont trop caloriques", "Ils manquent de sucre"], 0, "Il propose de l'eau pétillante au citron ou une tisane glacée."),
 ("Qu'est-ce qui abîme les fast-foods frits, selon lui ?", ["Le sel seulement", "Des huiles industrielles oxydées à haute température", "La congélation"], 1, "Il conseille des versions cuites au four, avec de l'huile d'olive ou d'avocat."),
 ("Que recommande-t-il avant un grand changement d'alimentation ?", ["De jeûner une semaine", "De consulter un professionnel de santé", "D'arrêter tout sport"], 1, "Il préfère aussi les produits bruts ou faits maison, et croit aux petits échanges qui s'additionnent."),
]),
("sante-ramakrishnan", "Quiz 1 : pourquoi on vieillit", [
 ("Pour Venki Ramakrishnan, vieillir, c'est surtout…", ["accumuler des dégâts à tous les niveaux", "perdre un seul gène", "manquer de vitamines"], 0, "ADN abîmé, protéines mal assemblées, mitochondries usées…"),
 ("Que font les cellules « sénescentes » ?", ["Elles se divisent très vite", "Elles ne se divisent plus mais émettent des signaux inflammatoires", "Elles disparaissent seules"], 1, "Avec l'âge, le système immunitaire les élimine trop lentement."),
 ("Pourquoi se méfie-t-il des start-up de la longévité ?", ["Elles n'existent pas", "Leurs scientifiques ont un intérêt financier à promettre beaucoup", "Elles sont gérées par l'État"], 1, "Certaines valent des dizaines de milliards de dollars."),
 ("Quel cercle vicieux décrit-il ?", ["L'inflammation aggrave les dégâts, qui aggravent l'inflammation", "Le sport fatigue le cœur", "Le sommeil abîme l'ADN"], 0, "C'est l'inflammation chronique liée à l'âge."),
 ("Quel âge record cite-t-il ?", ["100 ans", "122 ans, atteint par Jeanne Calment", "150 ans"], 1, "Il place le plafond actuel entre 110 et 120 ans, sans loi physique qui interdise d'aller plus loin."),
]),
("sante-ramakrishnan", "Quiz 2 : les pistes et les bons gestes", [
 ("Quel est le défaut de la rapamycine ?", ["Elle est trop chère", "Elle ralentit la cicatrisation et affaiblit l'immunité", "Elle n'a aucun effet"], 1, "Et son bon dosage reste inconnu."),
 ("Que font les sénolytiques ?", ["Ils éliminent les cellules sénescentes", "Ils remplacent le sang", "Ils font maigrir"], 0, "Chez la souris, jusqu'à 20 à 30 % de vie en plus."),
 ("Pourquoi la reprogrammation cellulaire est-elle risquée ?", ["Une cellule trop « rajeunie » peut devenir cancéreuse", "Elle est interdite partout", "Elle rend aveugle"], 0, "C'est pourtant, selon lui, la piste la plus prometteuse à long terme."),
 ("Quels sont ses trois piliers solides ?", ["Alimentation modérée, activité physique, bon sommeil", "Compléments, café, sieste", "Jeûne, sauna, plasma"], 0, "Il y ajoute les liens sociaux, un sens à sa vie et des bilans dès 40 ans."),
 ("Au Royaume-Uni, de combien les 10 % les plus riches vivent-ils plus longtemps que les 10 % les plus pauvres ?", ["Un an", "Dix ans", "Trente ans"], 1, "Il rappelle que ce mode de vie est un privilège."),
]),
("sante-gastro", "Quiz 1 : la bouche et l'assiette", [
 ("Où commence la digestion ?", ["Dans l'estomac", "Dans la bouche", "Dans l'intestin"], 1, "C'est le point de départ de « Pauline hépato »."),
 ("Combien de temps met le signal de satiété pour atteindre le cerveau ?", ["Une vingtaine de minutes", "Deux secondes", "Deux heures"], 0, "D'où l'intérêt de bien mâcher et de manger lentement."),
 ("Combien de salive produit-on par jour ?", ["Un verre à peine", "0,5 à 1,5 litre", "5 litres"], 1, "La salive commence à décomposer l'amidon."),
 ("Pourquoi augmenter les fibres progressivement ?", ["Les fibres insolubles peuvent irriter", "Les fibres font grossir", "Elles sont rares"], 0, "Les solubles régulent le transit, les insolubles peuvent irriter."),
 ("Que reproche-t-elle aux aliments industriels ?", ["Trop gras, sucrés, salés et pauvres en fibres", "Trop chers", "Trop riches en fibres"], 0, "Elle conseille de cuisiner maison."),
]),
("sante-gastro", "Quiz 2 : boire, dormir, bouger", [
 ("Combien d'eau suffit par jour ?", ["0,5 litre", "1,5 à 2 litres", "4 litres"], 1, "Les boissons gazeuses peuvent donner des ballonnements."),
 ("Pourquoi éviter les boissons brûlantes ?", ["Elles irritent les muqueuses", "Elles font grossir", "Elles coupent la faim"], 0, ""),
 ("Contre les remontées acides, de quel côté dormir ?", ["Sur le côté droit", "Sur le côté gauche", "Sur le ventre"], 1, "Et ne pas s'allonger juste après le repas."),
 ("Pourquoi ne pas prendre longtemps des inhibiteurs de la pompe à protons ?", ["Ils fragilisent le microbiote", "Ils rendent somnolent", "Ils coûtent trop cher"], 0, ""),
 ("Quel est l'effet de l'activité physique sur la digestion ?", ["Elle ralentit le transit", "Elle stimule le transit et réduit l'inflammation", "Aucun"], 1, "Le stress nuit à la digestion : méditation, yoga et bon sommeil aident."),
]),
("sante-farine", "Quiz : les types de farine", [
 ("Que signifie le « T » de T55 ?", ["Température", "Type", "Tamis"], 1, "Le chiffre indique la teneur en minéraux."),
 ("Comment mesure-t-on ce chiffre ?", ["Par les résidus laissés après combustion de 100 g de farine", "Par la couleur", "Par le prix"], 0, ""),
 ("Plus le chiffre est élevé, plus la farine est…", ["blanche et légère", "riche en son et en fibres", "sucrée"], 1, "Plus nutritive, mais plus foncée et moins légère."),
 ("Quelle farine pour une brioche ?", ["T45", "T110", "T150"], 0, "La T45, très blanche, sert à la pâtisserie."),
 ("Quelle farine la plupart des artisans utilisent-ils pour la baguette tradition ?", ["T45", "T65", "T150"], 1, "Parfois un mélange de T55 et T65."),
]),
]
