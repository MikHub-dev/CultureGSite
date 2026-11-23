# -*- coding: utf-8 -*-
"""Génère la fiche vidéo « Raymond Aron et l'Europe protégée » (Géopolitique) :
parcours SVG, une planche SVG animée par étape, pages HTML (parcours, planches, fiche).
Lancer depuis la racine du dépôt : python3 -I outils/aron_europe.py
"""
import os, random, html, math

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOSSIER = os.path.join(RACINE, 'fiches-geopolitique')
SUJET = 'aron-europe'
IMG = os.path.join(DOSSIER, 'images', SUJET)
VID = 'ztwn4T2IbNc'

OR, CYAN, ROUGE, VERT, BLEU, GRIS = '#f2b84b', '#5ad1e6', '#ff6b7a', '#7ee0a0', '#7aa2ff', '#9fb3d6'
TEXTE = '#e6eefc'
SERIF = "Spectral, Georgia, 'Times New Roman', serif"
SANS = "Jost, 'Segoe UI', system-ui, sans-serif"

# ---------------------------------------------------------------- contenu
ETAPES = [
    dict(slug='regard-des-autres', court='Le regard des autres',
         parcours=['Le regard', 'des autres'],
         titre="Trois éloges funèbres imaginés",
         sous="Aron se juge par la voix d'un adversaire, d'un critique modéré et d'un ami",
         legG="Pierre Dumayet lui demande son testament politique. Aron commence par imaginer trois éloges funèbres : un journal extrémiste, un journal de gauche modérée, un ami.",
         legD="Pour l'ami, il partage le sort des libéraux français : ne rejoindre ni la révolution sans idée, ni la conservation sans cœur, et rester seul.",
         texte="Pour présenter <i>République impériale</i>, Pierre Dumayet propose à Raymond Aron d'improviser son testament politique. Aron commence par trois éloges funèbres qu'il imagine. Un journal extrémiste le décrirait comme un ennemi viscéral du communisme, avocat du grand capital et idéologue de l'impérialisme. Un journal de gauche modérée saluerait sa lucidité mais lui reprocherait de manquer de sensibilité pour la douleur humaine. Un ami dirait qu'il a partagé le sort des libéraux français depuis le XVIII<sup>e</sup> siècle : vouloir une politique raisonnable, refuser à la fois « la révolution sans idée » et « la conservation sans cœur », et se sentir seul au milieu de l'intelligentsia, comme Montesquieu ou Tocqueville avant lui.",
         anim="Les trois bulles A, B et C apparaissent l'une après l'autre autour d'Aron, puis s'effacent ensemble avant de recommencer.",
         t=17),
    dict(slug='credo-reformiste', court='Le credo du réformiste',
         parcours=['Le credo', 'du réformiste'],
         titre="Réduire le volume de la violence",
         sous="Le testament : voir le monde tel qu'il est et avancer pas à pas",
         legG="Sartre parle des « âmes tendres des libéraux ». Aron répond qu'il sait le monde violent et brutal, et que la violence accompagne l'histoire.",
         legD="Son credo : lucidité, mesures progressives plutôt que changements globaux, scepticisme envers la révolution, optimisme sans croire au paradis sur terre.",
         texte="Aron répond à Sartre, son ancien ami, qui moque « ces âmes tendres des libéraux ». Il n'a pas l'âme tendre, dit-il : il sait que le monde est violent et brutal et que la violence est « l'accoucheuse de l'histoire ». Ce qu'il croit, c'est qu'il vaut mieux réduire le volume de cette violence. D'où son testament en quelques mots : lucidité pour voir le monde tel qu'il est, préférence pour les mesures progressives plutôt que pour les changements globaux, scepticisme envers la révolution, acceptation des duretés de la civilisation. Il se dit enfin optimiste, contrairement à sa réputation : il croit à l'avenir de l'humanité, mais pas au paradis sur terre.",
         anim="La ligne de la violence ondule de moins en moins fort de gauche à droite. À droite, un point gravit l'escalier des mesures progressives, tandis que le grand saut de la révolution reste marqué d'un point d'interrogation.",
         t=150),
    dict(slug='europe-etat-protege', court="L'Europe, État protégé",
         parcours=["L'Europe,", 'État protégé'],
         titre="L'Europe de l'Ouest, État protégé",
         sous="Sécurité à l'ombre des États-Unis et prospérité : la moitié des ambitions",
         legG="Après la guerre, les Européens de l'Ouest se résignent à la domination soviétique sur l'Est et cherchent sécurité et prospérité à l'ombre de la force américaine.",
         legD="Vingt-cinq ans plus tard : essor économique sans précédent, pas de guerre, France et Allemagne réconciliées. La moitié des ambitions est atteinte.",
         texte="Interrogé sur l'Europe, Aron reprend l'expression d'« État protégé ». Quelques années après 1945, explique-t-il, les Européens de l'Ouest se sont résignés à la domination de l'Union soviétique sur l'Europe de l'Est. Ils ont voulu deux choses : la sécurité à l'ombre de la force américaine et la prospérité. Vingt-cinq ans plus tard, ils les ont obtenues : le relèvement économique dépasse les espoirs des plus optimistes, il n'y a pas eu de guerre et la réconciliation entre la France et l'Allemagne de l'Ouest est un fait accompli. La politique américaine a donc atteint son but en Europe. Mais ceux qui défendaient la politique atlantique et européenne n'ont réalisé que la moitié de leurs ambitions : l'autre moitié aurait été une Europe assez unie et assez volontaire pour se défendre seule.",
         anim="Le parapluie américain (U) couvre l'Europe de l'Ouest, dont les barres de prospérité montent. À droite, la jauge des ambitions se remplit jusqu'à la moitié, l'autre moitié reste en pointillés.",
         t=222),
    dict(slug='de-gaulle-presence-americaine', court='De Gaulle et les troupes américaines',
         parcours=['De Gaulle et', 'les troupes', 'américaines'],
         titre="Indépendance, mais pas sans l'Amérique",
         sous="Les troupes américaines quittent la France, pas l'Europe",
         legG="Les gouvernements français tiennent à leur indépendance. De Gaulle obtient, sans difficulté selon Aron, que les troupes américaines quittent la France.",
         legD="Mais aucun dirigeant ne voulait leur départ d'Europe : face au bloc soviétique, cette présence laisse justement à la France sa liberté d'action.",
         texte="Dumayet objecte que les gouvernements français ont cherché une certaine indépendance vis-à-vis des États-Unis. Aron l'admet, mais il affirme n'avoir connu aucun homme d'État responsable, pas même le général de Gaulle, qui ait souhaité le départ des troupes américaines d'Europe. De Gaulle a voulu qu'elles quittent la France et l'a obtenu sans difficulté. Il savait pourtant, selon Aron, que la présence américaine en Europe donnait à la France une liberté d'action qu'elle perdrait si l'Europe de l'Ouest se retrouvait sans défense face au bloc soviétique, puissance militaire considérable. Conclusion d'Aron : tous les gouvernements français ont voulu que l'Europe reste protégée par les États-Unis tant que l'URSS ne changerait pas ou que l'Europe ne saurait pas se défendre seule.",
         anim="Les points bleus (troupes américaines, U) sortent de la France et s'installent dans le reste de l'Europe de l'Ouest, entre la France et le bloc soviétique. La France garde sa liberté d'action derrière ce bouclier.",
         t=326),
    dict(slug='bilan-vingt-cinq-ans', court='Le bilan de 25 ans',
         parcours=['Le bilan', 'de 25 ans'],
         titre="Vingt-cinq ans : ce qui a vraiment compté",
         sous="Une Europe redevenue puissance économique, des craintes qui ne se sont pas réalisées",
         legG="Le fait majeur : l'Europe est redevenue une grande puissance économique. La preuve, selon Aron : ses différends monétaires et commerciaux avec les États-Unis, demain peut-être le Japon.",
         legD="Le réarmement de l'Allemagne de l'Ouest a soulevé des passions. Aucune des conséquences annoncées ne s'est réalisée : elles étaient disproportionnées.",
         texte="Qu'est-ce qui a compté en Europe depuis vingt-cinq ans ? À l'échelle mondiale, répond Aron, l'Europe est redevenue une grande puissance économique. Il en voit la meilleure preuve dans les difficultés monétaires et commerciales entre l'Europe de l'Ouest, les États-Unis et peut-être demain le Japon. Dumayet évoque les grandes querelles européennes, comme le réarmement de l'Allemagne. Aron juge, avec le recul, que les passions de chaque camp étaient disproportionnées. On peut encore discuter de la nécessité de ce réarmement, dit-il, mais aucune des conséquences redoutées ne s'est produite : l'Allemagne de l'Ouest n'est pas devenue militariste, n'a pas provoqué l'URSS, n'a pas empêché la réconciliation européenne et n'a pas tendu durablement les relations entre l'Est et l'Ouest.",
         anim="À gauche, des échanges circulent entre l'Europe (E), les États-Unis (U) et le Japon (J, en pointillés : « demain »). À droite, les quatre craintes liées au réarmement allemand sont barrées l'une après l'autre.",
         t=387),
    dict(slug='exister-pour-changer-l-est', court="Exister pour changer l'Est",
         parcours=['Exister pour', "changer l'Est"],
         titre="Exister, pour qu'à l'Est le régime évolue",
         sous="Le souhaitable selon Aron : sortir un jour du statut d'État protégé",
         legG="Ambition ultime : ne pas rester indéfiniment des États protégés. D'abord, exister assez fort pour inciter le régime soviétique à se transformer de l'intérieur.",
         legD="Le levier : le dialogue avec les intellectuels soviétiques. Pas à court terme ; et si l'Ouest entrait dans le système soviétique, la tyrannie serait pire.",
         texte="Pour l'avenir, Aron souhaite que l'Europe de l'Ouest ne se contente pas indéfiniment d'être un ensemble d'États protégés : c'est l'ambition ultime. Mais il faut d'abord qu'elle continue d'exister assez fortement pour inciter le régime soviétique à se transformer de l'intérieur. Son objectif n'a jamais été que les deux parties de l'Europe se regardent « en chiens de faïence » : l'idéal reste qu'une libéralisation à l'Est permette une existence commune. L'Europe ne peut pas y contribuer directement, reconnaît-il, mais les intellectuels soviétiques discutent davantage avec les Européens qu'entre eux, même quand leurs livres ne sont pas publiés là-bas. Pour que ce dialogue continue, il faut que l'Ouest continue d'exister. Il ne croit pas à un changement à court terme, et il avertit : si l'Ouest entrait dans le système soviétique, l'URSS deviendrait pire encore, car elle devrait tenir des pays récalcitrants, et l'Europe connaîtrait une longue tyrannie.",
         anim="Des points d'idées et de livres traversent sans cesse la frontière entre l'Ouest et l'Est, qui pâlit puis se raffermit. En bas, les trois étapes du souhaitable s'allument une à une ; le contre-scénario reste en rouge pointillé.",
         t=474),
]

