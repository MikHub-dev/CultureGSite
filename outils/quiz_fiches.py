"""Génère quiz-fiches.js : les quiz (5 questions) placés en bas de fiches de index.html,
pour que chaque vignette de l'accueil ait au moins 7 quiz.
Les questions sont dans outils/quiz_*.py (liste QUIZ de (fiche, titre, questions)).
Lancer depuis la racine : python3 -I outils/quiz_fiches.py"""
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import quiz_sante, quiz_physique_info, quiz_maths_philo, quiz_etudes_langue

SUP = str.maketrans("0123456789−-e", "⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁻ᵉ")
def texte(s):
    return re.sub(r"<sup>(.*?)</sup>", lambda m: m.group(1).translate(SUP), s)

idx = open("index.html", encoding="utf-8").read()
tous, vus = [], {}
for mod in (quiz_sante, quiz_physique_info, quiz_maths_philo, quiz_etudes_langue):
    for fiche, titre, qs in mod.QUIZ:
        assert f'id="{fiche}"' in idx, fiche
        assert len(qs) == 5, (fiche, titre)
        vus[fiche] = vus.get(fiche, 0) + 1
        tous.append([fiche, titre, [{"q": texte(q), "o": [texte(x) for x in o], "a": a, "e": texte(e)} for q, o, a, e in qs]])
for q in tous:
    q.insert(0, q[0] + ("-" + q[1][5] if vus[q[0]] > 1 else ""))   # « Quiz 1 : … » → id fiche-1
donnees = json.dumps([{"id": i, "fiche": f, "titre": t, "questions": qs} for i, f, t, qs in tous], ensure_ascii=False, indent=0)

JS = """/* quiz-fiches.js — quiz de 5 questions en bas de fiches de l'accueil (généré par outils/quiz_fiches.py : ne pas modifier à la main).
   Meilleur score gardé sous la clé famzak:quiz:culturegsite:fiche:<id> ; l'accueil compte ces quiz sur chaque vignette. */
(function () {
  "use strict";
  var QUIZ = %s;
  window.CGS_QUIZ_FICHES = QUIZ;
  if (!window.FamZakQuiz) return;
  QUIZ.forEach(function (z) {
    var art = document.getElementById(z.fiche);
    if (!art) return;
    var bloc = document.createElement("div");
    bloc.className = "quiz-fiche";
    bloc.id = "quiz-" + z.id;
    var h = document.createElement("h4");
    h.textContent = "🎯 " + z.titre;
    var p = document.createElement("p");
    p.className = "meta";
    p.textContent = "5 questions sur cette fiche. Ton meilleur score est gardé et s'affiche sur la vignette du thème.";
    var zone = document.createElement("div");
    bloc.append(h, p, zone);
    var avant = art.querySelector(":scope > p.meta:last-of-type");
    if (avant && avant.nextElementSibling === null) art.insertBefore(bloc, avant); else art.appendChild(bloc);
    FamZakQuiz.monter(zone, { cle: "culturegsite:fiche:" + z.id, questions: z.questions });
  });
})();
"""
open("quiz-fiches.js", "w", encoding="utf-8").write(JS % donnees)
print(len(tous), "quiz écrits dans quiz-fiches.js")
