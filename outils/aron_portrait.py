# -*- coding: utf-8 -*-
"""Génère la fiche vidéo « Raymond Aron, portrait de 1974 » (Géopolitique) :
émission Variances (ORTF, 13 décembre 1974) en entier, publiée par INA Culture.
Parcours SVG, une planche SVG animée par étape, pages HTML (parcours, planches, fiche).
Même modèle que outils/aron_europe.py (dont les fonctions communes sont reprises).
Lancer depuis la racine du dépôt : python3 -I outils/aron_portrait.py
"""
import os, random, html, math

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOSSIER = os.path.join(RACINE, 'fiches-geopolitique')
SUJET = 'aron-portrait'
IMG = os.path.join(DOSSIER, 'images', SUJET)
VID = '83bZzMMGnCI'

OR, CYAN, ROUGE, VERT, BLEU, GRIS = '#f2b84b', '#5ad1e6', '#ff6b7a', '#7ee0a0', '#7aa2ff', '#9fb3d6'
TEXTE = '#e6eefc'
SERIF = "Spectral, Georgia, 'Times New Roman', serif"
SANS = "Jost, 'Segoe UI', system-ui, sans-serif"

# ---------------------------------------------------------------- contenu
ETAPES = [
    dict(slug='choc-de-1930', court='Le choc de 1930',
         parcours=['Le choc', 'de 1930'],
         titre="« L'histoire est en mouvement »",
         sous="Comment l'Allemagne de 1930 et Max Weber ont tourné le philosophe vers la politique",
         legG="Jeune philosophe néo-kantien, Aron fuyait la politique. En mars 1930, l'Allemagne en crise le saisit : il veut comprendre l'histoire en y participant, « dedans et dehors ».",
         legD="Son modèle devient Max Weber, savant et politique, pour qui choisir une vie, c'est en abandonner une autre. Aron se dit homme politique frustré, et secrètement satisfait de l'être.",
         texte="L'émission s'ouvre sur l'autoportrait d'un touche-à-tout : Aron refuse les étiquettes et se dit tantôt « marxiste », parce qu'il essaie comme Marx de ne pas s'enfermer dans une discipline, tantôt « survivant d'un autre âge ». Il raconte ensuite d'où vient sa passion pour l'économie, la société et la politique. Jeune, il la refusait : il plaçait au-dessus de tout la philosophie pure et voyait dans la politique une forme de décadence. Le choc vient en mars 1930, quand il arrive en Allemagne, « pur étudiant sorti du néo-kantisme français ». Il découvre un pays déchiré par la crise et les passions idéologiques, et résume son intuition par une formule de Toynbee : <i>History is on the move</i>, l'histoire est en mouvement. Au cours d'une promenade au bord du Rhin, il décide de son projet : comprendre l'histoire en la réfléchissant, y participer tout en gardant du détachement, être à la fois dedans et dehors. Être juif ne lui posait alors pas de difficulté à Cologne ou à Berlin, mais l'expérience du nazisme lui fait prendre conscience d'un judaïsme qui lui était extérieur ; il l'affirmera désormais par dignité, et Israël deviendra pour lui un sujet personnel. C'est aussi l'époque de sa rencontre avec l'œuvre de Max Weber, savant qui voulait aussi faire de la politique. Aron retient de lui le sens tragique de la contradiction des valeurs : choisir une existence, c'est en abandonner une autre, et l'homme politique doit renoncer à beaucoup des vertus de la vie privée. Il se dit lui-même « homme politique frustré », et peut-être secrètement satisfait de l'avoir été, car il se juge doué pour analyser la politique, non pour la faire.",
         anim="Un point quitte la philosophie pure, traverse le choc de l'Allemagne de 1930 et arrive au projet d'Aron, à cheval entre l'histoire vécue et l'histoire comprise. À droite, la balance de Max Weber oscille entre le savant et le politique.",
         t=87),
    dict(slug='marx-keynes-sartre', court='Marx, Keynes et Sartre',
         parcours=['Marx, Keynes', 'et Sartre'],
         titre="Lire Marx, choisir Keynes, perdre Sartre",
         sous="Comment Aron est devenu libéral, et pourquoi l'amitié avec Sartre s'est brisée",
         legG="Il aurait voulu devenir marxiste pour que l'histoire choisisse à sa place. Il lit les trois tomes du Capital, n'est pas convaincu, puis Keynes : il choisira d'améliorer ce qui peut l'être.",
         legD="Ami intime de Sartre à l'École normale, il quitte vite Les Temps modernes. Pour Sartre, on ne reste pas amis en désaccord politique ; pour Aron, « un libéral a la peau dure ».",
         texte="Jeune philosophe, Aron se demandait quelles opinions adopter si l'on voulait être raisonnable. Il se disait socialiste et fut quelques mois inscrit au Parti socialiste, avant de se lasser de jeunes bourgeois qui se proclamaient révolutionnaires. Il décide alors d'étudier l'économie politique et le marxisme, « avec bonne volonté » : il aurait aimé devenir marxiste, car l'histoire lui aurait dicté son opinion et l'aurait débarrassé de l'embarras du choix. Il lit courageusement les trois tomes du <i>Capital</i> et conclut à regret que ce n'est pas vrai. Le socialisme devient pour lui un choix aussi arbitraire qu'un autre, à juger en comparant les avantages des différentes organisations de l'économie. Un peu plus tard, la lecture de la <i>Théorie générale</i> de Keynes et un goût « organique » de la liberté fixent son attitude : il n'aime pas les conservateurs, il est contre la révolution violente, et il cherche à améliorer ce qui peut l'être dans un monde mauvais. Une position décevante, reconnaît-il, mais honnête. Sur Sartre, il raconte une amitié intime à l'École normale, puis la courte aventure des <i>Temps modernes</i>, à l'image du « consensus fictif » de la Libération, qui se défait avec lui. Ce qui n'était pas inévitable, c'est la rupture de l'amitié : pour Sartre, moraliste, l'amitié intellectuelle ne survit pas à un désaccord politique sérieux. Aron répond qu'un libéral n'a pas l'âme tendre mais la peau dure : il accepte les conflits sans injurier ceux qui pensent autrement. Il rappelle enfin leur promesse de jeunesse : le survivant écrirait la nécrologie de l'autre dans l'annuaire des anciens élèves.",
         anim="Un point suit le chemin d'Aron : le Parti socialiste, puis le Capital, barré, puis Keynes et le choix libéral. À droite, la ligne de l'amitié avec Sartre se sépare en deux après les Temps modernes.",
         t=591),
    dict(slug='crise-sociale', court='Une crise sociale ?',
         parcours=['Une crise', 'sociale ?'],
         titre="Y a-t-il une crise de la société ?",
         sous="Violence, frustration et « machine folle » : le passage repris dans l'extrait de l'INA",
         legG="Rien ne prouve que la violence ait augmenté, même si certaines formes sont nouvelles. Mais les sociétés qui proclament l'égalité sans la réaliser créent de la frustration.",
         legD="Chacun se sent pris dans une « machine folle » que personne ne dirige. Aron distingue trois horizons de la crise : 5-8 ans, un demi-siècle, et l'utopie d'une civilisation stationnaire.",
         texte="Au milieu de l'émission, le journaliste demande à Aron si la violence dans la rue signale une crise sociale. C'est le passage repris dans l'extrait de neuf minutes publié par l'INA (voir la fiche liée). Aron relativise : la violence est endémique dans l'histoire, rien ne prouve qu'il y ait plus d'attentats ou d'assassinats qu'il y a cinquante ans, et le nombre de suicides n'a pas bougé, ce qui rend fausse la formule de Durkheim. Certaines formes sont pourtant nouvelles, comme les prises d'otages et la violence de groupes politiques. Il explique une partie de la petite criminalité par la frustration de sociétés qui montrent à tous des biens que beaucoup ne peuvent acquérir, et qui proclament l'égalité sans la réaliser : sous Louis XIV, la cour et les paysans vivaient dans deux mondes séparés. Il élargit la formule de Marx sur la protestation romantique : elle accompagnera toute civilisation rationalisée, capitaliste ou socialiste, où chacun se sent prisonnier d'une « machine folle » anonyme, celle qui fabrique des millions de voitures pour une circulation impossible. Mais dès que la croissance est menacée, tous accourent à son secours. Il conclut sur trois distances : la crise pétrolière à cinq ou huit ans, des conditions de croissance changées dans un demi-siècle, et pour ses « arrière-neveux » l'utopie d'une civilisation technique stationnaire.",
         anim="Trois panneaux s'allument : la courbe de la violence qui ne monte pas, la vitrine de biens inaccessibles, et la machine qui tourne seule. En bas, les trois horizons de la crise s'étirent depuis 1974.",
         t=952),
    dict(slug='inflation', court="L'inflation et l'Europe",
         parcours=["L'inflation", "et l'Europe"],
         titre="La grande inflation de 1974",
         sous="Des sociétés déjà inflationnistes, le choc du pétrole et le risque pour le marché commun",
         legG="Depuis 20 ans, l'Occident vivait avec 3 à 8 % d'inflation ; le pétrole quadruplé la pousse à 10-20 %. Or la crise de 1930, petite « dent » sur la courbe, a mené à Hitler.",
         legD="Avec 7 % en Allemagne et 15 à 20 % en France, en Italie et en Angleterre, le marché commun « sauterait ». Il faut sauver un noyau dur autour de la RFA, avec la France.",
         texte="Aron explique pourquoi les sociétés occidentales sont devenues inflationnistes. Les gouvernements préfèrent une croissance rapide à la stabilité des prix, ce qui est la politique facile. Les entreprises transforment leurs gains de productivité en hausses de salaires ; comme ces hausses se diffusent à tous les secteurs, même à ceux où la productivité progresse peu, les prix montent. Depuis vingt ans, l'inflation se situait ainsi entre 3 et 8 %, et la sagesse consistait à ne pas faire plus de bêtises que le voisin. Sur cet équilibre précaire s'est abattue, « comme l'aigle sur sa proie », la hausse subite du prix du pétrole : l'inflation passe à 10 à 20 %. Il ne croit pas que nos sociétés puissent supporter longtemps de tels taux ; revenir vers 8 à 10 % en trois ans lui paraît déjà difficile. Il rappelle que la crise des années 1930, minuscule « dent » sur la courbe de long terme, a signifié des millions de chômeurs, Hitler, puis des dizaines de millions de morts : l'histoire est faite d'accidents, et la hausse du pétrole en est un, car c'est son quadruplement en quelques mois, non le manque de pétrole, qui crée la crise. Le retour du nationalisme économique pourrait venir d'un autre biais qu'en 1930 : avec 7 % d'inflation en Allemagne et 15 à 20 % en France, en Italie et en Angleterre, les déséquilibres feraient sauter le marché commun. Il faut donc ramener les économies à une allure comparable et préserver un « noyau dur » autour de la République fédérale (Benelux, pays scandinaves, France), ce que cherchent Valéry Giscard d'Estaing et le chancelier allemand. Il ajoute que les querelles sociales portent désormais sur le pouvoir d'achat, ce qu'il trouve normal : il est trop facile de dénoncer la société de consommation quand on est du bon côté de la barricade.",
         anim="Les barres d'inflation montent d'un coup quand le prix du pétrole quadruple. Puis les pays du marché commun s'écartent selon leur taux, et un cercle tente de garder le noyau dur réuni.",
         t=1441),
    dict(slug='dedans-et-dehors', court='Dedans et dehors',
         parcours=['Dedans et', 'dehors'],
         titre="L'observateur engagé",
         sous="Prendre position de temps en temps, et regarder agir de Gaulle, Kennedy et Kissinger",
         legG="Professeur et journaliste, Aron prend parfois position : l'Algérie, Mai 68, l'élection de 1974. À Londres, il n'était pas gaulliste orthodoxe et ménageait les Français de Vichy.",
         legD="À Kennedy, qui l'interroge sur Cuba, il conseille de ne rien faire. Il admire Kissinger, négociateur exceptionnel, mais n'aurait pas pu ordonner des bombardements puis dormir.",
         texte="Comment concilier le professeur et le journaliste devenu presque homme d'action ? Aron dit avoir pris position une demi-douzaine de fois : sur l'Algérie, en Mai 68, dans la campagne présidentielle de 1974. Il ne voit pas pourquoi celui qui passe sa vie à réfléchir sur les événements ne pourrait pas, de temps en temps, s'engager, à condition de le dire ; il ne prétend pas, comme les « mandarins », être hors du siècle. Ses articles du <i>Figaro</i> en 1968 lui valurent beaucoup d'amitiés et plus encore d'inimitiés ; il avait déjà été mis au ban de l'intelligentsia de 1946-1947 à 1956, pour avoir dit du stalinisme une partie de ce qu'en dirait Khrouchtchev, puis de nouveau en 1967. À Londres pendant la guerre, il écrivait dans <i>La France libre</i> sans être gaulliste orthodoxe : jusqu'en novembre 1942, il espérait que Pétain et Vichy rejoindraient l'Afrique du Nord, et voulait ménager la réconciliation des « bons Français » de Vichy avec ceux de Londres. Avec le recul, il juge ce raisonnement acceptable pour un observateur, pas pour l'homme d'action qu'était de Gaulle. À Harvard en 1960-1961, il fréquente les conseillers de Kennedy, dont McGeorge Bundy. Il reproche à Kennedy d'avoir cité au Sénat son livre favorable à l'indépendance algérienne, et quand le président lui demande, après l'échec de la baie des Cochons, ce qu'il faut faire à Cuba, il répond « rien », citant Machiavel. Il connaît Kissinger depuis vingt-cinq ans et admire en lui un négociateur exceptionnel : retrait du Vietnam sans perdre la face (sans la paix), et au Proche-Orient des armes à Israël puis la sauvegarde de la troisième armée égyptienne et les accords de désengagement. Mais il n'aurait pas pu, comme lui, ordonner des bombardements puis aller dormir tranquille.",
         anim="Sur une frise, les prises de position d'Aron s'allument une à une, de Londres à 1974. À droite, deux portraits : Kennedy et la question de Cuba, Kissinger et ses négociations.",
         t=1897),
    dict(slug='europe-dependante', court="L'Europe dépendante",
         parcours=["L'Europe", 'dépendante'],
         titre="Le déclin de l'Europe, ou sa dépendance",
         sous="Ce que la guerre du Kippour et la facture du pétrole ont révélé en 1973-1974",
         legG="La guerre du Kippour montre que l'Europe n'a aucun moyen militaire dans la région dont dépend sa prospérité. Puis le pétrole quadruple : elle ne peut plus payer sa facture d'énergie.",
         legD="Elle paie avec des dollars prêtés par les pays pétroliers, via un marché des pétrodollars commandé par les États-Unis. « On ne change pas la réalité par des cocoricos. »",
         texte="On reparle en 1974 du déclin de l'Europe. Un an plus tôt, les observateurs constataient au contraire que l'Europe avait progressé plus vite que les États-Unis depuis un quart de siècle et que l'écart de niveau de vie se réduisait. Puis vint « le coup de tonnerre » de la guerre du Kippour (octobre 1973). Elle révèle que l'Europe occidentale n'a ni force militaire ni moyen d'intervenir dans une région dont dépendent sa prospérité et son existence : sa survie dépend d'une force qu'elle ne possède pas. Le quadruplement du prix du pétrole crée ensuite une situation sans précédent : les pays d'Europe sont incapables de payer leur facture d'énergie. Ils doivent emprunter les dollars nécessaires, prêtés par les pays producteurs à travers le marché des pétrodollars, lui-même commandé en dernière analyse par les autorités monétaires américaines. L'Europe dépend donc d'autrui non seulement pour sa sécurité mais pour son existence économique ; on peut le nier en paroles, dit-il, mais « on ne change pas la réalité par des cocoricos ». L'émission se termine sur son futur cours au Collège de France, intitulé avec ironie « la société post-industrielle ». Il veut reprendre ses <i>Dix-huit leçons sur la société industrielle</i> à la lumière des désillusions du progrès. Ce ne sera pas une analyse scientifique : on peut étudier de façon semi-scientifique des systèmes partiels (l'économie, la politique, les classes sociales), mais pas le « système des systèmes », la société globale, que l'on n'aborde qu'à partir de quelques questions marquées par notre subjectivité.",
         anim="Le pétrole coule vers l'Europe, dont la facture grossit ; des dollars reviennent en prêt depuis les pays producteurs, par un circuit qui passe par les États-Unis. Un bouclier américain recouvre l'Europe.",
         t=2961),
]

