# -*- coding: utf-8 -*-
"""Génère la fiche vidéo « Raymond Aron, philosophie et histoire » (Géopolitique) :
cours de la Sorbonne 1963-1964 (cinq leçons), parcours SVG, une planche SVG animée par étape,
pages HTML (parcours, planches, fiche).
Même modèle que outils/aron_europe.py (dont les fonctions communes sont reprises).
Lancer depuis la racine du dépôt : python3 -I outils/aron_histoire.py
"""
import os, random, html, math

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOSSIER = os.path.join(RACINE, 'fiches-geopolitique')
SUJET = 'aron-histoire'
IMG = os.path.join(DOSSIER, 'images', SUJET)
VID = '_5M_eaFbPTA'

OR, CYAN, ROUGE, VERT, BLEU, GRIS = '#f2b84b', '#5ad1e6', '#ff6b7a', '#7ee0a0', '#7aa2ff', '#9fb3d6'
TEXTE = '#e6eefc'
SERIF = "Spectral, Georgia, 'Times New Roman', serif"
SANS = "Jost, 'Segoe UI', system-ui, sans-serif"

# ---------------------------------------------------------------- contenu
ETAPES = [
    dict(slug='hegel-et-ses-heritiers', court='Hegel et ses héritiers',
         parcours=['Hegel et', 'ses héritiers'],
         titre="L'histoire a-t-elle un sens ?",
         sous="Entre Burckhardt et Croce, Hegel et ses trois héritiers",
         legG="Pour Burckhardt, philosophie et histoire s'excluent ; pour Croce, l'histoire est la philosophie. Deux réactions à Hegel, pour qui l'histoire est la raison qui se réalise.",
         legD="Ses héritiers : le marxisme (une fin, la société sans classes), l'historicisme (pas de fin), l'existentialisme (la conscience seule). Ou le « récit d'un idiot » de Shakespeare ?",
         texte="Aron ouvre le cycle par deux formules extrêmes. Pour l'historien suisse Jacob Burckhardt, philosophie et histoire sont incompatibles : le philosophe cherche ce qui vaut toujours, l'historien ce qu'on ne verra jamais deux fois. Pour l'Italien Benedetto Croce, au contraire, l'histoire est la philosophie. Aron y voit deux réactions à Hegel, chez qui la suite des concepts épouse la suite des temps historiques : l'histoire est la raison qui se réalise. De Hegel descendent trois courants. Le marxisme garde l'idée d'une histoire rationnelle, mais en fait une dialectique des régimes économiques qui aboutit à la société sans classes. L'historicisme supprime la fin : les époques et les cultures se juxtaposent, et l'on aboutit au relativisme intégral. L'existentialisme de Heidegger et de Sartre part au contraire de la conscience solitaire et nie la totalité historique (« l'homme est une passion inutile ») ; Sartre et Merleau-Ponty ont ensuite tenté de le marier au marxisme. D'où la question qui traverse le cours : l'histoire a-t-elle un sens, ou n'est-elle, comme dans <i>Macbeth</i>, qu'« une histoire racontée par un idiot, pleine de bruit et de fureur, et qui ne signifie rien » ? Il distingue enfin deux domaines classiques, la critique de la connaissance historique (épistémologie) et la philosophie globale de l'histoire (Bossuet, Comte, Marx), avec des zones intermédiaires entre elles et, au-dessus, une théologie ou une métaphysique de l'histoire.",
         anim="Au centre, Hegel ; à gauche et à droite, les deux formules extrêmes. Trois branches descendent vers le marxisme, l'historicisme et l'existentialisme, puis une balance oscille entre « sens » et « non-sens ».",
         t=0),
    dict(slug='trente-ans-apres', court='Trente ans après',
         parcours=['Trente ans', 'après'],
         titre="Des années 1930 aux années 1960",
         sous="Comment la question a changé entre la thèse d'Aron et ce cours",
         legG="Vers 1930, élève de Brunschvicg, Aron écrit sa thèse sur les limites de l'objectivité historique, dans une Allemagne doublement historiciste, en philosophie et en politique.",
         legD="En 1963, l'histoire est devenue planétaire. Après le débat de 1945-1956 avec Sartre et Merleau-Ponty, on compare les régimes concrètement ; reste la question de la totalisation.",
         texte="Aron revient sur son propre parcours, une trentaine d'années plus tôt. Élève de Léon Brunschvicg, philosophe néo-kantien pour qui la philosophie était réflexion sur les sciences, il a choisi de réfléchir non sur les mathématiques ou la physique mais sur la connaissance historique : sa thèse, <i>Introduction à la philosophie de l'histoire</i>, porte sur les limites de l'objectivité historique et fixe la frontière entre ce que la science établit et ce qui relève de la décision et de l'engagement. Elle s'accompagnait d'un livre sur les philosophes allemands de l'histoire (Dilthey, Rickert, Simmel, Weber). Ce choix tenait aussi à l'époque : l'Allemagne d'avant Hitler était doublement historiciste, en philosophie et en politique, chaque parti y portant sa vision du monde. Trente ans plus tard, la situation a changé. L'histoire est devenue planétaire : des cultures très diverses emploient le même vocabulaire (démocratie, développement) et le monde est coupé entre soviétiques et occidentaux. En France, de 1945 à 1956, le débat a opposé les marxistes orthodoxes, les marxistes existentialistes (Sartre, Merleau-Ponty) et les critiques des uns et des autres, dont Aron, autour de la totalisation, c'est-à-dire la saisie d'une période dans son unité et par rapport à une fin. Aujourd'hui, dit-il, on compare plutôt les régimes de façon pragmatique ; le problème philosophique qui demeure est celui de la totalisation historique. Au début du deuxième cours, il ajoute que le « cercle historiciste » (l'historien est lui-même dans l'histoire) n'est pas un cercle vicieux, et que les sciences sociales, la linguistique structurale ou la macroéconomie ont depuis renouvelé le paysage.",
         anim="Un point lumineux suit la frise : Brunschvicg et la thèse, l'Allemagne doublement historiciste, le débat de l'après-guerre, puis le monde planétaire de 1963.",
         t=1866),
    dict(slug='reconstruire', court='Reconstruire, pas reproduire',
         parcours=['Reconstruire,', 'pas reproduire'],
         titre="L'histoire reconstruit, elle ne reproduit pas",
         sous="Rickert, Dilthey et Max Weber : d'où vient l'originalité de la connaissance historique",
         legG="On ne retrouve jamais le passé « tel qu'il s'est réellement passé » (Ranke). Rickert : l'esprit choisit le singulier selon des valeurs. Dilthey : l'objet est humain, on le comprend.",
         legD="Weber concilie les deux : l'historien choisit librement son objet, puis la preuve causale doit valoir pour tous. Et la part du jugement varie selon l'objet étudié.",
         texte="Le deuxième cours pose les bases de la philosophie critique de l'histoire. La connaissance historique est une reconstruction, pas une reproduction : la formule de Ranke, raconter le passé « tel qu'il s'est réellement passé », est un idéal qu'on n'atteint jamais. Deux philosophes allemands expliquent cette originalité de deux manières. Pour Heinrich Rickert, elle tient à l'orientation de l'esprit : l'historien s'intéresse au singulier et à l'unique, et choisit ce qui compte par référence à des valeurs. Mais, objecte Aron, ces valeurs ne sont pas universelles, et la matière historique est déjà structurée avant l'historien. Pour Wilhelm Dilthey, elle tient à l'objet : les sciences de l'esprit portent sur des êtres humains, que l'on peut comprendre de l'intérieur ; Aron distingue la compréhension psychologique (Jaspers, la psychanalyse), celle des œuvres et la compréhension historique d'ensemble. Max Weber réconcilie l'homme d'action et le savant : le choix de l'objet est libre, mais la démonstration causale doit être objective. Aron ajoute que la subjectivité change selon l'objet : une personne (la biographie, comme un peintre devant son modèle), une œuvre d'art ou de pensée (on ne la comprend pas sans la juger) ou une époque entière (le poids donné à l'économie, à l'art…). C'est pourquoi il ne croit pas à une « critique de la raison historique » transcendantale au sens de Kant, ni chez Dilthey ou Rickert ni dans la <i>Critique de la raison dialectique</i> de Sartre.",
         anim="La formule de Ranke se barre. Deux chemins partent ensuite, Rickert (l'esprit qui choisit) et Dilthey (l'objet qu'on comprend), et se rejoignent chez Weber. En bas, les trois objets de l'historien apparaissent un à un.",
         t=3397),
    dict(slug='quatre-plans', court="Quatre plans et Thucydide",
         parcours=['Quatre plans', 'et Thucydide'],
         titre="Quatre plans et une histoire dramatique",
         sous="Raconter les événements, comprendre les autres, les œuvres, le sens du tout",
         legG="Quatre plans : le récit des événements, la compréhension des autres, l'histoire des œuvres de l'esprit, le sens global. Le premier est plein d'événements : les hommes naissent et meurent.",
         legD="Le récit est un « roman vrai ». Thucydide en est le modèle : la guerre est le personnage central, entre volonté et destin, décisions rationnelles et ensemble absurde.",
         texte="Au troisième cours, Aron distingue quatre plans de la connaissance historique : la reconstitution et le récit des événements ; la compréhension d'autrui et de la diversité humaine ; l'histoire des univers intellectuels (philosophie, art) ; enfin la totalisation, c'est-à-dire le sens de l'histoire. Il commence par l'événement, au sens large (tout ce qui est daté et situé) et au sens fort (ce qui surprend ou a des conséquences). L'histoire en est pleine pour trois raisons : les hommes naissent et meurent ; certains rôles sociaux donnent un poids énorme à une personnalité (il pense aux deux hommes qui peuvent, avec l'arme nucléaire, détruire des millions de vies en quelques minutes) ; la guerre et la révolution. Le récit historique est un « roman vrai », né du mythe mais interdit d'invention ; reste à savoir de qui l'on raconte l'histoire (l'humanité, ou la France comme une personne chez Michelet). On raconte par admiration du présent (Tite-Live), par nostalgie d'un passé meilleur, ou par curiosité pour le mécanisme : c'est l'histoire dramatique, pleine de bruit et de fureur, mais ni absurde ni fatale. Son modèle est Thucydide, chez qui la guerre du Péloponnèse est le personnage central. Aron y relève quatre tensions : la volonté contre le destin (Périclès et le roi de Sparte), Nicias qui ne méritait pas son sort, des décisions rationnelles qui produisent un ensemble absurde (la « montée aux extrêmes » de Clausewitz), la nécessité contre l'accident (Athènes prisonnière de son empire). Une histoire écrite pour être utile aux vivants.",
         anim="Quatre marches s'allument de bas en haut, du récit au sens de l'histoire. À droite, la guerre du Péloponnèse est au centre, et ses quatre tensions apparaissent une à une.",
         t=6765),
    dict(slug='pourquoi-1914', court='Pourquoi la guerre de 1914 ?',
         parcours=['Pourquoi', 'la guerre', 'de 1914 ?'],
         titre="Pourquoi la guerre de 1914 ?",
         sous="Un exemple pour montrer les limites de l'explication historique",
         legG="Juillet 1914 en trois phases. Personne ne voulait cette guerre générale, mais beaucoup s'y attendaient, et les alliances et les plans des états-majors ont joué comme des engrenages.",
         legD="Trois questions à ne pas mélanger : la légitimité, les intentions, les conséquences. Des principes d'incertitude, pas de relativité : l'objectivité reste un devoir.",
         texte="Le quatrième cours pose la question : pourquoi l'événement est-il arrivé ? Aron prend l'exemple des origines de la guerre de 1914, dont le traité de Versailles attribuait la responsabilité à l'Allemagne. Il découpe la crise en trois phases : de l'attentat de Sarajevo (28 juin) à l'ultimatum autrichien à la Serbie (23 juillet) ; jusqu'à la déclaration de guerre autrichienne et à la mobilisation russe (29-30 juillet) ; puis les déclarations de guerre. Il propose de distinguer trois questions : la légitimité diplomatique des actes ; les intentions et l'état d'esprit des acteurs ; leur responsabilité dans les conséquences probables. Ses constats : beaucoup s'attendaient à une guerre, mais personne ne voulait cette guerre générale ; la guerre n'a été criminalisée qu'après coup ; les acteurs collectifs sont pluriels ; et les mécanismes ont pesé, alliances et plans des états-majors (le tsar ne pouvait pas mobiliser partiellement, l'Allemagne avait un plan pour deux fronts). Il en tire trois « principes d'incertitude », sur la légitimité, sur les motivations et sur les conséquences, qui ne sont pas des principes de relativité. Il met en garde contre les généralisations : la politique qui aurait évité 1914 n'aurait pas évité 1939. Sur 1939, il discute <i>The Origins of the Second World War</i> d'A. J. P. Taylor, qui présentait Munich comme un triomphe de la morale britannique et lisait le rapport Hossbach comme une rêverie. La leçon : ne pas prendre la vérité d'une conjoncture unique pour une vérité générale (la course aux armements en 1914, le refus de réarmer avant 1939). Il revient enfin à Thucydide : la « cause la plus vraie » de la guerre est la puissance croissante d'Athènes qui inquiète Sparte.",
         anim="Un point parcourt juillet 1914, de Sarajevo aux déclarations de guerre. En dessous, les trois principes d'incertitude s'allument, et la phrase sur la « leçon de l'histoire » apparaît.",
         t=10322),
    dict(slug='que-se-serait-il-passe', court='Et si… ?',
         parcours=['Et si… ?'],
         titre="« Que se serait-il passé si… ? »",
         sous="Le détail et la conjoncture, et l'expérience mentale de Max Weber",
         legG="Micro-analyse : les décisions d'une quarantaine d'hommes. Macro-analyse : le rapport des forces, qui demande l'histoire économique et militaire. Une différence de degré, non de nature.",
         legD="Pour juger une cause, on imagine ce qui serait arrivé sans elle. C'est légitime : les acteurs eux-mêmes calculent des risques, et certaines situations sont instables.",
         texte="Le cinquième cours distingue la micro-analyse, qui suit les décisions d'une quarantaine d'hommes dans six chancelleries, et la macro-analyse, qui étudie la conjoncture et le rapport des forces. Ce n'est pas l'opposition entre histoire et sociologie : « il n'y a pas d'historien qui ne soit sociologue ». Thucydide consacre son premier livre à la macro-analyse et les sept autres au détail. Le rapport des forces demande l'histoire économique, sociale et militaire (Hans Delbrück, la Révolution française qui change la guerre) ; en 1914, les acteurs connaissaient les alliances mais pas la nature d'une guerre industrielle. Aron esquisse un « Thucydide » de 1870-1914 : la France qui n'accepte pas la perte de l'Alsace-Lorraine, l'alliance franco-russe face à une Allemagne montante, et le choix britannique, qu'il explique d'abord par la flotte allemande plutôt que par la rivalité économique (il cite <i>La Grande Illusion</i> de Norman Angell). La macro-analyse comporte plus d'interprétation, mais la différence est de degré, non de nature. Contre l'illusion rétrospective de fatalité (Bergson), il défend l'expérience mentale de Max Weber : pour mesurer le poids d'une cause, on se demande ce qui se serait passé sans elle, comme pour une voiture lancée à 150 km/h. Ce calcul rétrospectif de probabilité est légitime parce que les acteurs eux-mêmes calculent des risques (le débarquement en Afrique du Nord, MacArthur en Corée), parce que les situations sont stables ou instables (1848, la démission de Guizot), parce qu'il existe des points de non-retour, et parce que le rôle d'un individu compte plus ou moins selon la place qu'il occupe (Louis XVI, Napoléon).",
         anim="À gauche, une loupe passe du détail des décisions à la vue d'ensemble du rapport des forces. À droite, à partir d'un même carrefour, le chemin réel et les chemins possibles se séparent, chacun avec sa probabilité.",
         t=13823),
]

