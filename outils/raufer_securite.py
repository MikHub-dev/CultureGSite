# -*- coding: utf-8 -*-
"""Génère la fiche vidéo « La sécurité selon Xavier Raufer » (Politique et Géopolitique) :
entretien publié par la chaîne Front Populaire (2024).
Parcours SVG, une planche SVG animée par étape, pages HTML (parcours, planches, fiche).
Même modèle que outils/aron_europe.py (dont les fonctions communes sont reprises).
Lancer depuis la racine du dépôt : python3 -I outils/raufer_securite.py
"""
import os, random, html, math

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOSSIER = os.path.join(RACINE, 'fiches-geopolitique')
SUJET = 'raufer-securite'
IMG = os.path.join(DOSSIER, 'images', SUJET)
VID = 'O12-6fjKU5U'

OR, CYAN, ROUGE, VERT, BLEU, GRIS = '#f2b84b', '#5ad1e6', '#ff6b7a', '#7ee0a0', '#7aa2ff', '#9fb3d6'
TEXTE = '#e6eefc'
SERIF = "Spectral, Georgia, 'Times New Roman', serif"
SANS = "Jost, 'Segoe UI', system-ui, sans-serif"

# ---------------------------------------------------------------- contenu
ETAPES = [
    dict(slug='pas-un-mexique', court='La France, un futur Mexique ?',
         parcours=['Un futur', 'Mexique ?'],
         titre="La France n'est pas le Mexique",
         sous="Des magistrats mexicains alertent ; Xavier Raufer répond que l'État français tient encore",
         legG="Des magistrats mexicains préviennent : sans réaction, la France pourrait devenir un nouveau Mexique d'ici dix ans. Là-bas, des cartels ont plus d'hommes armés que l'armée.",
         legD="Pour Raufer, c'est impossible en France : territoire plus petit, gendarmerie bien informée, État encore solide. L'échec actuel vient, selon lui, de dirigeants incompétents.",
         texte="L'entretien s'ouvre sur l'appel d'une délégation de magistrats mexicains venus en France : sans mesures contre le narcobanditisme, la France risquerait de devenir un nouveau Mexique d'ici dix ans. Le criminologue Xavier Raufer juge l'alerte peu réaliste. Il dit être allé au Mexique avec des membres du cabinet du ministre de la Défense, et y avoir entendu les fusiliers marins mexicains, en première ligne contre les narcotrafiquants, expliquer que les cartels avaient plus d'hommes armés que l'armée, et mieux armés, avec des blindés et de quoi abattre des hélicoptères. Il rappelle aussi l'affaire des quarante-trois étudiants disparus d'Ayotzinapa (2014) : les écoutes ont montré que la police locale obéissait au cartel, au point que le commissaire appelait son chef « chef ». Rien de tel, selon lui, n'est possible en France : le territoire est plus réduit, la gendarmerie nationale reste assez bien informée hors des villes pour voir se former un groupe armé, et l'appareil d'État conserve sa force. Les magistrats mexicains voient partir de chez eux des centaines de tonnes de cocaïne, mais connaissent mal la France. Sa thèse, posée dès le début : si le pays était dirigé par des gens qui comprennent le crime, la lutte contre le narcotrafic réussirait bien mieux ; l'échec actuel tient au côté « brouillon » et « amateur » des dirigeants, qu'il qualifie d'incompétents.",
         anim="Deux cartes face à face : au Mexique, la tache du cartel dépasse l'armée ; en France, les points chauds restent petits et la gendarmerie veille sur le reste du territoire.",
         t=64),
    dict(slug='zones-hors-controle', court='Les zones hors contrôle',
         parcours=['Les zones', 'hors contrôle'],
         titre="« Des favelas sur le territoire français »",
         sous="Pour Raufer, la France n'a qu'un seul problème criminel, très localisé",
         legG="Environ 1 300 quartiers de la politique de la ville ; des tonnes de cocaïne entrent par les ports. Dans les quartiers nord de Marseille, 17,5 homicides pour 100 000 habitants.",
         legD="C'est quinze fois la moyenne nationale (1,15). Pour Raufer, la police pourrait y rétablir l'ordre si on le lui ordonnait, et si ses commissariats étaient placés là où il le faut.",
         texte="Les « territoires perdus de la République » sont-ils un fantasme ? Pour Raufer, c'est une réalité décrite par les rapports officiels : on compte en France entre 1 300 et 1 350 quartiers de la politique de la ville, en périphérie des métropoles et de plus en plus dans des villes moyennes, où la police n'entre plus que pour des opérations « coup de poing » et où des bandes armées vivent du cannabis et, de plus en plus, de la cocaïne. Il insiste sur le choix des mots : on ne soigne pas un mal qu'on nomme mal. Il donne l'ordre de grandeur du marché : 116 tonnes de cocaïne saisies en 2023 au seul port d'Anvers, et, selon les estimations qu'il cite, 700 à 800 tonnes qui passent chaque année entre les mailles du filet en Europe, où les frontières de l'espace Schengen ne l'arrêtent plus ; à 60 euros le gramme, des sommes qui donnent un énorme pouvoir de corruption. Son exemple central : les quatre arrondissements des quartiers nord de Marseille (13e à 16e). Il y compte 44 homicides en 2023, soit environ 17,5 pour 100 000 habitants, contre 1,15 pour la France entière, un niveau proche du Brésil ou du Guatemala. D'où sa formule : « on a des favelas sur le territoire français ». Ces zones ne représentent, dit-il, qu'environ 2 % des 5 % urbanisés du territoire ; il n'y a pas de commissariat dans ces arrondissements alors qu'il y en a dans les quartiers aisés. Si la police recevait l'ordre de faire régner l'ordre et était placée là où il le faut, les violences baisseraient nettement.",
         anim="Une barre monte : 1,15 homicide pour 100 000 habitants en France, 17,5 dans les quartiers nord de Marseille. Une carte de la ville montre les quatre arrondissements en rouge et les commissariats ailleurs.",
         t=260),
    dict(slug='fourmiliere', court='Le coup de pied dans la fourmilière',
         parcours=['La', 'fourmilière'],
         titre="Un coup de pied dans la fourmilière",
         sous="Pourquoi, selon Raufer, le trafic gagne les villes moyennes et les campagnes",
         legG="Raufer accuse l'État d'avoir dispersé en province des personnes sans ressources ni statut. Un coup de pied dans une fourmilière ne tue pas les fourmis : il les éparpille.",
         legD="Les bandits ne peuvent pas aller au tribunal entre eux. Quand la concurrence fait baisser les gains, il ne leur reste que l'intimidation, puis l'homicide.",
         texte="Ces violences sont-elles nouvelles, ou simplement plus visibles grâce aux réseaux sociaux ? Pour Raufer, elles ont toujours existé, mais elles se diffusent dans tout le pays. Il en accuse le gouvernement, qui aurait cherché depuis deux ou trois ans à disperser en province des personnes en situation irrégulière ou sans statut, notamment avant les Jeux olympiques : sans ressources ni maîtrise de la langue, elles n'auraient d'autre issue que la rapine ou le trafic. C'est sa thèse, présentée sans chiffres. Le problème, dit-il, n'est pas une criminalité qui s'aggrave partout, mais un État qui, au lieu de concentrer puis de réduire le crime, l'éparpille : « un coup de pied dans une fourmilière ne tue pas les fourmis, il les éparpille ». Il explique ensuite le mécanisme de la violence. Tous les hors-la-loi, de la mafia sicilienne au petit voleur, ont un point commun : ils ne peuvent pas faire appel à la loi. Quand deux bandes vendent la même drogue, la concurrence fait baisser les prix et les gains (la loi des rendements décroissants). Un épicier gêné par un concurrent irait voir un avocat ; un trafiquant n'a que deux « barreaux » à son échelle des peines : l'intimidation, puis l'homicide. Disperser des réseaux, c'est donc multiplier les règlements de comptes. Il ajoute un jugement politique très tranché : le président, dont l'univers serait celui de la finance, ne s'intéresserait pas au monde criminel.",
         anim="Un coup frappe une fourmilière au centre : les points rouges s'éparpillent vers des villes moyennes et des villages. Puis une échelle n'a que deux barreaux, « intimidation » et « homicide ».",
         t=1020),
    dict(slug='impunite', court="L'impunité",
         parcours=["L'impunité"],
         titre="« Les malfaiteurs ne s'arrêtent que quand on les arrête »",
         sous="Une justice que même les trafiquants ne prennent plus au sérieux, selon Raufer",
         legG="Le crime est un métier, pas un plaisir : sans sanction, il continue. Raufer juge la justice laxiste et les annonces des ministres purement « pour la galerie ».",
         legD="Son anecdote : des jeunes d'une cité s'étonnent qu'un cousin arrêté pour trafic ressorte libre du tribunal. Les bandits, très réalistes, savent ce qu'ils risquent.",
         texte="Le trafic va-t-il s'installer durablement dans les campagnes ? Oui, répond Raufer, si l'on n'y prend pas garde, en vertu d'un principe de base de la criminologie : « les malfaiteurs ne s'arrêtent que quand on les arrête ». Ils ne braquent pas, ne vendent pas de drogue et ne prostituent pas par plaisir : c'est leur gagne-pain. Il faut donc, à un moment, les empêcher de continuer, dans le cadre du code pénal, qu'il juge mesuré ; il se dit lui-même non « répressif fanatique ». Or il décrit une justice devenue, sous le ministre Éric Dupond-Moretti, incapable de sanctionner : des récidivistes au casier chargé ressortiraient libres du tribunal. Les bandits vivant dans un monde « darwinien », ils savent très bien ce que la police et la justice peuvent faire ; s'ils continuent à se tuer et à vendre malgré les opérations annoncées par les ministres, c'est qu'ils n'ont pas peur. Il raconte qu'un jour, à la terrasse d'un café, de jeunes livreurs d'une cité l'ont reconnu et lui ont demandé pourquoi leur cousin, arrêté pour un gros trafic, était ressorti « les mains dans les poches » : même eux ne comprenaient pas. Il cite aussi un braquage de bijouterie avenue Montaigne, à dix minutes de l'Élysée. Dans la partie suivante, il affirme que la délinquance de voie publique serait le fait d'étrangers dans une très large majorité, en s'appuyant sur les rapports annuels de la gendarmerie et de la police sur le crime organisé. C'est une affirmation qu'il ne chiffre pas précisément et qui est très discutée (voir les précautions).",
         anim="Une balance de la justice reste vide d'un côté : les dossiers s'empilent, la sanction ne tombe pas, et le trafic repart en boucle.",
         t=1403),
    dict(slug='mots-et-chiffres', court='Les mots et les chiffres',
         parcours=['Les mots', 'et les chiffres'],
         titre="Nommer les choses, compter juste",
         sous="Les statistiques qu'il retient et le vocabulaire des médias qu'il critique",
         legG="Pour mesurer la violence, Raufer additionne homicides et tentatives, car les SAMU sauvent aujourd'hui des blessés qui seraient morts en 1980. Selon lui : +110 % en vingt ans.",
         legD="Il refuse de parler de « consommateurs » pour des toxicomanes, d'« auteurs » pour des malfaiteurs, ou de « sentiment d'insécurité » : ces mots adouciraient le réel.",
         texte="Raufer s'en prend au traitement médiatique de l'insécurité. Les grands médias appartiennent selon lui à des milliardaires ou à l'État, qui défendent une « mondialisation heureuse » et taisent donc la réalité criminelle ; il qualifie durement les sociologues qui la relativisent. Sur les chiffres, il défend une méthode : compter ensemble les homicides et les tentatives d'homicide. Depuis les années 1980, la médecine d'urgence (SAMU et SMUR) sauve beaucoup de blessés qui seraient morts autrefois ; il estime qu'une victime grave avait alors 70 % de risques de mourir avant d'arriver au bloc, contre trois sur dix aujourd'hui. Compter les seuls morts sous-estimerait donc la violence. Avec cette méthode, il annonce une hausse d'environ 110 % en vingt ans, et pour les coups et blessures volontaires hors du cadre familial, une hausse d'environ 6 % par an de 2017 à 2023. Pour lui, l'expression « sentiment d'insécurité » nie le réel. Il refuse aussi de dire « consommateurs » pour des toxicomanes, « auteurs » pour des malfaiteurs, « produits » pour des drogues, ou « ressortissant algérien » pour un Algérien : ce vocabulaire uniforme, qu'il appelle une « langue de coton », empêcherait de comprendre ce qui se passe. Il conclut qu'un sondage récent montre 75 % de Français mécontents de la politique de sécurité : les gens ont compris. La vidéo se termine par quelques extraits de la suite de l'entretien, réservée aux abonnés : la légalisation du cannabis, qu'il juge inapplicable, et une justice débordée, avec moins de procureurs par habitant que l'Albanie et des magistrats qui ont 300 dossiers au lieu de 30.",
         anim="Deux courbes : les morts seuls stagnent, mais les morts et les blessés graves additionnés montent. Puis des mots « adoucis » remplacent les mots précis, et le tableau devient flou.",
         t=1975),
]

