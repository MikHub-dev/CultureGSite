# -*- coding: utf-8 -*-
"""Génère la fiche vidéo « Le réalisme géopolitique selon Sapir et Rougeyron » (Géopolitique) :
entretien publié par la chaîne Front Populaire (2026).
Parcours SVG, une planche SVG animée par étape, pages HTML (parcours, planches, fiche).
Même modèle que outils/aron_europe.py (dont les fonctions communes sont reprises).
Lancer depuis la racine du dépôt : python3 -I outils/realisme.py
"""
import os, random, html, math

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOSSIER = os.path.join(RACINE, 'fiches-geopolitique')
SUJET = 'realisme'
IMG = os.path.join(DOSSIER, 'images', SUJET)
VID = 'vJkFa29g46s'

OR, CYAN, ROUGE, VERT, BLEU, GRIS = '#f2b84b', '#5ad1e6', '#ff6b7a', '#7ee0a0', '#7aa2ff', '#9fb3d6'
TEXTE = '#e6eefc'
SERIF = "Spectral, Georgia, 'Times New Roman', serif"
SANS = "Jost, 'Segoe UI', system-ui, sans-serif"

# ---------------------------------------------------------------- contenu
ETAPES = [
    dict(slug='idealisme-wilsonien', court="L'idéalisme wilsonien",
         parcours=["L'idéalisme", 'wilsonien'],
         titre="Après 1918, un ordre fondé sur la morale",
         sous="La SDN, les sanctions et les « points » de Wilson, vus par deux réalistes",
         legG="Après le massacre de 1914-1918, on veut un ordre garanti par une institution, la SDN, et par les sanctions économiques. Mais les États-Unis ne ratifient pas le traité.",
         legD="Pour les invités, l'idéalisme de Wilson a « criminalisé » le jeu de puissance au lieu de le comprendre, et cette cécité a préparé la Seconde Guerre mondiale.",
         texte="L'émission oppose deux grandes manières de penser les relations internationales : le paradigme libéral, ou idéaliste, et le réalisme, dont se réclament les deux invités, l'économiste Jacques Sapir et Pierre-Yves Rougeyron, président du Cercle Aristote. Le paradigme libéral naît de la Première Guerre mondiale. Devant l'horreur du massacre, les dirigeants veulent un ordre international garanti par une institution, la Société des nations, qui ferait céder les États sans moyens militaires, grâce aux sanctions économiques découvertes avec le blocus franco-britannique de l'Allemagne. Mais l'édifice est fragile dès le départ : les États-Unis ne ratifient pas le traité de Versailles, et la Grande-Bretagne voit d'un mauvais œil la France dominer le continent. Pour Sapir, cette pensée des institutions est aussi une réponse au pacifisme internationaliste des bolcheviks. Rougeyron s'en prend aux « points » du président Wilson : une vision marquée selon lui par une théologie protestante nord-américaine, qui colle mal à l'Europe et remplace l'analyse de la guerre, née d'impérialismes croisés, par une condamnation morale. En « criminalisant » la puissance au lieu de la comprendre, l'idéalisme wilsonien aurait laissé faire le réarmement allemand et porterait une part de responsabilité dans la Seconde Guerre mondiale. C'est la thèse des invités, discutée par les historiens.",
         anim="Sur la balance de l'après-1918, le plateau « morale et institutions » (la SDN, les sanctions) pèse plus lourd que celui des puissances. Le siège des États-Unis reste vide, et une fissure court sous l'édifice.",
         t=38),
    dict(slug='racines-du-realisme', court='Les racines du réalisme',
         parcours=['Les racines', 'du réalisme'],
         titre="Grotius, Vienne et l'équilibre européen",
         sous="Pour Sapir, le réalisme naît en 1815, bien avant la théorie des années 1930",
         legG="Au XVIIe siècle, Grotius pense le droit entre États à partir de la mer, espace « lisse ». L'acteur essentiel des relations internationales, c'est l'État.",
         legD="Au congrès de Vienne (1815), Metternich juge que tout ordre vaut mieux que le chaos. Kissinger y consacre sa thèse. Le XIXe siècle européen cherche l'équilibre des puissances.",
         texte="Pour remonter aux origines, les invités citent d'abord Grotius, au XVIIe siècle, qui pense les relations entre États à partir de la question maritime : la mer est un espace « lisse », où l'on peut fixer des règles communes, alors que la terre est pleine d'irrégularités géographiques, culturelles, religieuses et politiques. Chez lui, l'acteur essentiel est déjà l'État. Sapir place la vraie naissance du réalisme au congrès de Vienne, en 1815, autour de Metternich, pour qui tout ordre, même imposé aux peuples, vaut mieux que le chaos de la Révolution et de l'Empire. Il rappelle que Henry Kissinger a consacré sa thèse à ce congrès. C'est un réalisme conservateur, comme celui de Bismarck, à qui l'on prête la formule « la force prime le droit ». Le réalisme évolue ensuite : l'Empire britannique, dominant et peu contesté pendant une quarantaine d'années, doit faire face entre 1890 et 1900 à d'autres puissances, avec des chocs comme la guerre des Boers (1899-1902) ou la guerre russo-japonaise (1904-1905). On tente d'encadrer ces rivalités par des traités et par des alliances entre familles royales (« le roi mon cousin »). Dès la fin des années 1920, la Grande-Bretagne ne croit plus au libéralisme international.",
         anim="Une frise s'allume de Grotius à 1914 : la mer de Grotius, le congrès de Vienne et son équilibre, puis la montée des rivalités de la fin du XIXe siècle qui fait pencher la balance.",
         t=198),
    dict(slug='guerre-froide', court='La guerre froide',
         parcours=['La guerre', 'froide'],
         titre="« Paix impossible, guerre improbable »",
         sous="De l'échec du consensus de 1945 à la chute de l'URSS, selon les invités",
         legG="En 1945, l'URSS siège à Bretton Woods et à l'ONU, puis le monde se coupe en deux. Mais la décolonisation et Bandung (1955) font naître un autre monde, celui des non-alignés.",
         legD="Pour Rougeyron, la guerre froide (« paix impossible, guerre improbable », disait Aron) a servi la puissance américaine. En 1990, l'URSS « prive » l'Occident de son ennemi.",
         texte="Après 1945, explique Sapir, on tente de reconduire un consensus : l'Union soviétique participe à la conférence de Bretton Woods et à la fondation des Nations unies. Ce consensus échoue, après un débat interne en URSS tranché tardivement par Staline, et le monde se coupe en deux. Mais cette division est elle-même une fiction, car une autre apparaît que peu de gens avaient prévue : la décolonisation. La conférence de Bandung, en 1955, porte l'idée réaliste que les peuples colonisés doivent retrouver leur souveraineté pour qu'un ordre mondial équilibré devienne possible. Elle s'oppose à l'anticommunisme américain (« ce sont des fils de… mais ce sont les nôtres », phrase prêtée à un président américain) comme au « qui n'est pas avec nous est contre nous » soviétique ; le mouvement des non-alignés se fragmente toutefois vite. Rougeyron ajoute qu'entre 1945 et 1955, trois discours s'opposent : celui de l'URSS, celui des États-Unis, dont la morale servirait d'habit à leur puissance (Dean Acheson, les frères Dulles), et un discours réaliste d'égalité des États, dont la charte de La Havane serait un témoin oublié. Il décrit la guerre froide, « paix impossible, guerre improbable » selon la formule de Raymond Aron, comme une mobilisation permanente sans épreuve du feu, qui rendait le chef du camp occidental intouchable. En 1990, un responsable soviétique aurait lancé : « nous allons vous priver d'ennemi » ; un militaire américain confie à Sapir que les deux superpuissances étaient « deux planches pourries » qui se tenaient l'une l'autre.",
         anim="Le monde se coupe en deux blocs, puis un troisième groupe apparaît en 1955 avec Bandung. À la fin, l'un des deux blocs s'effondre, et l'autre vacille faute d'appui.",
         t=857),
    dict(slug='principes', court='Les principes du réalisme',
         parcours=['Les principes', 'du réalisme'],
         titre="« Le pouvoir arrête le pouvoir »",
         sous="Les principes du réalisme selon Morgenthau, Aron et les deux invités",
         legG="Les principes classiques : un système international anarchique, l'État souverain au centre, l'intérêt national, l'équilibre des puissances, toujours précaire, comme seule régulation.",
         legD="Pour Rougeyron, tous les États sont égaux en dignité, pas en moyens. La puissance passe, d'où l'équilibre ; et la question morale devient : combien de morts inutiles évités ?",
         texte="Le réalisme classique a pour théoriciens Hans Morgenthau et, en France, Raymond Aron. L'animateur en rappelle les principes tels qu'on les trouve dans les manuels : le système international est anarchique, l'État souverain en est l'acteur central, chaque État cherche son intérêt national, et l'équilibre des puissances, toujours précaire, est le seul cadre de régulation possible ; les institutions et le droit international ne suffisent pas en dernière instance. Rougeyron insiste sur ce qu'il juge le cœur égalitaire de cette pensée : la puissance est un droit pour tous les États ; tout intérêt n'est pas légitime, mais tout État est légitime à en avoir. La souveraineté est à la fois pouvoir et limite : elle suppose des frontières nettes. Il cite Pascal (« plaisante justice qu'une rivière borne ») pour retourner l'argument : une justice sans frontière autorise à enfoncer la porte du voisin. D'où la dialectique réaliste, « le pouvoir arrête le pouvoir » : les États sont égaux en dignité, pas en moyens, et la puissance passe, si bien que même le fort d'aujourd'hui aura besoin de l'équilibre demain. Contre le reproche d'indifférence morale, il répond que les réalistes s'intéressent au « fait moral incarné » : combien de morts inutiles évite-t-on ? « Est-ce que vos belles idées, payées par d'autres, en valent le coût ? » Il oppose cette pensée à la logique coloniale, et voit dans les guerres d'Ukraine et d'Iran le face-à-face des deux doctrines.",
         anim="Deux plateaux se font contrepoids : quand l'un monte, l'autre le retient. Les quatre principes du réalisme apparaissent un à un, et la question « combien de morts épargnés ? » s'affiche au centre.",
         t=1477),
    dict(slug='kissinger', court="Kissinger et l'Europe",
         parcours=['Kissinger', "et l'Europe"],
         titre="Kissinger, l'art du contrepoids",
         sous="Un réalisme américain, puis la naissance européenne de la « diplomatie des valeurs »",
         legG="Pour Sapir, Kissinger tempère le messianisme américain : sortir du Vietnam au moindre coût, s'ouvrir à la Chine pour l'éloigner de l'URSS. « Esprit supérieur, politiquement contestable. »",
         legD="L'Europe, elle, invente la « diplomatie des valeurs » pendant l'éclatement de la Yougoslavie : « nous sommes les bons ». Les États-Unis reprennent la main à Dayton.",
         texte="Sapir retrace la carrière de Henry Kissinger, conseiller à la sécurité nationale puis secrétaire d'État de Nixon, à la fin de la guerre du Vietnam. Sa ligne est réaliste : gagner si l'on peut, sinon limiter les pertes pour les intérêts américains. Convaincu que la guerre ne peut plus être gagnée, il ouvre la négociation avec la Chine en jouant de sa rivalité avec l'URSS, conclut en 1973 un accord avec le Nord-Vietnam qu'il sait fragile (il tiendra deux ans), puis cherche à empêcher le Vietnam de dominer l'Indochine. Sapir y voit un impérialisme qui sait qu'il n'est pas seul et apprend à jouer des contrepoids : le réalisme vient tempérer le messianisme américain. Il dit avoir rencontré Kissinger à Moscou en 2016 et en garder un sentiment partagé : un esprit supérieur, qui avait compris la montée de la Chine et des BRICS, mais un homme politique qu'il juge responsable de millions de morts, notamment au Cambodge (un jugement très sévère qui n'engage que lui). Il oppose ce réalisme américain à la « montée en idéologie » de l'Europe. Pendant l'éclatement de la Yougoslavie, au lieu de défendre ses intérêts et de chercher un accord, la Communauté européenne se pose en camp du bien : c'est le début de la « diplomatie des valeurs ». Les États-Unis, qui gardent une politique réaliste derrière un discours de valeurs, reprennent la main avec les accords de Dayton (1995). Depuis, selon lui, l'Union européenne se définit par des valeurs qu'elle ne respecte pas elle-même.",
         anim="Kissinger place des contrepoids sur l'échiquier : la Chine d'un côté, l'URSS de l'autre, le Vietnam au milieu. Puis, côté européen, le mot « valeurs » grossit pendant que la balance des intérêts disparaît.",
         t=1899),
    dict(slug='de-gaulle-et-les-valeurs', court='De Gaulle contre les valeurs',
         parcours=['De Gaulle', 'contre', 'les valeurs'],
         titre="Reconnaître des États, pas des gouvernements",
         sous="Le réalisme du général de Gaulle, et l'impasse de la diplomatie des valeurs selon les invités",
         legG="De Gaulle reconnaît les États, pas les régimes : la Russie survivra au système soviétique, la Chine est reconnue en 1964. Les nations qui ont produit un État comptent.",
         legD="Pour Rougeyron, la diplomatie des valeurs n'a ni à justifier, ni à définir, ni à évaluer ses valeurs. Sans la puissance nécessaire, elle mène l'Europe à l'impuissance.",
         texte="Rougeyron voit en de Gaulle un grand réaliste. Une diplomatie normale reconnaît des États, pas des gouvernements : de Gaulle pense que le système soviétique passera mais que la Russie demeure, et il reconnaît la République populaire de Chine en 1964, au nom de la civilisation chinoise. Selon un témoignage de Nixon publié par l'Institut Charles-de-Gaulle, le général lui aurait conseillé, après sa défaite contre Kennedy, de reconnaître la Chine une fois président, « avant qu'elle ait les moyens de vous y forcer ». Pour de Gaulle, élève de Guizot, les nations prennent conscience d'elles-mêmes et produisent un État dont il faut tenir compte : il n'y a pas de valeurs, il y a des intérêts. Rougeyron note un regain d'intérêt pour de Gaulle chez certains conservateurs américains et chez des intellectuels britanniques depuis le Brexit (le « gaullo-britannisme »). Il définit la diplomatie des valeurs comme une valeur qu'on n'a ni à justifier, ni à définir, ni à évaluer, ce qui permet de tout faire. Il raconte comment Brzezinski, adversaire de Kissinger, finit sur des positions proches des siennes, et comment les néoconservateurs, venus en partie du trotskisme, ont imposé cette diplomatie aux républicains jusqu'à la guerre d'Irak, qu'il appelle le cimetière de la puissance américaine. Sa conclusion : une politique des valeurs suppose une puissance écrasante que les États-Unis n'ont plus ; une puissance moyenne doit plutôt être un « hérisson », capable de faire payer cher toute atteinte à ses intérêts, et la dissuasion nucléaire fait qu'on l'écoute.",
         anim="Sur une carte, des États restent stables pendant que leurs régimes changent de couleur. Puis le mot « valeurs » enfle sans contrepoids, jusqu'à ce qu'un hérisson montre l'autre voie : se rendre coûteux à attaquer.",
         t=2490),
]