CHAPITRES = [
    (0, "Ouverture", "Aron refuse les étiquettes : « marxiste » parce qu'il touche à tout comme Marx, ou « survivant d'un autre âge »."),
    (53, "Présentation", "Philosophe passionné de politique, sociologue économiste, professeur au Collège de France et journaliste au <i>Figaro</i>."),
    (87, "Le choc de l'Allemagne, 1930", "Du refus de la politique à « l'histoire est en mouvement » ; la promenade au bord du Rhin."),
    (236, "Juif en Allemagne", "Aucune difficulté à Cologne ou à Berlin, mais une prise de conscience durable ; Israël devient un sujet personnel."),
    (437, "Max Weber", "Le savant et le politique, la contradiction des valeurs ; « un homme politique frustré, et secrètement satisfait »."),
    (591, "Marx lu, Keynes choisi", "Le Parti socialiste, les trois tomes du <i>Capital</i>, la <i>Théorie générale</i> ; contre la révolution violente."),
    (751, "Sartre et Les Temps modernes", "L'amitié d'École normale, le consensus de la Libération, la rupture ; la promesse de la nécrologie."),
    (952, "Y a-t-il une crise sociale ?", "Violence, frustration, « machine folle », trois horizons de la crise (passage repris dans l'extrait de l'INA)."),
    (1441, "L'inflation", "Des sociétés inflationnistes depuis vingt ans, le choc du pétrole, la leçon de la crise des années 1930."),
    (1641, "Nationalisme et marché commun", "Des taux d'inflation divergents qui menacent le marché commun ; le noyau dur ; la société de consommation."),
    (1897, "Professeur, journaliste, homme d'action", "Les prises de position (Algérie, 1968, 1974) ; mis au ban de l'intelligentsia."),
    (2180, "De Gaulle et Londres", "<i>La France libre</i>, un gaullisme non orthodoxe et l'espoir d'une réconciliation avec les Français de Vichy."),
    (2400, "Kennedy et Kissinger", "Harvard, l'Algérie, la question de Cuba ; Kissinger, du professeur au négociateur du Vietnam et du Proche-Orient."),
    (2961, "Le déclin de l'Europe", "La guerre du Kippour, la facture pétrolière, les pétrodollars : une Europe dépendante."),
    (3161, "La société post-industrielle", "Le futur cours au Collège de France ; le « système des systèmes » échappe à la science."),
]