CHAPITRES = [
    (0, "Cours 1. Deux formules extrêmes", "Burckhardt (philosophie et histoire incompatibles) et Croce (l'histoire est philosophie), deux réactions à Hegel, pour qui l'histoire est la raison qui se réalise."),
    (449, "Les héritiers de Hegel", "Le marxisme, l'historicisme et l'existentialisme ; les tentatives de Sartre et de Merleau-Ponty pour unir existentialisme et marxisme."),
    (1068, "Sens ou non-sens", "Le récit « fait par un idiot » de Shakespeare contre l'histoire rationnelle de Hegel et de Marx."),
    (1175, "Les domaines de la philosophie de l'histoire", "Critique de la connaissance historique, philosophie globale (Bossuet, Comte, Marx), zones intermédiaires, théologie de l'histoire."),
    (1866, "Trente ans plus tôt", "Brunschvicg et le néo-kantisme, la thèse sur les limites de l'objectivité historique, les philosophes allemands de l'histoire."),
    (2303, "L'Allemagne des années 1930 et le monde de 1963", "Une Allemagne doublement historiciste ; une histoire devenue planétaire ; le débat de 1945-1956 sur la totalisation (à 47:14)."),
    (3397, "Cours 2 (9 décembre 1963). Reconstruire le passé", "Le cercle historiciste, les nouvelles sciences sociales, trois objets de l'historien, Rickert, Dilthey et Weber."),
    (6765, "Cours 3 (16 décembre 1963). Les quatre plans", "Pas de critique transcendantale de la raison historique ; l'événement, le récit comme « roman vrai », Thucydide."),
    (10322, "Cours 4 (13 janvier 1964). Pourquoi l'événement est-il arrivé ?", "Les origines de 1914, les trois principes d'incertitude, Taylor et 1939, la « cause la plus vraie » chez Thucydide."),
    (13823, "Cours 5 (20 janvier 1964). Micro et macro-analyse", "Le rapport des forces, un « Thucydide » de 1870-1914, l'expérience mentale de Max Weber et le calcul rétrospectif de probabilité."),
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


def planche1():
    c = ''
    # les deux formules extrêmes
    c += boite(50, 180, 250, 110, ROUGE, '.08') + txt(175, 212, 'Burckhardt', 20, ROUGE, weight='600')
    c += lignes(175, 240, ['philosophie et histoire', 'sont incompatibles'], 16, TEXTE, h=21)
    c += boite(980, 180, 250, 110, BLEU, '.08') + txt(1105, 212, 'Croce', 20, BLEU, weight='600')
    c += lignes(1105, 240, ["l'histoire est", 'la philosophie'], 16, TEXTE, h=21)
    c += '<path d="M300 235 H545" stroke="%s" stroke-width="2" stroke-dasharray="6 6" marker-end="url(#fl)"/>' % ROUGE
    c += '<path d="M980 235 H735" stroke="%s" stroke-width="2" stroke-dasharray="6 6" marker-end="url(#fl)"/>' % BLEU
    c += disque(640, 235, 62, OR, extra=' filter="url(#glow)"') + txt(640, 232, 'Hegel', 24, OR, weight='600', family=SERIF)
    c += lignes(640, 254, ["l'histoire, raison", 'qui se réalise'], 12, OR, h=15)
    # trois héritiers
    hs = [(250, 'Marxisme', VERT, ['une fin :', 'la société sans classes']),
          (640, 'Historicisme', CYAN, ['pas de fin :', 'tout est relatif']),
          (1030, 'Existentialisme', ROUGE, ['la conscience seule,', '« passion inutile »'])]
    for k, (x, nom, col, ls) in enumerate(hs):
        c += '<path d="M640 297 C640 330 %d 320 %d 350" fill="none" stroke="%s" stroke-width="2.5" opacity="0">%s</path>' % (x, x, col, apparait(0.05 + k * 0.12).replace('attributeName="opacity"', 'attributeName="opacity"'))
        c += '<g opacity="0">' + apparait(0.1 + k * 0.12) + boite(x - 135, 352, 270, 96, col, '.1')
        c += txt(x, 382, nom, 20, col, weight='600') + lignes(x, 408, ls, 16, TEXTE, h=21) + '</g>'
    # balance sens / non-sens
    c += '<g><animateTransform attributeName="transform" type="rotate" values="-6 640 500;6 640 500;-6 640 500" dur="7s" repeatCount="indefinite"/>'
    c += '<line x1="330" y1="500" x2="950" y2="500" stroke="%s" stroke-width="3"/>' % GRIS
    c += txt(330, 490, 'Un sens : Hegel, Marx', 17, VERT, weight='600')
    c += txt(950, 490, 'Un non-sens : Shakespeare', 17, ROUGE, weight='600') + '</g>'
    c += '<path d="M640 500 l-16 32 h32z" fill="%s" fill-opacity=".5"/>' % GRIS
    c += txt(640, 556, "« Un récit fait par un idiot, plein de bruit et de fureur, qui ne signifie rien »", 16, GRIS, extra=' font-style="italic"')
    e = ETAPES[0]
    return base(1, e['titre'], e['sous'], c, e['legG'], e['legD'])


def planche2():
    c = ''
    pts = [(170, 'Vers 1930', ['Élève de', 'Brunschvicg :', 'le néo-kantisme'], CYAN),
           (490, '1931-1933', ['Une Allemagne', '« doublement', 'historiciste »'], ROUGE),
           (810, '1945-1956', ['Débat avec Sartre', 'et Merleau-Ponty :', 'la totalisation'], OR),
           (1110, '1963', ['Une histoire', 'devenue', 'planétaire'], VERT)]
    c += '<path d="M170 250 H1110" stroke="%s" stroke-width="3" stroke-opacity=".5" filter="url(#glow)"/>' % CYAN
    c += '<circle r="10" fill="%s" filter="url(#glow)"><animateMotion dur="9s" repeatCount="indefinite" path="M170 250 H1110"/></circle>' % OR
    for x, date, ls, col in pts:
        c += '<circle cx="%d" cy="250" r="16" fill="#0e1228" stroke="%s" stroke-width="3"/>' % (x, col)
        c += txt(x, 216, date, 20, col, weight='600')
        c += boite(x - 125, 285, 250, 105, col, '.08')
        c += lignes(x, 318, ls, 18, TEXTE, h=25)
    # thèse
    c += boite(60, 418, 560, 140, CYAN, '.05')
    c += txt(340, 450, 'Sa thèse (1938)', 19, CYAN, weight='600')
    c += lignes(340, 478, ["Les limites de l'objectivité historique :", 'ce que la science établit, et ce qui', "relève de la décision et de l'engagement"], 16, TEXTE, h=22)
    # cercle historiciste
    c += boite(660, 418, 560, 140, OR, '.05')
    c += '<circle cx="740" cy="488" r="34" fill="none" stroke="%s" stroke-width="3" stroke-dasharray="150 64"><animateTransform attributeName="transform" type="rotate" values="0 740 488;360 740 488" dur="6s" repeatCount="indefinite"/></circle>' % OR
    c += txt(960, 450, 'Le « cercle historiciste »', 19, OR, weight='600')
    c += lignes(960, 478, ["L'historien est lui-même dans l'histoire :", "un cercle, mais pas un cercle vicieux", '(Sartre, Marx)'], 16, TEXTE, h=22)
    e = ETAPES[1]
    return base(2, e['titre'], e['sous'], c, e['legG'], e['legD'])


def planche3():
    c = ''
    # Ranke barré
    c += boite(60, 185, 330, 80, GRIS, '.06')
    c += lignes(225, 216, ['« Tel que cela s\'est', 'réellement passé » (Ranke)'], 17, GRIS, h=24, weight='600')
    c += '<line x1="80" y1="250" x2="370" y2="200" stroke="%s" stroke-width="4" stroke-dasharray="340" stroke-dashoffset="340"><animate attributeName="stroke-dashoffset" values="340;340;0;0;340" keyTimes="0;.1;.2;.92;1" dur="9s" repeatCount="indefinite"/></line>' % ROUGE
    c += txt(225, 292, 'Reproduire ? Non : reconstruire', 17, ROUGE, weight='600')
    # deux chemins vers Weber
    c += boite(470, 185, 330, 100, BLEU, '.1') + txt(635, 215, 'Rickert : l\'esprit', 20, BLEU, weight='600')
    c += lignes(635, 241, ['choisit le singulier', 'selon des valeurs'], 16, TEXTE, h=21)
    c += boite(470, 325, 330, 100, VERT, '.1') + txt(635, 355, 'Dilthey : l\'objet', 20, VERT, weight='600')
    c += lignes(635, 381, ["des humains, qu'on peut", "comprendre de l'intérieur"], 16, TEXTE, h=21)
    c += '<path d="M800 235 C860 235 860 305 905 305" fill="none" stroke="%s" stroke-width="2.5" marker-end="url(#fl)"/>' % BLEU
    c += '<path d="M800 375 C860 375 860 305 905 305" fill="none" stroke="%s" stroke-width="2.5" marker-end="url(#fl)"/>' % VERT
    for k, p in enumerate(['M800 235 C860 235 860 305 905 305', 'M800 375 C860 375 860 305 905 305']):
        c += '<circle r="6" fill="%s" filter="url(#glow)"><animateMotion dur="3s" begin="%ds" repeatCount="indefinite" path="%s"/></circle>' % (OR, k, p)
    c += boite(910, 245, 320, 120, OR, '.12') + txt(1070, 278, 'Max Weber', 21, OR, weight='600')
    c += lignes(1070, 306, ["choix libre de l'objet,", 'puis preuve causale', 'valable pour tous'], 16, TEXTE, h=21)
    c += lignes(225, 350, ['Les valeurs ne sont pas', 'universelles, et la matière', 'est déjà structurée'], 15, GRIS, h=20)
    c += txt(225, 330, "Limite de Rickert", 16, BLEU, weight='600')
    # trois objets
    c += txt(640, 470, "Trois objets, trois façons d'y mettre du sien", 18, CYAN, weight='600')
    c += chips([('Une personne : la biographie', VERT), ("Une œuvre : comprendre, c'est juger", OR), ('Une époque : quel poids à chaque domaine ?', BLEU)], 492, gap=22)
    c += txt(640, 556, 'Pas de « critique de la raison historique » transcendantale, au sens de Kant', 16, GRIS, extra=' font-style="italic"')
    e = ETAPES[2]
    return base(3, e['titre'], e['sous'], c, e['legG'], e['legD'])


def planche4():
    c = ''
    marches = [('1', "Récit des événements", VERT), ('2', "Comprendre les autres", CYAN), ('3', "Histoire des œuvres de l'esprit", BLEU), ('4', "Le sens de l'histoire", OR)]
    for k, (n, lab, col) in enumerate(marches):
        x, y = 60 + k * 70, 500 - k * 82
        c += '<g opacity="0">' + apparait(0.05 + k * 0.14)
        c += '<rect x="%d" y="%d" width="%d" height="64" rx="10" fill="%s" fill-opacity=".14" stroke="%s" stroke-width="2"/>' % (x, y, 560 - k * 70, col, col)
        c += disque(x + 34, y + 32, 20, col, n, 20) + txt(x + 70, y + 40, lab, 18, TEXTE, 'start', '600') + '</g>'
    c += txt(60, 215, 'Les quatre plans, du récit au sens', 21, OR, 'start', '600', SERIF)
    # Thucydide
    c += boite(670, 180, 560, 384, ROUGE, '.05')
    c += txt(950, 212, 'Thucydide : la guerre, personnage central', 19, ROUGE, weight='600')
    c += disque(950, 330, 52, ROUGE, extra=' filter="url(#glow)"') + lignes(950, 326, ['La guerre du', 'Péloponnèse'], 15, TEXTE, h=19, weight='600')
    ant = [(790, 262, ['Volonté', 'ou destin ?']), (1110, 262, ['Nicias, un sort', 'non mérité']),
           (790, 400, ['Décisions rationnelles,', 'ensemble absurde']), (1110, 400, ['Nécessité', 'ou accident ?'])]
    for k, (x, y, ls) in enumerate(ant):
        c += '<g opacity="0">' + apparait(0.15 + k * 0.15)
        c += '<line x1="950" y1="330" x2="%d" y2="%d" stroke="%s" stroke-opacity=".5" stroke-width="2"/>' % (x, y + 4, ROUGE)
        c += '<rect x="%d" y="%d" width="190" height="56" rx="10" fill="#0e1228" stroke="%s"/>' % (x - 95, y - 22, OR)
        c += lignes(x, y, ls, 15, OR, h=20, weight='600') + '</g>'
    c += lignes(950, 486, ['Le récit, un « roman vrai » : né du mythe,', "mais l'invention y est interdite"], 16, TEXTE, h=22)
    c += txt(950, 545, '« Bruit et fureur », mais ni absurde ni fatal', 16, GRIS, extra=' font-style="italic"')
    e = ETAPES[3]
    return base(4, e['titre'], e['sous'], c, e['legG'], e['legD'])


def planche5():
    c = ''
    jal = [(110, '28 juin', 'Sarajevo'), (430, '23 juillet', 'ultimatum à la Serbie'), (790, '29-30 juillet', 'mobilisation russe'), (1150, 'début août', 'déclarations de guerre')]
    c += '<path d="M110 250 H1150" stroke="%s" stroke-width="3" stroke-opacity=".5"/>' % CYAN
    for (x1, _, _), (x2, _, _), col, lab in zip(jal, jal[1:], [CYAN, OR, ROUGE], ['Phase 1', 'Phase 2', 'Phase 3']):
        c += '<path d="M%d 250 H%d" stroke="%s" stroke-width="5" stroke-opacity=".6"/>' % (x1 + 16, x2 - 16, col)
        c += txt((x1 + x2) // 2, 240, lab, 15, col, weight='600')
    c += '<circle r="10" fill="%s" filter="url(#glow)"><animateMotion dur="8s" repeatCount="indefinite" path="M110 250 H1150"/></circle>' % OR
    for x, d, l in jal:
        c += '<circle cx="%d" cy="250" r="14" fill="#0e1228" stroke="%s" stroke-width="3"/>' % (x, OR)
        c += txt(x, 290, d, 18, OR, weight='600') + txt(x, 312, l, 15, TEXTE)
    c += lignes(640, 350, ["Personne ne voulait cette guerre générale, mais beaucoup s'y attendaient ;", "les alliances et les plans des états-majors ont joué comme des engrenages."], 16, GRIS, h=22)
    c += txt(640, 412, "Trois principes d'incertitude (et non de relativité)", 19, CYAN, weight='600')
    pr = [(220, 'Légitimité', 'Qui était dans son droit ?', BLEU), (640, 'Intentions', 'Que voulaient-ils ?', VERT), (1060, 'Conséquences', 'Qui a pris quel risque ?', ROUGE)]
    for k, (x, t1, t2, col) in enumerate(pr):
        c += '<g opacity="0">' + apparait(0.1 + k * 0.15) + boite(x - 170, 428, 340, 72, col, '.12')
        c += txt(x, 458, t1, 19, col, weight='600') + txt(x, 484, t2, 16, TEXTE) + '</g>'
    c += txt(640, 545, "Leçon : ne pas prendre la vérité d'une conjoncture unique pour une vérité générale (1914 ≠ 1939)", 16, OR, extra=' font-style="italic"')
    e = ETAPES[4]
    return base(5, e['titre'], e['sous'], c, e['legG'], e['legD'])


def planche6():
    c = ''
    # micro / macro
    c += boite(50, 180, 470, 380, CYAN, '.05') + txt(285, 212, 'Micro et macro-analyse', 20, CYAN, weight='600')
    rnd = random.Random(16)
    for k in range(40):
        x, y = 90 + (k % 10) * 39 + rnd.randint(-5, 5), 250 + (k // 10) * 30 + rnd.randint(-4, 4)
        c += '<circle cx="%d" cy="%d" r="5" fill="%s" fill-opacity=".8"/>' % (x, y, BLEU)
    c += ('<g><animateTransform attributeName="transform" type="translate" values="0 0;250 60;0 0" dur="8s" repeatCount="indefinite"/>'
          '<circle cx="130" cy="270" r="40" fill="%s" fill-opacity=".08" stroke="%s" stroke-width="3"/><line x1="158" y1="298" x2="185" y2="325" stroke="%s" stroke-width="5"/></g>') % (OR, OR, OR)
    c += txt(285, 395, 'Une quarantaine de décideurs, six chancelleries', 15, TEXTE)
    c += '<rect x="90" y="420" width="390" height="24" rx="6" fill="%s" fill-opacity=".25"/>' % VERT
    c += '<rect x="90" y="420" width="230" height="24" rx="6" fill="%s" fill-opacity=".6"><animate attributeName="width" values="230;300;230" dur="7s" repeatCount="indefinite"/></rect>' % VERT
    c += txt(285, 470, 'Le rapport des forces : économie, armée, société', 15, TEXTE)
    c += lignes(285, 510, ['Une différence de degré,', 'non de nature'], 17, OR, h=23, weight='600')
    # Et si... ?
    c += boite(560, 180, 670, 380, OR, '.05') + txt(895, 212, 'L\'expérience mentale de Max Weber', 20, OR, weight='600')
    reel = 'M600 380 C700 380 740 300 840 300 H1080'
    alts = ['M600 380 C700 380 740 380 840 380 H1080', 'M600 380 C700 380 740 460 840 460 H1080']
    c += '<path d="%s" fill="none" stroke="%s" stroke-width="4"/>' % (reel, VERT)
    for p in alts:
        c += '<path d="%s" fill="none" stroke="%s" stroke-width="2.5" stroke-dasharray="8 7"/>' % (p, GRIS)
    c += disque(600, 380, 18, CYAN) + txt(600, 420, 'la cause', 15, CYAN, weight='600') + txt(600, 438, 'à juger', 15, CYAN, weight='600')
    for y, lab, prob, col in [(300, 'Ce qui est arrivé', '', VERT), (380, 'Sans la cause ?', 'probable', GRIS), (460, 'Autre possible', 'peu probable', GRIS)]:
        c += txt(1088, y + 6, lab, 16, col, 'start', '600')
        if prob:
            c += txt(960, y - 10, prob, 14, GRIS, extra=' font-style="italic"')
    for k, p in enumerate([reel] + alts):
        c += '<circle r="7" fill="%s" filter="url(#glow)"><animateMotion dur="5s" begin="%.1fs" repeatCount="indefinite" path="%s"/></circle>' % (OR if k == 0 else GRIS, k * 1.2, p)
    c += txt(895, 260, '« Que se serait-il passé si… ? »', 18, TEXTE, extra=' font-style="italic"')
    c += chips([('Risque calculé', OR), ('Instabilité', ROUGE), ('Non-retour', BLEU), ("L'individu", VERT)], 505, x0=590, gap=10)
    e = ETAPES[5]
    return base(6, e['titre'], e['sous'], c, e['legG'], e['legD'])


def icone(k, x, y):
    if k == 1:
        return disque(x, y - 15, 16, OR) + ''.join('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="3"/>' % (x, y + 1, x + dx, y + 30, col) for dx, col in [(-40, VERT), (0, CYAN), (40, ROUGE)])
    if k == 2:
        return ''.join('<circle cx="%d" cy="%d" r="8" fill="%s"/>' % (x - 45 + i * 30, y, col) for i, col in enumerate([CYAN, ROUGE, OR, VERT])) + \
            '<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-opacity=".5" stroke-width="2"/>' % (x - 45, y, x + 45, y, CYAN)
    if k == 3:
        return ('<path d="M%d %d C%d %d %d %d %d %d" fill="none" stroke="%s" stroke-width="3"/>' % (x - 45, y - 20, x - 10, y - 20, x, y, x + 35, y, BLEU)
                + '<path d="M%d %d C%d %d %d %d %d %d" fill="none" stroke="%s" stroke-width="3"/>' % (x - 45, y + 20, x - 10, y + 20, x, y, x + 35, y, VERT)
                + disque(x + 42, y, 9, OR))
    if k == 4:
        return ''.join('<rect x="%d" y="%d" width="%d" height="12" rx="3" fill="%s" fill-opacity=".7"/>' % (x - 50 + i * 12, y + 24 - i * 16, 100 - i * 24, col) for i, col in enumerate([VERT, CYAN, BLEU, OR]))
    if k == 5:
        return ('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="3"/>' % (x - 50, y, x + 50, y, ROUGE)
                + ''.join('<circle cx="%d" cy="%d" r="7" fill="#0e1228" stroke="%s" stroke-width="2.5"/>' % (x - 50 + i * 33, y, OR) for i in range(4)))
    return ('<path d="M%d %d C%d %d %d %d %d %d" fill="none" stroke="%s" stroke-width="3"/>' % (x - 45, y + 10, x - 10, y + 10, x, y - 25, x + 45, y - 25, VERT)
            + '<path d="M%d %d H%d" stroke="%s" stroke-width="2.5" stroke-dasharray="6 5"/>' % (x - 10, y + 10, x + 45, GRIS)
            + '<path d="M%d %d C%d %d %d %d %d %d" fill="none" stroke="%s" stroke-width="2.5" stroke-dasharray="6 5"/>' % (x - 45, y + 10, x - 10, y + 10, x, y + 35, x + 45, y + 35, GRIS))


def parcours():
    s = ouvrir("Parcours : Raymond Aron, philosophie et histoire, en six étapes") + etoiles(11)
    s += txt(640, 92, "Raymond Aron, 1963-1964 : philosophie et histoire", 38, TEXTE, weight='600', family=SERIF)
    s += txt(640, 130, "Cinq cours à la Sorbonne en six étapes, du sens de l'histoire à « que se serait-il passé si… ? »", 19, CYAN)
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
                          "(cours « Philosophie et Histoire », Sorbonne, 1963-1964, rediffusé par France Culture)."], 17, TEXTE, 'start', h=24)
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


TITRE = "Raymond Aron, philosophie et histoire"
DESC = "Fiche vidéo (cours à la Sorbonne, 1963-1964) : Raymond Aron interroge le sens de l'histoire, de Hegel à Max Weber, et montre avec Thucydide et la guerre de 1914 ce que l'historien peut expliquer."

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
             '<div class="badges"><span class="b">YouTube</span><span class="b">Cours, 1963-1964</span><span class="b b-lu">Lu en entier</span></div>\n'
             '<h1>Vidéo : « Raymond Aron, cours du cycle Philosophie et Histoire à la Sorbonne »</h1>\n'
             '<p class="meta">Chaîne Artes2 · 4 h 47 min · mise en ligne le 11 mai 2021 · cours 1 à 5 du cycle « Philosophie et Histoire » (1963-1964), enregistrés pour Radio Sorbonne et rediffusés par France Culture · en français · transcription automatique lue en entier · pas de chapitres : découpage proposé en %d parties</p>\n'
             '<p class="actions"><a class="bouton" href="%s" target="_blank" rel="noopener">Voir sur YouTube</a><a class="bouton bouton-2" href="%s.html">Parcours en %d étapes</a></p>\n</div>\n' % (len(CHAPITRES), yt, SUJET, N))
    h.append('<article class="fiche" id="synthese">\n<h3>Synthèse et conclusion</h3>\n<h4>Synthèse</h4>\n'
             '<p>Dans ces cinq cours donnés à la Sorbonne pendant l\'hiver 1963-1964, Raymond Aron se demande ce que la philosophie peut dire de l\'histoire. Il part de Hegel, pour qui l\'histoire est la raison qui se réalise, et de ses trois héritiers (marxisme, historicisme, existentialisme). Il revient sur sa propre thèse des années 1930, sur les limites de l\'objectivité historique, et sur le débat d\'après-guerre avec Sartre et Merleau-Ponty sur le sens de l\'histoire.</p>\n'
             '<p>Il montre ensuite comment travaille l\'historien. Il reconstruit le passé sans jamais le reproduire, en choisissant son objet (Rickert, Dilthey, Max Weber). Il travaille sur quatre plans, du récit des événements au sens global. Il raconte une histoire « dramatique », dont Thucydide reste le modèle. L\'exemple des origines de la guerre de 1914 lui sert à distinguer trois questions, la légitimité, les intentions et les conséquences, qui sont autant de « principes d\'incertitude ».</p>\n'
             '<h4>Conclusion</h4>\n'
             '<p>Pour Aron, l\'histoire n\'est ni le déroulement fatal d\'un sens connu d\'avance, ni un pur non-sens. L\'historien peut rester objectif en distinguant le détail des décisions et la conjoncture, et en se demandant, avec Max Weber, ce qui se serait passé si une cause avait manqué. Ce calcul rétrospectif des probabilités évite l\'illusion que ce qui est arrivé devait arriver.</p>\n'
             '<p class="note"><b>Voir aussi.</b> Du même Aron, une dizaine d\'années plus tard, les fiches <a href="aron-europe-fiche.html">Raymond Aron et l\'Europe protégée</a> (1973) et <a href="aron-politique-fiche.html">Raymond Aron face aux totalitarismes</a> (1975).</p>\n</article>\n')
    h.append('<h2 class="sec" id="etapes">Les %d étapes expliquées</h2>\n' % N)
    for e in ETAPES:
        h.append('<article class="fiche etape" id="etape-%d">\n<h3><a class="num" href="%s" aria-label="Ouvrir la planche de l\'étape %d">%d</a> %s</h3>\n'
                 '<p>%s</p>\n<p class="anim"><b>Dans l\'animation.</b> %s</p>\n'
                 '<p class="liens"><a href="%s">Voir le schéma</a> · <a href="%s?t=%d" target="_blank" rel="noopener">À %s dans la vidéo</a></p>\n</article>\n'
                 % (e['n'], e['page'], e['n'], e['n'], esc(e['court']), e['texte'], esc(e['anim']), e['page'], yt, e['t'], hms(e['t'])))
    h.append('<article class="fiche" id="chapitres">\n<h3>Les %d parties de la vidéo</h3>\n<p class="meta">La vidéo n\'a pas de chapitres : découpage proposé d\'après la transcription. Chaque cours est précédé d\'une courte présentation radiophonique.</p>\n<ul class="chap">\n' % len(CHAPITRES))
    for t, ti, r in CHAPITRES:
        h.append('<li><a href="%s?t=%d" target="_blank" rel="noopener">%s</a> <b>%s.</b> %s</li>\n' % (yt, t, hms(t), esc(ti), r))
    h.append('</ul>\n</article>\n')
    h.append('<article class="fiche" id="precautions">\n<h3>Précautions</h3>\n'
             '<p class="note">Ce sont des cours de 1963-1964, enregistrés pour Radio Sorbonne puis rediffusés par France Culture (« Les conférences du soir »), et mis en ligne par une chaîne qui n\'est pas l\'éditeur d\'origine. Les dates des cours 2 à 5 viennent des présentations radiophoniques. Aron y expose sa propre lecture : sa présentation de la crise de juillet 1914, plutôt modérée sur les responsabilités, et celle des thèses d\'A. J. P. Taylor sur 1939 sont rapportées comme il les donne, dans l\'état du débat de 1964 (avant que la thèse de Fritz Fischer, qu\'il évoque sans le nommer, ne s\'impose largement). Quelques précisions de contexte sont ajoutées ici, comme la date de la thèse (1938).</p>\n'
             '<p class="note">La transcription est automatique, sans ponctuation, et déforme presque tous les noms propres. J\'ai lu « igle », « eagle » et « hic » comme Hegel ; « les ombres un chèque » comme Léon Brunschvicg ; « rigueur tu » et « ricker » comme Rickert ; « deal taille » comme Dilthey ; « max payne » comme Max Weber ; « rank vie est ce que chaînistes » comme la formule de Ranke <i>wie es eigentlich gewesen</i> ; « ja spurs » comme Jaspers ; « gaye stevie saône shaft » comme <i>Geisteswissenschaften</i> (sciences de l\'esprit) ; « met à l\'eau ponty » comme Merleau-Ponty ; « tu si dit » comme Thucydide ; « ni cias » comme Nicias ; « egypt élan taylor » comme A. J. P. Taylor ; « rossbach » comme le rapport Hossbach ; « delbrück » comme Hans Delbrück ; « normal enjoy » comme Norman Angell ; « louis saez » comme Louis XVI ; « aller tester ya prof à 6 » comme l\'expression grecque <i>alêthestatê prophasis</i> (« la cause la plus vraie »). Les citations entre guillemets sont reformulées d\'après cette transcription et peuvent s\'écarter un peu des mots exacts.</p>\n</article>\n')
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

