# -*- coding: utf-8 -*-
"""Génère la fiche vidéo « Raymond Aron face aux totalitarismes » (Géopolitique) :
parcours SVG, une planche SVG animée par étape, pages HTML (parcours, planches, fiche).
Même modèle que outils/aron_europe.py (dont les fonctions communes sont reprises).
Lancer depuis la racine du dépôt : python3 -I outils/aron_politique.py
"""
import os, random, html, math

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOSSIER = os.path.join(RACINE, 'fiches-geopolitique')
SUJET = 'aron-politique'
IMG = os.path.join(DOSSIER, 'images', SUJET)
VID = 'zPffjGnJxCE'

OR, CYAN, ROUGE, VERT, BLEU, GRIS = '#f2b84b', '#5ad1e6', '#ff6b7a', '#7ee0a0', '#7aa2ff', '#9fb3d6'
TEXTE = '#e6eefc'
SERIF = "Spectral, Georgia, 'Times New Roman', serif"
SANS = "Jost, 'Segoe UI', system-ui, sans-serif"

# ---------------------------------------------------------------- contenu
ETAPES = [
    dict(slug='verite-qui-gene', court='La vérité qui gêne',
         parcours=['La vérité', 'qui gêne'],
         titre="La politique, amorale et souvent immorale",
         sous="Pourquoi Aron est resté spectateur de la politique plutôt qu'acteur",
         legG="La vérité qui le gêne le plus : les relations humaines qu'il aime et la politique sont incompatibles. Conquérir et exercer le pouvoir est amoral, souvent immoral.",
         legD="Il reste donc spectateur, « voyeur » dit-il. Autres raisons : son impatience, et il ne pourrait pas ordonner des actes violents puis dormir en paix.",
         texte="Jacques Paugam demande à Raymond Aron quelle vérité le gêne le plus. Sa réponse remonte à sa jeunesse : entre les relations humaines telles qu'il les aime et la politique, il y a une incompatibilité radicale. Pour arriver au pouvoir et plus encore pour l'exercer, la politique est selon lui, au mieux, amorale, et souvent immorale. C'est la raison qu'il se donne pour être resté en marge, spectateur ou même « voyeur » de la politique. Il ajoute, par franchise, d'autres raisons : il est très impatient, supporte mal les imbéciles, alors que la démocratie, le seul régime qu'il aime, exige une patience inépuisable. Il évoque ses amis de Harvard, bons pères et bons époux, qui ordonnaient des bombardements terribles puis dormaient paisiblement : il ne les condamne pas, car la violence fait partie de la politique, mais lui en serait incapable. Il reconnaît la nécessité de la violence en politique tout en la détestant.",
         anim="Les deux cercles, relations humaines et politique, s'écartent puis se rapprochent sans jamais se rejoindre. L'œil d'Aron reste du côté du spectateur, et ses raisons apparaissent une à une.",
         t=0),
    dict(slug='autorite-et-adversaires', court='Autorité et adversaires',
         parcours=['Autorité et', 'adversaires'],
         titre="Croire à l'autorité, la détester pour soi",
         sous="Un non-conformiste qui respecte ses adversaires, Sartre compris",
         legG="En politique, il croit l'autorité nécessaire. À titre personnel, il la déteste : il laisse ses étudiants choisir leur sujet de thèse, même s'il le juge mauvais.",
         legD="Il a critiqué tous les dirigeants, de Gaulle compris. Avec Sartre, l'amitié de jeunesse a cédé à la polémique, mais il admire toujours le philosophe.",
         texte="Aron dit s'accommoder très bien de la vie sociale, entre amis comme à l'université. Même les étudiants gauchistes, après 1968, le tenaient pour un adversaire digne de respect, parce qu'il disait ouvertement ce que beaucoup de collègues n'osaient pas dire. Il distingue la politique et la vie personnelle : il croit l'autorité nécessaire en politique, mais la déteste pour lui-même, au point de refuser d'imposer un sujet de thèse. N'ayant jamais été acteur politique, il a critiqué tous les dirigeants, y compris le général de Gaulle, qui finissaient par le juger « impossible » ; il se dit non-conformiste. Sur Sartre, il raconte une amitié d'École normale, puis un éloignement, puis la rupture de la guerre froide et des polémiques qu'il juge personnelles, comme l'interview de 1968 où Sartre le disait indigne d'enseigner. Il met ce Sartre polémiste « dans un petit coin » et continue d'admirer le philosophe.",
         anim="La balance penche d'un côté (l'autorité nécessaire en politique) puis de l'autre (l'autorité détestée pour soi). À droite, un point parcourt l'histoire de l'amitié avec Sartre, de l'École normale à la polémique.",
         t=182),
    dict(slug='antitotalitaire', court="Antitotalitaire depuis l'Allemagne",
         parcours=['Antitotalitaire', "depuis", "l'Allemagne"],
         titre="Antitotalitaire depuis l'Allemagne de 1933",
         sous="Une conviction née en voyant monter le national-socialisme",
         legG="Aron se dit anti-révolutionnaire : les révolutions coûtent très cher et font plus de mal que de bien. Le fond, c'est l'antitotalitarisme.",
         legD="Il le date de son séjour en Allemagne (1931-1933). Après 1945, sa colère vise le stalinisme, ce qui le met au ban de l'intelligentsia.",
         texte="On le dit conservateur ; Aron se définit plutôt comme anti-révolutionnaire. Comme beaucoup d'hommes de sa génération, il pense que les révolutions coûtent très cher, causent plus de mal que de bien et guérissent rarement les maux qu'elles visent : elles en suppriment certains et en créent d'autres. Ce qui lui paraît fondamental chez lui, c'est l'antitotalitarisme. Il le fait remonter à son expérience en Allemagne entre 1931 et 1933 : il y a vu le national-socialisme arriver au pouvoir, le déchaînement des passions et de la violence, et il a prévu la guerre. De 1933 à 1939, il vit « dans l'attente de la catastrophe » et se hâte d'écrire ses premiers livres. Après 1945, sa « fureur antitotalitaire » se tourne vers le stalinisme, ce qui le fait mettre au ban de l'intelligentsia pour avoir dit, selon ses mots, la moitié de ce que Khrouchtchev dira lui-même au XX<sup>e</sup> congrès (en 1956, date ajoutée ici).",
         anim="Un point lumineux suit la frise de la vie d'Aron : Allemagne 1931-1933, l'attente de la guerre, puis la critique du stalinisme après 1945 et le XXe congrès.",
         t=323),
    dict(slug='revolution-ou-reforme', court='Révolution ou réforme',
         parcours=['Révolution', 'ou réforme'],
         titre="Révolutionnaire ou anti-révolutionnaire",
         sous="Pour Aron, le vrai choix des pays d'Europe de l'Ouest en 1975",
         legG="Citant Malraux, il dit que la droite traditionnelle n'existe plus : on est révolutionnaire ou anti-révolutionnaire, donc libéral et démocrate comme lui.",
         legD="Améliorer peu à peu la démocratie libérale, ou passer au parti unique. L'union des socialistes avec le PC finirait, selon lui, par une rupture ou par la dérive.",
         texte="Peut-on se définir d'abord négativement, comme anti-révolutionnaire ? Oui, répond Aron. Reprenant une formule de Malraux, il estime que la droite traditionnelle, celle qui refusait la société moderne, le développement économique et les institutions démocratiques, n'existe plus : on est révolutionnaire ou anti-révolutionnaire, et dans ce second cas libéral et démocrate. En Europe de l'Ouest, la question fondamentale est donc de savoir si l'on améliore progressivement les régimes démocratiques et libéraux, ou si on leur substitue un régime de parti unique avec gestion intégrale de l'économie. Il dit estimer des socialistes comme Michel Rocard ou Jacques Attali, qui croient pouvoir transformer l'économie sans tomber dans le totalitarisme. Mais il juge leur alliance avec le Parti communiste non viable : elle aboutirait soit à une rupture et à un retour à la démocratie libérale, soit à une dérive vers un régime plus ou moins totalitaire. Il ne doute pas qu'ils choisiraient la liberté, mais préférerait qu'ils n'aient pas à choisir.",
         anim="Un point part du carrefour : un chemin vert monte vers la démocratie libérale améliorée pas à pas, un chemin rouge vers le parti unique. Le chemin du milieu, l'union de la gauche avec le PC, se sépare en deux : rupture (retour au vert) ou dérive (vers le rouge).",
         t=436),
    dict(slug='deux-totalitarismes', court='Deux régimes inhumains',
         parcours=['Deux régimes', 'inhumains'],
         titre="La plus grande hypocrisie du temps",
         sous="Le stalinisme présenté comme « de gauche », et sa comparaison avec le nazisme",
         legG="La plus grande hypocrisie, selon Aron : avoir présenté pendant des années le régime stalinien, qui supprimait les libertés et remplissait les camps, comme un régime de gauche.",
         legD="Pour lui, le nazisme fut inhumain à cause de ses idées (l'extermination), le stalinisme inhumain malgré les siennes : qui veut faire l'ange fait la bête.",
         texte="Pour Aron, la plus grande hypocrisie de son temps est d'avoir présenté pendant des années le régime stalinien comme un régime de gauche : des hommes qui se réclamaient de l'humanisme et de la liberté ont refusé de condamner un régime qui avait supprimé toutes les libertés et envoyé des millions de personnes dans des camps. Il distingue ensuite les deux totalitarismes. Le régime hitlérien a selon lui une « triste originalité » : avoir exterminé industriellement des millions d'êtres humains au nom d'une pensée biologique appliquée aux peuples, ce qu'il tient pour l'acte le plus monstrueux du siècle. Il était inhumain en fonction de ses idées ; le régime stalinien l'était contre et en dépit des siennes, mais il a infligé l'inhumanité à des dizaines de millions de personnes et s'y est installé durablement. Aron voit une petite ouverture dans le fait qu'après Staline le régime, toujours totalitaire, a renoncé aux formes extrêmes de violence et se réclame d'idées qui condamnent ses pratiques. Mais « qui veut faire l'ange fait la bête » : l'utopie d'une société sans classes, interprétée par les marxistes-léninistes, conduit à la toute-puissance du parti.",
         anim="Pour chaque régime, deux barres : les idées affichées et les pratiques. Pour le nazisme, elles vont dans le même sens. Pour le stalinisme, l'écart entre l'idéal affiché et les camps se creuse.",
         t=713),
    dict(slug='la-conscience-resiste', court='La conscience résiste',
         parcours=['La conscience', 'résiste'],
         titre="La conscience résiste à la pesanteur du régime",
         sous="Ce qui donne le plus d'espoir à Aron : la dissidence soviétique",
         legG="Son plus grand espoir : l'opposition libérale et religieuse en URSS, avec Sakharov et son courage tranquille, Soljenitsyne et ses livres.",
         legD="Il croit qu'il existe des millions de Soljenitsyne potentiels : les régimes despotiques durent, mais la conscience individuelle leur survit.",
         texte="Interrogé sur l'événement qui lui laisse le plus d'espoir, Aron répond, en se disant lui-même « obsédé », par la dissidence en Union soviétique : la persistance d'une opposition à la fois libérale et religieuse dans le monde communiste. Il cite Sakharov, dont il admire le « courage tranquille » à Moscou, et Soljenitsyne. Il recommande en particulier <i>Le Chêne et le Veau</i>, à la fois roman et témoignage : le combat d'un homme sorti des camps contre la bureaucratie d'État, avec le sens de ce qui est possible à chaque moment, et les choix permanents entre conscience et opportunité. Ce livre est pour lui un avertissement pour des sociétés toutes menacées par le totalitarisme, et un signe encourageant. Soljenitsyne est un génie littéraire unique, dit-il, mais tous les régimes autoritaires ou totalitaires, de droite comme de gauche, comptent des millions de Soljenitsyne potentiels. En libéral et en humaniste, il croit que la conscience humaine résiste à la violence et que, même si les régimes despotiques durent, elle leur survit.",
         anim="Sous le bloc sombre du régime, de petites lumières (les consciences) continuent de briller et de pulser ; deux d'entre elles portent les noms de Sakharov et de Soljenitsyne.",
         t=1153),
]

