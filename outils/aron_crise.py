# -*- coding: utf-8 -*-
"""Génère la fiche vidéo « Raymond Aron et le concept de crise » (Géopolitique) :
extrait de l'émission Variances (ORTF, 13 décembre 1974) publié par INA Podcasts.
Parcours SVG, une planche SVG animée par étape, pages HTML (parcours, planches, fiche).
Même modèle que outils/aron_europe.py (dont les fonctions communes sont reprises).
Lancer depuis la racine du dépôt : python3 -I outils/aron_crise.py
"""
import os, random, html, math

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOSSIER = os.path.join(RACINE, 'fiches-geopolitique')
SUJET = 'aron-crise'
IMG = os.path.join(DOSSIER, 'images', SUJET)
VID = 'oSaLB5vyy-w'

OR, CYAN, ROUGE, VERT, BLEU, GRIS = '#f2b84b', '#5ad1e6', '#ff6b7a', '#7ee0a0', '#7aa2ff', '#9fb3d6'
TEXTE = '#e6eefc'
SERIF = "Spectral, Georgia, 'Times New Roman', serif"
SANS = "Jost, 'Segoe UI', system-ui, sans-serif"

# ---------------------------------------------------------------- contenu
ETAPES = [
    dict(slug='violence', court='Plus de violence ?',
         parcours=['Plus de', 'violence ?'],
         titre="La violence a-t-elle augmenté ?",
         sous="Une impression de crise que les chiffres ne confirment pas",
         legG="La violence est endémique dans l'histoire. Rien ne prouve qu'il y ait plus d'attentats ou d'assassinats qu'il y a cinquante ans : même les villages d'autrefois étaient violents.",
         legD="Certaines formes sont nouvelles (otages, violence politique). Mais les suicides n'ont pas augmenté : la formule de Durkheim, « plus de suicides, donc crise », serait fausse.",
         texte="En décembre 1974, en plein premier choc pétrolier, le journaliste demande à Raymond Aron si la violence que l'on voit dans la rue est le signe d'une crise sociale. Aron commence par relativiser : la violence est endémique dans l'histoire humaine, et rien ne prouve que le nombre des attentats, des agressions ou des assassinats soit sensiblement plus élevé qu'il y a cinquante ans. Même les sociétés traditionnelles, que l'on imagine stables et tranquilles autour de la communauté villageoise, comportaient selon lui de la violence. Les études qui essaient de la mesurer donnent des résultats incertains. Un seul point lui paraît presque sûr : le nombre des suicides n'est ni plus ni moins important qu'il y a cinquante ans. La formule de Durkheim, pour qui la hausse des suicides témoignait d'une crise profonde de la société, serait donc aussi fausse aujourd'hui qu'à son époque. Aron reconnaît pourtant que certains phénomènes sont qualitativement nouveaux : la violence de certains jeunes, la violence dans les beaux quartiers, les prises d'otages, l'usage de méthodes violentes par des groupes politiques, qui aurait paru inconcevable quelques dizaines d'années plus tôt.",
         anim="La courbe de la violence ondule sans monter d'une époque à l'autre. Puis les formes nouvelles apparaissent une à une, et la formule de Durkheim se barre.",
         t=64),
    dict(slug='frustration', court="La frustration de l'égalité",
         parcours=['La frustration', "de l'égalité"],
         titre="Tant de biens à la vue de tous",
         sous="Pourquoi certaines formes de criminalité sont propres aux sociétés qui se veulent égalitaires",
         legG="Peu de sociétés ont montré autant de biens à tous leurs membres tout en empêchant tant d'entre eux de les acquérir. La petite criminalité (vols de voitures) en découle en partie.",
         legD="La cour de Louis XIV et les paysans vivaient dans deux mondes séparés : la hiérarchie était acceptée. Aujourd'hui, l'égalité proclamée rend l'inégalité des conditions insupportable.",
         texte="Pour la criminalité des grandes villes et des banlieues, surtout la petite criminalité comme les vols de voitures, Aron avance une explication sociale. Cette criminalité est probablement liée à une certaine organisation de nos sociétés, qu'il faudrait modifier pour en réduire le volume. Peu de sociétés, dit-il, ont à la fois offert autant de biens à la vue de tous leurs membres et empêché un si grand nombre d'entre eux de les acquérir. On objectera que l'écart entre la cour de Louis XIV et les paysans français était bien plus grand. Mais ils vivaient dans deux mondes radicalement distincts : il n'y avait pas de frustration, et la hiérarchie sociale était acceptée comme voulue par le destin, par Dieu, ou au moins comme un fait de la vie. Aujourd'hui, le mot d'ordre est l'égalité, et l'inégalité réelle des conditions tourne ce principe en dérision. La frustration est donc plus forte. Certaines formes de criminalité seraient ainsi propres aux sociétés qui veulent être égalitaires sans l'être, ou qui le sont devant la loi mais pas dans les conditions de vie des différentes classes.",
         anim="À gauche, un mur sépare la cour et les paysans : chacun reste dans son monde. À droite, une vitrine pleine de biens est visible de tous, mais seuls quelques-uns y accèdent, et la jauge de frustration monte.",
         t=208),
    dict(slug='machine-folle', court='La machine folle',
         parcours=['La machine', 'folle'],
         titre="Une civilisation rationalisée qui pèse",
         sous="La protestation contre la machine anonyme, et la course au secours de la croissance",
         legG="Marx disait que la protestation romantique accompagnerait le capitalisme jusqu'à sa mort. Aron l'étend : elle accompagnera toute civilisation rationalisée, capitaliste ou socialiste.",
         legD="Chacun se sent prisonnier d'un mécanisme anonyme où personne ne décide : une « machine folle » qui produit des millions de voitures pour une circulation impossible.",
         texte="Aron reprend une formule de Marx : la protestation romantique contre la civilisation capitaliste accompagnera celle-ci jusqu'à sa mort. Il la traduit à sa façon : la protestation romantique ou affective contre la civilisation rationalisée accompagnera en permanence cette civilisation, qu'elle soit capitaliste ou socialiste ; dans le monde socialiste, on entendrait exactement les mêmes protestations si l'on pouvait s'y exprimer. Ces protestations ne sont pas sans importance. Une civilisation rationnelle pèse souvent sur les individus comme une chape de plomb, et la plupart ont le sentiment d'être prisonniers d'un mécanisme social d'autant plus oppressant qu'il est anonyme. Comme personne ne peut désigner le coupable, naissent des mythologies qui en désignent un. Mais le sentiment profond, c'est que les grandes décisions ne sont prises par personne et que l'ensemble fonctionne comme une « machine folle » : on construit chaque année des millions d'automobiles pour aboutir à une circulation impossible. Aron ajoute aussitôt l'autre face : dès que la croissance et la prospérité sont menacées, gouvernements et simples citoyens se précipitent au secours de ce bien ambigu que l'on dénonçait la veille. Depuis que le pétrole est cher, que la balance des comptes est en déficit et que l'on craint la récession, le premier souci est de reconstituer les conditions de la prospérité.",
         anim="Des engrenages tournent sans personne aux commandes, et les voitures sortent de la machine jusqu'à l'embouteillage. Puis une flèche montre gouvernements et opinion qui reviennent au secours de la croissance.",
         t=287),
    dict(slug='trois-horizons', court='Trois horizons de la crise',
         parcours=['Trois horizons', 'de la crise'],
         titre="Trois distances pour comprendre la crise",
         sous="De la facture pétrolière à une civilisation technique stationnaire",
         legG="À 5-8 ans : la crise du prix des hydrocarbures, sans doute le temps qu'il faudra pour la résoudre. À un demi-siècle : des conditions de la croissance profondément changées.",
         legD="Pour ses « arrière-neveux » : une civilisation technique stationnaire, qui ferait progresser la science pour mieux vivre, non pour produire toujours plus. Une utopie, dit-il.",
         texte="Pour Aron, la crise de 1974 ne se comprend qu'en prenant trois distances dans le temps. La première est de cinq à huit ans : c'est la crise liée au prix des hydrocarbures, et cinq à huit ans sont probablement le temps nécessaire pour la résoudre. La deuxième est d'un demi-siècle : d'ici là, les conditions de la croissance dans le monde entier auront sans doute été profondément modifiées. La troisième, il la laisse à ses « arrière-neveux » : que pourrait être une civilisation technique stationnaire ? Une civilisation qui continuerait à faire progresser la science et la technique, non plus pour augmenter indéfiniment le nombre des hommes et des objets, mais pour assurer, dans un monde devenu peu à peu stationnaire, les conditions de vie les plus tolérables au plus grand nombre. Là, conclut-il, on sort des limites de l'épure : c'est une représentation utopique, sur laquelle il aime spéculer, mais plutôt dans le silence de son bureau.",
         anim="Trois flèches partent de 1974, de plus en plus longues : la facture pétrolière, la croissance mondiale, puis l'horizon lointain d'une civilisation stationnaire, dessiné en pointillé comme une utopie.",
         t=419),
]