CHAPITRES = [
    (0, "Introduction", "L'émission <i>Le temps de lire</i> (ORTF, 12 mars 1973) présente le livre de Raymond Aron, <i>République impériale : les États-Unis dans le monde, 1945-1972</i> (Calmann-Lévy). Un extrait annonce le thème : le monde est violent."),
    (17, "Les éloges funèbres imaginés", "Invité à improviser son testament politique, Aron imagine d'abord ce que diraient de lui un journal extrémiste, un journal de gauche modérée et un ami. L'ami le rangerait parmi les libéraux français isolés, comme Montesquieu et Tocqueville."),
    (150, "Le testament : lucidité et réformisme", "Face à Sartre qui moque les « âmes tendres » des libéraux, il dit voir un monde violent et vouloir en réduire la violence : lucidité, mesures progressives, scepticisme envers la révolution, optimisme sans paradis sur terre."),
    (222, "L'Europe, ensemble d'États protégés", "Les Européens de l'Ouest ont obtenu ce qu'ils voulaient après la guerre : sécurité sous protection américaine, prospérité, paix, réconciliation franco-allemande. C'est la moitié de leurs ambitions ; manque une Europe capable de se défendre seule."),
    (326, "La France, de Gaulle et la présence américaine", "Les gouvernements français veulent l'indépendance, mais aucun, pas même de Gaulle, n'a voulu que les troupes américaines quittent l'Europe : leur présence garantit à la France sa liberté d'action face au bloc soviétique."),
    (387, "Bilan : puissance économique et réarmement allemand", "L'Europe est redevenue une grande puissance économique, comme le montrent ses différends avec les États-Unis et le Japon. Le réarmement de l'Allemagne de l'Ouest n'a eu aucune des conséquences redoutées."),
    (474, "Le souhaitable : exister face à l'Est", "L'Europe devrait un jour cesser d'être protégée. D'abord, elle doit exister assez fort pour encourager une libéralisation du régime soviétique, par le dialogue avec ses intellectuels. Sinon, une tyrannie plus lourde menacerait."),
]