CHAPITRES = [
    (0, "La vérité qui gêne", "La politique, pour conquérir et exercer le pouvoir, est au mieux amorale et souvent immorale : c'est pourquoi Aron se dit spectateur plutôt qu'acteur."),
    (64, "Pourquoi il n'est pas entré en politique", "Impatience, intolérance aux imbéciles, refus d'être « conseiller du prince » ; il ne pourrait pas ordonner des bombardements puis dormir paisiblement, comme certains de ses amis de Harvard."),
    (182, "La vie sociale et l'autorité", "Bonnes relations avec ses étudiants, gauchistes compris ; l'autorité nécessaire en politique, détestée à titre personnel."),
    (268, "Adversaires et non-conformisme", "N'ayant jamais été acteur, il a critiqué tous les présidents et Premiers ministres, de Gaulle compris, qui le jugeaient « impossible »."),
    (323, "Anti-révolutionnaire et antitotalitaire", "Les révolutions coûtent cher ; son antitotalitarisme vient de l'Allemagne de 1931-1933, puis se tourne vers le stalinisme après 1945."),
    (436, "Révolution ou réforme", "La droite traditionnelle n'existe plus : on est révolutionnaire ou non. Rocard, Attali et l'union avec le Parti communiste : une combinaison qu'il juge non viable."),
    (579, "Sartre", "Amis à l'École normale, éloignés ensuite, séparés par la guerre froide. Aron met de côté le polémiste et admire le philosophe."),
    (713, "La plus grande hypocrisie : stalinisme et nazisme", "Le stalinisme présenté comme régime de gauche. Le nazisme inhumain par ses idées, le stalinisme malgré les siennes ; « qui veut faire l'ange fait la bête »."),
    (1153, "L'espoir : la dissidence soviétique", "Sakharov, Soljenitsyne et <i>Le Chêne et le Veau</i> ; des millions de Soljenitsyne potentiels ; la conscience survit aux régimes despotiques."),
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


def planche1():
    c = ''
    # deux mondes qui ne se rejoignent pas
    c += '<g><animateTransform attributeName="transform" type="translate" values="0 0;-30 0;0 0" dur="6s" repeatCount="indefinite"/>'
    c += disque(420, 330, 120, VERT) + lignes(420, 300, ['Les relations', 'humaines', "qu'il aime"], 22, VERT, h=30, weight='600') + '</g>'
    c += '<g><animateTransform attributeName="transform" type="translate" values="0 0;30 0;0 0" dur="6s" repeatCount="indefinite"/>'
    c += disque(860, 330, 120, ROUGE) + lignes(860, 300, ['La politique :', 'conquérir et', 'exercer le pouvoir'], 22, ROUGE, h=30, weight='600') + '</g>'
    c += '<path d="M640 200 l-14 40 l22 30 l-20 36 l18 34 l-16 40 l10 70" fill="none" stroke="%s" stroke-width="3" filter="url(#glow)"><animate attributeName="stroke-opacity" values="1;.4;1" dur="3s" repeatCount="indefinite"/></path>' % OR
    c += txt(640, 192, 'Incompatibilité radicale', 18, OR, weight='600')
    c += txt(860, 480, 'au mieux amorale, souvent immorale', 17, ROUGE)
    # l'œil du spectateur
    c += '<path d="M90 230 Q140 190 190 230 Q140 270 90 230Z" fill="none" stroke="%s" stroke-width="2.5"/><circle cx="140" cy="230" r="12" fill="%s"><animate attributeName="cx" values="132;148;132" dur="4s" repeatCount="indefinite"/></circle>' % (CYAN, CYAN)
    c += txt(140, 290, 'Spectateur', 18, CYAN, weight='600') + txt(140, 312, 'plutôt qu\'acteur', 16, CYAN)
    c += chips([('Impatience', OR), ('Supporte mal les imbéciles', OR), ("Ne pourrait ordonner la violence puis dormir", ROUGE)], 520)
    e = ETAPES[0]
    return base(1, e['titre'], e['sous'], c, e['legG'], e['legD'])


def planche2():
    c = ''
    # balance
    c += boite(60, 180, 560, 370, BLEU, '.05') + txt(340, 214, "L'autorité", 21, BLEU, weight='600')
    c += '<path d="M340 470 L340 270 M300 470 H380" stroke="%s" stroke-width="3"/>' % GRIS
    c += '<g><animateTransform attributeName="transform" type="rotate" values="-10 340 270;10 340 270;-10 340 270" dur="7s" repeatCount="indefinite"/>'
    c += '<line x1="170" y1="270" x2="510" y2="270" stroke="%s" stroke-width="4"/>' % GRIS
    for cx, col, ls in [(170, VERT, ['En politique :', 'nécessaire']), (510, ROUGE, ['Pour lui-même :', 'détestée'])]:
        c += '<line x1="%d" y1="270" x2="%d" y2="330" stroke="%s" stroke-width="2"/>' % (cx, cx, GRIS)
        c += '<path d="M%d 330 h120 l-20 24 h-80z" fill="%s" fill-opacity=".2" stroke="%s" stroke-width="2"/>' % (cx - 60, col, col)
        c += lignes(cx, 390, ls, 18, col, h=24, weight='600')
    c += '</g>'
    c += lignes(340, 500, ["Il laisse ses étudiants choisir", "leur sujet de thèse"], 16, GRIS, h=21)
    # Sartre
    c += boite(660, 180, 560, 370, OR, '.05') + txt(940, 214, 'Sartre, de l\'ami au polémiste', 21, OR, weight='600')
    jal = [(700, 'École', 'normale', VERT), (830, 'Distance', 'amicale', CYAN), (960, 'Guerre', 'froide', BLEU), (1090, '1968 :', 'polémique', ROUGE)]
    c += '<line x1="700" y1="300" x2="1170" y2="300" stroke="%s" stroke-opacity=".5" stroke-width="3"/>' % GRIS
    for x, l1, l2, col in jal:
        c += '<circle cx="%d" cy="300" r="10" fill="#0e1228" stroke="%s" stroke-width="3"/>' % (x + 20, col)
        c += txt(x + 20, 345, l1, 17, col, weight='600') + txt(x + 20, 367, l2, 17, col, weight='600')
    c += '<circle r="8" fill="%s" filter="url(#glow)"><animateMotion dur="7s" repeatCount="indefinite" path="M720 300 H1110"/></circle>' % OR
    c += lignes(940, 430, ["Le polémiste « dans un petit coin »,", 'le philosophe toujours admiré'], 18, TEXTE, h=26)
    c += txt(940, 515, 'Critique de tous les dirigeants, de Gaulle compris', 16, GRIS)
    e = ETAPES[1]
    return base(2, e['titre'], e['sous'], c, e['legG'], e['legD'])


def planche3():
    c = ''
    pts = [(160, '1931-1933', ['En Allemagne :', 'montée du', 'nazisme'], ROUGE),
           (450, '1933-1939', ["« Dans l'attente", 'de la catastrophe »', 'premiers livres'], OR),
           (740, 'Après 1945', ['La « fureur', 'antitotalitaire »', 'vise le stalinisme'], BLEU),
           (1030, 'XXe congrès', ['Khrouchtchev dit', 'le double de ce', "qu'écrivait Aron"], VERT)]
    c += '<path d="M160 260 H1030" stroke="%s" stroke-width="3" stroke-opacity=".5" filter="url(#glow)"/>' % CYAN
    c += '<circle r="10" fill="%s" filter="url(#glow)"><animateMotion dur="8s" repeatCount="indefinite" path="M160 260 H1030"/></circle>' % OR
    for x, date, ls, col in pts:
        c += '<circle cx="%d" cy="260" r="16" fill="#0e1228" stroke="%s" stroke-width="3"/>' % (x, col)
        c += txt(x, 225, date, 20, col, weight='600')
        c += boite(x - 115, 300, 230, 110, col, '.08')
        c += lignes(x, 334, ls, 18, TEXTE, h=26)
    c += boite(240, 440, 800, 110, ROUGE, '.06')
    c += txt(640, 474, 'Les révolutions, selon Aron', 19, ROUGE, weight='600')
    c += lignes(640, 504, ["coûtent très cher, font plus de mal que de bien :", "elles suppriment certains maux et en créent d'autres"], 17, TEXTE, h=23)
    e = ETAPES[2]
    return base(3, e['titre'], e['sous'], c, e['legG'], e['legD'])


def planche4():
    c = ''
    dep = (160, 400)
    vert = 'M160 400 C320 400 360 230 560 230 H1050'
    rouge = 'M160 400 C320 400 360 520 560 520 H1050'
    milieu = 'M160 400 H700'
    c += '<path d="%s" fill="none" stroke="%s" stroke-width="4"/>' % (vert, VERT)
    c += '<path d="%s" fill="none" stroke="%s" stroke-width="4"/>' % (rouge, ROUGE)
    c += '<path d="%s" fill="none" stroke="%s" stroke-width="3" stroke-dasharray="10 8"/>' % (milieu, OR)
    c += '<path d="M700 400 C780 400 800 230 900 230" fill="none" stroke="%s" stroke-width="2.5" stroke-dasharray="8 6" marker-end="url(#fl)"/>' % VERT
    c += '<path d="M700 400 C780 400 800 520 900 520" fill="none" stroke="%s" stroke-width="2.5" stroke-dasharray="8 6" marker-end="url(#fl)"/>' % ROUGE
    c += disque(dep[0], dep[1], 30, CYAN) + txt(160, 460, 'Europe de', 16, CYAN) + txt(160, 480, "l'Ouest, 1975", 16, CYAN)
    c += boite(1060, 190, 190, 84, VERT, '.12') + lignes(1155, 222, ['Démocratie libérale', 'améliorée pas à pas'], 17, VERT, h=24, weight='600')
    c += boite(1060, 478, 190, 84, ROUGE, '.12') + lignes(1155, 510, ['Parti unique,', 'économie dirigée'], 17, ROUGE, h=24, weight='600')
    c += txt(560, 385, 'Union de la gauche avec le PC', 17, OR, weight='600')
    c += txt(560, 430, '(Rocard, Attali : estimés, mais', 15, OR) + txt(560, 450, 'combinaison jugée non viable)', 15, OR)
    c += txt(860, 320, 'Rupture', 16, VERT, 'start', '600') + txt(860, 488, 'Dérive', 16, ROUGE, 'start', '600')
    for k, (chemin, col) in enumerate([(vert, VERT), (rouge, ROUGE), (milieu + ' C780 400 800 230 900 230', OR), (milieu + ' C780 400 800 520 900 520', OR)]):
        c += '<circle r="8" fill="%s" filter="url(#glow)"><animateMotion dur="6s" begin="%.1fs" repeatCount="indefinite" path="%s"/></circle>' % (col, k * 1.5, chemin)
    c += txt(450, 210, 'Anti-révolutionnaire = libéral et démocrate', 17, VERT, weight='600')
    e = ETAPES[3]
    return base(4, e['titre'], e['sous'], c, e['legG'], e['legD'])


def planche5():
    c = ''
    cols = [(70, 'Régime hitlérien', ROUGE, "inhumain en fonction de ses idées", ['Idées : une pensée', 'biologique appliquée', 'aux peuples'], ['Pratique :', 'extermination', 'industrielle'], False),
            (660, 'Régime stalinien', BLEU, 'inhumain contre et malgré ses idées', ['Idées affichées :', 'humanisme, liberté,', 'peuple'], ['Pratique : libertés', 'supprimées, millions', 'de détenus'], True)]
    for x, nom, col, sous, idees, prat, ecart in cols:
        c += boite(x, 180, 550, 330, col, '.06')
        c += txt(x + 275, 214, nom, 22, col, weight='600') + txt(x + 275, 240, sous, 17, TEXTE)
        c += txt(x + 40, 290, 'Idées', 17, GRIS, 'start', '600') + txt(x + 40, 400, 'Pratiques', 17, GRIS, 'start', '600')
        c += '<rect x="%d" y="300" width="220" height="20" rx="6" fill="%s" fill-opacity=".7"/>' % (x + 40, ROUGE if not ecart else VERT)
        c += lignes(x + 290, 296, idees, 15, TEXTE, 'start', h=19)
        if not ecart:
            c += '<rect x="%d" y="410" width="220" height="20" rx="6" fill="%s" fill-opacity=".7"/>' % (x + 40, ROUGE)
            c += '<path d="M%d 330 V400" stroke="%s" stroke-width="2.5" marker-end="url(#fl)"/>' % (x + 150, ROUGE)
            c += txt(x + 275, 470, 'Les deux vont dans le même sens', 17, ROUGE, weight='600')
        else:
            c += ('<rect x="%d" y="410" width="220" height="20" rx="6" fill="%s" fill-opacity=".7">'
                  '<animate attributeName="x" values="%d;%d;%d" dur="7s" repeatCount="indefinite"/></rect>') % (x + 40, ROUGE, x + 40, x + 60, x + 40)
            c += '<path d="M%d 330 V400" stroke="%s" stroke-width="2.5" stroke-dasharray="6 6"/>' % (x + 150, GRIS)
            c += txt(x + 275, 470, "L'écart entre l'idéal et les camps", 17, BLEU, weight='600')
        c += lignes(x + 290, 406, prat, 15, TEXTE, 'start', h=19)
    c += txt(640, 545, "« Qui veut faire l'ange fait la bête » : l'utopie sans classes mène au parti tout-puissant", 17, OR, extra=' font-style="italic"')
    e = ETAPES[4]
    return base(5, e['titre'], e['sous'], c, e['legG'], e['legD'])


def planche6():
    c = ''
    c += '<rect x="300" y="180" width="680" height="190" rx="10" fill="#2a2f4a" stroke="%s" stroke-opacity=".5"/>' % GRIS
    c += txt(640, 255, 'Régime autoritaire ou totalitaire', 24, GRIS, weight='600') + txt(640, 290, '(de droite comme de gauche)', 18, GRIS)
    c += txt(640, 335, 'bureaucratie, violence, pesanteur', 17, GRIS, extra=' font-style="italic"')
    c += '<path d="M640 372 v30" stroke="%s" stroke-width="3" marker-end="url(#fl)"/>' % GRIS
    rnd = random.Random(6)
    for k in range(26):
        x, y = 140 + k * 39 + rnd.randint(-6, 6), 450 + rnd.randint(-14, 14)
        if min(abs(x - 330), abs(x - 950)) < 36:
            continue
        d = 2 + rnd.random() * 2.5
        c += ('<circle cx="%d" cy="%d" r="6" fill="%s" filter="url(#glow)"><animate attributeName="r" values="4;8;4" dur="%.1fs" repeatCount="indefinite"/>'
              '<animate attributeName="fill-opacity" values=".5;1;.5" dur="%.1fs" repeatCount="indefinite"/></circle>') % (x, y, OR, d, d)
    for x, nom, sous in [(330, 'Sakharov', 'courage tranquille'), (950, 'Soljenitsyne', 'Le Chêne et le Veau')]:
        c += disque(x, 450, 20, VERT)
        c += txt(x, 505, nom, 20, VERT, weight='600') + txt(x, 528, sous, 16, VERT, extra=' font-style="italic"' if 'Chêne' in sous else '')
    c += txt(640, 535, 'Des millions de « Soljenitsyne potentiels »', 18, OR, weight='600')
    c += txt(160, 240, 'Les régimes', 17, ROUGE, weight='600') + txt(160, 262, 'durent...', 17, ROUGE)
    c += txt(1120, 240, '...la conscience', 17, VERT, weight='600') + txt(1120, 262, 'leur survit', 17, VERT)
    e = ETAPES[5]
    return base(6, e['titre'], e['sous'], c, e['legG'], e['legD'])


def icone(k, x, y):
    if k == 1:
        return disque(x - 22, y, 22, VERT) + disque(x + 22, y, 22, ROUGE)
    if k == 2:
        return ('<path d="M%d %d H%d M%d %d V%d" stroke="%s" stroke-width="3"/>' % (x - 40, y - 12, x + 40, x, y - 12, y + 28, GRIS)
                + '<path d="M%d %d h30 l-6 10 h-18z" fill="%s" fill-opacity=".4" stroke="%s"/>' % (x - 55, y - 2, VERT, VERT)
                + '<path d="M%d %d h30 l-6 10 h-18z" fill="%s" fill-opacity=".4" stroke="%s"/>' % (x + 25, y - 2, ROUGE, ROUGE))
    if k == 3:
        return ''.join('<circle cx="%d" cy="%d" r="8" fill="%s"/>' % (x - 45 + i * 30, y, col) for i, col in enumerate([ROUGE, OR, BLEU, VERT])) + \
            '<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-opacity=".5" stroke-width="2"/>' % (x - 45, y, x + 45, y, CYAN)
    if k == 4:
        return ('<path d="M%d %d C%d %d %d %d %d %d" fill="none" stroke="%s" stroke-width="3"/>' % (x - 45, y + 10, x - 10, y + 10, x, y - 25, x + 45, y - 25, VERT)
                + '<path d="M%d %d C%d %d %d %d %d %d" fill="none" stroke="%s" stroke-width="3"/>' % (x - 45, y + 10, x - 10, y + 10, x, y + 35, x + 45, y + 35, ROUGE))
    if k == 5:
        return ('<rect x="%d" y="%d" width="40" height="8" fill="%s"/><rect x="%d" y="%d" width="40" height="8" fill="%s"/>' % (x - 50, y - 15, ROUGE, x - 50, y + 10, ROUGE)
                + '<rect x="%d" y="%d" width="40" height="8" fill="%s"/><rect x="%d" y="%d" width="40" height="8" fill="%s"/>' % (x + 10, y - 15, VERT, x + 18, y + 10, ROUGE))
    return ('<rect x="%d" y="%d" width="100" height="30" rx="4" fill="#2a2f4a" stroke="%s"/>' % (x - 50, y - 30, GRIS)
            + ''.join('<circle cx="%d" cy="%d" r="4" fill="%s"><animate attributeName="fill-opacity" values=".4;1;.4" dur="%ds" repeatCount="indefinite"/></circle>' % (x - 40 + i * 20, y + 20, OR, 2 + i % 3) for i in range(5)))


def parcours():
    s = ouvrir("Parcours : Raymond Aron face aux totalitarismes, en six étapes") + etoiles(10)
    s += txt(640, 92, "Raymond Aron, 1975 : la politique, la violence et la liberté", 38, TEXTE, weight='600', family=SERIF)
    s += txt(640, 130, "Le raisonnement de l'entretien en six étapes, de sa place en marge de la politique à l'espoir", 19, CYAN)
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
                          "passent à l'étape précédente ou suivante. La fiche explique chaque étape et donne les parties de la vidéo",
                          "(entretien avec Jacques Paugam, émission Parti pris, France Culture, 1975)."], 17, TEXTE, 'start', h=24)
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
    return ('<!DOCTYPE html>\n<html lang="fr">\n<head>\n<meta charset="utf-8">\n<script src="https://mikhub-dev.github.io/RoutineSite/famzak-verrou.js"></script>\n<meta name="viewport" content="width=device-width,initial-scale=1">\n'
            '<title>%s</title>\n<meta name="description" content="%s">\n<meta name="robots" content="noindex, nofollow">\n'
            '<link rel="preconnect" href="https://fonts.googleapis.com">\n<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
            '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Jost:wght@400;500;600&family=Spectral:ital,wght@0,400;0,500;0,600;1,400&family=Inter:wght@400;500;700&display=swap">\n'
            '<link rel="stylesheet" href="frise.css">\n</head>\n<body%s>\n%s%s%s</body>\n</html>\n'
            % (esc(titre), esc(desc), ' class="%s"' % classe if classe else '', entete(), corps, script))


