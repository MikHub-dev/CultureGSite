/* quiz-videos.js — quiz court (5 questions) en bas de chaque fiche vidéo de fiches-geopolitique/.
   Chargé par les pages <sujet>-fiche.html (voir SCRIPT_QUIZ dans outils/*.py), avec ../quiz-famzak.js.
   Le meilleur score est gardé sur l'appareil (clé famzak:quiz:culturegsite:video:<sujet>) ;
   l'accueil (index.html, thème Politique et Géopolitique) affiche les quiz réussis. */
(function () {
  "use strict";
  var QUIZ = {
    "aron-crise": [
      { q: "Selon Aron, en 1974, la violence a-t-elle nettement augmenté ?", o: ["Oui, elle a doublé en cinquante ans", "Rien ne le prouve, même si certaines formes sont nouvelles", "Non, elle a disparu des grandes villes"], a: 1, e: "Il relativise : la violence est endémique dans l'histoire, et le nombre des suicides n'a pas changé." },
      { q: "Comment explique-t-il une partie de la petite criminalité ?", o: ["Par la frustration de sociétés qui proclament l'égalité sans la réaliser", "Par le manque de policiers", "Par la télévision"], a: 0, e: "Ces sociétés montrent à tous des biens que beaucoup ne peuvent acquérir." },
      { q: "Que désigne la « machine folle » ?", o: ["Le choc pétrolier", "Le sentiment d'être pris dans une civilisation rationalisée que personne ne dirige", "Un ordinateur de l'État"], a: 1, e: "Cette protestation vaut, dit-il, pour les sociétés capitalistes comme socialistes." },
      { q: "Que se passe-t-il dès que la croissance est menacée ?", o: ["Tout le monde s'en réjouit", "Tout le monde se précipite à son secours", "Rien ne change"], a: 1, e: "Malgré le malaise, chacun tient à la croissance." },
      { q: "Quel est le premier des trois horizons de la crise ?", o: ["Un siècle", "Cinq à huit ans, pour absorber la hausse du pétrole", "Six mois"], a: 1, e: "Puis un demi-siècle pour des conditions de croissance changées, et plus loin l'utopie d'une civilisation technique stationnaire." }
    ],
    "aron-europe": [
      { q: "Quel livre Aron présente-t-il en 1973 ?", o: ["L'Opium des intellectuels", "République impériale", "Paix et guerre entre les nations"], a: 1, e: "Son livre sur la politique mondiale des États-Unis de 1945 à 1972." },
      { q: "Comment Aron qualifie-t-il l'Europe de l'Ouest ?", o: ["Un « État protégé » par les États-Unis", "Une superpuissance militaire", "Un satellite soviétique"], a: 0, e: "Elle a obtenu sécurité et prospérité à l'ombre de la force américaine." },
      { q: "Que pense-t-il de la violence, en répondant à Sartre ?", o: ["Qu'elle n'existe plus", "Qu'elle est « l'accoucheuse de l'histoire », mais qu'il vaut mieux en réduire le volume", "Qu'elle est toujours juste"], a: 1, e: "D'où son credo : lucidité et préférence pour les réformes progressives." },
      { q: "Selon Aron, de Gaulle souhaitait-il le départ des troupes américaines d'Europe ?", o: ["Oui, de toute l'Europe", "Non : il a voulu qu'elles quittent la France, pas l'Europe", "Il n'en a jamais parlé"], a: 1, e: "Aron dit n'avoir connu aucun homme d'État responsable qui ait souhaité leur départ d'Europe." },
      { q: "Que souhaite Aron pour l'avenir de l'Europe ?", o: ["Qu'elle rejoigne le bloc soviétique", "Qu'elle continue d'exister avec force pour encourager une libéralisation à l'Est", "Qu'elle se dissolve dans les États-Unis"], a: 1, e: "L'ambition ultime : cesser un jour d'être un ensemble d'États protégés." }
    ],
    "aron-histoire": [
      { q: "Pour Hegel, qu'est-ce que l'histoire ?", o: ["Un pur hasard", "La raison qui se réalise", "Une suite de récits sans lien"], a: 1, e: "Aron part de Hegel et de ses trois héritiers : marxisme, historicisme, existentialisme." },
      { q: "La connaissance historique est…", o: ["une reproduction exacte du passé", "une reconstruction, jamais une reproduction", "impossible"], a: 1, e: "Raconter le passé « tel qu'il s'est réellement passé » (Ranke) est un idéal qu'on n'atteint jamais." },
      { q: "Quel historien antique reste, pour Aron, le modèle de l'histoire « dramatique » ?", o: ["Hérodote", "Thucydide", "Tacite"], a: 1, e: "Thucydide consacre son premier livre à la macro-analyse et les sept autres au détail." },
      { q: "Quel exemple sert à distinguer légitimité, intentions et conséquences ?", o: ["La Révolution française", "Les origines de la guerre de 1914", "La chute de Rome"], a: 1, e: "Ce sont autant de « principes d'incertitude »." },
      { q: "Quelle question, empruntée à Max Weber, aide l'historien à rester objectif ?", o: ["Qui avait raison ?", "Que se serait-il passé si une cause avait manqué ?", "Quel est le sens final de l'histoire ?"], a: 1, e: "Ce calcul rétrospectif des probabilités évite à la fois le fatalisme et le non-sens." }
    ],
    "aron-politique": [
      { q: "Quelle vérité gêne le plus Aron ?", o: ["Que la politique est au mieux amorale, et souvent immorale", "Que l'économie est une science exacte", "Que la France a perdu son empire"], a: 0, e: "C'est pourquoi il est resté spectateur plutôt qu'acteur." },
      { q: "Comment Aron se définit-il d'abord ?", o: ["Révolutionnaire", "Anti-révolutionnaire et surtout antitotalitaire", "Monarchiste"], a: 1, e: "Une conviction née en Allemagne au moment de la montée du nazisme." },
      { q: "En Europe de l'Ouest, quel est pour lui le vrai choix ?", o: ["Droite ou gauche traditionnelles", "L'amélioration progressive de la démocratie libérale ou le parti unique", "La monarchie ou la république"], a: 1, e: "La droite qui refusait la société moderne n'existe plus, dit-il." },
      { q: "Comment distingue-t-il les deux totalitarismes ?", o: ["Ils sont identiques", "Le nazisme, inhumain à cause de ses idées ; le stalinisme, inhumain malgré les siennes", "Seul le nazisme est un totalitarisme"], a: 1, e: "La plus grande hypocrisie de son temps : avoir présenté le stalinisme comme un régime de gauche." },
      { q: "D'où vient son espoir ?", o: ["De la croissance économique", "De la dissidence soviétique (Sakharov, Soljenitsyne)", "Des élections américaines"], a: 1, e: "La conscience individuelle résiste à la violence de l'État." }
    ],
    "aron-portrait": [
      { q: "Quel événement a tourné Aron de la philosophie pure vers l'histoire et la politique ?", o: ["Le choc de l'Allemagne de 1930", "Mai 68", "La guerre d'Algérie"], a: 0, e: "La montée du nazisme lui a fait voir l'importance de l'économie, de la société et de la politique." },
      { q: "Quel économiste a nourri son choix libéral ?", o: ["Marx", "Keynes", "Proudhon"], a: 1, e: "Sa lecture de Marx l'a déçu ; il a ensuite rompu avec Sartre." },
      { q: "D'où vient, selon Aron, la grande inflation de 1974 ?", o: ["Du quadruplement du prix du pétrole, sur des sociétés devenues inflationnistes", "D'une mauvaise récolte", "De la fin de l'or"], a: 0, e: "Les gouvernements préfèrent une croissance rapide à la stabilité des prix." },
      { q: "Combien de fois dit-il avoir pris position publiquement ?", o: ["Jamais", "Une demi-douzaine de fois", "Chaque semaine"], a: 1, e: "Sur l'Algérie, en Mai 68, dans la campagne présidentielle de 1974… à condition de le dire." },
      { q: "Quel est pour lui le vrai déclin de l'Europe ?", o: ["Sa démographie", "Sa dépendance : elle ne peut ni défendre ni payer son énergie", "Sa culture"], a: 1, e: "La guerre du Kippour (octobre 1973) l'a révélé ; il refuse de se consoler « par des cocoricos »." }
    ],
    "raufer-securite": [
      { q: "Pour Xavier Raufer, la France va-t-elle devenir un « nouveau Mexique » ?", o: ["Oui, d'ici dix ans", "Non : l'État reste solide et le crime très localisé", "Elle l'est déjà"], a: 1, e: "Il juge l'alerte des magistrats mexicains peu réaliste." },
      { q: "Où situe-t-il surtout le crime ?", o: ["Dans les centres-villes", "Dans les quartiers de la politique de la ville, surtout les quartiers nord de Marseille", "Dans les campagnes"], a: 1, e: "Il y calcule un taux d'homicides environ quinze fois la moyenne nationale." },
      { q: "Quel principe de criminologie cite-t-il ?", o: ["« Les malfaiteurs ne s'arrêtent que quand on les arrête »", "« La prison ne sert à rien »", "« Le crime suit la météo »"], a: 0, e: "Selon lui, la justice ne sanctionne plus, et même les trafiquants s'en étonnent." },
      { q: "Comment veut-il compter la violence ?", o: ["Seulement les homicides", "Homicides et tentatives ensemble, à cause des progrès des secours", "Par sondage"], a: 1, e: "Les progrès médicaux sauvent des victimes qui seraient mortes autrefois." },
      { q: "Comment lire ce diagnostic ?", o: ["Comme un fait établi par tous", "Comme le point de vue d'un seul intervenant, souvent polémique", "Comme une étude officielle"], a: 1, e: "La fiche le précise : c'est une analyse personnelle, sans contradicteur." }
    ],
    "realisme": [
      { q: "À quoi les invités opposent-ils le réalisme ?", o: ["Au paradigme libéral, ou idéaliste, né après 1918", "Au marxisme", "Au féodalisme"], a: 0, e: "Avec la SDN et les « points » de Wilson." },
      { q: "Quel congrès marque, pour Sapir, la vraie naissance du réalisme ?", o: ["Le congrès de Vienne (1815)", "Le congrès de Berlin (1878)", "Le congrès de Tours (1920)"], a: 0, e: "Après Grotius, qui pensait déjà les relations entre États." },
      { q: "Lequel n'est PAS un principe du réalisme classique ?", o: ["L'anarchie du système international", "L'État souverain au centre", "Un gouvernement mondial qui garantit la paix"], a: 2, e: "Les principes : anarchie, État souverain, intérêt national, équilibre des puissances (Morgenthau, Aron)." },
      { q: "Comment Kissinger sort-il du Vietnam ?", o: ["En gagnant la guerre", "En jouant de la rivalité entre la Chine et l'URSS", "En quittant l'OTAN"], a: 1, e: "Sa ligne : gagner si l'on peut, sinon limiter les pertes pour les intérêts américains." },
      { q: "Que reconnaît une diplomatie réaliste, selon l'exemple de de Gaulle ?", o: ["Des régimes", "Des États", "Des partis"], a: 1, e: "De Gaulle reconnaît la Chine populaire en 1964 au nom de la civilisation chinoise." }
    ]
  };
  var sujet = location.pathname.split("/").pop().replace(/-fiche\.html$/, "");
  var Q = QUIZ[sujet];
  if (!Q || !window.FamZakQuiz) return;
  var main = document.querySelector("main.fiche-video");
  if (!main) return;
  var art = document.createElement("article");
  art.className = "fiche";
  art.id = "quiz";
  art.innerHTML = "<h3>Quiz : as-tu bien suivi ?</h3><p class=\"meta\">5 questions sur la vidéo. Ton meilleur score est gardé sur cet appareil et s'affiche sur l'accueil.</p><div class=\"quiz-zone\"></div>";
  var retours = main.querySelectorAll(":scope > a.back");
  var fin = retours.length ? retours[retours.length - 1] : null;
  if (fin) main.insertBefore(art, fin); else main.appendChild(art);
  FamZakQuiz.monter(art.querySelector(".quiz-zone"), { cle: "culturegsite:video:" + sujet, questions: Q });
  window.QUIZ_VIDEOS = QUIZ;
})();