N = len(ETAPES)
for i, e in enumerate(ETAPES, 1):
    e['n'] = i
    e['page'] = '%s-%02d-%s.html' % (SUJET, i, e['slug'])
    e['svg'] = '%02d-%s.svg' % (i, e['slug'])


def hms(s):
    return '%d:%02d' % (s // 60, s % 60)


# ---------------------------------------------------------------- outils SVG
def esc(s):
    return html.escape(s, quote=True)


def txt(x, y, s, size=18, fill=TEXTE, anchor='middle', weight='400', family=SANS, extra=''):
    return ('<text x="%s" y="%s" font-size="%s" fill="%s" text-anchor="%s" font-weight="%s" font-family="%s"%s>%s</text>'
            % (x, y, size, fill, anchor, weight, esc(family), extra, esc(s)))


def lignes(x, y, ls, size=18, fill=TEXTE, anchor='middle', h=None, **kw):
    h = h or size * 1.3
    return ''.join(txt(x, y + k * h, l, size, fill, anchor, **kw) for k, l in enumerate(ls))


def couper(s, n):
    mots, out, cur = s.split(), [], ''
    for m in mots:
        if cur and len(cur) + 1 + len(m) > n:
            out.append(cur); cur = m
        else:
            cur = (cur + ' ' + m).strip()
    if cur:
        out.append(cur)
    return out


def disque(cx, cy, r, couleur, lettre='', fs=None, extra=''):
    s = '<circle cx="%s" cy="%s" r="%s" fill="%s" fill-opacity=".16" stroke="%s" stroke-width="2.5"%s/>' % (cx, cy, r, couleur, couleur, extra)
    if lettre:
        s += txt(cx, cy + (fs or r) * 0.36, lettre, fs or r, couleur, weight='600', family=SERIF)
    return s


def apparait(debut, fin=0.92, dur=9):
    return ('<animate attributeName="opacity" values="0;0;1;1;0" keyTimes="0;%.3f;%.3f;%.3f;1" dur="%ss" repeatCount="indefinite"/>'
            % (debut, debut + 0.06, fin, dur))


def etoiles(seed):
    rnd = random.Random(seed)
    out = []
    for _ in range(70):
        x, y = rnd.uniform(0, 1280), rnd.uniform(0, 560)
        r, o = rnd.choice([0.6, 0.9, 1.2, 1.6]), rnd.choice([0.25, 0.4, 0.6])
        out.append('<circle cx="%.1f" cy="%.1f" r="%s" fill="#e6eefc" fill-opacity="%s"/>' % (x, y, r, o))
    return ''.join(out)


DEFS = ('<defs><linearGradient id="fond" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0e1228"/><stop offset="1" stop-color="#1b1e42"/></linearGradient>'
        '<filter id="glow" filterUnits="userSpaceOnUse" x="0" y="0" width="1280" height="720"><feGaussianBlur stdDeviation="4" result="b"/>'
        '<feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>'
        '<marker id="fl" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="context-stroke"/></marker>'
        '</defs>')


def ouvrir(titre_acc):
    return ('<?xml version="1.0" encoding="UTF-8"?>\n<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 720" role="img" aria-label="%s">'
            % esc(titre_acc) + DEFS + '<rect width="1280" height="720" fill="url(#fond)"/>')


def base(n, titre, sous, corps, legG, legD):
    s = ouvrir('Étape %d sur %d : %s' % (n, N, titre)) + etoiles(n)
    # pastille
    s += '<rect x="40" y="34" width="150" height="36" rx="18" fill="%s" fill-opacity=".14" stroke="%s"/>' % (OR, OR)
    s += txt(115, 58, 'ÉTAPE %02d / %02d' % (n, N), 16, OR, weight='600')
    # points de progression (dernier point à 1250 - 30 de marge)
    for k in range(1, N + 1):
        cx = 1250 - (N - k) * 26 - 30
        actif = k == n
        s += '<circle cx="%d" cy="52" r="%d" fill="%s" fill-opacity="%s" stroke="%s"/>' % (cx, 8 if actif else 6, OR if actif else CYAN, '1' if actif else '.15', OR if actif else CYAN)
    s += txt(640, 118, titre, 40, TEXTE, weight='600', family=SERIF)
    s += txt(640, 152, sous, 19, CYAN)
    s += corps
    # panneau du bas
    s += '<rect x="40" y="578" width="1200" height="118" rx="16" fill="#0a0f26" fill-opacity=".78" stroke="%s" stroke-opacity=".35"/>' % CYAN
    s += '<line x1="640" y1="596" x2="640" y2="678" stroke="%s" stroke-opacity=".3"/>' % CYAN
    s += lignes(66, 612, couper(legG, 64), 17, TEXTE, 'start', h=24)
    s += lignes(664, 612, couper(legD, 64), 17, TEXTE, 'start', h=24)
    return s + '</svg>\n'


def boite(x, y, w, h, couleur, opa='.12'):
    return '<rect x="%s" y="%s" width="%s" height="%s" rx="14" fill="%s" fill-opacity="%s" stroke="%s" stroke-width="2"/>' % (x, y, w, h, couleur, opa, couleur)


# ---------------------------------------------------------------- planches
def planche1():
    c = ''
    # Aron au centre
    c += '<g>' + disque(640, 455, 62, OR) + txt(640, 448, 'Raymond', 20, OR, weight='600') + txt(640, 472, 'Aron', 20, OR, weight='600')
    c += '<circle cx="640" cy="455" r="62" fill="none" stroke="%s" stroke-width="2" filter="url(#glow)"><animate attributeName="r" values="62;74;62" dur="3s" repeatCount="indefinite"/><animate attributeName="stroke-opacity" values=".8;0;.8" dur="3s" repeatCount="indefinite"/></circle></g>' % OR
    bulles = [
        (70, ROUGE, 'A', 'Journal extrémiste', ['Haine du communisme,', 'défense du grand capital,', '« idéologue de l\'impérialisme »'], 0.04),
        (465, BLEU, 'B', 'Gauche modérée', ['Lucide, mais peu sensible', 'à la douleur humaine,', 'des causes discutables'], 0.30),
        (860, VERT, 'C', 'Un ami', ['Un libéral isolé, comme', 'Montesquieu et Tocqueville :', 'ni révolution, ni réaction'], 0.56),
    ]
    for x, col, L, nom, ls, deb in bulles:
        g = '<g opacity="0">' + apparait(deb)
        g += boite(x, 185, 350, 175, col)
        g += disque(x + 36, 222, 20, col, L, 22)
        g += txt(x + 68, 230, nom, 22, col, 'start', '600')
        g += lignes(x + 22, 272, ls, 18, TEXTE, 'start', h=26)
        g += '<path d="M%d 360 L640 393" stroke="%s" stroke-width="2" stroke-dasharray="6 6" fill="none"/>' % (x + 175, col)
        g += '</g>'
        c += g
    c += txt(640, 552, "« Mon testament politique, ou l'éloge funèbre rédigé par mes amis ou mes ennemis ? »", 18, GRIS, extra=' font-style="italic"')
    e = ETAPES[0]
    return base(1, e['titre'], e['sous'], c, e['legG'], e['legD'])


def planche2():
    c = ''
    # gauche : violence de l'histoire, amplitude décroissante
    c += boite(60, 180, 560, 330, ROUGE, '.06')
    c += txt(340, 214, "La violence dans l'histoire", 21, ROUGE, weight='600')
    pts = []
    for k in range(0, 201):
        x = 90 + k * 2.5
        amp = 80 * (1 - k / 230.0)
        y = 360 + amp * math.sin(k / 6.0)
        pts.append('%.1f %.1f' % (x, y))
    d = 'M' + ' L'.join(pts)
    c += '<path d="%s" fill="none" stroke="%s" stroke-width="3" stroke-dasharray="14 8" filter="url(#glow)"><animate attributeName="stroke-dashoffset" values="0;-44" dur="1.6s" repeatCount="indefinite"/></path>' % (d, ROUGE)
    c += '<line x1="90" y1="460" x2="590" y2="460" stroke="%s" stroke-opacity=".5" marker-end="url(#fl)"/>' % GRIS
    c += txt(340, 488, "Le temps : réduire le volume de la violence", 17, GRIS)
    # droite : deux chemins
    c += boite(660, 180, 560, 330, VERT, '.06')
    c += txt(940, 214, 'Deux façons de changer', 21, VERT, weight='600')
    c += '<path d="M700 450 Q860 210 1180 290" fill="none" stroke="%s" stroke-width="3" stroke-dasharray="8 8" marker-end="url(#fl)"/>' % ROUGE
    c += disque(905, 270, 22, ROUGE, '?', 28)
    c += txt(770, 250, 'Changement global', 17, ROUGE, weight='600')
    c += txt(770, 272, '(révolution) : scepticisme', 16, ROUGE)
    marches = 'M700 470 h80 v-30 h80 v-30 h80 v-30 h80 v-30 h80 v-30 h60'
    c += '<path d="%s" fill="none" stroke="%s" stroke-width="3"/>' % (marches, VERT)
    c += '<circle r="10" fill="%s" filter="url(#glow)"><animateMotion dur="6s" repeatCount="indefinite" path="%s"/></circle>' % (OR, 'M700 460 h80 v-30 h80 v-30 h80 v-30 h80 v-30 h80 v-30 h60')
    c += txt(1110, 435, 'Mesures', 17, VERT, weight='600') + txt(1110, 457, 'progressives', 17, VERT, weight='600')
    # pastilles du credo
    chips = [('Lucidité', CYAN), ('Pas à pas', VERT), ('Scepticisme', ROUGE), ('Optimisme, sans paradis', OR)]
    x = 150
    for k, (lab, col) in enumerate(chips):
        w = 30 + len(lab) * 10
        g = '<g opacity="0">' + apparait(0.08 + k * 0.18) + '<rect x="%d" y="525" width="%d" height="36" rx="18" fill="%s" fill-opacity=".14" stroke="%s"/>' % (x, w, col, col)
        g += txt(x + w / 2, 549, lab, 17, col, weight='600') + '</g>'
        c += g
        x += w + 40
    e = ETAPES[1]
    return base(2, e['titre'], e['sous'], c, e['legG'], e['legD'])


def planche3():
    c = ''
    # Europe de l'Ouest
    c += boite(90, 300, 420, 230, BLEU, '.08')
    c += txt(300, 332, "Europe de l'Ouest", 22, TEXTE, weight='600')
    # parapluie américain
    c += '<g><animateTransform attributeName="transform" type="translate" values="0 0;0 -6;0 0" dur="4s" repeatCount="indefinite"/>'
    c += '<path d="M90 272 Q300 150 510 272 Q475 252 440 272 Q405 252 370 272 Q335 252 300 272 Q265 252 230 272 Q195 252 160 272 Q125 252 90 272Z" fill="%s" fill-opacity=".22" stroke="%s" stroke-width="2.5"/>' % (BLEU, BLEU)
    c += '<line x1="300" y1="200" x2="300" y2="300" stroke="%s" stroke-width="2.5"/>' % BLEU
    c += disque(300, 222, 18, BLEU, 'U', 20)
    c += '</g>'
    c += txt(560, 214, 'Protection', 17, BLEU, 'start', '600') + txt(560, 236, 'américaine', 17, BLEU, 'start', '600')
    # barres de prospérité
    for k, hmax in enumerate([60, 95, 130, 160]):
        x = 130 + k * 48
        c += ('<rect x="%d" y="%d" width="32" height="%d" fill="%s" fill-opacity=".55" stroke="%s">'
              '<animate attributeName="height" values="4;%d;%d;4" keyTimes="0;.45;.9;1" dur="8s" repeatCount="indefinite"/>'
              '<animate attributeName="y" values="%d;%d;%d;%d" keyTimes="0;.45;.9;1" dur="8s" repeatCount="indefinite"/></rect>'
              % (x, 515 - hmax, hmax, OR, OR, hmax, hmax, 511, 515 - hmax, 515 - hmax, 511))
    c += txt(205, 370, 'Prospérité', 17, OR, weight='600')
    c += txt(410, 400, 'Paix', 18, VERT, weight='600')
    c += txt(410, 440, 'France + RFA', 17, VERT) + txt(410, 462, 'réconciliées', 17, VERT)
    # rideau
    c += '<line x1="545" y1="290" x2="545" y2="540" stroke="%s" stroke-width="3" stroke-dasharray="10 8"/>' % GRIS
    c += boite(580, 300, 210, 230, ROUGE, '.10')
    c += txt(685, 335, "Europe de l'Est", 19, ROUGE, weight='600')
    c += lignes(685, 400, ['Domination', 'soviétique', 'acceptée'], 18, TEXTE, h=26)
    c += disque(685, 490, 18, ROUGE, 'S', 20)
    # jauge des ambitions
    c += txt(1020, 214, 'Les ambitions', 22, OR, weight='600')
    c += '<rect x="960" y="240" width="120" height="290" rx="12" fill="none" stroke="%s" stroke-width="2.5" stroke-dasharray="8 6"/>' % OR
    c += ('<rect x="964" y="526" width="112" height="0" rx="8" fill="%s" fill-opacity=".45">'
          '<animate attributeName="height" values="0;141;141;0" keyTimes="0;.45;.9;1" dur="8s" repeatCount="indefinite"/>'
          '<animate attributeName="y" values="526;385;385;526" keyTimes="0;.45;.9;1" dur="8s" repeatCount="indefinite"/></rect>') % OR
    c += '<line x1="950" y1="385" x2="1090" y2="385" stroke="%s" stroke-width="2"/>' % OR
    c += txt(1100, 470, '1/2 atteinte', 17, OR, 'start', '600') + txt(1100, 492, 'sécurité,', 16, TEXTE, 'start') + txt(1100, 512, 'prospérité', 16, TEXTE, 'start')
    c += txt(1100, 300, 'Manque :', 17, GRIS, 'start', '600') + lignes(1100, 322, ['Europe unie,', 'capable de se', 'défendre seule'], 16, GRIS, 'start', h=21)
    e = ETAPES[2]
    return base(3, e['titre'], e['sous'], c, e['legG'], e['legD'])


def planche4():
    c = ''
    c += boite(90, 210, 300, 320, CYAN, '.08') + txt(240, 245, 'France', 24, CYAN, weight='600')
    c += boite(430, 210, 360, 320, BLEU, '.08') + txt(610, 245, "Reste de l'Europe", 21, BLEU, weight='600') + txt(610, 268, "de l'Ouest", 21, BLEU, weight='600')
    c += boite(880, 210, 320, 320, ROUGE, '.12') + txt(1040, 245, 'Bloc soviétique', 22, ROUGE, weight='600')
    c += lignes(1040, 330, ['Puissance', 'militaire', 'considérable'], 20, TEXTE, h=28)
    c += disque(1040, 465, 26, ROUGE, 'S', 28)
    # bouclier
    c += '<path d="M835 230 L835 520" stroke="%s" stroke-width="6" filter="url(#glow)"><animate attributeName="stroke-opacity" values=".5;1;.5" dur="3s" repeatCount="indefinite"/></path>' % BLEU
    c += txt(835, 552, 'Bouclier américain', 16, BLEU, weight='600')
    # troupes qui quittent la France pour le reste de l'Europe
    rnd = random.Random(4)
    for k in range(8):
        x0, y0 = 150 + (k % 4) * 55, 330 + (k // 4) * 70
        dx = 330 + (k // 4) * 40
        c += ('<g><circle cx="%d" cy="%d" r="11" fill="%s"/><text x="%d" y="%d" font-size="12" fill="#0e1228" text-anchor="middle" font-family="%s" font-weight="700">U</text>'
              '<animateTransform attributeName="transform" type="translate" values="0 0;0 0;%d 0;%d 0;0 0" keyTimes="0;.15;.5;.9;1" dur="8s" repeatCount="indefinite"/></g>'
              % (x0, y0, BLEU, x0, y0 + 4, esc(SANS), dx, dx))
    c += txt(240, 485, 'Liberté', 18, OR, weight='600') + txt(240, 507, "d'action", 18, OR, weight='600')
    c += '<path d="M330 380 L470 380" stroke="%s" stroke-width="2.5" stroke-dasharray="8 6" marker-end="url(#fl)" fill="none"/>' % BLEU
    c += txt(240, 290, 'De Gaulle : « départ', 16, GRIS) + txt(240, 310, 'de France », obtenu', 16, GRIS)
    e = ETAPES[3]
    return base(4, e['titre'], e['sous'], c, e['legG'], e['legD'])


def planche5():
    c = ''
    c += boite(60, 180, 560, 360, OR, '.05')
    c += txt(340, 214, 'Une grande puissance économique', 21, OR, weight='600')
    E, U, J = (200, 330), (480, 330), (340, 470)
    for (a, b, col) in [(E, U, OR), (E, J, CYAN), (U, J, BLEU)]:
        d = 'M%d %d L%d %d' % (a[0], a[1], b[0], b[1])
        c += '<path d="%s" stroke="%s" stroke-opacity=".4" stroke-width="2"/>' % (d, col)
        c += '<circle r="7" fill="%s" filter="url(#glow)"><animateMotion dur="3s" repeatCount="indefinite" path="%s"/></circle>' % (col, d)
        c += '<circle r="7" fill="%s"><animateMotion dur="3s" begin="1.5s" repeatCount="indefinite" keyPoints="1;0" keyTimes="0;1" calcMode="linear" path="%s"/></circle>' % (col, d)
    c += disque(E[0], E[1], 44, OR, 'E', 34) + txt(E[0], E[1] - 58, 'Europe', 18, OR, weight='600')
    c += disque(U[0], U[1], 44, BLEU, 'U', 34) + txt(U[0], U[1] - 58, 'États-Unis', 18, BLEU, weight='600')
    c += '<circle cx="%d" cy="%d" r="36" fill="%s" fill-opacity=".1" stroke="%s" stroke-width="2.5" stroke-dasharray="6 5"/>' % (J[0], J[1], CYAN, CYAN)
    c += txt(J[0], J[1] + 11, 'J', 30, CYAN, weight='600', family=SERIF) + txt(J[0] + 48, J[1] + 6, 'Japon, « demain »', 17, CYAN, 'start')
    c += txt(340, 528, 'Différends monétaires et commerciaux', 17, GRIS)
    # craintes du réarmement
    c += boite(660, 180, 560, 360, ROUGE, '.05')
    c += txt(940, 214, "Réarmement de la RFA : les craintes", 21, ROUGE, weight='600')
    craintes = ['Devenir militariste', "Provoquer l'URSS", 'Empêcher la réconciliation', 'Tendre durablement Est-Ouest']
    for k, cr in enumerate(craintes):
        y = 275 + k * 62
        w = len(cr) * 9.6
        c += txt(700, y, '%d.' % (k + 1), 20, ROUGE, 'start', '600') + txt(735, y, cr, 20, TEXTE, 'start')
        deb = 0.08 + k * 0.17
        c += ('<line x1="730" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="3" stroke-dasharray="%d" stroke-dashoffset="%d">'
              '<animate attributeName="stroke-dashoffset" values="%d;%d;0;0;%d" keyTimes="0;%.2f;%.2f;.92;1" dur="9s" repeatCount="indefinite"/></line>'
              % (y - 7, 740 + w, y - 7, OR, w + 20, w + 20, w + 20, w + 20, w + 20, deb, deb + 0.08))
        c += '<g opacity="0">' + apparait(deb + 0.08) + txt(1180, y, 'non', 18, VERT, 'end', '600') + '</g>'
    c += txt(940, 528, 'Aucune ne s\'est réalisée', 18, VERT, weight='600')
    e = ETAPES[4]
    return base(5, e['titre'], e['sous'], c, e['legG'], e['legD'])


def planche6():
    c = ''
    c += boite(90, 185, 380, 245, BLEU, '.08') + txt(280, 220, "Europe de l'Ouest", 22, BLEU, weight='600')
    c += lignes(280, 290, ['Exister assez fort', 'pour rester un modèle', 'et un interlocuteur'], 18, TEXTE, h=26)
    c += boite(810, 185, 380, 245, ROUGE, '.08') + txt(1000, 220, 'Union soviétique', 22, ROUGE, weight='600')
    c += lignes(1000, 290, ['Des intellectuels qui', 'discutent avec les', 'Européens'], 18, TEXTE, h=26)
    # frontière
    c += '<line x1="640" y1="185" x2="640" y2="430" stroke="%s" stroke-width="4" stroke-dasharray="12 8"><animate attributeName="stroke-opacity" values="1;.25;1" dur="6s" repeatCount="indefinite"/></line>' % GRIS
    c += txt(640, 450, '« chiens de faïence » ?', 16, GRIS)
    # dialogue
    for k in range(4):
        y = 250 + k * 45
        d = 'M470 %d C560 %d 720 %d 810 %d' % (y, y - 30, y + 30, y)
        col = OR if k % 2 == 0 else CYAN
        c += '<path d="%s" stroke="%s" stroke-opacity=".18" fill="none"/>' % (d, col)
        if k % 2 == 0:
            c += '<rect x="-8" y="-6" width="16" height="12" rx="2" fill="%s"><animateMotion dur="4s" begin="%ss" repeatCount="indefinite" path="%s"/></rect>' % (col, k * 0.6, d)
        else:
            c += '<circle r="7" fill="%s" filter="url(#glow)"><animateMotion dur="4s" begin="%ss" repeatCount="indefinite" keyPoints="1;0" keyTimes="0;1" calcMode="linear" path="%s"/></circle>' % (col, k * 0.6, d)
    # trois étapes du souhaitable
    etapes = [(VERT, '1', "Exister"), (VERT, '2', "Libéralisation à l'Est"), (OR, '3', "Existence commune")]
    xs = [130, 390, 740]
    for k, (col, num, lab) in enumerate(etapes):
        x = xs[k]
        g = '<g opacity="0">' + apparait(0.08 + k * 0.2)
        g += disque(x, 505, 18, col, num, 20) + txt(x + 28, 512, lab, 19, col, 'start', '600') + '</g>'
        c += g
    c += '<path d="M250 505 H350" stroke="%s" stroke-width="2" marker-end="url(#fl)"/><path d="M615 505 H700" stroke="%s" stroke-width="2" marker-end="url(#fl)"/>' % (GRIS, GRIS)
    c += '<rect x="985" y="478" width="245" height="58" rx="10" fill="%s" fill-opacity=".08" stroke="%s" stroke-dasharray="6 5"/>' % (ROUGE, ROUGE)
    c += txt(1107, 501, "Contre-scénario : l'Ouest", 15, ROUGE, weight='600') + txt(1107, 523, 'absorbé, tyrannie plus dure', 15, ROUGE)
    e = ETAPES[5]
    return base(6, e['titre'], e['sous'], c, e['legG'], e['legD'])


def icone(k, x, y):
    """Petit dessin au-dessus de chaque étape du parcours (centre x, base y)."""
    if k == 1:
        return ''.join('<circle cx="%d" cy="%d" r="13" fill="%s" fill-opacity=".2" stroke="%s" stroke-width="2"/>' % (x + dx, y + dy, col, col)
                       for dx, dy, col in [(-30, -10, ROUGE), (0, -32, BLEU), (30, -10, VERT)]) + disque(x, y + 18, 14, OR)
    if k == 2:
        return '<path d="M%d %d h18 v-14 h18 v-14 h18 v-14 h18" fill="none" stroke="%s" stroke-width="3"/>' % (x - 36, y + 26, VERT)
    if k == 3:
        return ('<path d="M%d %d Q%d %d %d %dZ" fill="%s" fill-opacity=".25" stroke="%s" stroke-width="2"/>' % (x - 40, y, x, y - 50, x + 40, y, BLEU, BLEU)
                + '<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="2"/>' % (x, y - 25, x, y + 25, BLEU))
    if k == 4:
        return (boite(x - 50, y - 20, 34, 44, CYAN) + '<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="5"/>' % (x + 4, y - 26, x + 4, y + 28, BLEU)
                + boite(x + 16, y - 20, 34, 44, ROUGE))
    if k == 5:
        return ''.join('<rect x="%d" y="%d" width="14" height="%d" fill="%s" fill-opacity=".6"/>' % (x - 36 + i * 20, y + 26 - h, h, OR) for i, h in enumerate([16, 26, 38, 52]))
    return (boite(x - 50, y - 20, 36, 44, BLEU) + boite(x + 14, y - 20, 36, 44, ROUGE)
            + '<circle r="5" fill="%s"><animateMotion dur="2.5s" repeatCount="indefinite" path="M%d %d H%d"/></circle>' % (OR, x - 14, y, x + 14))


def parcours():
    s = ouvrir("Parcours : Raymond Aron et l'Europe protégée, en six étapes") + etoiles(0)
    s += txt(640, 92, "Raymond Aron, 1973 : l'Europe à l'ombre des États-Unis", 38, TEXTE, weight='600', family=SERIF)
    s += txt(640, 130, "Le raisonnement de l'entretien en six étapes, de son portrait à l'avenir de l'Europe", 19, CYAN)
    xs = [140 + 200 * k for k in range(N)]
    ligne = 'M%d 360 H%d' % (xs[0], xs[-1])
    s += '<path d="%s" stroke="%s" stroke-width="3" stroke-opacity=".5" filter="url(#glow)"/>' % (ligne, CYAN)
    s += '<circle r="9" fill="%s" filter="url(#glow)"><animateMotion dur="9s" repeatCount="indefinite" path="%s"/></circle>' % (OR, ligne)
    for e, x in zip(ETAPES, xs):
        a = '<a href="../../%s" target="_top" aria-label="Étape %d : %s">' % (e['page'], e['n'], esc(e['court']))
        a += '<rect x="%d" y="190" width="190" height="320" rx="16" fill="#ffffff" fill-opacity="0"><set attributeName="fill-opacity" to=".06" begin="mouseover" end="mouseout"/></rect>' % (x - 95)
        a += icone(e['n'], x, 260)
        a += '<circle cx="%d" cy="360" r="24" fill="#0e1228" stroke="%s" stroke-width="3"/>' % (x, OR)
        a += txt(x, 368, str(e['n']), 22, OR, weight='600')
        a += lignes(x, 420, e['parcours'], 20, TEXTE, h=26, weight='600')
        a += '</a>'
        s += a
    s += '<rect x="40" y="560" width="1200" height="130" rx="16" fill="#0a0f26" fill-opacity=".78" stroke="%s" stroke-opacity=".35"/>' % CYAN
    s += txt(70, 596, 'Comment lire', 20, OR, 'start', '600', SERIF)
    s += lignes(70, 628, ["Cliquez sur une étape pour ouvrir sa planche animée. Sur une planche, les flèches gauche et droite du clavier",
                          "passent à l'étape précédente ou suivante. La fiche explique chaque étape et donne les chapitres de la vidéo",
                          "(INA, émission Le temps de lire, ORTF, 12 mars 1973)."], 17, TEXTE, 'start', h=24)
    return s + '</svg>\n'


# ---------------------------------------------------------------- pages HTML
MENU = [('sante', 'Santé'), ('geopolitique', 'Politique et Géopolitique'), ('economie', 'Économie'), ('physique', 'Physique'),
        ('informatique', 'Informatique'), ('maths', 'Maths'), ('etudes', 'Études'), ('philosophie', 'Philosophie et Sagesse'), ('langue', 'Langue')]


def entete():
    items = ''.join('<li><a href="../index.html#%s"%s>%s</a></li>' % (i, ' aria-current="page"' if i == 'geopolitique' else '', l) for i, l in MENU)
    return ('<header class="entete">\n  <a class="famzak-retour" href="https://famzak.github.io/" title="Retour à FamZakSites">&larr; FamZakSites</a>'
            '<a class="nom-site" href="../index.html#accueil">Culture<b>G</b>Site</a>\n'
            '  <nav class="menu" aria-label="Menu principal"><ul>%s</ul></nav>\n</header>\n' % items)


def page(titre, desc, corps, classe='', script=''):
    return ('<!DOCTYPE html>\n<html lang="fr">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width,initial-scale=1">\n'
            '<title>%s</title>\n<meta name="description" content="%s">\n<meta name="robots" content="noindex, nofollow">\n'
            '<link rel="preconnect" href="https://fonts.googleapis.com">\n<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
            '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Jost:wght@400;500;600&family=Spectral:ital,wght@0,400;0,500;0,600;1,400&family=Inter:wght@400;500;700&display=swap">\n'
            '<link rel="stylesheet" href="frise.css">\n</head>\n<body%s>\n%s%s%s</body>\n</html>\n'
            % (esc(titre), esc(desc), ' class="%s"' % classe if classe else '', entete(), corps, script))


TITRE = "Raymond Aron et l'Europe protégée"
DESC = "Fiche vidéo (INA, 1973) : Raymond Aron présente République impériale, juge l'Europe de l'Ouest « État protégé » des États-Unis et dit ce qu'il souhaite pour son avenir."

SCRIPT_FLECHES = ('<script>\ndocument.addEventListener("keydown",function(e){\n'
                  '  if(e.altKey||e.ctrlKey||e.metaKey||e.shiftKey)return;\n'
                  '  var r=e.key==="ArrowRight"?"next":e.key==="ArrowLeft"?"prev":"";\n'
                  '  if(!r)return;var a=document.querySelector(\'.planche-nav a[rel="\'+r+\'"]\');if(a){e.preventDefault();location.href=a.href;}\n'
                  '});\n</script>\n')


def page_parcours():
    sr = ' '.join('Étape %d : %s.' % (e['n'], e['court']) for e in ETAPES)
    corps = ('<main class="frise">\n<h1 class="sr-only">%s : parcours en %d étapes</h1>\n<p class="sr-only">%s <a href="%s-fiche.html">Lire la fiche vidéo</a>.</p>\n'
             '<div class="scene"><object type="image/svg+xml" data="images/%s/00-parcours.svg" aria-label="Parcours en %d étapes">Parcours : %s</object></div>\n</main>\n'
             % (TITRE, N, sr, SUJET, SUJET, N, esc(sr)))
    return page('%s — Parcours' % TITRE, DESC, corps, 'page-frise')


def page_planche(e):
    n = e['n']
    prev = ETAPES[n - 2] if n > 1 else None
    nxt = ETAPES[n] if n < N else None
    lp = '<a rel="prev" href="%s">&larr; Étape %d</a>' % (prev['page'], n - 1) if prev else '<a rel="prev" href="%s.html">&larr; Parcours</a>' % SUJET
    ln = '<a rel="next" href="%s">Étape %d &rarr;</a>' % (nxt['page'], n + 1) if nxt else '<a rel="next" href="%s.html">Parcours &rarr;</a>' % SUJET
    corps = ('<main class="frise planche">\n<h1 class="sr-only">Étape %d sur %d : %s</h1>\n'
             '<div class="scene"><object type="image/svg+xml" data="images/%s/%s" aria-label="%s">%s</object></div>\n'
             '<nav class="planche-nav" aria-label="Navigation entre les étapes">%s<span class="milieu"><a href="%s.html">Parcours</a><a href="%s-fiche.html#etape-%d">Explication et fiche vidéo</a></span>%s</nav>\n</main>\n'
             % (n, N, esc(e['titre']), SUJET, e['svg'], esc(e['titre']), esc(e['legG'] + ' ' + e['legD']), lp, SUJET, SUJET, n, ln))
    return page('%s — Étape %d : %s' % (TITRE, n, e['court']), DESC, corps, 'page-frise', SCRIPT_FLECHES)


def page_fiche():
    yt = 'https://youtu.be/%s' % VID
    h = ['<main class="wrap fiche-video">\n']
    h.append('<div class="vid-tete">\n<a class="back" href="../index.html#geopolitique">&larr; Politique et Géopolitique</a>\n'
             '<div class="badges"><span class="b">YouTube</span><span class="b">Archive INA, 1973</span><span class="b b-lu">Lu en entier</span></div>\n'
             '<h1>Vidéo : « Raymond Aron analyse la puissance américaine et l\'avenir de l\'Europe »</h1>\n'
             '<p class="meta">Chaîne INA Culture · 9 min 50 s · mise en ligne le 22 février 2026 · extrait de l\'émission <i>Le temps de lire</i> (ORTF, 12 mars 1973), entretien avec Pierre Dumayet · en français · transcription lue en entier · pas de chapitres : découpage proposé en 7 parties</p>\n'
             '<p class="actions"><a class="bouton" href="%s" target="_blank" rel="noopener">Voir sur YouTube</a><a class="bouton bouton-2" href="%s.html">Parcours en %d étapes</a></p>\n</div>\n' % (yt, SUJET, N))
    h.append('<article class="fiche" id="synthese">\n<h3>Synthèse et conclusion</h3>\n<h4>Synthèse</h4>\n'
             '<p>En 1973, Raymond Aron présente à la télévision <i>République impériale</i>, son livre sur la politique mondiale des États-Unis de 1945 à 1972. L\'entretien avec Pierre Dumayet suit deux temps. D\'abord un autoportrait : Aron imagine les éloges funèbres que lui consacreraient ses adversaires et ses amis, puis résume son « testament politique » de libéral lucide, partisan des réformes progressives et sceptique envers la révolution.</p>\n'
             '<p>Ensuite l\'Europe. Sa thèse : l\'Europe de l\'Ouest est un « État protégé » par les États-Unis. Elle a obtenu ce qu\'elle voulait après la guerre (sécurité, prospérité, paix, réconciliation franco-allemande), et même la France gaulliste tenait à la présence militaire américaine sur le continent. Mais elle n\'a réalisé que la moitié de ses ambitions, faute d\'être assez unie pour se défendre seule.</p>\n'
             '<h4>Conclusion</h4>\n'
             '<p>Aron souhaite que l\'Europe cesse un jour d\'être protégée. D\'abord, elle doit continuer d\'exister avec force, car c\'est ce qui peut, à long terme et par le dialogue avec les intellectuels soviétiques, encourager une libéralisation à l\'Est et une existence commune des deux parties de l\'Europe. Il ne l\'attend pas à court terme, et il juge qu\'une Europe absorbée dans le système soviétique connaîtrait une tyrannie plus lourde.</p>\n</article>\n')
    h.append('<h2 class="sec" id="etapes">Les %d étapes expliquées</h2>\n' % N)
    for e in ETAPES:
        h.append('<article class="fiche etape" id="etape-%d">\n<h3><a class="num" href="%s" aria-label="Ouvrir la planche de l\'étape %d">%d</a> %s</h3>\n'
                 '<p>%s</p>\n<p class="anim"><b>Dans l\'animation.</b> %s</p>\n'
                 '<p class="liens"><a href="%s">Voir le schéma</a> · <a href="%s?t=%d" target="_blank" rel="noopener">À %s dans la vidéo</a></p>\n</article>\n'
                 % (e['n'], e['page'], e['n'], e['n'], esc(e['court']), e['texte'], esc(e['anim']), e['page'], yt, e['t'], hms(e['t'])))
    h.append('<article class="fiche" id="chapitres">\n<h3>Les %d parties de la vidéo</h3>\n<p class="meta">La vidéo n\'a pas de chapitres : découpage proposé d\'après la transcription.</p>\n<ul class="chap">\n' % len(CHAPITRES))
    for t, ti, r in CHAPITRES:
        h.append('<li><a href="%s?t=%d" target="_blank" rel="noopener">%s</a> <b>%s.</b> %s</li>\n' % (yt, t, hms(t), esc(ti), r))
    h.append('</ul>\n</article>\n')
    h.append('<article class="fiche" id="precautions">\n<h3>Précautions</h3>\n'
             '<p class="note">C\'est une archive de 1973 : Aron parle de l\'Europe de la guerre froide (URSS, RFA, bloc soviétique) et donne son analyse personnelle, sans contradicteur. Ses jugements, par exemple sur ce que voulait le général de Gaulle, sont ceux d\'un intervenant et ne sont pas vérifiés ici. La description de la chaîne et les commentaires présentent l\'entretien comme « visionnaire » : c\'est une appréciation, pas un fait.</p>\n'
             '<p class="note">La transcription est automatique et déforme des noms : j\'ai lu « Raymond Aaron » comme Raymond Aron, « Calman Levi » comme Calmann-Lévy, « 1945-172 » comme 1945-1972, « Montes qui » comme Montesquieu, « Tville » comme Tocqueville, « la coucheuse de l\'histoire » comme l\'accoucheuse de l\'histoire et « chien de faillance » comme chiens de faïence.</p>\n</article>\n')
    h.append('<a class="back" href="../index.html#geopolitique">&larr; Politique et Géopolitique</a>\n</main>\n')
    # Quiz de 5 questions en bas de la fiche (données : fiches-geopolitique/quiz-videos.js).
    return page('%s — Fiche vidéo' % TITRE, DESC, ''.join(h), '', '<script src="../quiz-famzak.js"></script>\n<script src="quiz-videos.js"></script>\n<script src="../famzak-progres.js" data-site="culturegsite"></script>\n')


def main():
    os.makedirs(IMG, exist_ok=True)
    fichiers = {'00-parcours.svg': parcours()}
    for e, f in zip(ETAPES, [planche1, planche2, planche3, planche4, planche5, planche6]):
        fichiers[e['svg']] = f()
    for nom, contenu in fichiers.items():
        with open(os.path.join(IMG, nom), 'w', encoding='utf-8') as fh:
            fh.write(contenu)
    pages = {'%s.html' % SUJET: page_parcours(), '%s-fiche.html' % SUJET: page_fiche()}
    for e in ETAPES:
        pages[e['page']] = page_planche(e)
    for nom, contenu in pages.items():
        with open(os.path.join(DOSSIER, nom), 'w', encoding='utf-8') as fh:
            fh.write(contenu)
    print('%d SVG, %d pages' % (len(fichiers), len(pages)))


if __name__ == '__main__':
    main()