CHAPITRES = [
    (0, "Extraits en ouverture", "Quelques phrases fortes de l'entretien, avant la présentation de l'invité."),
    (64, "Les magistrats mexicains et le « risque Mexique »", "Des cartels plus armés que l'armée mexicaine ; pourquoi la France n'en est pas là, selon Raufer."),
    (260, "Les territoires perdus : fantasme ou réalité ?", "Les quartiers de la politique de la ville ; l'importance des mots."),
    (352, "La cocaïne en Europe", "Les saisies d'Anvers, l'espace Schengen, le prix du gramme ; l'affaire des étudiants disparus au Mexique."),
    (601, "Un préfet contrôlé par des guetteurs ?", "Police et gendarmerie, les zones hors contrôle, l'ordre qui ne vient pas."),
    (737, "Les quartiers nord de Marseille", "44 homicides, 17,5 pour 100 000 habitants ; « des favelas sur le territoire français » ; où sont les commissariats."),
    (1020, "Une violence qui se diffuse", "La dispersion vers la province, la fourmilière, la loi des rendements décroissants, intimidation puis homicide."),
    (1289, "Le président et la sécurité", "Le jugement politique de Raufer sur Emmanuel Macron."),
    (1403, "« Les malfaiteurs ne s'arrêtent que quand on les arrête »", "La justice jugée laxiste, l'anecdote du cousin, le braquage de l'avenue Montaigne."),
    (1803, "Le profil des trafiquants", "Les rapports annuels de la gendarmerie et de la police ; ses affirmations sur les étrangers, très discutées."),
    (1975, "Les médias et l'insécurité", "Qui possède les médias ; la police et la justice à l'image du pays."),
    (2145, "Compter les homicides et les tentatives", "Le rôle des SAMU, +110 % en vingt ans, les coups et blessures hors famille."),
    (2361, "Le « sentiment d'insécurité »", "Une expression qu'il rejette."),
    (2431, "Toxicomanes ou consommateurs ?", "La « langue de coton » des médias et le sondage final."),
    (2816, "Extraits de la suite de l'entretien", "Cannabis, manque de procureurs, magistrats débordés."),
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


HEXA = [(0, -1), (0.87, -0.5), (0.87, 0.5), (0, 1), (-0.87, 0.5), (-0.87, -0.5)]


def hexagone(cx, cy, r, col, opa='.08', w=2.5):
    pts = ' '.join('%.0f,%.0f' % (cx + r * a, cy + r * b) for a, b in HEXA)
    return '<polygon points="%s" fill="%s" fill-opacity="%s" stroke="%s" stroke-width="%s"/>' % (pts, col, opa, col, w)


def planche1():
    c = ''
    # Mexique
    c += boite(60, 180, 560, 380, ROUGE, '.04') + txt(340, 212, 'Au Mexique, selon les Marines mexicains', 18, ROUGE, weight='600')
    for k, (lab, col, h0, h1) in enumerate([(["Hommes armés", "de l'armée"], BLEU, 150, 150), (['Hommes armés', 'des cartels'], ROUGE, 60, 200)]):
        x = 170 + k * 220
        c += ('<rect x="%d" y="%d" width="120" height="%d" rx="8" fill="%s" fill-opacity=".35" stroke="%s" stroke-width="2">'
              '<animate attributeName="height" values="%d;%d;%d" keyTimes="0;.4;1" dur="9s" repeatCount="indefinite"/>'
              '<animate attributeName="y" values="%d;%d;%d" keyTimes="0;.4;1" dur="9s" repeatCount="indefinite"/></rect>') % (
            x, 460 - h1, h1, col, col, h0, h1, h1, 460 - h0, 460 - h1, 460 - h1)
        c += lignes(x + 60, 484, lab, 15, col, h=20, weight='600')
    c += '<line x1="140" y1="460" x2="540" y2="460" stroke="%s" stroke-width="2"/>' % GRIS
    c += txt(340, 545, 'Blindés, armes capables d\'abattre des hélicoptères', 15, GRIS, extra=' font-style="italic"')
    # France
    c += boite(660, 180, 560, 380, BLEU, '.04') + txt(940, 212, 'En France, selon Raufer', 18, BLEU, weight='600')
    c += '<g>' + hexagone(860, 370, 130, VERT, '.1') + '<animate attributeName="opacity" values=".6;1;.6" dur="4s" repeatCount="indefinite"/></g>'
    c += txt(860, 375, 'Gendarmerie', 17, VERT, weight='600') + txt(860, 398, '95 % du territoire', 14, VERT)
    for x, y in [(800, 300), (920, 320), (830, 455), (935, 430)]:
        c += '<circle cx="%d" cy="%d" r="7" fill="%s"><animate attributeName="r" values="5;9;5" dur="2.4s" repeatCount="indefinite"/></circle>' % (x, y, ROUGE)
    c += lignes(1105, 290, ['Points chauds', 'très localisés,', 'en ville'], 16, ROUGE, h=22, weight='600')
    c += lignes(1105, 400, ['Un État qui', 'garde sa force'], 16, TEXTE, h=22)
    c += txt(940, 545, "L'échec viendrait des dirigeants, pas de la menace", 15, OR, weight='600')
    e = ETAPES[0]
    return base(1, e['titre'], e['sous'], c, e['legG'], e['legD'])


def planche2():
    c = ''
    c += boite(60, 180, 600, 380, ROUGE, '.04') + txt(360, 212, 'Homicides pour 100 000 habitants (2023)', 18, ROUGE, weight='600')
    base_y = 480
    for x, lab, v, col in [(170, 'France entière', 1.15, BLEU), (420, 'Quartiers nord de Marseille', 17.5, ROUGE)]:
        h = round(v * 12)
        c += ('<rect x="%d" y="%d" width="140" height="%d" rx="6" fill="%s" fill-opacity=".4" stroke="%s" stroke-width="2">'
              '<animate attributeName="height" values="0;%d;%d" keyTimes="0;.35;1" dur="9s" repeatCount="indefinite"/>'
              '<animate attributeName="y" values="%d;%d;%d" keyTimes="0;.35;1" dur="9s" repeatCount="indefinite"/></rect>') % (
            x, base_y - h, h, col, col, h, h, base_y, base_y - h, base_y - h)
        c += txt(x + 70, base_y - h - 12, ('%s' % v).replace('.', ','), 22, col, weight='600', family=SERIF)
        c += txt(x + 70, base_y + 26, lab, 15, col, weight='600')
    c += '<line x1="120" y1="%d" x2="620" y2="%d" stroke="%s" stroke-width="2"/>' % (base_y, base_y, GRIS)
    c += txt(360, 540, 'Environ quinze fois la moyenne nationale', 17, OR, weight='600')
    c += boite(700, 180, 520, 380, OR, '.04') + txt(960, 212, 'Le marché, selon les chiffres cités', 18, OR, weight='600')
    faits = [('1 300 à 1 350', 'quartiers de la politique de la ville', CYAN), ('116 tonnes', 'de cocaïne saisies à Anvers en 2023', OR),
             ('700 à 800 t', 'entrées en Europe chaque année', ROUGE), ('60 €', 'le gramme en France', VERT)]
    for k, (gros, pt, col) in enumerate(faits):
        y = 250 + k * 72
        c += '<g opacity="0">' + apparait(0.08 + k * 0.16) + '<rect x="730" y="%d" width="460" height="60" rx="12" fill="%s" fill-opacity=".1" stroke="%s"/>' % (y, col, col)
        c += txt(750, y + 38, gros, 21, col, 'start', '600', SERIF) + txt(900, y + 37, pt, 15, TEXTE, 'start') + '</g>'
    e = ETAPES[1]
    return base(2, e['titre'], e['sous'], c, e['legG'], e['legD'])


def planche3():
    c = ''
    c += boite(60, 180, 640, 380, OR, '.04') + txt(380, 212, "On éparpille au lieu de réduire", 18, OR, weight='600')
    cx, cy = 380, 380
    c += '<path d="M%d %d q60 -90 120 0z" fill="%s" fill-opacity=".25" stroke="%s" stroke-width="2"/>' % (cx - 60, cy + 20, OR, OR)
    c += txt(cx, cy + 46, 'Métropole', 15, OR, weight='600')
    cibles = [(140, 270, 'Ville moyenne'), (620, 270, 'Ville moyenne'), (150, 500, 'Village'), (610, 500, 'Village'), (380, 260, '')]
    for k, (x, y, lab) in enumerate(cibles):
        for j in range(3):
            dx, dy = (j - 1) * 10, (j % 2) * 8
            c += ('<circle r="5" fill="%s"><animate attributeName="cx" values="%d;%d;%d" keyTimes="0;.45;1" dur="7s" repeatCount="indefinite"/>'
                  '<animate attributeName="cy" values="%d;%d;%d" keyTimes="0;.45;1" dur="7s" repeatCount="indefinite"/></circle>') % (
                ROUGE, cx + dx, x + dx, x + dx, cy + dy, y + dy, y + dy)
        if lab:
            c += txt(x, y + 34, lab, 14, GRIS)
    c += txt(380, 545, '« Un coup de pied dans une fourmilière… »', 16, TEXTE, extra=' font-style="italic"')
    # échelle à deux barreaux
    c += boite(740, 180, 480, 380, ROUGE, '.04') + txt(980, 212, "L'échelle des peines du milieu", 18, ROUGE, weight='600')
    c += '<path d="M860 260 V530 M960 260 V530" stroke="%s" stroke-width="4"/>' % GRIS
    for k, (y, lab, col) in enumerate([(470, 'Intimidation', OR), (320, 'Homicide', ROUGE)]):
        c += '<g opacity="0">' + apparait(0.15 + k * 0.3) + '<line x1="860" y1="%d" x2="960" y2="%d" stroke="%s" stroke-width="6"/>' % (y, y, col)
        c += txt(985, y + 6, lab, 18, col, 'start', '600') + '</g>'
    c += txt(1090, 395, 'Pas de tribunal', 15, GRIS, extra=' font-style="italic"') + txt(1090, 415, 'entre bandits', 15, GRIS, extra=' font-style="italic"')
    e = ETAPES[2]
    return base(3, e['titre'], e['sous'], c, e['legG'], e['legD'])


def planche4():
    c = ''
    # cycle de l'impunité
    c += boite(60, 180, 600, 380, CYAN, '.04') + txt(360, 212, "Le cycle de l'impunité, selon Raufer", 18, CYAN, weight='600')
    pts = [(360, 270, 'Trafic', ROUGE), (540, 400, 'Arrestation', BLEU), (360, 510, 'Sortie libre', GRIS), (180, 400, 'Pas de peur', OR)]
    for k in range(4):
        x1, y1 = pts[k][:2]
        x2, y2 = pts[(k + 1) % 4][:2]
        c += '<path d="M%d %d Q%d %d %d %d" fill="none" stroke="%s" stroke-opacity=".5" stroke-width="2.5" marker-end="url(#fl)"/>' % (
            x1 + (x2 - x1) * .25, y1 + (y2 - y1) * .25, (x1 + x2) / 2 + (360 - (x1 + x2) / 2) * -.3, (y1 + y2) / 2 + (400 - (y1 + y2) / 2) * -.3, x2 - (x2 - x1) * .25, y2 - (y2 - y1) * .25, GRIS)
    c += '<circle r="8" fill="%s" filter="url(#glow)"><animateMotion dur="6s" repeatCount="indefinite" path="M360 270 Q540 270 540 400 Q540 510 360 510 Q180 510 180 400 Q180 270 360 270"/></circle>' % OR
    for x, y, lab, col in pts:
        c += '<rect x="%d" y="%d" width="140" height="40" rx="20" fill="#0e1228" stroke="%s" stroke-width="2"/>' % (x - 70, y - 20, col)
        c += txt(x, y + 6, lab, 16, col, weight='600')
    # balance de la justice
    c += boite(700, 180, 520, 380, OR, '.04') + txt(960, 212, 'Une justice débordée', 18, OR, weight='600')
    c += '<path d="M960 470 V270 M910 470 H1010" stroke="%s" stroke-width="4"/>' % GRIS
    c += '<g><animateTransform attributeName="transform" type="rotate" values="0 960 270;-10 960 270;-10 960 270;0 960 270" keyTimes="0;.3;.9;1" dur="9s" repeatCount="indefinite"/>'
    c += '<line x1="800" y1="270" x2="1120" y2="270" stroke="%s" stroke-width="4"/>' % GRIS
    for x, lab, col in [(800, 'Dossiers', BLEU), (1120, 'Sanctions', ROUGE)]:
        c += '<path d="M%d 270 V300 M%d 300 h120 l-16 20 h-88z" stroke="%s" stroke-width="2" fill="%s" fill-opacity=".2"/>' % (x, x - 60, col, col)
        c += txt(x, 345, lab, 16, col, weight='600')
    for k in range(4):
        c += '<rect x="772" y="%d" width="56" height="9" rx="2" fill="%s" fill-opacity=".7"/>' % (290 - k * 11, BLEU)
    c += '</g>'
    c += lignes(960, 505, ['« Ils n\'ont pas peur » :', 'des annonces « pour la galerie »'], 16, TEXTE, h=22)
    e = ETAPES[3]
    return base(4, e['titre'], e['sous'], c, e['legG'], e['legD'])


def planche5():
    c = ''
    c += boite(60, 180, 600, 380, CYAN, '.04') + txt(360, 212, 'Compter les morts, ou morts et blessés graves ?', 17, CYAN, weight='600')
    c += '<path d="M110 500 H620 M110 500 V250" stroke="%s" stroke-width="2"/>' % GRIS
    c += txt(120, 525, 'il y a 20 ans', 13, GRIS, 'start') + txt(615, 525, '2023', 13, GRIS, 'end')
    d1 = 'M110 440 C250 438 400 442 610 436'
    d2 = 'M110 440 C260 420 420 340 610 280'
    for d, col in [(d1, BLEU), (d2, ROUGE)]:
        c += ('<path d="%s" fill="none" stroke="%s" stroke-width="4" stroke-dasharray="700" stroke-dashoffset="700">'
              '<animate attributeName="stroke-dashoffset" values="700;0;0" keyTimes="0;.45;1" dur="9s" repeatCount="indefinite"/></path>') % (d, col)
    c += txt(600, 462, 'Morts seuls', 15, BLEU, 'end', '600')
    c += txt(600, 266, 'Morts + tentatives : +110 % (selon lui)', 15, ROUGE, 'end', '600')
    c += txt(360, 548, "Le SAMU sauve des blessés qui seraient morts en 1980", 14, GRIS, extra=' font-style="italic"')
    # mots
    c += boite(700, 180, 520, 380, OR, '.04') + txt(960, 212, 'Les mots qu\'il refuse', 18, OR, weight='600')
    mots = [('toxicomane', 'consommateur'), ('malfaiteur', 'auteur'), ('drogue', 'produit'), ('insécurité', "« sentiment d'insécurité »")]
    for k, (vrai, doux) in enumerate(mots):
        y = 262 + k * 66
        c += txt(800, y, vrai, 19, VERT, weight='600')
        c += '<path d="M860 %d H910" stroke="%s" stroke-width="2" marker-end="url(#fl)"/>' % (y - 6, GRIS)
        c += ('<text x="1060" y="%d" font-size="17" fill="%s" text-anchor="middle" font-family="%s">%s'
              '<animate attributeName="opacity" values="0;0;1;.35;0" keyTimes="0;%.2f;%.2f;.9;1" dur="9s" repeatCount="indefinite"/></text>') % (
            y, GRIS, esc(SANS), esc(doux), 0.1 + k * 0.12, 0.18 + k * 0.12)
    c += txt(960, 535, '« Une langue de coton » qui brouille le réel', 16, OR, weight='600')
    e = ETAPES[4]
    return base(5, e['titre'], e['sous'], c, e['legG'], e['legD'])


PLANCHES = [planche1, planche2, planche3, planche4, planche5]


def icone(k, x, y):
    if k == 1:
        return hexagone(x, y, 34, VERT, '.12') + '<circle cx="%d" cy="%d" r="5" fill="%s"/>' % (x - 8, y - 6, ROUGE) + '<circle cx="%d" cy="%d" r="5" fill="%s"/>' % (x + 10, y + 10, ROUGE)
    if k == 2:
        return ('<rect x="%d" y="%d" width="22" height="8" fill="%s" fill-opacity=".5" stroke="%s"/>' % (x - 30, y + 22, BLEU, BLEU)
                + '<rect x="%d" y="%d" width="22" height="60" fill="%s" fill-opacity=".5" stroke="%s"/>' % (x + 8, y - 30, ROUGE, ROUGE))
    if k == 3:
        return '<path d="M%d %d q16 -24 32 0z" fill="%s" fill-opacity=".3" stroke="%s"/>' % (x - 16, y + 8, OR, OR) + ''.join(
            '<circle cx="%d" cy="%d" r="4" fill="%s"/>' % (x + dx, y + dy, ROUGE) for dx, dy in [(-40, -20), (40, -22), (-36, 26), (38, 24), (0, -32)])
    if k == 4:
        return ('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="3"/>' % (x - 45, y + 8, x + 45, y - 8, GRIS)
                + disque(x - 45, y + 20, 12, BLEU) + disque(x + 45, y + 4, 12, ROUGE) + '<path d="M%d %d V%d" stroke="%s" stroke-width="3"/>' % (x, y, y + 34, GRIS))
    return ('<path d="M%d %d C%d %d %d %d %d %d" fill="none" stroke="%s" stroke-width="3"/>' % (x - 45, y + 20, x - 10, y + 15, x + 10, y - 5, x + 45, y - 25, ROUGE)
            + '<path d="M%d %d H%d" stroke="%s" stroke-width="3"/>' % (x - 45, y + 20, x + 45, BLEU))


def parcours():
    s = ouvrir("Parcours : la sécurité selon Xavier Raufer, en %d étapes" % N) + etoiles(15)
    s += txt(640, 92, "L'insécurité et le narcotrafic, selon Xavier Raufer", 38, TEXTE, weight='600', family=SERIF)
    s += txt(640, 130, "L'entretien en %d étapes, du « risque Mexique » à la bataille des mots" % N, 19, CYAN)
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
                          "passent à l'étape précédente ou suivante. La fiche explique chaque étape, donne des repères dans la vidéo",
                          "et précise ce qui relève de l'opinion de l'invité (chaîne Front Populaire, 2024)."], 17, TEXTE, 'start', h=24)
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