CHAPITRES = [
    (7, "Présentation", "Générique du podcast Échos et présentation de Raymond Aron et de l'archive de 1974, en plein premier choc pétrolier."),
    (64, "La violence a-t-elle augmenté ?", "Violence endémique, pas de preuve d'une hausse, formes nouvelles ; les suicides et la formule de Durkheim."),
    (208, "Criminalité et frustration", "Tant de biens visibles et si peu accessibles ; la cour de Louis XIV et les paysans ; l'égalité proclamée."),
    (287, "La protestation et la machine folle", "La formule de Marx élargie à toute civilisation rationalisée ; le mécanisme anonyme ; la course au secours de la croissance."),
    (419, "Trois distances temporelles", "La crise pétrolière à 5-8 ans, la croissance à cinquante ans, l'utopie d'une civilisation technique stationnaire."),
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
    """Trait qui se dessine puis reste (pour barrer une formule)."""
    L = int(math.hypot(x2 - x1, y2 - y1)) + 2
    return ('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="4" stroke-dasharray="%d" stroke-dashoffset="%d">'
            '<animate attributeName="stroke-dashoffset" values="%d;%d;0;0;%d" keyTimes="0;%.2f;%.2f;.92;1" dur="9s" repeatCount="indefinite"/></line>'
            % (x1, y1, x2, y2, col, L, L, L, L, L, debut, debut + .1))


def planche1():
    c = ''
    # courbe de la violence à travers le temps
    c += boite(60, 180, 640, 250, CYAN, '.04') + txt(380, 210, 'La violence à travers le temps', 19, CYAN, weight='600')
    c += '<line x1="100" y1="390" x2="670" y2="390" stroke="%s" stroke-width="2" marker-end="url(#fl)"/>' % GRIS
    c += '<line x1="100" y1="390" x2="100" y2="235" stroke="%s" stroke-width="2" marker-end="url(#fl)"/>' % GRIS
    pts = []
    rnd = random.Random(3)
    for k in range(20):
        pts.append('%d %d' % (110 + k * 28, 320 + rnd.randint(-28, 28)))
    d = 'M' + ' L'.join(pts)
    c += '<path d="%s" fill="none" stroke="%s" stroke-width="3" stroke-dasharray="900" stroke-dashoffset="900" filter="url(#glow)"><animate attributeName="stroke-dashoffset" values="900;0;0" keyTimes="0;.5;1" dur="9s" repeatCount="indefinite"/></path>' % (d, ROUGE)
    for x, lab in [(130, 'Village d\'autrefois'), (390, 'Il y a 50 ans'), (640, '1974')]:
        c += txt(x, 412, lab, 15, GRIS)
    c += txt(380, 254, 'Pas de preuve d\'une hausse', 17, OR, weight='600')
    # formes nouvelles
    c += txt(380, 466, 'Mais des formes nouvelles', 18, ROUGE, weight='600')
    c += chips([('Prises d\'otages', ROUGE), ('Violence politique', ROUGE), ('Beaux quartiers', ROUGE)], 484, x0=72, gap=18)
    # Durkheim
    c += boite(750, 180, 470, 380, OR, '.05') + txt(985, 214, 'Le test des suicides', 20, OR, weight='600')
    c += lignes(985, 270, ['« Plus de suicides,', 'donc la société est', 'en crise » (Durkheim)'], 20, TEXTE, h=28, extra=' font-style="italic"')
    c += barre_animee(800, 330, 1170, 250, ROUGE, .3)
    for k, h in enumerate([70, 72, 69, 71]):
        x = 850 + k * 80
        c += '<rect x="%d" y="%d" width="44" height="%d" rx="4" fill="%s" fill-opacity=".55"/>' % (x, 470 - h, h, BLEU)
    c += '<line x1="830" y1="470" x2="1150" y2="470" stroke="%s"/>' % GRIS
    c += lignes(985, 500, ['Le nombre de suicides n\'a pas bougé', 'en cinquante ans : la formule est fausse'], 16, TEXTE, h=22)
    e = ETAPES[0]
    return base(1, e['titre'], e['sous'], c, e['legG'], e['legD'])


def planche2():
    c = ''
    # Louis XIV
    c += boite(60, 180, 520, 380, BLEU, '.05') + txt(320, 214, 'Sous Louis XIV', 21, BLEU, weight='600')
    c += boite(90, 250, 200, 150, OR, '.12') + lignes(190, 310, ['La cour', 'de Louis XIV'], 19, OR, h=26, weight='600')
    c += boite(350, 250, 200, 150, VERT, '.12') + lignes(450, 310, ['Les', 'paysans'], 19, VERT, h=26, weight='600')
    c += '<rect x="312" y="236" width="16" height="180" fill="%s" fill-opacity=".7"/>' % GRIS
    c += lignes(320, 450, ['Deux mondes séparés :', 'la hiérarchie est acceptée,', 'peu de frustration'], 17, TEXTE, h=24)
    # 1974
    c += boite(620, 180, 600, 380, ROUGE, '.05') + txt(920, 214, 'En 1974', 21, ROUGE, weight='600')
    c += '<rect x="660" y="240" width="330" height="120" rx="10" fill="%s" fill-opacity=".1" stroke="%s" stroke-dasharray="6 5"/>' % (CYAN, CYAN)
    c += txt(825, 262, 'Des biens visibles par tous', 16, CYAN, weight='600')
    for k, lab in enumerate(['voiture', 'télé', 'vacances', 'maison']):
        c += '<rect x="%d" y="280" width="66" height="60" rx="8" fill="%s" fill-opacity=".25"/>' % (676 + k * 77, OR) + txt(709 + k * 77, 316, lab, 14, OR)
    rnd = random.Random(8)
    for k in range(14):
        x = 680 + k * 22 + rnd.randint(-4, 4)
        ok = k in (2, 9)
        c += '<circle cx="%d" cy="%d" r="8" fill="%s"%s/>' % (x, 400 + (0 if ok else 14), VERT if ok else GRIS,
                                                             '' if not ok else ' filter="url(#glow)"')
        if ok:
            c += '<path d="M%d 392 V366" stroke="%s" stroke-width="2" marker-end="url(#fl)"/>' % (x, VERT)
    c += txt(825, 446, 'Beaucoup regardent, peu accèdent', 16, TEXTE)
    # jauge
    c += txt(1110, 250, 'Frustration', 16, ROUGE, weight='600')
    c += '<rect x="1090" y="262" width="40" height="200" rx="8" fill="none" stroke="%s" stroke-width="2"/>' % ROUGE
    c += '<rect x="1094" y="300" width="32" height="158" rx="6" fill="%s" fill-opacity=".7"><animate attributeName="y" values="440;300;300;440" keyTimes="0;.5;.9;1" dur="9s" repeatCount="indefinite"/><animate attributeName="height" values="18;158;158;18" keyTimes="0;.5;.9;1" dur="9s" repeatCount="indefinite"/></rect>' % ROUGE
    c += lignes(920, 490, ['Égalité proclamée, inégalité des conditions', '→ certaines formes de criminalité'], 17, OR, h=24, weight='600')
    e = ETAPES[1]
    return base(2, e['titre'], e['sous'], c, e['legG'], e['legD'])


def roue(cx, cy, r, col, dur, sens=1):
    dents = ''.join('<rect x="%d" y="%d" width="12" height="14" fill="%s" transform="rotate(%d %d %d)"/>' % (cx - 6, cy - r - 10, col, a, cx, cy) for a in range(0, 360, 30))
    return ('<g><animateTransform attributeName="transform" type="rotate" values="0 %d %d;%d %d %d" dur="%ds" repeatCount="indefinite"/>' % (cx, cy, 360 * sens, cx, cy, dur)
            + dents + '<circle cx="%d" cy="%d" r="%d" fill="#0e1228" stroke="%s" stroke-width="5"/><circle cx="%d" cy="%d" r="%d" fill="%s"/></g>' % (cx, cy, r, col, cx, cy, r // 4, col))


def planche3():
    c = ''
    c += boite(60, 180, 600, 300, GRIS, '.05') + txt(360, 212, 'Un mécanisme anonyme', 20, GRIS, weight='600')
    c += roue(190, 320, 55, BLEU, 8) + roue(300, 275, 36, CYAN, 6, -1) + roue(300, 375, 30, GRIS, 5, -1)
    c += lignes(520, 290, ['Personne', 'ne décide'], 22, ROUGE, h=30, weight='600')
    c += txt(520, 370, '« une machine folle »', 18, OR, extra=' font-style="italic"')
    c += lignes(360, 440, ['Une « chape de plomb » sur les individus,', 'des coupables imaginaires'], 15, TEXTE, h=20)
    # voitures
    c += '<path d="M660 330 H1220" stroke="%s" stroke-width="44" stroke-opacity=".15"/>' % GRIS
    for k in range(9):
        c += ('<g><rect x="0" y="318" width="44" height="22" rx="6" fill="%s"/>'
              '<animateTransform attributeName="transform" type="translate" values="680 0;%d 0;%d 0" keyTimes="0;.6;1" dur="9s" begin="%.1fs" repeatCount="indefinite"/></g>') % (
            [OR, ROUGE, CYAN, VERT, BLEU][k % 5], 1160 - k * 50, 1160 - k * 50, k * 0.5)
    c += txt(940, 290, 'Des millions de voitures par an…', 17, TEXTE, weight='600')
    c += txt(940, 385, '… pour une circulation impossible', 17, ROUGE, weight='600')
    # Marx / Aron
    c += boite(60, 498, 560, 66, ROUGE, '.06')
    c += lignes(340, 524, ['La protestation romantique accompagnera', 'toute civilisation rationalisée'], 16, TEXTE, h=22)
    c += boite(660, 420, 560, 144, VERT, '.06')
    c += txt(940, 450, 'Mais dès que la croissance est menacée…', 17, VERT, weight='600')
    c += lignes(940, 480, ['gouvernements et opinion accourent', 'au secours de ce « bien ambigu »', '(pétrole cher, déficit, peur de la récession)'], 16, TEXTE, h=22)
    e = ETAPES[2]
    return base(3, e['titre'], e['sous'], c, e['legG'], e['legD'])


def planche4():
    c = ''
    x0 = 110
    c += disque(x0, 360, 34, OR, extra=' filter="url(#glow)"') + txt(x0, 366, '1974', 17, OR, weight='600')
    fl = [(240, 640, CYAN, '5 à 8 ans', 'La crise du prix des hydrocarbures', ''),
          (360, 900, BLEU, 'Un demi-siècle', 'Les conditions de la croissance mondiale profondément changées', ''),
          (480, 1180, VERT, 'Les « arrière-neveux »', 'Une civilisation technique stationnaire : la science pour des vies tolérables, non pour produire sans fin', ' stroke-dasharray="10 8"')]
    for k, (y, x2, col, lab, desc, dash) in enumerate(fl):
        p = 'M%d 360 C%d 360 %d %d %d %d H%d' % (x0 + 34, x0 + 110, x0 + 90, y, x0 + 190, y, x2)
        c += '<path d="%s" fill="none" stroke="%s" stroke-width="4"%s marker-end="url(#fl)"/>' % (p, col, dash)
        c += '<circle r="7" fill="%s" filter="url(#glow)"><animateMotion dur="%ds" repeatCount="indefinite" path="%s"/></circle>' % (col, 3 + k * 2, p)
        c += '<g opacity="0">' + apparait(0.08 + k * 0.2) + txt(330, y - 14, lab, 20, col, 'start', '600')
        c += txt(330, y + 30, desc, 16, TEXTE, 'start') + '</g>'
    c += txt(640, 556, '« Nous sortons des limites de l\'épure » : une utopie, à méditer dans le silence du cabinet', 16, GRIS, extra=' font-style="italic"')
    e = ETAPES[3]
    return base(4, e['titre'], e['sous'], c, e['legG'], e['legD'])


PLANCHES = [planche1, planche2, planche3, planche4]


def icone(k, x, y):
    if k == 1:
        return '<path d="M%d %d l15 -12 l15 10 l15 -14 l15 12 l15 -8 l15 6" fill="none" stroke="%s" stroke-width="3"/>' % (x - 45, y + 6, ROUGE)
    if k == 2:
        return ('<rect x="%d" y="%d" width="8" height="46" fill="%s"/>' % (x - 4, y - 23, GRIS)
                + disque(x - 30, y, 16, OR) + disque(x + 30, y, 16, VERT))
    if k == 3:
        return '<circle cx="%d" cy="%d" r="20" fill="none" stroke="%s" stroke-width="6" stroke-dasharray="8 6"/><circle cx="%d" cy="%d" r="14" fill="none" stroke="%s" stroke-width="5" stroke-dasharray="6 5"/>' % (x - 14, y, BLEU, x + 22, y - 10, CYAN)
    return ''.join('<path d="M%d %d H%d" stroke="%s" stroke-width="3"%s/>' % (x - 45, y - 16 + i * 16, x - 10 + i * 30, col, ' stroke-dasharray="6 5"' if i == 2 else '')
                   for i, col in enumerate([CYAN, BLEU, VERT]))


def parcours():
    s = ouvrir("Parcours : Raymond Aron et le concept de crise, en %d étapes" % N) + etoiles(12)
    s += txt(640, 92, "Raymond Aron, 1974 : y a-t-il une crise ?", 38, TEXTE, weight='600', family=SERIF)
    s += txt(640, 130, "Un extrait de neuf minutes en %d étapes, de la violence dans la rue aux trois horizons de la crise" % N, 19, CYAN)
    pas = 1000 / (N - 1)
    xs = [round(140 + pas * k) for k in range(N)]
    ligne = 'M%d 360 H%d' % (xs[0], xs[-1])
    s += '<path d="%s" stroke="%s" stroke-width="3" stroke-opacity=".5" filter="url(#glow)"/>' % (ligne, CYAN)
    s += '<circle r="9" fill="%s" filter="url(#glow)"><animateMotion dur="9s" repeatCount="indefinite" path="%s"/></circle>' % (OR, ligne)
    for e, x in zip(ETAPES, xs):
        a = '<a href="../../%s" target="_top" aria-label="Étape %d : %s">' % (e['page'], e['n'], esc(e['court']))
        a += '<rect x="%d" y="190" width="220" height="320" rx="16" fill="#ffffff" fill-opacity="0"><set attributeName="fill-opacity" to=".06" begin="mouseover" end="mouseout"/></rect>' % (x - 110)
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
                          "(extrait de l'émission Variances, ORTF, 13 décembre 1974, publié par l'INA)."], 17, TEXTE, 'start', h=24)
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
    return ('<!DOCTYPE html>\n<html lang="fr">\n<head>\n<meta charset="utf-8">\n<script src="https://mikhub-dev.github.io/RoutineSite/famzak-verrou.js?v=3" onerror="document.documentElement.hidden=true"></script>\n<meta name="viewport" content="width=device-width,initial-scale=1">\n'
            '<title>%s</title>\n<meta name="description" content="%s">\n<meta name="robots" content="noindex, nofollow">\n'
            '<link rel="preconnect" href="https://fonts.googleapis.com">\n<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
            '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Jost:wght@400;500;600&family=Spectral:ital,wght@0,400;0,500;0,600;1,400&family=Inter:wght@400;500;700&display=swap">\n'
            '<link rel="stylesheet" href="frise.css">\n</head>\n<body%s>\n%s%s%s</body>\n</html>\n'
            % (esc(titre), esc(desc), ' class="%s"' % classe if classe else '', entete(), corps, script))


TITRE = 'Raymond Aron et le concept de crise'
DESC = 'Fiche vidéo (ORTF, 1974) : en plein choc pétrolier, Raymond Aron relativise la hausse de la violence, explique la frustration des sociétés égalitaires et distingue trois horizons de la crise.'

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
             '<h1>Vidéo : « 1974 - Raymond Aron et le concept de crise »</h1>\n'
             '<p class="meta">Chaîne INA Podcasts (podcast <i>Échos</i>) · 8 min 53 s · mise en ligne le 23 mai 2023 · extrait de l\'émission <i>Variances</i> de Michèle Arnaud, ORTF, 13 décembre 1974, questions de Bernard Bonilauri · en français · transcription automatique lue en entier · pas de chapitres : découpage proposé en %d parties</p>\n'
             '<p class="actions"><a class="bouton" href="%s" target="_blank" rel="noopener">Voir sur YouTube</a><a class="bouton bouton-2" href="%s.html">Parcours en %d étapes</a></p>\n</div>\n' % (len(CHAPITRES), yt, SUJET, N))
    h.append('<article class="fiche" id="synthese">\n<h3>Synthèse et conclusion</h3>\n<h4>Synthèse</h4>\n'
             '<p>Dans cet extrait télévisé de décembre 1974, en plein premier choc pétrolier, Raymond Aron répond à une question sur la « crise » de la société. Il refuse d\'abord le catastrophisme : rien ne prouve que la violence ait augmenté, même si certaines de ses formes sont nouvelles, et le nombre des suicides n\'a pas changé. Il explique ensuite une partie de la petite criminalité par la frustration propre aux sociétés qui proclament l\'égalité sans la réaliser, en montrant à tous des biens que beaucoup ne peuvent acquérir.</p>\n'
             '<p>Il décrit enfin le malaise d\'une civilisation rationalisée, capitaliste ou socialiste, où chacun se sent pris dans une « machine folle » que personne ne dirige. Pourtant, dès que la croissance est menacée, tout le monde se précipite à son secours.</p>\n'
             '<h4>Conclusion</h4>\n'
             '<p>Aron propose de regarder la crise à trois distances : cinq à huit ans pour absorber la hausse du pétrole, un demi-siècle pour des conditions de croissance profondément changées, et, plus loin, l\'utopie d\'une civilisation technique stationnaire, qui mettrait la science au service de vies tolérables pour le plus grand nombre.</p>\n'
             '<p class="note"><b>Voir aussi.</b> L\'émission complète, avec cet extrait à 16:45 : <a href="aron-portrait-fiche.html">Raymond Aron, portrait de 1974</a>. Et du même Aron : <a href="aron-europe-fiche.html">l\'Europe protégée</a> (1973), <a href="aron-politique-fiche.html">face aux totalitarismes</a> (1975), <a href="aron-histoire-fiche.html">philosophie et histoire</a> (1963-1964).</p>\n</article>\n')
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
             '<p class="note">C\'est un extrait de huit minutes d\'un entretien télévisé de 1974, remonté en podcast par l\'INA avec une présentation ajoutée. Aron y donne son analyse personnelle, sans contradicteur. Ses constats sur la violence et les suicides sont ceux qu\'il tire des études de l\'époque, sans chiffres précis : ils ne sont pas vérifiés ici. Ses horizons de 5 à 8 ans et d\'un demi-siècle sont des pronostics de 1974.</p>\n'
             '<p class="note">La transcription est automatique. J\'ai lu « durkem » comme Durkheim, « Marc a dit » comme « Marx a dit » et « bonnilori » comme Bonilauri (orthographe de la description de la vidéo). Les citations entre guillemets sont légèrement resserrées.</p>\n</article>\n')
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