N = len(ETAPES)
for i, e in enumerate(ETAPES, 1):
    e['n'] = i
    e['page'] = '%s-%02d-%s.html' % (SUJET, i, e['slug'])
    e['svg'] = '%02d-%s.svg' % (i, e['slug'])




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
def chips(liste, y, x0=None, dur=9, gap=36):
    larg = [30 + len(l) * 9.6 for l, _ in liste]
    total = sum(larg) + gap * (len(liste) - 1)
    x = x0 if x0 is not None else 640 - total / 2
    s = ''
    for k, ((lab, col), w) in enumerate(zip(liste, larg)):
        s += '<g opacity="0">' + apparait(0.08 + k * 0.18, dur=dur)
        s += '<rect x="%.0f" y="%d" width="%.0f" height="36" rx="18" fill="%s" fill-opacity=".14" stroke="%s"/>' % (x, y, w, col, col)
        s += txt(round(x + w / 2), y + 24, lab, 17, col, weight='600') + '</g>'
        x += w + gap
    return s



def hms(s):
    if s >= 3600:
        return '%d:%02d:%02d' % (s // 3600, s % 3600 // 60, s % 60)
    return '%d:%02d' % (s // 60, s % 60)


def barre_animee(x1, y1, x2, y2, col, debut=0.15):
    L = int(math.hypot(x2 - x1, y2 - y1)) + 2
    return ('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="4" stroke-dasharray="%d" stroke-dashoffset="%d">'
            '<animate attributeName="stroke-dashoffset" values="%d;%d;0;0;%d" keyTimes="0;%.2f;%.2f;.92;1" dur="9s" repeatCount="indefinite"/></line>'
            % (x1, y1, x2, y2, col, L, L, L, L, L, debut, debut + .1))


def planche1():
    c = ''
    etapes = [(150, 'Philosophie pure', ['la politique, une', '« décadence »'], GRIS),
              (390, 'Mars 1930', ["l'Allemagne en crise :", '« History is on the move »'], ROUGE),
              (630, 'Le projet', ["comprendre l'histoire", 'en y participant'], OR)]
    ligne = 'M150 270 H630'
    c += '<path d="%s" stroke="%s" stroke-width="3" stroke-opacity=".5" filter="url(#glow)"/>' % (ligne, CYAN)
    c += '<circle r="9" fill="%s" filter="url(#glow)"><animateMotion dur="7s" repeatCount="indefinite" path="%s"/></circle>' % (OR, ligne)
    for x, t1, ls, col in etapes:
        c += '<circle cx="%d" cy="270" r="15" fill="#0e1228" stroke="%s" stroke-width="3"/>' % (x, col)
        c += txt(x, 236, t1, 19, col, weight='600') + lignes(x, 310, ls, 16, TEXTE, h=22)
    c += boite(470, 370, 320, 80, OR, '.08') + lignes(630, 402, ['« Dedans et dehors » :', "l'action et le détachement"], 17, OR, h=24, weight='600')
    c += boite(60, 370, 380, 80, BLEU, '.06') + lignes(250, 400, ['Juif sous Hitler : un judaïsme', 'reçu « du dehors », assumé'], 16, TEXTE, h=22)
    # Weber
    c += boite(830, 180, 400, 380, VERT, '.05') + txt(1030, 212, 'Max Weber, le modèle', 20, VERT, weight='600')
    c += '<path d="M1030 400 V280 M990 400 H1070" stroke="%s" stroke-width="3"/>' % GRIS
    c += '<g><animateTransform attributeName="transform" type="rotate" values="-9 1030 280;9 1030 280;-9 1030 280" dur="7s" repeatCount="indefinite"/>'
    c += '<line x1="900" y1="280" x2="1160" y2="280" stroke="%s" stroke-width="4"/>' % GRIS
    for cx, col, lab in [(900, CYAN, 'Le savant'), (1160, ROUGE, 'Le politique')]:
        c += '<line x1="%d" y1="280" x2="%d" y2="320" stroke="%s" stroke-width="2"/>' % (cx, cx, GRIS)
        c += '<path d="M%d 320 h100 l-16 22 h-68z" fill="%s" fill-opacity=".2" stroke="%s" stroke-width="2"/>' % (cx - 50, col, col)
        c += txt(cx, 370, lab, 17, col, weight='600')
    c += '</g>'
    c += lignes(1030, 440, ['Choisir une existence,', "c'est en abandonner une autre"], 16, TEXTE, h=22)
    c += lignes(1030, 505, ['« Homme politique frustré,', 'et secrètement satisfait »'], 16, OR, h=22, extra=' font-style="italic"')
    e = ETAPES[0]
    return base(1, e['titre'], e['sous'], c, e['legG'], e['legD'])


def planche2():
    c = ''
    c += boite(60, 180, 620, 380, OR, '.04') + txt(370, 212, 'De Marx à Keynes', 20, OR, weight='600')
    jal = [(130, 290, 'Parti', 'socialiste', GRIS), (290, 290, 'Le Capital,', '3 tomes', ROUGE), (450, 290, 'Keynes,', 'Théorie générale', VERT), (600, 290, 'Le choix', 'libéral', OR)]
    ligne = 'M130 290 H600'
    c += '<path d="%s" stroke="%s" stroke-width="3" stroke-opacity=".5"/>' % (ligne, CYAN)
    c += '<circle r="8" fill="%s" filter="url(#glow)"><animateMotion dur="7s" repeatCount="indefinite" path="%s"/></circle>' % (OR, ligne)
    for x, y, l1, l2, col in jal:
        c += '<circle cx="%d" cy="%d" r="14" fill="#0e1228" stroke="%s" stroke-width="3"/>' % (x, y, col)
        c += txt(x, y + 44, l1, 16, col, weight='600') + txt(x, y + 64, l2, 15, col)
    c += barre_animee(262, 270, 318, 310, ROUGE, .25)
    c += txt(290, 250, '« pas vrai »', 15, ROUGE, extra=' font-style="italic"')
    c += lignes(370, 420, ["Contre la révolution violente ;", "améliorer ce qui peut l'être", 'dans un monde mauvais'], 18, TEXTE, h=26)
    c += txt(370, 520, '« Décevant, je l\'accorde »', 16, GRIS, extra=' font-style="italic"')
    # Sartre
    c += boite(720, 180, 500, 380, BLEU, '.04') + txt(970, 212, 'Sartre, l\'ami perdu', 20, BLEU, weight='600')
    c += '<path d="M760 300 H900" stroke="%s" stroke-width="5"/>' % VERT
    c += '<path d="M900 300 C960 300 980 260 1180 260" fill="none" stroke="%s" stroke-width="4"/>' % BLEU
    c += '<path d="M900 300 C960 300 980 340 1180 340" fill="none" stroke="%s" stroke-width="4"/>' % ROUGE
    for k, p in enumerate(['M760 300 H900 C960 300 980 260 1180 260', 'M760 300 H900 C960 300 980 340 1180 340']):
        c += '<circle r="7" fill="%s" filter="url(#glow)"><animateMotion dur="6s" begin="%.1fs" repeatCount="indefinite" path="%s"/></circle>' % ([BLEU, ROUGE][k], k * 0.4, p)
    c += txt(830, 285, 'École normale', 15, VERT, weight='600') + txt(900, 330, 'Temps modernes', 14, GRIS)
    c += txt(1180, 248, 'Aron', 16, BLEU, 'end', '600') + txt(1180, 368, 'Sartre', 16, ROUGE, 'end', '600')
    c += lignes(970, 420, ['Sartre : pas d\'amitié', 'avec un adversaire politique'], 16, ROUGE, h=22)
    c += lignes(970, 475, ['Aron : « un libéral n\'a pas l\'âme', 'tendre, il a la peau dure »'], 16, BLEU, h=22)
    c += txt(970, 535, 'La promesse : le survivant écrira la nécrologie', 14, GRIS, extra=' font-style="italic"')
    e = ETAPES[1]
    return base(2, e['titre'], e['sous'], c, e['legG'], e['legD'])


def roue(cx, cy, r, col, dur, sens=1):
    dents = ''.join('<rect x="%d" y="%d" width="10" height="12" fill="%s" transform="rotate(%d %d %d)"/>' % (cx - 5, cy - r - 9, col, a, cx, cy) for a in range(0, 360, 30))
    return ('<g><animateTransform attributeName="transform" type="rotate" values="0 %d %d;%d %d %d" dur="%ds" repeatCount="indefinite"/>' % (cx, cy, 360 * sens, cx, cy, dur)
            + dents + '<circle cx="%d" cy="%d" r="%d" fill="#0e1228" stroke="%s" stroke-width="4"/><circle cx="%d" cy="%d" r="%d" fill="%s"/></g>' % (cx, cy, r, col, cx, cy, r // 4, col))


def planche3():
    c = ''
    cols = [(60, 'La violence', ROUGE), (450, 'La frustration', OR), (840, 'La machine folle', BLEU)]
    for k, (x, t, col) in enumerate(cols):
        c += '<g opacity="0">' + apparait(0.05 + k * 0.15) + boite(x, 180, 380, 220, col, '.06') + txt(x + 190, 212, t, 20, col, weight='600')
        if k == 0:
            rnd = random.Random(2)
            d = 'M' + ' L'.join('%d %d' % (x + 30 + i * 22, 290 + rnd.randint(-20, 20)) for i in range(15))
            c += '<path d="%s" fill="none" stroke="%s" stroke-width="3"/>' % (d, ROUGE)
            c += lignes(x + 190, 350, ['pas de hausse prouvée,', 'des formes nouvelles'], 16, TEXTE, h=22)
        elif k == 1:
            for i in range(4):
                c += '<rect x="%d" y="245" width="56" height="44" rx="8" fill="%s" fill-opacity=".25"/>' % (x + 60 + i * 68, OR)
            c += ''.join('<circle cx="%d" cy="310" r="6" fill="%s"/>' % (x + 60 + i * 24, VERT if i in (3, 9) else GRIS) for i in range(12))
            c += lignes(x + 190, 350, ["l'égalité proclamée,", 'les biens hors de portée'], 16, TEXTE, h=22)
        else:
            c += roue(x + 150, 285, 34, BLEU, 7) + roue(x + 225, 285, 26, CYAN, 5, -1)
            c += lignes(x + 190, 350, ['personne ne décide :', 'des voitures sans route'], 16, TEXTE, h=22)
        c += '</g>'
    # trois horizons
    c += txt(640, 432, 'Trois horizons de la crise', 19, CYAN, weight='600')
    for k, (x2, col, lab) in enumerate([(380, CYAN, '5 à 8 ans : le pétrole'), (700, BLEU, 'un demi-siècle : la croissance'), (960, VERT, 'les arrière-neveux : une utopie')]):
        y = 460 + k * 38
        c += '<path d="M100 %d H%d" stroke="%s" stroke-width="4"%s marker-end="url(#fl)"/>' % (y, x2, col, ' stroke-dasharray="10 8"' if k == 2 else '')
        c += txt(x2 + 16, y + 6, lab, 16, col, 'start', '600')
    c += disque(66, 498, 24, OR) + txt(66, 503, '1974', 12, OR, weight='600')
    e = ETAPES[2]
    return base(3, e['titre'], e['sous'], c, e['legG'], e['legD'])


def planche4():
    c = ''
    # inflation avant / après
    c += boite(60, 180, 520, 380, ROUGE, '.04') + txt(320, 212, "L'inflation (par an)", 20, ROUGE, weight='600')
    c += '<line x1="110" y1="470" x2="540" y2="470" stroke="%s"/>' % GRIS
    for v in (0, 10, 20):
        c += txt(100, 474 - v * 10, '%d %%' % v, 13, GRIS, 'end')
    bars = [(150, 3, 8, CYAN, ['1954-1973', '3 à 8 %']), (300, 10, 20, ROUGE, ['1974', '10 à 20 %']), (450, 8, 10, VERT, ['Objectif', '8 à 10 %'])]
    for x, lo, hi, col, ls in bars:
        if col == ROUGE:
            c += ('<rect x="%d" y="%d" width="70" height="%d" rx="6" fill="%s" fill-opacity=".7">'
                  '<animate attributeName="height" values="80;200;200;80" keyTimes="0;.3;.9;1" dur="9s" repeatCount="indefinite"/>'
                  '<animate attributeName="y" values="390;270;270;390" keyTimes="0;.3;.9;1" dur="9s" repeatCount="indefinite"/></rect>') % (x, 470 - hi * 10, hi * 10, col)
        else:
            c += '<rect x="%d" y="%d" width="70" height="%d" rx="6" fill="%s" fill-opacity=".6"/>' % (x, 470 - hi * 10, hi * 10, col)
        c += '<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-dasharray="4 4"/>' % (x - 6, 470 - lo * 10, x + 76, 470 - lo * 10, TEXTE)
        c += txt(x + 35, 494, ls[0], 15, col, weight='600') + txt(x + 35, 514, ls[1], 15, TEXTE)
    c += '<path d="M228 300 L290 300" stroke="%s" stroke-width="3" marker-end="url(#fl)"/>' % OR
    c += txt(240, 290, 'pétrole ×4', 15, OR, weight='600')
    c += txt(320, 545, '1930 : une petite « dent », des millions de chômeurs, Hitler', 14, GRIS, extra=' font-style="italic"')
    # marché commun
    c += boite(620, 180, 600, 380, BLEU, '.04') + txt(920, 212, 'Le marché commun en danger', 20, BLEU, weight='600')
    pays = [('RFA', 7, 860, 330, VERT), ('Benelux', 0, 760, 330, VERT), ('Scandinavie', 0, 940, 280, VERT), ('France', 16, 880, 420, OR),
            ('Italie', 20, 690, 470, ROUGE), ('Royaume-Uni', 20, 1110, 460, ROUGE)]
    c += '<circle cx="860" cy="350" r="150" fill="%s" fill-opacity=".06" stroke="%s" stroke-width="2.5" stroke-dasharray="10 7"><animate attributeName="r" values="150;130;150" dur="6s" repeatCount="indefinite"/></circle>' % (VERT, VERT)
    c += txt(860, 245, 'le « noyau dur »', 15, VERT, weight='600')
    for nom, inf, x, y, col in pays:
        dx = 0 if col == VERT else (-20 if x < 860 else 20)
        c += ('<g><animateTransform attributeName="transform" type="translate" values="0 0;%d 0;0 0" dur="6s" repeatCount="indefinite"/>' % (dx * 2)
              + disque(x, y, 24, col) + txt(x, y + 44, nom, 15, col, weight='600') + (txt(x, y + 5, '%d %%' % inf, 13, TEXTE, weight='600') if inf else '') + '</g>')
    e = ETAPES[3]
    return base(4, e['titre'], e['sous'], c, e['legG'], e['legD'])


def planche5():
    c = ''
    c += txt(360, 205, 'Les prises de position', 20, OR, weight='600')
    jal = [(90, 'Londres', '1940-1944', CYAN), (230, 'Stalinisme', '1947-1956', ROUGE), (370, 'Algérie', '1957', VERT), (510, 'Mai 68', 'Le Figaro', OR), (630, '1974', 'présidentielle', BLEU)]
    c += '<path d="M90 260 H630" stroke="%s" stroke-width="3" stroke-opacity=".5"/>' % CYAN
    for k, (x, l1, l2, col) in enumerate(jal):
        c += '<g opacity="0">' + apparait(0.05 + k * 0.12)
        c += '<circle cx="%d" cy="260" r="14" fill="#0e1228" stroke="%s" stroke-width="3"/>' % (x, col)
        c += txt(x, 300, l1, 16, col, weight='600') + txt(x, 320, l2, 14, TEXTE) + '</g>'
    c += boite(60, 350, 600, 210, CYAN, '.05')
    c += lignes(360, 382, ['Ni « mandarin hors du siècle », ni militant :', 'il dit quand il parle en citoyen'], 17, TEXTE, h=24)
    c += lignes(360, 450, ["À Londres, pas gaulliste orthodoxe : il espérait", "réconcilier les « bons Français » de Vichy et de Londres.", "Juste pour un observateur, pas pour de Gaulle."], 15, GRIS, h=21)
    c += txt(360, 535, 'Mis au ban de l\'intelligentsia en 1947-1956, puis en 1967', 15, ROUGE, weight='600')
    # Kennedy / Kissinger
    for k, (y, nom, col, ls) in enumerate([(180, 'Kennedy', BLEU, ['« Que faire à Cuba ? »', '« Rien » (et Machiavel)']),
                                          (375, 'Kissinger', OR, ['Négociateur exceptionnel :', 'Vietnam, Proche-Orient'])]):
        c += boite(700, y, 520, 180, col, '.06')
        c += disque(780, y + 90, 46, col) + txt(780, y + 97, nom[0], 30, col, weight='600', family=SERIF)
        c += txt(850, y + 50, nom, 21, col, 'start', '600')
        c += lignes(850, y + 84, ls, 17, TEXTE, 'start', h=24)
    c += txt(850, 505, '« Je n\'aurais pas pu ordonner des bombardements', 14, GRIS, 'start', extra=' font-style="italic"')
    c += txt(850, 523, 'puis aller dormir tranquille »', 14, GRIS, 'start', extra=' font-style="italic"')
    e = ETAPES[4]
    return base(5, e['titre'], e['sous'], c, e['legG'], e['legD'])


def planche6():
    c = ''
    # pays producteurs -> Europe -> dollars
    c += boite(80, 250, 240, 120, OR, '.1') + lignes(200, 296, ['Pays producteurs', 'de pétrole'], 19, OR, h=26, weight='600')
    c += boite(520, 250, 240, 120, BLEU, '.1') + lignes(640, 296, ['Europe', "de l'Ouest"], 19, BLEU, h=26, weight='600')
    c += boite(960, 250, 240, 120, VERT, '.1') + lignes(1080, 296, ['États-Unis', 'autorités monétaires'], 19, VERT, h=26, weight='600')
    p1 = 'M320 285 H520'
    c += '<path d="%s" stroke="%s" stroke-width="4" marker-end="url(#fl)"/>' % (p1, OR)
    c += txt(420, 270, 'pétrole ×4', 16, OR, weight='600')
    p2 = 'M520 340 C460 420 380 420 320 340'
    c += '<path d="%s" fill="none" stroke="%s" stroke-width="3" stroke-dasharray="8 6" marker-end="url(#fl)"/>' % (p2, ROUGE)
    c += txt(420, 440, 'une facture impayable', 15, ROUGE, weight='600')
    p3 = 'M200 370 C200 520 1080 520 1080 370'
    c += '<path d="%s" fill="none" stroke="%s" stroke-width="2.5" stroke-dasharray="6 6"/>' % (p3, GRIS)
    p4 = 'M960 330 C880 330 840 340 760 340'
    c += '<path d="%s" fill="none" stroke="%s" stroke-width="3.5" marker-end="url(#fl)"/>' % (p4, VERT)
    c += txt(860, 375, 'dollars prêtés', 15, VERT, weight='600')
    c += txt(640, 515, 'le marché des pétrodollars', 15, GRIS, extra=' font-style="italic"')
    for k, (p, col) in enumerate([(p1, OR), (p3, GRIS), (p4, VERT)]):
        c += '<circle r="7" fill="%s" filter="url(#glow)"><animateMotion dur="5s" begin="%.1fs" repeatCount="indefinite" path="%s"/></circle>' % (col, k * 1.2, p)
    # bouclier
    c += '<path d="M640 190 C590 190 560 205 560 205 V235 M640 190 C690 190 720 205 720 205 V235" fill="none" stroke="%s" stroke-width="3"><animate attributeName="stroke-opacity" values=".4;1;.4" dur="3s" repeatCount="indefinite"/></path>' % VERT
    c += txt(640, 180, 'Sécurité : la force américaine (guerre du Kippour)', 15, VERT, weight='600')
    c += txt(640, 556, '« On ne change pas la réalité par des cocoricos »', 17, OR, extra=' font-style="italic"')
    e = ETAPES[5]
    return base(6, e['titre'], e['sous'], c, e['legG'], e['legD'])


PLANCHES = [planche1, planche2, planche3, planche4, planche5, planche6]


def icone(k, x, y):
    if k == 1:
        return '<path d="M%d %d H%d" stroke="%s" stroke-width="3"/>' % (x - 45, y, x + 45, CYAN) + ''.join('<circle cx="%d" cy="%d" r="8" fill="%s"/>' % (x - 45 + i * 45, y, col) for i, col in enumerate([GRIS, ROUGE, OR]))
    if k == 2:
        return ('<path d="M%d %d H%d C%d %d %d %d %d %d" fill="none" stroke="%s" stroke-width="3"/>' % (x - 45, y, x - 5, x + 15, y, x + 20, y - 18, x + 45, y - 18, BLEU)
                + '<path d="M%d %d C%d %d %d %d %d %d" fill="none" stroke="%s" stroke-width="3"/>' % (x - 5, y, x + 15, y, x + 20, y + 18, x + 45, y + 18, ROUGE))
    if k == 3:
        return '<path d="M%d %d l15 -12 l15 10 l15 -14 l15 12 l15 -8 l15 6" fill="none" stroke="%s" stroke-width="3"/>' % (x - 45, y + 6, ROUGE)
    if k == 4:
        return ''.join('<rect x="%d" y="%d" width="18" height="%d" rx="3" fill="%s" fill-opacity=".7"/>' % (x - 40 + i * 28, y + 25 - h, h, col) for i, (h, col) in enumerate([(16, CYAN), (44, ROUGE), (24, VERT)]))
    if k == 5:
        return disque(x - 25, y, 20, BLEU, 'K', 18) + disque(x + 25, y, 20, OR, 'K', 18)
    return ('<rect x="%d" y="%d" width="36" height="26" rx="5" fill="%s" fill-opacity=".3" stroke="%s"/>' % (x - 55, y - 13, OR, OR)
            + '<path d="M%d %d H%d" stroke="%s" stroke-width="3" marker-end="url(#fl)"/>' % (x - 17, y, x + 15, OR)
            + '<rect x="%d" y="%d" width="36" height="26" rx="5" fill="%s" fill-opacity=".3" stroke="%s"/>' % (x + 19, y - 13, BLEU, BLEU))


def parcours():
    s = ouvrir("Parcours : Raymond Aron, portrait de 1974, en %d étapes" % N) + etoiles(13)
    s += txt(640, 92, "Raymond Aron, 1974 : portrait d'un observateur engagé", 38, TEXTE, weight='600', family=SERIF)
    s += txt(640, 130, "L'émission Variances en %d étapes, du choc de l'Allemagne de 1930 à l'Europe dépendante" % N, 19, CYAN)
    pas = 1000 / (N - 1)
    xs = [round(140 + pas * k) for k in range(N)]
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
                          "passent à l'étape précédente ou suivante. La fiche explique chaque étape et donne les parties de la vidéo",
                          "(émission Variances de Michèle Arnaud, ORTF, 13 décembre 1974, publiée par l'INA)."], 17, TEXTE, 'start', h=24)
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


TITRE = 'Raymond Aron, portrait de 1974'
DESC = "Fiche vidéo (ORTF, 1974) : Raymond Aron raconte le choc de l'Allemagne de 1930, Marx, Keynes et Sartre, analyse la crise et l'inflation de 1974, Kennedy, Kissinger et une Europe dépendante."

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
             '<div class="badges"><span class="b">YouTube</span><span class="b">Archive télé, 1974</span><span class="b b-lu">Lu en entier</span></div>\n'
             '<h1>Vidéo : « Raymond Aron analyse la crise de 1974, le marxisme et la politique mondiale »</h1>\n'
             '<p class="meta">Chaîne INA Culture · 57 min 13 s · mise en ligne le 28 septembre 2025 · émission <i>Variances</i> de Michèle Arnaud, ORTF, 13 décembre 1974 · en français · transcription automatique lue en entier · pas de chapitres : découpage proposé en %d parties</p>\n'
             '<p class="actions"><a class="bouton" href="%s" target="_blank" rel="noopener">Voir sur YouTube</a><a class="bouton bouton-2" href="%s.html">Parcours en %d étapes</a></p>\n</div>\n' % (len(CHAPITRES), yt, SUJET, N))
    h.append('<article class="fiche" id="synthese">\n<h3>Synthèse et conclusion</h3>\n<h4>Synthèse</h4>\n'
             '<p>Ce portrait télévisé de décembre 1974 suit Raymond Aron de sa jeunesse à l\'actualité. Il raconte le choc de l\'Allemagne de 1930, qui l\'a tourné de la philosophie pure vers l\'histoire et la politique, l\'influence de Max Weber, sa lecture déçue de Marx et son choix libéral nourri de Keynes, puis la rupture avec Sartre. Il explique sa place singulière d\'observateur engagé, qui prend parfois position (Londres, stalinisme, Algérie, Mai 68), et raconte ses rencontres avec Kennedy et Kissinger.</p>\n'
             '<p>Sur l\'actualité de 1974, il relativise la « crise » de la société (la violence n\'a pas augmenté de façon prouvée, mais la frustration des sociétés égalitaires et le sentiment d\'une « machine folle » sont réels) et analyse la grande inflation née du quadruplement du prix du pétrole, qui menace le marché commun.</p>\n'
             '<h4>Conclusion</h4>\n'
             '<p>Pour Aron, le vrai déclin de l\'Europe est sa dépendance : la guerre du Kippour a montré qu\'elle ne peut ni défendre ni payer l\'énergie dont dépend sa prospérité, et qu\'elle vit des dollars prêtés par un circuit que commandent les États-Unis. Il refuse de se consoler « par des cocoricos », et annonce un cours sur la société post-industrielle, sans prétendre saisir scientifiquement la société globale.</p>\n'
             '<p class="note"><b>Voir aussi.</b> Le passage sur la crise sociale existe en extrait : <a href="aron-crise-fiche.html">Raymond Aron et le concept de crise</a>. Et du même Aron : <a href="aron-europe-fiche.html">l\'Europe protégée</a> (1973), <a href="aron-politique-fiche.html">face aux totalitarismes</a> (1975), <a href="aron-histoire-fiche.html">philosophie et histoire</a> (1963-1964).</p>\n</article>\n')
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
             '<p class="note">C\'est un entretien télévisé de 1974 où Aron parle de lui-même, sans contradicteur : ses souvenirs (Allemagne, Londres, Kennedy, Kissinger) et ses jugements sont rapportés comme il les donne, sans vérification. Ses chiffres d\'inflation sont ceux qu\'il cite de mémoire pour 1974, et ses pronostics (marché commun, durée de la crise) sont ceux de cette date. Le nom du journaliste, Bernard Bonilauri, vient de la description de l\'extrait publié par l\'INA, pas de celle de cette vidéo. J\'ai ajouté quelques repères (guerre du Kippour en octobre 1973, titre exact des <i>Dix-huit leçons</i>).</p>\n'
             '<p class="note">La transcription est automatique et déforme des noms. J\'ai lu « Toinb » comme Toynbee, « le rein » comme le Rhin, « Maxweb » comme Max Weber, « Kanes » comme Keynes, « Crouchef » comme Khrouchtchev, « Kipour » comme Kippour, « Henrique Singer » et « Kissigur » comme Kissinger, « McGeorge Bandy » comme McGeorge Bundy, « Maavel » comme Machiavel, « Pétin » comme Pétain, « Ain Touren » comme Alain Touraine, « Les 18 sur la société industrielle » comme <i>Dix-huit leçons sur la société industrielle</i>, « l\'année 601 » comme l\'année universitaire 1960-1961 et « Eris Dabay » comme l\'allemand <i>er ist dabei</i> (« il est présent »). Le titre de l\'article contre le programme commun qu\'il cite est illisible : je ne l\'ai pas repris.</p>\n</article>\n')
    h.append('<a class="back" href="../index.html#geopolitique">&larr; Politique et Géopolitique</a>\n</main>\n')
    # Quiz de 5 questions en bas de la fiche (données : fiches-geopolitique/quiz-videos.js).
    return page('%s — Fiche vidéo' % TITRE, DESC, ''.join(h), '', '<script src="../quiz-famzak.js"></script>\n<script src="quiz-videos.js"></script>\n<script src="../famzak-progres.js" data-site="culturegsite"></script>\n')


def main():
    os.makedirs(IMG, exist_ok=True)
    fichiers = {'00-parcours.svg': parcours()}
    for e, f in zip(ETAPES, PLANCHES):
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