TITRE = "L'insécurité et le narcotrafic, selon Xavier Raufer"
DESC = "Entretien avec le criminologue Xavier Raufer (Front Populaire, 2024) en parcours animé : le risque Mexique, les quartiers hors contrôle, la diffusion du trafic, l'impunité et les mots de l'insécurité."

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
             '<div class="badges"><span class="b">YouTube</span><span class="b">Entretien, 2024</span><span class="b b-lu">Lu en entier</span></div>\n'
             '<h1>Vidéo : « La sécurité n\'intéresse pas Emmanuel Macron » – Entretien avec Xavier Raufer</h1>\n'
             '<p class="meta">Chaîne Front Populaire · 47 min 40 s · mise en ligne le 16 juillet 2024 · série « Les rencontres de FP+ » · entretien avec le criminologue Xavier Raufer · en français · transcription automatique lue en entier · la vidéo n\'a pas de chapitres : %d repères établis d\'après la transcription</p>\n'
             '<p class="actions"><a class="bouton" href="%s" target="_blank" rel="noopener">Voir sur YouTube</a><a class="bouton bouton-2" href="%s.html">Parcours en %d étapes</a></p>\n</div>\n' % (len(CHAPITRES), yt, SUJET, N))
    h.append('<article class="fiche" id="synthese">\n<h3>Synthèse et conclusion</h3>\n<h4>Synthèse</h4>\n'
             '<p>Pour le criminologue Xavier Raufer, la France ne deviendra pas un « nouveau Mexique » : son État reste solide et le crime y est très localisé. Il le concentre dans les quartiers de la politique de la ville, et surtout dans les quartiers nord de Marseille, où le taux d\'homicides qu\'il calcule est environ quinze fois la moyenne nationale. Il y voit l\'effet d\'un trafic de cocaïne énorme et d\'un État qui, au lieu de réduire le crime là où il est, l\'aurait éparpillé vers les villes moyennes et les campagnes. Entre trafiquants, qui ne peuvent pas aller au tribunal, la concurrence se règle par l\'intimidation puis l\'homicide.</p>\n'
             '<p>Son principe : « les malfaiteurs ne s\'arrêtent que quand on les arrête ». Or, selon lui, la justice ne sanctionne plus, et même les trafiquants s\'en étonnent. Il défend aussi une façon de compter la violence (homicides et tentatives ensemble, à cause des progrès des secours) et critique un vocabulaire médiatique qui, à ses yeux, adoucit la réalité.</p>\n'
             '<h4>Conclusion</h4>\n'
             '<p>Le diagnostic de Raufer est surtout politique : le problème ne serait pas une criminalité hors de portée, mais des dirigeants qu\'il juge incompétents ou indifférents, et une justice sans moyens ni fermeté. C\'est le point de vue d\'un seul intervenant, souvent formulé de façon polémique, et plusieurs de ses affirmations sont contestées. Les précautions ci-dessous disent lesquelles.</p>\n'
             '<p class="note"><b>Voir aussi.</b> Le <a href="realisme-fiche.html">réalisme géopolitique selon Sapir et Rougeyron</a>, autre entretien de la même chaîne. Pour un regard contradictoire, à croiser avec les bilans statistiques du ministère de l\'Intérieur (SSMSI) et avec des chercheurs d\'autres écoles en criminologie et en sociologie.</p>\n</article>\n')
    h.append('<h2 class="sec" id="etapes">Les %d étapes expliquées</h2>\n' % N)
    for e in ETAPES:
        h.append('<article class="fiche etape" id="etape-%d">\n<h3><a class="num" href="%s" aria-label="Ouvrir la planche de l\'étape %d">%d</a> %s</h3>\n'
                 '<p>%s</p>\n<p class="anim"><b>Dans l\'animation.</b> %s</p>\n'
                 '<p class="liens"><a href="%s">Voir le schéma</a> · <a href="%s?t=%d" target="_blank" rel="noopener">À %s dans la vidéo</a></p>\n</article>\n'
                 % (e['n'], e['page'], e['n'], e['n'], esc(e['court']), e['texte'], esc(e['anim']), e['page'], yt, e['t'], hms(e['t'])))
    h.append('<article class="fiche" id="chapitres">\n<h3>%d repères dans la vidéo</h3>\n<p class="meta">La vidéo n\'a pas de chapitres. Ces repères et leurs horodatages sont établis d\'après la transcription.</p>\n<ul class="chap">\n' % len(CHAPITRES))
    for t, ti, r in CHAPITRES:
        h.append('<li><a href="%s?t=%d" target="_blank" rel="noopener">%s</a> <b>%s.</b> %s</li>\n' % (yt, t, hms(t), esc(ti), r))
    h.append('</ul>\n</article>\n')
    h.append('<article class="fiche" id="precautions">\n<h3>Précautions</h3>\n'
             '<p class="note">C\'est un entretien d\'opinion publié par Front Populaire, média souverainiste, avec un seul invité et sans contradicteur ; le titre de la vidéo reprend un jugement de l\'invité. La version publiée sur YouTube est un extrait : l\'entretien complet est réservé aux abonnés, et la vidéo se termine par quelques phrases de cette suite. Xavier Raufer est un criminologue connu pour ses positions très critiques sur la politique pénale. Ses jugements sur Emmanuel Macron, Gérald Darmanin, Éric Dupond-Moretti ou les journalistes sont rapportés comme ses opinions ; les qualificatifs injurieux employés dans la vidéo (contre des ministres, des sociologues, des médias ou la justice) ne sont pas repris.</p>\n'
             '<p class="note">Affirmations très discutées. Quand il dit que la délinquance de voie publique serait le fait d\'étrangers dans une écrasante majorité, il ne donne pas de chiffre précis. Les statistiques publiques du ministère de l\'Intérieur (SSMSI) montrent une surreprésentation des étrangers parmi les personnes mises en cause pour certains vols, surtout dans les transports, mais pas dans de telles proportions pour l\'ensemble de cette délinquance. La dispersion volontaire de personnes sans statut vers la province « pour les Jeux olympiques » et son effet sur le trafic dans les campagnes sont présentés sans source. Le rôle qu\'il prête à la propriété des médias relève de l\'opinion.</p>\n'
             '<p class="note">Chiffres cités dans la vidéo et non vérifiés ici : 1 300 à 1 350 quartiers de la politique de la ville ; 116 tonnes de cocaïne saisies à Anvers en 2023 (chiffre proche de celui annoncé par les douanes belges ; il dit aussi 113 tonnes) ; 700 à 800 tonnes entrées chaque année en Europe ; 60 euros le gramme ; 44 homicides en 2023 dans les quartiers nord de Marseille (il donne 250 000 puis 150 000 habitants : le taux de 17,5 pour 100 000 correspond à 250 000) ; 1,15 homicide pour 100 000 habitants en France ; +110 % d\'homicides et tentatives en vingt ans ; +6 % par an de coups et blessures hors famille de 2017 à 2023 ; 70 % puis 30 % de risque de mourir avant l\'opération ; 75 % de Français mécontents ; moins de procureurs par habitant qu\'en Albanie. L\'absence de commissariat dans les quartiers nord de Marseille est aussi son affirmation.</p>\n'
             '<p class="note">La transcription est automatique. J\'ai lu « Xavier offer » et « refire » comme Xavier Raufer, « Darman » comme Darmanin, « dupom Moretti » comme Dupond-Moretti, « hatal » comme Attal, « enverse » et « renverse » comme Anvers, « Godon a un coup de pied » comme « donner un coup de pied », « Beltram » comme Beltrame, « fleurerogis » comme Fleury-Mérogis, « mafzoli » comme Maffesoli et « le Casco » comme le SIRASCO, service de la police nationale sur le crime organisé. L\'affaire des étudiants disparus au Mexique est celle d\'Ayotzinapa (2014), que la vidéo ne nomme pas.</p>\n</article>\n')
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