CHAPITRES = [
    (0, "Introduction : l'impasse de la diplomatie des « valeurs »", "Extraits de l'émission en ouverture."),
    (38, "Pourquoi théoriser les relations internationales ?", "Le paradigme libéral né de la Première Guerre mondiale : la SDN, les sanctions, l'absence des États-Unis."),
    (198, "Les origines du réalisme : Grotius, la mer et l'État-nation", "Le droit maritime, l'État comme acteur essentiel."),
    (295, "Le congrès de Vienne (1815) et la naissance de l'idéalisme wilsonien", "Metternich, la thèse de Kissinger ; un ordre de 1919 en réaction au massacre et au bolchevisme ; les « points » de Wilson."),
    (669, "La criminalisation de la puissance", "Le piège moral de l'après-1918 ; le réalisme né en 1815 selon Sapir ; Metternich et Bismarck."),
    (857, "De l'Empire britannique aux non-alignés (Bandung, 1955)", "L'Empire face aux nouvelles puissances, l'échec du consensus de 1945, la décolonisation, trois discours entre 1945 et 1955."),
    (1347, "La guerre froide : « paix impossible, guerre improbable »", "Une mobilisation sans épreuve du feu, selon Rougeyron."),
    (1432, "La chute de l'URSS : « on va vous priver d'ennemi »", "Les « deux planches pourries » d'un militaire américain."),
    (1477, "Qu'est-ce que le réalisme ?", "Morgenthau, Aron : la puissance comme droit de tous, la souveraineté comme limite, la frontière."),
    (1560, "La dialectique réaliste : « le pouvoir arrête le pouvoir »", "L'égalité en dignité, l'équilibre, le « fait moral incarné » ; les quatre principes."),
    (1899, "Henry Kissinger : l'art du contrepoids", "Vietnam, Chine, Cambodge, les BRICS ; la diplomatie européenne des valeurs née en Yougoslavie."),
    (2490, "Charles de Gaulle et le « gaullo-britannisme »", "Reconnaître les États ; la Chine en 1964 ; les nations et le temps long."),
    (2714, "L'impasse du néoconservatisme", "Brzezinski, les néoconservateurs et l'Irak ; la puissance « hérisson » et la dissuasion."),
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


def plateau(cx, y, col, lab, w=150):
    return ('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="2"/>' % (cx, y, cx, y + 40, GRIS)
            + '<path d="M%d %d h%d l-20 26 h-%dz" fill="%s" fill-opacity=".2" stroke="%s" stroke-width="2"/>' % (cx - w // 2, y + 40, w, w - 40, col, col)
            + txt(cx, y + 92, lab[0], 17, col, weight='600') + (txt(cx, y + 114, lab[1], 15, TEXTE) if len(lab) > 1 else ''))


def planche1():
    c = ''
    # balance penchée vers la morale
    c += '<path d="M400 470 V250 M340 470 H460" stroke="%s" stroke-width="4"/>' % GRIS
    c += '<g><animateTransform attributeName="transform" type="rotate" values="0 400 250;12 400 250;12 400 250;0 400 250" keyTimes="0;.3;.9;1" dur="9s" repeatCount="indefinite"/>'
    c += '<line x1="200" y1="250" x2="600" y2="250" stroke="%s" stroke-width="4"/>' % GRIS
    c += plateau(200, 250, BLEU, ['Puissances,', 'intérêts']) + plateau(600, 250, VERT, ['Morale,', 'SDN, sanctions']) + '</g>'
    c += txt(400, 220, "L'ordre de 1919", 20, OR, weight='600')
    # siège vide des États-Unis
    c += boite(700, 190, 520, 160, CYAN, '.05') + txt(960, 222, 'La Société des nations', 19, CYAN, weight='600')
    for k, (lab, col, vide) in enumerate([('France', BLEU, False), ('Royaume-Uni', ROUGE, False), ('États-Unis', GRIS, True), ('Italie', VERT, False), ('Japon', OR, False)]):
        x = 760 + k * 100
        if vide:
            c += '<rect x="%d" y="250" width="56" height="44" rx="8" fill="none" stroke="%s" stroke-dasharray="5 4"><animate attributeName="stroke-opacity" values="1;.2;1" dur="2.5s" repeatCount="indefinite"/></rect>' % (x - 28, GRIS)
        else:
            c += '<rect x="%d" y="250" width="56" height="44" rx="8" fill="%s" fill-opacity=".3" stroke="%s"/>' % (x - 28, col, col)
        c += txt(x, 318, lab, 13, col if not vide else GRIS, weight='600')
    c += txt(960, 340, 'Les États-Unis ne ratifient pas le traité de Versailles', 14, GRIS, extra=' font-style="italic"')
    c += boite(700, 380, 520, 180, ROUGE, '.06') + txt(960, 412, 'La critique réaliste', 19, ROUGE, weight='600')
    c += lignes(960, 444, ['« Criminaliser » la puissance', 'au lieu de comprendre les impérialismes', 'croisés de 1914 : une cécité qui aurait', 'préparé 1939 (thèse des invités)'], 16, TEXTE, h=23)
    c += txt(400, 545, 'Les « points » du président Wilson', 16, VERT, weight='600')
    e = ETAPES[0]
    return base(1, e['titre'], e['sous'], c, e['legG'], e['legD'])


def planche2():
    c = ''
    pts = [(140, 'XVIIe s.', 'Grotius', ['la mer, espace « lisse » ;', "l'État, acteur essentiel"], CYAN),
           (440, '1815', 'Congrès de Vienne', ['Metternich : tout ordre', 'vaut mieux que le chaos'], OR),
           (740, '1871-1890', 'Bismarck', ['un réalisme', 'conservateur'], BLEU),
           (1060, '1899-1905', 'Rivalités', ['Boers, Russie-Japon :', "l'Empire contesté"], ROUGE)]
    ligne = 'M140 270 H1060'
    c += '<path d="%s" stroke="%s" stroke-width="3" stroke-opacity=".5" filter="url(#glow)"/>' % (ligne, CYAN)
    c += '<circle r="9" fill="%s" filter="url(#glow)"><animateMotion dur="8s" repeatCount="indefinite" path="%s"/></circle>' % (OR, ligne)
    for x, d, nom, ls, col in pts:
        c += '<circle cx="%d" cy="270" r="15" fill="#0e1228" stroke="%s" stroke-width="3"/>' % (x, col)
        c += txt(x, 236, d, 18, col, weight='600')
        c += boite(x - 125, 300, 250, 110, col, '.08') + txt(x, 330, nom, 18, col, weight='600')
        c += lignes(x, 358, ls, 15, TEXTE, h=21)
    # balance européenne
    c += '<path d="M640 540 V460 M600 540 H680" stroke="%s" stroke-width="3"/>' % GRIS
    c += '<g><animateTransform attributeName="transform" type="rotate" values="-3 640 460;3 640 460;-3 640 460" dur="5s" repeatCount="indefinite"/>'
    c += '<line x1="440" y1="460" x2="840" y2="460" stroke="%s" stroke-width="3"/>' % GRIS
    for x, lab, col in [(440, 'Puissances de terre', BLEU), (840, 'Puissance maritime', CYAN)]:
        c += '<circle cx="%d" cy="478" r="14" fill="%s" fill-opacity=".4" stroke="%s"/>' % (x, col, col) + txt(x, 512, lab, 14, col, weight='600')
    c += '</g>'
    c += txt(640, 445, "L'équilibre européen du XIXe siècle", 16, OR, weight='600')
    e = ETAPES[1]
    return base(2, e['titre'], e['sous'], c, e['legG'], e['legD'])


def planche3():
    c = ''
    # deux blocs + non-alignés
    c += ('<g><rect x="120" y="200" width="300" height="200" rx="16" fill="%s" fill-opacity=".14" stroke="%s" stroke-width="2.5"/>'
          '<animate attributeName="opacity" values="1;1;1;.15;.15;1" keyTimes="0;.55;.7;.75;.95;1" dur="10s" repeatCount="indefinite"/></g>') % (ROUGE, ROUGE)
    c += lignes(270, 280, ['Bloc soviétique', '« qui n\'est pas avec nous', 'est contre nous »'], 17, ROUGE, h=24, weight='600')
    c += ('<g><rect x="860" y="200" width="300" height="200" rx="16" fill="%s" fill-opacity=".14" stroke="%s" stroke-width="2.5"/>'
          '<animateTransform attributeName="transform" type="rotate" values="0 1010 400;0 1010 400;0 1010 400;6 1010 400;6 1010 400;0 1010 400" keyTimes="0;.55;.7;.78;.95;1" dur="10s" repeatCount="indefinite"/></g>') % (BLEU, BLEU)
    c += lignes(1010, 280, ['Bloc occidental', 'la morale comme habit', 'de la puissance (thèse)'], 17, BLEU, h=24, weight='600')
    c += '<path d="M430 300 H850" stroke="%s" stroke-width="3" stroke-dasharray="10 8"/>' % GRIS
    c += txt(640, 288, '« Paix impossible, guerre improbable » (Aron)', 17, OR, weight='600')
    c += '<g opacity="0">' + apparait(0.2, dur=10) + boite(470, 330, 340, 90, VERT, '.12')
    c += lignes(640, 362, ['Bandung, 1955 : les non-alignés,', 'souveraineté et décolonisation'], 16, VERT, h=22, weight='600') + '</g>'
    c += txt(640, 210, '1945 : URSS à Bretton Woods et à l\'ONU, puis la coupure', 16, GRIS)
    # 1990
    c += '<g opacity="0">' + apparait(0.72, dur=10) + boite(160, 450, 960, 110, OR, '.08')
    c += txt(640, 484, '1990 : « Nous allons vous priver d\'ennemi »', 19, OR, weight='600')
    c += txt(640, 516, 'Deux « planches pourries » qui se tenaient l\'une l\'autre : quand l\'une tombe, l\'autre vacille', 16, TEXTE) + '</g>'
    e = ETAPES[2]
    return base(3, e['titre'], e['sous'], c, e['legG'], e['legD'])


def planche4():
    c = ''
    c += '<path d="M640 430 V240 M590 430 H690" stroke="%s" stroke-width="4"/>' % GRIS
    c += '<g><animateTransform attributeName="transform" type="rotate" values="-8 640 240;8 640 240;-8 640 240" dur="6s" repeatCount="indefinite"/>'
    c += '<line x1="440" y1="240" x2="840" y2="240" stroke="%s" stroke-width="4"/>' % GRIS
    c += plateau(440, 240, BLEU, ['Pouvoir A']) + plateau(840, 240, ROUGE, ['Pouvoir B']) + '</g>'
    c += txt(640, 210, 'Deux puissances qui se retiennent', 19, OR, weight='600')
    c += boite(270, 450, 740, 56, OR, '.1') + txt(640, 485, '« Combien de morts inutiles épargnés ? »', 19, OR, weight='600')
    pr = [(60, 190, 'Anarchie', ['pas de pouvoir', 'au-dessus des États'], CYAN), (60, 330, "L'État au centre", ['acteur souverain,', 'égal en dignité'], VERT),
          (1020, 190, 'Intérêt national', ['tout État est', 'légitime à en avoir'], BLEU), (1020, 330, 'Équilibre', ['seule régulation,', 'toujours précaire'], ROUGE)]
    for k, (x, y, t, ls, col) in enumerate(pr):
        c += '<g opacity="0">' + apparait(0.05 + k * 0.15) + boite(x, y, 200, 110, col, '.1')
        c += txt(x + 100, y + 32, t, 17, col, weight='600') + lignes(x + 100, y + 60, ls, 15, TEXTE, h=21) + '</g>'
    c += txt(640, 545, 'Pascal : « Plaisante justice qu\'une rivière borne » ; sans frontière, on enfonce la porte du voisin', 15, GRIS, extra=' font-style="italic"')
    e = ETAPES[3]
    return base(4, e['titre'], e['sous'], c, e['legG'], e['legD'])


def planche5():
    c = ''
    c += boite(60, 180, 620, 380, OR, '.04') + txt(370, 212, 'Le jeu de Kissinger (1969-1977)', 19, OR, weight='600')
    pos = [(170, 300, 'URSS', ROUGE), (570, 300, 'Chine', OR), (370, 420, 'Vietnam', VERT)]
    c += '<path d="M170 300 L570 300 L370 420 Z" fill="none" stroke="%s" stroke-opacity=".4" stroke-width="2" stroke-dasharray="6 6"/>' % GRIS
    for x, y, nom, col in pos:
        c += disque(x, y, 40, col) + txt(x, y + 6, nom, 16, col, weight='600')
    c += disque(370, 300, 30, BLEU, extra=' filter="url(#glow)"') + txt(370, 305, 'USA', 15, BLEU, weight='600')
    c += '<path d="M400 300 H525" stroke="%s" stroke-width="3" marker-end="url(#fl)"><animate attributeName="stroke-opacity" values=".2;1;.2" dur="3s" repeatCount="indefinite"/></path>' % OR
    c += txt(460, 288, 'ouverture', 14, OR)
    c += txt(270, 340, 'rivalité', 14, ROUGE)
    c += lignes(370, 500, ['Sortir du Vietnam au moindre coût :', "le réalisme tempère le messianisme"], 15, TEXTE, h=21)
    c += txt(370, 545, '« Esprit supérieur, politiquement contestable » (Sapir)', 14, GRIS, extra=' font-style="italic"')
    # Europe
    c += boite(720, 180, 500, 380, BLEU, '.04') + txt(970, 212, "L'Europe et la Yougoslavie", 19, BLEU, weight='600')
    c += ('<text x="970" y="330" font-size="40" fill="%s" text-anchor="middle" font-weight="600" font-family="%s">« Valeurs »'
          '<animate attributeName="font-size" values="26;52;52;26" keyTimes="0;.5;.9;1" dur="9s" repeatCount="indefinite"/></text>') % (ROUGE, esc(SERIF))
    c += ('<g><rect x="830" y="380" width="280" height="40" rx="8" fill="%s" fill-opacity=".25" stroke="%s"/>'
          '<animate attributeName="opacity" values="1;.15;.15;1" keyTimes="0;.5;.9;1" dur="9s" repeatCount="indefinite"/></g>') % (VERT, VERT)
    c += txt(970, 406, 'Intérêts, accord négocié', 16, VERT, weight='600')
    c += lignes(970, 460, ['« Nous sommes les bons » : naissance', 'de la diplomatie des valeurs'], 16, TEXTE, h=22)
    c += txt(970, 530, 'Dayton (1995) : les États-Unis reprennent la main', 15, GRIS, extra=' font-style="italic"')
    e = ETAPES[4]
    return base(5, e['titre'], e['sous'], c, e['legG'], e['legD'])


def planche6():
    c = ''
    c += boite(60, 180, 560, 380, VERT, '.04') + txt(340, 212, 'De Gaulle : des États, pas des régimes', 18, VERT, weight='600')
    for k, (nom, a, b, col) in enumerate([('Russie', 'le régime soviétique passe…', 'la Russie demeure', ROUGE), ('Chine', 'État reconnu en 1964', 'malgré le régime', OR)]):
        y = 250 + k * 120
        c += '<rect x="100" y="%d" width="200" height="80" rx="12" fill="none" stroke="%s" stroke-width="3"/>' % (y, col)
        c += txt(200, y + 48, nom, 22, col, weight='600', family=SERIF)
        c += ('<rect x="330" y="%d" width="250" height="80" rx="12" fill="%s" fill-opacity=".2">'
              '<animate attributeName="fill" values="%s;%s;%s" dur="6s" repeatCount="indefinite"/></rect>') % (y, BLEU, BLEU, CYAN, BLEU)
        c += txt(455, y + 36, a, 16, TEXTE) + txt(455, y + 60, b, 15, col, weight='600')
    c += lignes(340, 510, ['« Il n\'y a pas de valeurs,', 'il y a des intérêts »'], 17, VERT, h=24, weight='600')
    # valeurs vs hérisson
    c += boite(660, 180, 560, 180, ROUGE, '.05') + txt(940, 212, 'La diplomatie des valeurs, selon Rougeyron', 17, ROUGE, weight='600')
    c += chips([('Ni justifier', ROUGE), ('Ni définir', ROUGE), ('Ni évaluer', ROUGE)], 236, x0=690, gap=14)
    c += lignes(940, 310, ['Néoconservateurs, Irak : une puissance', "qu'aucun pays n'a plus (thèse des invités)"], 15, TEXTE, h=21)
    c += boite(660, 380, 560, 180, OR, '.05') + txt(940, 412, 'La puissance moyenne : le hérisson', 17, OR, weight='600')
    cx, cy = 760, 490
    pics = ''.join('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="3"/>' % (cx, cy, cx + 44 * math.cos(a), cy - 40 * abs(math.sin(a)) - 4, OR) for a in [math.pi * i / 10 for i in range(11)])
    c += '<g><animate attributeName="opacity" values=".6;1;.6" dur="2.5s" repeatCount="indefinite"/>' + pics + '</g>'
    c += '<ellipse cx="%d" cy="%d" rx="40" ry="22" fill="#0e1228" stroke="%s" stroke-width="2"/>' % (cx, cy + 4, OR)
    c += lignes(1000, 456, ['Faire payer cher toute atteinte', 'à ses intérêts ; la dissuasion', 'nucléaire fait qu\'on l\'écoute'], 15, TEXTE, h=21)
    e = ETAPES[5]
    return base(6, e['titre'], e['sous'], c, e['legG'], e['legD'])


PLANCHES = [planche1, planche2, planche3, planche4, planche5, planche6]


def icone(k, x, y):
    if k == 1:
        return ('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="3"/>' % (x - 45, y - 10, x + 45, y + 10, GRIS)
                + disque(x - 45, y - 4, 10, BLEU) + disque(x + 45, y + 16, 14, VERT))
    if k == 2:
        return ''.join('<circle cx="%d" cy="%d" r="8" fill="%s"/>' % (x - 45 + i * 30, y, col) for i, col in enumerate([CYAN, OR, BLEU, ROUGE])) + \
            '<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-opacity=".5" stroke-width="2"/>' % (x - 45, y, x + 45, y, CYAN)
    if k == 3:
        return ('<rect x="%d" y="%d" width="34" height="30" rx="5" fill="%s" fill-opacity=".3" stroke="%s"/>' % (x - 55, y - 15, ROUGE, ROUGE)
                + '<rect x="%d" y="%d" width="34" height="30" rx="5" fill="%s" fill-opacity=".3" stroke="%s"/>' % (x + 21, y - 15, BLEU, BLEU)
                + disque(x, y + 20, 9, VERT))
    if k == 4:
        return ('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="3"/>' % (x - 45, y, x + 45, y, GRIS)
                + disque(x - 45, y + 14, 12, BLEU) + disque(x + 45, y + 14, 12, ROUGE) + '<path d="M%d %d V%d" stroke="%s" stroke-width="3"/>' % (x, y, y + 30, GRIS))
    if k == 5:
        return ('<path d="M%d %d L%d %d L%d %d Z" fill="none" stroke="%s" stroke-width="2.5"/>' % (x - 40, y - 15, x + 40, y - 15, x, y + 25, GRIS)
                + disque(x - 40, y - 15, 9, ROUGE) + disque(x + 40, y - 15, 9, OR) + disque(x, y + 25, 9, VERT))
    return ''.join('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="3"/>' % (x, y + 12, x + 34 * math.cos(a), y + 12 - 30 * math.sin(a), OR) for a in [math.pi * i / 6 for i in range(7)]) + \
        '<ellipse cx="%d" cy="%d" rx="30" ry="14" fill="#0e1228" stroke="%s" stroke-width="2"/>' % (x, y + 16, OR)


def parcours():
    s = ouvrir("Parcours : le réalisme géopolitique, en %d étapes" % N) + etoiles(14)
    s += txt(640, 92, "Le réalisme géopolitique, selon Sapir et Rougeyron", 38, TEXTE, weight='600', family=SERIF)
    s += txt(640, 130, "L'entretien en %d étapes, de l'idéalisme de 1918 à la critique de la « diplomatie des valeurs »" % N, 19, CYAN)
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
                          "passent à l'étape précédente ou suivante. La fiche explique chaque étape, donne les chapitres de la vidéo",
                          "et précise ce qui relève de l'opinion des deux invités (chaîne Front Populaire, 2026)."], 17, TEXTE, 'start', h=24)
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