TITRE = "Raymond Aron face aux totalitarismes"
DESC = "Fiche vidéo (France Culture, 1975) : Raymond Aron dit la politique amorale, explique son antitotalitarisme, compare nazisme et stalinisme et place son espoir dans la dissidence soviétique."

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
             '<div class="badges"><span class="b">YouTube</span><span class="b">Archive radio, 1975</span><span class="b b-lu">Lu en entier</span></div>\n'
             '<h1>Vidéo : « Raymond Aron, entretien (Parti pris) : la politique est amorale et immorale »</h1>\n'
             '<p class="meta">Chaîne Artesquieu · 23 min 30 s · mise en ligne le 9 juin 2022 · entretien avec Jacques Paugam, émission <i>Parti pris</i>, France Culture (1975 selon la description) · en français · transcription automatique lue en entier · pas de chapitres : découpage proposé en %d parties</p>\n'
             '<p class="actions"><a class="bouton" href="%s" target="_blank" rel="noopener">Voir sur YouTube</a><a class="bouton bouton-2" href="%s.html">Parcours en %d étapes</a></p>\n</div>\n' % (len(CHAPITRES), yt, SUJET, N))
    h.append('<article class="fiche" id="synthese">\n<h3>Synthèse et conclusion</h3>\n<h4>Synthèse</h4>\n'
             '<p>Dans cet entretien radiophonique, Jacques Paugam pose à Raymond Aron une série de questions personnelles : la vérité qui le gêne, ses adversaires, la plus grande hypocrisie de son temps, ce qui lui donne de l\'espoir. Aron y dessine son autoportrait politique. Il dit la politique amorale et souvent immorale, et explique ainsi qu\'il soit resté spectateur plutôt qu\'acteur. Il se définit comme anti-révolutionnaire et surtout antitotalitaire, conviction née en Allemagne au moment de la montée du nazisme, puis tournée vers le stalinisme.</p>\n'
             '<p>Sa thèse : en Europe de l\'Ouest, le vrai choix oppose l\'amélioration progressive de la démocratie libérale au parti unique. Il juge que la gauche s\'est longtemps aveuglée sur le stalinisme, et distingue deux totalitarismes : le nazisme, inhumain à cause de ses idées, et le stalinisme, inhumain malgré les siennes.</p>\n'
             '<h4>Conclusion</h4>\n'
             '<p>Son espoir vient de la dissidence soviétique, de Sakharov et de Soljenitsyne. En libéral et en humaniste, il conclut que la conscience individuelle résiste à la violence de l\'État et survit même aux régimes despotiques, qui pourtant durent.</p>\n'
             '<p class="note"><b>Voir aussi.</b> Du même Aron, deux ans plus tôt, la fiche <a href="aron-europe-fiche.html">Raymond Aron et l\'Europe protégée</a> (1973).</p>\n</article>\n')
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
             '<p class="note">C\'est un entretien d\'opinion de 1975, mis en ligne par une chaîne qui n\'est pas l\'éditeur d\'origine ; la date et l\'émission viennent de la description, je ne les ai pas vérifiées. Aron y donne son point de vue personnel, sans contradicteur, sur des sujets lourds (nazisme, stalinisme, union de la gauche). Sa comparaison des deux régimes et ses ordres de grandeur, par exemple le nombre de détenus dans les camps allemands et soviétiques au milieu des années 1930, sont rapportés comme il les donne et ne sont pas vérifiés ici. Ses pronostics sur l\'union de la gauche sont ceux de 1975.</p>\n'
             '<p class="note">La transcription est automatique, sans ponctuation, et déforme beaucoup de noms. J\'ai lu « seul génie tsin » et « soljénitsyne » comme Soljenitsyne, « l\'archipel bull hague » et « gulak » comme <i>L\'Archipel du Goulag</i>, « le chêne elle vaut » comme <i>Le Chêne et le Veau</i>, « où 14 » comme <i>Août 14</i>, « paix et guerre » comme <i>Guerre et Paix</i>, « heatley » comme Hitler, « phénologie » comme phénoménologie, « styles et tziganes » comme Slaves et Tziganes. Le passage sur le « conseiller du prince » cite un homme d\'État américain dont le nom est illisible (sans doute Kissinger) : je ne l\'ai pas nommé dans la fiche.</p>\n</article>\n')
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