TITRE = 'Le réalisme géopolitique selon Sapir et Rougeyron'
DESC = "Fiche vidéo (Front Populaire, 2026) : Jacques Sapir et Pierre-Yves Rougeyron opposent le réalisme à l'idéalisme wilsonien, de Vienne à Kissinger et de Gaulle, et critiquent la « diplomatie des valeurs »."

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
             '<div class="badges"><span class="b">YouTube</span><span class="b">Entretien, 2026</span><span class="b b-lu">Lu en entier</span></div>\n'
             '<h1>Vidéo : « Comprendre le réalisme géopolitique – Jacques Sapir et Pierre-Yves Rougeyron »</h1>\n'
             '<p class="meta">Chaîne Front Populaire · 50 min 24 s · mise en ligne le 5 août 2026 · entretien avec Jacques Sapir (économiste) et Pierre-Yves Rougeyron (président du Cercle Aristote) · en français · transcription automatique lue en entier · %d chapitres fournis par la vidéo</p>\n'
             '<p class="actions"><a class="bouton" href="%s" target="_blank" rel="noopener">Voir sur YouTube</a><a class="bouton bouton-2" href="%s.html">Parcours en %d étapes</a></p>\n</div>\n' % (len(CHAPITRES), yt, SUJET, N))
    h.append('<article class="fiche" id="synthese">\n<h3>Synthèse et conclusion</h3>\n<h4>Synthèse</h4>\n'
             '<p>Deux invités qui se réclament du réalisme opposent cette école au paradigme libéral, ou idéaliste, né après 1918 avec la SDN et les « points » de Wilson. Ils font remonter le réalisme à Grotius et surtout au congrès de Vienne (1815), décrivent la guerre froide comme un affrontement figé que la décolonisation et Bandung ont déjà fissuré, et rappellent les principes classiques de l\'école (Morgenthau, Aron) : anarchie du système international, État souverain au centre, intérêt national, équilibre des puissances.</p>\n'
             '<p>Pour eux, le réalisme est une éthique : il reconnaît à tous les États une égale dignité et cherche d\'abord à épargner des vies. Ils en voient l\'illustration chez Kissinger, qui joue des contrepoids pour sortir du Vietnam, et surtout chez de Gaulle, qui reconnaît des États plutôt que des régimes.</p>\n'
             '<h4>Conclusion</h4>\n'
             '<p>Leur cible est la « diplomatie des valeurs », née selon eux en Europe pendant les guerres de Yougoslavie et portée aux États-Unis par les néoconservateurs jusqu\'à la guerre d\'Irak. Elle supposerait une puissance écrasante que personne n\'a plus ; une puissance moyenne comme la France devrait plutôt se rendre coûteuse à attaquer, en « hérisson », et s\'appuyer sur la dissuasion.</p>\n'
             '<p class="note"><b>Voir aussi.</b> Raymond Aron, souvent cité dans l\'entretien : <a href="aron-portrait-fiche.html">portrait de 1974</a> (Kissinger, l\'Europe dépendante) et <a href="aron-histoire-fiche.html">philosophie et histoire</a>. À croiser avec des analystes d\'autres écoles (libérale, institutionnaliste) pour un regard contradictoire.</p>\n</article>\n')
    h.append('<h2 class="sec" id="etapes">Les %d étapes expliquées</h2>\n' % N)
    for e in ETAPES:
        h.append('<article class="fiche etape" id="etape-%d">\n<h3><a class="num" href="%s" aria-label="Ouvrir la planche de l\'étape %d">%d</a> %s</h3>\n'
                 '<p>%s</p>\n<p class="anim"><b>Dans l\'animation.</b> %s</p>\n'
                 '<p class="liens"><a href="%s">Voir le schéma</a> · <a href="%s?t=%d" target="_blank" rel="noopener">À %s dans la vidéo</a></p>\n</article>\n'
                 % (e['n'], e['page'], e['n'], e['n'], esc(e['court']), e['texte'], esc(e['anim']), e['page'], yt, e['t'], hms(e['t'])))
    h.append('<article class="fiche" id="chapitres">\n<h3>Les %d chapitres de la vidéo</h3>\n<p class="meta">Chapitres et horodatages fournis par la vidéo ; résumés d\'après la transcription.</p>\n<ul class="chap">\n' % len(CHAPITRES))
    for t, ti, r in CHAPITRES:
        h.append('<li><a href="%s?t=%d" target="_blank" rel="noopener">%s</a> <b>%s.</b> %s</li>\n' % (yt, t, hms(t), esc(ti), r))
    h.append('</ul>\n</article>\n')
    h.append('<article class="fiche" id="precautions">\n<h3>Précautions</h3>\n'
             '<p class="note">C\'est un entretien d\'opinion publié par Front Populaire, média souverainiste qui le présente comme tel. Les deux invités partagent la même école de pensée et il n\'y a pas de contradicteur. Plusieurs thèses sont discutées par les historiens et les spécialistes : la responsabilité de l\'idéalisme wilsonien dans la Seconde Guerre mondiale, la lecture de la guerre froide comme un « roman » servant la puissance américaine, le jugement très sévère de Jacques Sapir sur Kissinger, présenté comme responsable de millions de morts au Cambodge, et la critique de la diplomatie européenne. La fiche les rapporte comme leurs opinions. Quelques propos tenus de façon polémique dans la vidéo (sur l\'Europe, ou des insultes visant des personnes) ne sont pas repris.</p>\n'
             '<p class="note">Faits et attributions non vérifiés ici : la phrase « nous allons vous priver d\'ennemi », attribuée dans la vidéo à l\'ambassadeur soviétique à l\'ONU (on la prête souvent au conseiller soviétique Gueorgui Arbatov) ; la formule sur les dictateurs « fils de… », prêtée à un président américain sans source sûre ; « la force prime le droit », prêtée à Bismarck ; l\'anecdote du conseil de De Gaulle à Nixon sur la Chine ; l\'élection de Kissinger à l\'Académie des sciences de Russie en 2016. J\'ai corrigé la fonction de Kissinger, présenté dans la vidéo comme « président du Conseil de sécurité nationale » : il en était le conseiller avant de devenir secrétaire d\'État.</p>\n'
             '<p class="note">La transcription est automatique. J\'ai lu « Grossus » comme Grotius, « Mernir », « Mné » et « Méternique » comme Metternich, « vilsonnien » comme wilsonien, « Boudre Wilson » comme Woodrow Wilson, « Morgan Tao » comme Morgenthau, « Henrique Singer » comme Henry Kissinger, « Din Chesson » comme Dean Acheson, « les frères de l\'us » comme les frères Dulles, « Brezinski » comme Brzezinski, « Guiseau » comme Guizot, « Circle Aristote » comme Cercle Aristote, « Sapierre » comme Sapir et « Blincen » comme Blinken.</p>\n</article>\n')
    h.append('<a class="back" href="../index.html#geopolitique">&larr; Politique et Géopolitique</a>\n</main>\n')
    return page('%s — Fiche vidéo' % TITRE, DESC, ''.join(h))


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

