---
title: "Des milliers de petites STEP possibles en Europe : où, combien, et ce que le karst change"
titre_recherche: "Petites STEP en Europe : combien, où, et pourquoi le karst compte"
key: stockage
ref: micro-step
tags: petites STEP, STEP, stockage d'électricité, pompage-turbinage, hydroélectricité, karst, relief numérique, SIG, Europe, Applied Energy
article_header:
  type: cover
  image:
    src: /assets/images/Posts/2026-11-02/micro_step_banner.png
---
<span class="summary" style="display:block; text-align: justify">
Résumé -- Une STEP (Station de Transfert d'Énergie par Pompage, pas une station d'épuration !) stocke l'électricité en remontant de l'eau d'un bassin à un autre, puis en la turbinant quand on en a besoin. En Europe, les grands sites sont souvent pris ou difficiles à faire accepter ; on peut aussi chercher du côté des petits : un lac et une cuvette naturelle, ou deux cuvettes, distants de quelques kilomètres, avec quelques dizaines de mètres de dénivelé. Avec Antoine Rogeau (Mines Paris) et Emanuele Quaranta (Centre commun de recherche de la Commission européenne), nous venons de publier dans Applied Energy, en accès libre, le premier inventaire européen de ces petites STEP [\[1\]](#note-1). Sur 37 pays, notre méthode retient 21 115 sites, qui stockeraient ensemble 0,40 TWh, dont 0,24 TWh dans l'Union européenne : de l'ordre de la moitié du stockage réellement utilisable des grandes STEP de l'Union. J'explique ici comment on trouve ces sites sur une carte, pourquoi il faut se méfier des cuvettes sèches posées sur du calcaire — c'est le karst, ces plateaux calcaires qui sont comme du gruyère —, et pourquoi le total dépend d'abord de deux choix : la distance admise entre les bassins et le sort réservé au karst. C'est un gisement réel, mais cher et souvent loin des consommateurs, que les études de terrain ne pourront que réduire : un outil pour savoir où chercher, pas une promesse.
</span>
<!--more-->

## Stocker l'électricité en remontant de l'eau

<span class="mytext">
**Une STEP, c'est une batterie faite de deux bassins et d'un dénivelé.** Une station de transfert d'énergie par pompage relie deux réservoirs situés à des altitudes différentes. Quand l'électricité est abondante, une pompe remonte l'eau du bassin bas vers le bassin haut ; quand on en a besoin, on la laisse redescendre dans une turbine, qui est souvent la même machine tournant dans l'autre sens. On ne récupère pas tout : sur le parc de l'Union européenne, environ 70 % de l'électricité consommée pour pomper revient au réseau [\[2\]](#note-2).
</span>

<span class="mytext">
**C'est la forme dominante du stockage d'électricité de longue durée.** Les STEP dépassaient 200 GW dans le monde fin 2025, même si les batteries progressent très vite. La France en compte six grandes, pour environ 5 GW, dont Grand'Maison, en Isère, la plus puissante (environ 1 800 MW en turbinage), et Montézic, en Aveyron, que nous retrouverons à propos du karst [\[3\]](#note-3).
</span>

<span class="mytext">
**Si l'on en reparle, c'est que le solaire et l'éolien demandent de la flexibilité.** Un système électrique qui repose de plus en plus sur des productions variables doit pouvoir déplacer l'énergie dans le temps, et le Centre commun de recherche (JRC) de la Commission européenne estime que les besoins de flexibilité de l'Union seront multipliés plusieurs fois d'ici 2050 [\[4\]](#note-4). Une STEP fait exactement cela à l'échelle de la journée : elle pompe le surplus solaire de midi et le rend le soir. En France, on les a développées pour pouvoir pomper la nuit et permettre à nos centrales nucléaires de tourner à plein régime.
</span>

<span class="mytext">
**Mais les grands sites sont souvent pris ou difficiles à faire accepter.** Le parc de STEP de l'Union européenne est souvent crédité de 1,3 TWh de stockage, mais ce qui est réellement utilisable serait plutôt de 0,5 à 0,6 TWh. Il reste de grands sites possibles, mais les évaluations récentes convergent : les sites les plus favorables sont déjà exploités, et les meilleures options d'extension consistent à valoriser des réservoirs existants plutôt qu'à en construire de grands nouveaux [\[2\]](#note-2). C'est ce que fait EDF à Montézic : le projet Montézic 2 y creuserait une seconde centrale souterraine entre les deux mêmes réservoirs, pour 460 MW de plus et une mise en service visée en 2035 [\[3\]](#note-3). D'où la recherche de gisements « alternatifs » : des paires de réservoirs existants, des circuits fermés construits hors des rivières, des mines désaffectées, des réservoirs agricoles. C'est dans cette famille que se range notre travail.
</span>

## Et si l'on faisait petit ?

<span class="mytext">
**Une petite STEP, c'est le même principe, à l'échelle d'un étang.** Nous appelons ainsi une STEP en circuit fermé — l'eau fait l'aller-retour entre deux bassins — dont chaque bassin couvre au plus 1 km², soit 100 hectares [\[5\]](#note-5). Chacun des deux bassins est soit un lac qui existe déjà, soit une cuvette naturelle du relief que l'on rendrait étanche pour la remplir. Dans notre scénario de référence, un site stocke de 5 à 100 MWh. Vidé en huit heures, cela fait de 0,6 à 12,5 MW, et 1,3 MW pour le site médian, quand une grande STEP en compte des centaines.
</span>

<span class="text" id="Figure1" style="display:block;text-align:center">
![Le principe d'une petite STEP]({{site.baseurl}}/assets/images/Posts/2026-11-02/micro_step_principe.png){:.border width="90%"}
</span>

<span class="legendtext" id="CAPFigure1" style="display:block;text-align:center">
**Figure 1** -- Le principe d'une petite STEP. Quand l'électricité est abondante, la machine pompe l'eau du bassin bas vers le bassin haut ; quand on en a besoin, la même machine turbine l'eau qui redescend. Ici le bassin bas est un lac existant, dont on ne fait varier le niveau que d'un mètre, et le bassin haut une cuvette naturelle rendue étanche. Les seuils sont ceux de notre scénario de référence : au moins 40 m de chute, au plus 3,5 km entre les bassins, une ligne électrique à moins de 5 km.
</span>

<span class="mytext">
**Un ordre de grandeur, pour fixer les idées.** L'énergie stockée est celle de l'eau qu'on a montée : sa masse, multipliée par la gravité et par la hauteur de chute. C'est peu : un mètre cube qui redescend de 82 m, la chute médiane de nos sites, ne fournit que 0,22 kWh, et il faut donc près de 4 500 m³ par mégawattheure. Un site de 11 MWh, l'énergie médiane de nos sites, demande ainsi environ 50 000 m³ d'eau qui font l'aller-retour : un étang de 5 hectares sur un mètre de profondeur [\[6\]](#note-6).
</span>

<span class="mytext">
**Personne n'en avait estimé le potentiel à l'échelle de l'Europe.** Les grands atlas les écartent par construction. L'atlas mondial des STEP en circuit fermé de l'Université nationale australienne ne retient que des réservoirs de plus d'un million de mètres cubes et des sites de 2 à 150 GWh, et il commence par « remplir » le relief avant de chercher, ce qui efface précisément les cuvettes que nous cherchons ; l'évaluation européenne des paires de réservoirs existants ne garde que les réservoirs de plus de 100 000 m³ et les chutes de plus de 150 m [\[7\]](#note-7). Le seul inventaire continental à petite échelle, en Australie, apparie des réservoirs agricoles distants de moins de 500 m : 30 295 sites pour 3,3 GWh, un gisement d'une autre nature, complémentaire du nôtre. Notre méthode est celle que nous avions mise au point en 2017 pour la France avec Antoine Rogeau et Georges Kariniotakis [\[8\]](#note-8), étendue ici à 37 pays et revue sur plusieurs points.
</span>

## Comment on cherche : verser de l'eau sur une carte

<span class="mytext">
**Tout part d'un relief numérique.** C'est une carte des altitudes du sol, ici sur une grille de 30 m de côté pour toute l'Europe, et de 10 m en Norvège et en Suède, où nous avons utilisé les relevés lidar nationaux. L'algorithme la « remplit » comme on verserait de l'eau sur une maquette en relief : partout où l'eau resterait sans déborder, il y a une cuvette fermée. Nous gardons celles qui font entre 2 500 m² et 1 km² et plus d'un mètre de profondeur. Les lacs existants viennent de la carte européenne d'occupation des sols, CORINE Land Cover [\[9\]](#note-9).
</span>

<span class="mytext">
**On forme ensuite des couples.** Un bassin haut et un bassin bas, à moins de 3,5 km l'un de l'autre, avec au moins 40 m de chute et une ligne électrique à moins de 5 km. Un lac existant ne peut monter ou descendre que d'un mètre — c'est notre hypothèse de référence, que nous faisons varier de 0,5 à 5 m — et son volume utile est donc sa surface multipliée par un mètre. C'est l'un des changements par rapport à 2017, où nous prenions une fraction fixe du volume, y compris pour les lacs naturels. Une paire doit stocker au moins 5 MWh.
</span>

<span class="mytext">
**On retire ce qui ne peut pas accueillir de bassin.** Les aires strictement protégées, les zones bâties et industrielles, les bassins hauts à plus de 2 500 m d'altitude, où névés et cirques glaciaires faussent le relief, et les cuvettes sur karst, dont je parle plus bas. Les parcs naturels et les sites Natura 2000 restent dans la référence, mais nous mesurons à part ce que coûterait de les exclure.
</span>

<span class="mytext">
**Enfin, on choisit sans compter deux fois le même bassin.** Un même lac peut figurer dans des dizaines de couples candidats, mais il ne peut servir qu'une fois. Choisir l'ensemble de couples qui stocke le plus d'énergie, chaque bassin n'étant utilisé qu'une fois, est un problème classique de la théorie des graphes, le « couplage de poids maximal » ; nous le résolvons exactement, en quelques secondes pour tout le continent [\[10\]](#note-10). Des 670 654 couples candidats, la référence retient 21 115 sites. Ils se rangent en trois grandes familles : ceux qui utilisent un lac existant, les grandes cuvettes sèches et les petites cuvettes sèches (figure 2).
</span>

<span class="text" id="Figure2" style="display:block;text-align:center">
![Trois sites types]({{site.baseurl}}/assets/images/Posts/2026-11-02/trois_types_de_sites.png){:.border width="90%"}
</span>

<span class="legendtext" id="CAPFigure2" style="display:block;text-align:center">
**Figure 2** -- Trois sites réels, les plus représentatifs de chacune des trois familles de la référence : un site avec un lac existant (3 559 sites, 109 GWh au total), une grande cuvette sèche (6 493 sites, 204 GWh) et une petite cuvette sèche (11 063 sites, 92 GWh). En bleu, un lac existant ; en orange, une cuvette à aménager ; en pointillés, la liaison en ligne droite entre les deux bassins.
</span>

<span class="mytext">
**La leçon la plus inattendue est venue du relief lui-même.** Un relief numérique qui « voit » les arbres et les bâtiments invente des cuvettes : en France, le modèle de surface de Copernicus donne cinq fois le gisement que l'on obtient avec le relief lidar national de l'IGN (394 GWh contre 72). FABDEM, une version du même modèle dont les arbres et les bâtiments ont été retirés par apprentissage automatique, ne s'écarte plus que de 17 % de la référence nationale (60 GWh contre 72), et c'est lui que nous avons retenu pour l'Europe. Mais cela ne suffit pas partout. En Norvège, l'erreur verticale typique de FABDEM, autour de 5 m, est plusieurs fois supérieure au mètre de profondeur qui définit une cuvette : avec le lidar national, la moitié des cuvettes détectées disparaissent, avec les deux tiers de leur volume, et le gisement norvégien perd 72 % (de 329 à 92 GWh). La Suède perd 72 % elle aussi. Les lacs, eux, ne bougent pas : ce sont les cuvettes sèches qui s'évanouissent. Pour chercher de petites cuvettes, la précision verticale du relief compte plus que sa résolution [\[11\]](#note-11).
</span>

## Le karst, ou pourquoi une cuvette sèche est suspecte

<span class="mytext">
**Le karst est un paysage creusé par l'eau qui dissout le calcaire.** L'eau de pluie, chargée de gaz carbonique, est légèrement acide : elle dissout le calcaire et la dolomie (le gypse, lui, se dissout dans l'eau pure). Au fil des millénaires, elle élargit les fissures, creuse des puits verticaux, les avens, des grottes et des rivières souterraines, puis ressort plus bas par des sources, les résurgences. En surface, hors des canyons, il reste des plateaux secs, sans rivière, criblés de cuvettes fermées : les dolines. Le mot vient de *Karst*, le nom allemand du Kras, un plateau calcaire de Slovénie qui se prolonge en Italie au-dessus de Trieste. En France, les roches carbonatées affleurent sur environ un tiers du territoire, et sur près de la moitié si l'on compte celles que recouvrent d'autres terrains [\[12\]](#note-12) : les Grands Causses, le Jura, le Vercors, le causse de Gramat et son gouffre de Padirac, ou encore la Fontaine de Vaucluse, la source karstique au plus fort débit moyen de France. Sur les Grands Causses, les dolines ont un nom occitan, les sotchs, et leur fond d'argile, la meilleure terre du plateau, est souvent cultivé (figure 3).
</span>

<span class="text" id="Figure3" style="display:block;text-align:center">
![Une doline sur le causse de Sauveterre]({{site.baseurl}}/assets/images/Posts/2026-11-02/doline_causse_sauveterre.jpg){:.border width="90%"}
</span>

<span class="legendtext" id="CAPFigure3" style="display:block;text-align:center">
**Figure 3** -- Une doline, ou sotch, sur le causse de Sauveterre, en Lozère : une cuvette fermée au fond plat, tapissé d'argile et cultivé, au milieu d'un plateau calcaire sec. C'est le genre de cuvette que notre algorithme détecte. Photo : [Myrabella / Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Causse_de_Sauveterre_doline.jpg), licence [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/), redimensionnée.
</span>

<span class="text" id="Figure4" style="display:block;text-align:center">
![Le karst]({{site.baseurl}}/assets/images/Posts/2026-11-02/karst_schema.png){:.border width="90%"}
</span>

<span class="legendtext" id="CAPFigure4" style="display:block;text-align:center">
**Figure 4** -- Le karst. L'eau de pluie dissout le calcaire, élargit les fissures et creuse un réseau souterrain qui ressort plus bas, à une résurgence. En surface, les dolines sont des cuvettes fermées parce que l'eau s'en va par le fond : un bassin construit là fuirait. Un lac qui existe déjà sur le karst prouve au contraire que son fond tient l'eau, et une cuvette sur roche imperméable la garde.
</span>

<span class="mytext">
**Pour notre algorithme, un plateau karstique ressemble au paradis.** Il cherche des cuvettes fermées, et le karst en est plein. Mais une doline est fermée précisément parce que l'eau s'en va par le fond : c'est un entonnoir vers la nappe. Un bassin construit là fuirait, et remplir puis mettre en pression une masse de calcaire karstique peut provoquer des effondrements, des affaissements, voire des séismes induits [\[13\]](#note-13).
</span>

<span class="mytext">
**Le Vajont rappelle ce que coûte un versant mal compris.** Le 9 octobre 1963 à 22 h 39, dans les Alpes du nord-est de l'Italie, environ 260 millions de m³ du mont Toc ont glissé dans la retenue du barrage du Vajont, haut de 262 m. Quelque 50 millions de m³ d'eau ont franchi le barrage, qui a tenu, et rasé Longarone, dans la vallée du Piave : 1 917 morts selon le bilan officiel, jusqu'à 2 500 selon d'autres estimations. Ce n'est pas une fuite par le karst, mais un versant de calcaires et de couches argileuses inclinées vers la vallée, que la mise en eau a déstabilisé malgré un premier glissement d'environ 800 000 m³ en 1960 (figure 5) [\[13\]](#note-13).
</span>

<span class="text" id="Figure5" style="display:block;text-align:center">
![Le glissement du Vajont]({{site.baseurl}}/assets/images/Posts/2026-11-02/vajont_schema.png){:.border width="90%"}
</span>

<span class="legendtext" id="CAPFigure5" style="display:block;text-align:center">
**Figure 5** -- Le glissement du Vajont, en coupe schématique à travers la gorge. Le versant du mont Toc glisse le long de couches argileuses inclinées vers la vallée et chasse l'eau de la retenue, qui remonte le versant opposé puis passe par-dessus le barrage, en aval. Schéma réalisé pour ce billet, pas à l'échelle.
</span>

<span class="mytext">
**Notre règle : on exclut les bassins à construire sur du karst, pas les lacs qui s'y trouvent déjà.** Nous utilisons la carte européenne des aquifères karstiques, WOKAM [\[12\]](#note-12). Un couple est écarté dès que l'emprise d'un bassin qu'il faudrait construire touche le karst cartographié. Un lac existant posé sur du karst, lui, est gardé : s'il garde l'eau, c'est que son fond est étanche, et la preuve est faite.
</span>

<span class="mytext">
**En 2017, notre étude française retenait les Grands Causses. C'étaient des dolines.** Le Massif central le montre bien (figure 6). Au sud, presque toutes les cuvettes détectées sont sur les calcaires des Grands Causses, et le filtre du karst retire environ 94 % du gisement sec de la région. Ce qui reste est au nord, sur le socle cristallin imperméable, là même où se trouvent les barrages de Sarrans et de Grandval et la STEP de Montézic, exploitée par EDF. Notre première étude, sans filtre du karst, gardait les cuvettes du sud [\[14\]](#note-14).
</span>

<span class="text" id="Figure6" style="display:block;text-align:center">
![Le karst et le Massif central]({{site.baseurl}}/assets/images/Posts/2026-11-02/massif_central_karst.png){:.border width="80%"}
</span>

<span class="legendtext" id="CAPFigure6" style="display:block;text-align:center">
**Figure 6** -- Le filtre du karst dans le Massif central. En rouge, les cuvettes sèches posées sur les calcaires karstiques (en ocre) : elles sont exclues, et elles se concentrent sur les Grands Causses. En bleu et en vert, les sites gardés, sur le socle imperméable du nord, comme les ouvrages hydroélectriques existants de la région. Calcul sur les données nationales françaises (voir la note 14).
</span>

<span class="mytext">
**Le karst n'est pas un interdit absolu.** Les ingénieurs savent construire des réservoirs dans le karst, avec des voiles d'injection et le colmatage des points de perte, comme à Buško Blato, en Bosnie-Herzégovine ; d'autres réservoirs perdent leur eau depuis leur construction, comme celui de Boljunčica, en Croatie [\[13\]](#note-13). Notre règle est une règle de précaution, pas un verdict, et le total sans karst est une borne basse. Accepter tout le karst multiplierait le gisement par 2,5 (1,02 TWh au lieu de 0,40) et ferait entrer le Monténégro, la Bosnie-Herzégovine et la Croatie dans le peloton de tête : c'est le karst dinarique. N'accepter les cuvettes karstiques que lorsqu'elles jouxtent un lac karstique existant n'ajoute que 8 %, parce que la plupart sont loin de tout lac. La vraie question, que nous laissons ouverte, est donc celle-ci : sait-on rendre étanches de petits bassins sur du karst, à un coût acceptable ?
</span>

## Combien ? Tout dépend de ce qu'on compte

<span class="mytext">
**Le chiffre le plus large n'a pas grand sens.** Avec un mètre de marnage sur les lacs et une ligne électrique à moins de 5 km, la sélection la plus large retient 45 428 sites et 2,57 TWh, mais elle contient encore le karst et de très grands sites. Sans les cuvettes sur karst ni les bassins au-dessus de 2 500 m, il reste 21 268 sites et 0,58 TWh. Plafonner chaque site à 100 MWh, pour rester à la petite échelle qui nous intéresse, donne notre référence : 21 115 sites, 0,40 TWh, dont 14 160 sites et 0,24 TWh dans l'Union européenne (figure 7).
</span>

<span class="text" id="Figure7" style="display:block;text-align:center">
![Le gisement selon ce que l'on compte]({{site.baseurl}}/assets/images/Posts/2026-11-02/cascade_gisement.png){:.border width="90%"}
</span>

<span class="legendtext" id="CAPFigure7" style="display:block;text-align:center">
**Figure 7** -- Le gisement selon ce que l'on compte, en TWh d'énergie hydraulique brute, pour les 37 pays étudiés et pour l'Union européenne. Chaque barre ajoute un filtre aux précédents et refait toute la sélection : ce ne sont pas des soustractions. Les trois dernières barres sont des scénarios, pas la référence.
</span>

<span class="mytext">
**Trois autres filtres, qu'une étude continentale peut chiffrer sans pouvoir les trancher.** Exclure aussi les sites Natura 2000 et les autres aires protégées, parcs compris, coûte 30 % de l'énergie, 40 % dans l'Union européenne mais 9 % seulement en Norvège, dont le gisement est en grande partie hors de ces zones. Écarter les cuvettes à moins de 20 m d'une rivière ou d'un canal — une cuvette traversée par un cours d'eau n'est pas fermée, et la barrer ferait une retenue sur la rivière — retire encore 64 GWh. Le filtre le plus sévère est hydraulique : 86 % de l'énergie de la référence se trouve dans des couples dont la distance dépasse dix fois la chute, c'est-à-dire de longues conduites pour peu de dénivelé, coûteuses et sources de pertes. Ne garder que les couples où la distance vaut au plus dix fois la chute laisse 2 811 sites et 73 GWh, moins d'un cinquième de la référence [\[15\]](#note-15).
</span>

<span class="mytext">
**Pour situer ces chiffres : un peu moins d'une heure de consommation de l'Union, mais près de la moitié de ses grandes STEP.** Les 0,24 TWh de l'Union européenne représentent un peu moins d'une heure de sa consommation moyenne d'électricité. Mais c'est de l'ordre de la moitié du stockage réellement utilisable de toutes ses grandes STEP, plusieurs fois son parc de batteries raccordées au réseau au milieu de la décennie, et c'est du même ordre que le gisement des paires de réservoirs existants, évalué à 141 GWh pour l'Union à des distances comparables [\[16\]](#note-16). Ce stockage servirait des cycles quotidiens ou de quelques jours, pas à passer l'hiver.
</span>

<span class="mytext">
**Deux choix pèsent plus que tous les autres : la distance entre les bassins et le karst.** Nous avons fait varier ensemble huit paramètres de la méthode et refait 40 000 fois la sélection continentale. La distance maximale entre les bassins et le traitement du karst expliquent à eux deux l'essentiel des écarts, loin devant la distance au réseau et le plafond de taille des sites ; le marnage admis sur les lacs et le plafond d'altitude ne changent presque rien au total continental, même s'ils comptent site par site. Selon les combinaisons, le total va de moins d'un gigawattheure à plus de 2 TWh. C'est pourquoi nous publions des courbes et des scénarios plutôt qu'un chiffre unique [\[17\]](#note-17).
</span>

## Où ? Au nord, et dans les montagnes

<span class="mytext">
**La Norvège arrive en tête, la France deuxième.** La Norvège porte 92 GWh, 23 % du total, devant la France (60 GWh), l'Allemagne (34), le Royaume-Uni (29), l'Autriche et la Suède (19 chacune). Le gisement s'étend sur 165 régions de 35 pays, mais il se concentre dans le centre et le sud de la Norvège et en Islande, puis le long des Alpes, des Pyrénées, des Carpates et des Balkans (figure 8). Les 34 GWh de l'Allemagne, eux, sont dispersés en petites quantités sur une multitude de collines.
</span>

<span class="text" id="Figure8" style="display:block;text-align:center">
![Où se trouve le gisement]({{site.baseurl}}/assets/images/Posts/2026-11-02/carte_europe_micro_step.png){:.border width="90%"}
</span>

<span class="legendtext" id="CAPFigure8" style="display:block;text-align:center">
**Figure 8** -- L'énergie stockable des 21 115 sites de la référence, en GWh pour 1 000 km², sur une grille régulière de 50 km de côté (une grille évite les biais des découpages administratifs, de tailles très inégales). Les hachures marquent les grands massifs calcaires karstiques, où les cuvettes sèches sont exclues.
</span>

<span class="mytext">
**« Distribué » ne veut pas dire « près des consommateurs ».** Les sites sont petits et dispersés, mais loin des grandes villes et du parc existant : un site est en médiane à une centaine de kilomètres de la STEP existante la plus proche, quand les STEP existantes sont à 29 km les unes des autres, et 11 % seulement sont à moins de 25 km d'une STEP. Ils se trouvent dans des régions moins peuplées, plus ventées et moins ensoleillées que celles des STEP existantes. Une complémentarité avec l'éolien régional est plausible, mais la démontrer demanderait de modéliser le réseau et son fonctionnement heure par heure, pas de superposer des cartes.
</span>

<span class="mytext">
**En France, 3 849 sites et 60 GWh, presque tous dans des cuvettes sèches.** Sur ces 60 GWh, 54 viennent de couples de deux cuvettes et 5 seulement de couples avec un lac — mais la carte européenne des lacs ne voit pas les petits plans d'eau, et ce gisement lacustre est une borne basse. Deux traits français ressortent : le réseau est proche (un poste électrique à 1,6 km en médiane), et plus de la moitié de l'énergie (54 %) est en Natura 2000 ou dans une aire protégée. En France, la question environnementale pèsera lourd [\[18\]](#note-18).
</span>

## À quel prix ?

<span class="mytext">
**C'est un gisement cher.** Nous avons ajouté à l'étude un modèle de coût simple et transparent, appliqué site par site, dont les résultats sont indicatifs [\[19\]](#note-19). Le site médian coûterait environ 1 150 € par kilowattheure de stockage pour une décharge en huit heures (1 620 € en quatre heures), plusieurs fois les fourchettes publiées pour les grandes STEP européennes. Le coût complet du stockage irait de 0,30 à 1,29 € par kilowattheure restitué selon les conditions de financement.
</span>

<span class="mytext">
**Ce n'est pas le bassin qui coûte, ce sont les tuyaux.** C'est contre-intuitif pour une technologie qui consiste à construire des réservoirs : pour une décharge en huit heures, la conduite pèse 44 % de l'investissement direct et les machines 30 %, les bassins 20 % et le raccordement 5 %. Les unités sont petites (1,3 MW en médiane, contre des centaines de mégawatts pour les grandes STEP) et la chute est faible au regard de la distance : en médiane, la distance entre les bassins vaut 32 fois la chute, soit des kilomètres de conduite pour quelques mégawatts. Des membranes d'étanchéité moins chères ne rendront pas ces sites bon marché. Cette répartition est celle de notre modèle, qui part de cuvettes naturelles et ne compte qu'un terrassement modeste : là où il faudrait des digues ou de gros déblais, les bassins pèseraient plus lourd, et les sites coûteraient plus cher encore [\[19\]](#note-19).
</span>

<span class="mytext">
**Ce qui est solide, c'est l'ordre, pas le montant.** Les deux familles les moins chères, avec un lac ou avec une grande cuvette sèche, coûtent environ 830 à 840 € par kilowattheure en médiane, contre 1 420 € pour les petites cuvettes sèches, et cet écart résiste à une variation de 50 % de chaque coût unitaire. La part du gisement sous un seuil de coût, elle, varie d'un facteur neuf avec les mêmes hypothèses : nous ne la donnons pas.
</span>

<span class="mytext">
**Et les petites machines ont un moins bon rendement.** À petite échelle, on peut utiliser des pompes ordinaires tournant à l'envers en guise de turbine, moins chères : une étude de cas a mesuré un rendement aller-retour de 42 à 50 %, contre environ 70 % en moyenne pour le parc européen [\[20\]](#note-20). Nos chiffres sont des énergies brutes, avant ces pertes.
</span>

## Ce que cette étude est, et ce qu'elle n'est pas

<span class="mytext">
**Un premier criblage, pas un potentiel exploitable.** Notre travail dit où regarder, il ne dit pas ce qu'on peut construire. Aucun site n'a été visité. Nous avons validé la méthode sur la France, où l'on peut comparer données nationales et européennes, sur la Norvège, avec l'inventaire national des lacs et le relief lidar, et sur la Suède, avec son relief lidar ; les 34 autres pays n'ont pas été recoupés avec des données nationales.
</span>

<span class="mytext">
**Tout ce qu'une étude de terrain ajoutera ne pourra que réduire ces chiffres.** Il faudra connaître la profondeur des lacs et le marnage qu'on peut y admettre, le tracé réel des conduites, la géotechnique de chaque emprise, la capacité des postes électriques voisins à accueillir quelques mégawatts dans les deux sens — un poste proche ne dit pas que le réseau peut les absorber —, le coût réel de chaque site et sa valeur pour le système électrique.
</span>

<span class="mytext">
**Les données et le code sont ouverts.** L'article est en accès libre, le code est publié, et les couches de sites candidats, pays par pays, sont archivées [\[1\]](#note-1). Qui travaille sur un territoire peut y chercher ses sites.
</span>

<span class="mytext">
**Ce que j'en retiens.** Le relief européen contient bien un gisement de petites STEP que les atlas ignoraient, du même ordre que celui des paires de réservoirs existants qu'ils avaient décrit. Mais ce n'est ni un gisement bon marché, ni un gisement proche des consommateurs, et sa taille dépend d'abord d'une question géologique, le karst, et d'une question hydraulique, la distance. Si les petites STEP ont un avenir, il est dans la fraction des sites qui cumulent un lac, une bonne chute sur une courte distance, un poste électrique proche et un sol qui tient l'eau, et c'est précisément ces sites-là que notre inventaire permet de trouver.
</span>

## Notes

<span id="note-1">[1]</span> R. Girard, A. Rogeau, E. Quaranta, [« Distributed small-reservoir pumped-storage hydropower in Europe: a GIS screening under drawdown and karst constraints »](https://doi.org/10.1016/j.apenergy.2026.129193), Applied Energy, vol. 427, 129193, 2027 (en ligne le 27 octobre 2026), en accès libre sous licence CC BY 4.0. Le code (R et Snakemake, licence MIT) est sur le [dépôt du projet](https://git.persee.minesparis.psl.eu/energy-alternatives/Micro-Hydo-Pumped-Storage-EU) ; les couches de sites candidats par pays, les sélections et les résultats des scénarios sont archivés sur [Zenodo](https://doi.org/10.5281/zenodo.21326693) (licence CC BY-NC-SA 4.0). Tous les chiffres de ce billet viennent de l'article et de son supplément, sauf mention contraire. Ce sont des énergies hydrauliques brutes, sans rendement de pompage ni de turbinage.

<span id="note-2">[2]</span> E. Quaranta, R. M. Boes, J. D. Hunt, S. Szabó, J. Tattini, A. Pistocchi, « Considerations on the existing capacity and future potential for energy storage in the European Union's hydropower reservoirs and pumped-storage hydropower », Journal of Energy Storage, vol. 104, 114431, 2024. Le rendement aller-retour de 0,71 est la moyenne du parc de l'Union pondérée par la puissance. Les comparaisons avec le parc existant sont indicatives : ses chiffres décrivent une électricité stockable sous les contraintes d'exploitation réelles de chaque centrale, les nôtres une énergie hydraulique brute.

<span id="note-3">[3]</span> Monde : 201 GW de STEP fin 2025, dont 11,7 GW mis en service dans l'année, selon l'International Hydropower Association, [2026 World Hydropower Outlook](https://www.hydropower.org/publications/2026-world-hydropower-outlook), et [son communiqué du 24 juin 2026](https://www.hydropower.org/news/year-of-the-water-battery-global-pumped-storage-capacity-surpasses-200-gw). France : six STEP pour 5 GW, d'après le [rapport du Sénat n° 498 (2025-2026)](https://www.senat.fr/rap/l25-498/l25-4981.pdf), p. 140, qui reprend la liste d'EDF : Grand'Maison (1 790 MW), Montézic (910 MW), Super-Bissorte (730 MW), Revin (720 MW), Le Cheylas (460 MW) et La Coche (330 MW). La puissance de Grand'Maison est celle du turbinage : seuls 8 de ses 12 groupes peuvent pomper. Projets d'EDF : Montézic 2, deux groupes turbine-pompe et 460 MW de plus, mise en service visée en 2035, soumis à concertation préalable du 23 septembre au 5 novembre 2026 ([site de la concertation](https://www.concertation-montezic2.fr/)) ; dans le Jura, Vouglans/Saut-Mortier, une pompe-turbine qui relie les retenues de Coiselet, Saut-Mortier et Vouglans sur l'Ain, travaux de 2026 à 2031 ([International Water Power](https://www.waterpowermagazine.com/news/vouglans-saut-mortier-pumped-storage-project-to-receive-new-andritz-pump-turbine/), en anglais).

<span id="note-4">[4]</span> D. Koolen, M. De Felice, S. Busch, *Flexibility requirements and the role of storage in future European power systems*, Office des publications de l'Union européenne, JRC, 2023.

<span id="note-5">[5]</span> Il n'existe pas de frontière admise entre « micro », « mini » et « petite » STEP : nous avons donc pris une définition physique, des bassins d'au plus 1 km² chacun, et nous donnons les résultats par classe d'énergie (sites plafonnés à 100 MWh, 500 MWh, 1 GWh, ou sans plafond). La référence plafonne chaque site à 100 MWh. Pour une décharge en quatre heures, les puissances vont de 1,3 à 25 MW (2,6 MW en médiane). Au sens du code de réseau européen sur le raccordement des installations de production (règlement (UE) 2016/631), un module de cette taille raccordé sous 110 kV est de type B en Europe continentale et en Grande-Bretagne, de type B ou C dans la zone nordique.

<span id="note-6">[6]</span> L'énergie hydraulique brute d'un couple vaut ρ g H V, avec ρ = 1 000 kg/m³, g = 9,81 m/s², H la chute brute et V le volume transférable, le plus petit des volumes utiles des deux bassins : 1 000 × 9,81 × 82 J par m³, soit 0,22 kWh/m³ à 82 m. L'énergie médiane des sites de la référence est de 11,0 MWh et leur chute médiane de 82 m ; 11 MWh à 82 m correspondent à 49 000 m³ environ. Ces deux médianes sont calculées séparément : le volume du « site médian » n'est qu'un ordre de grandeur.

<span id="note-7">[7]</span> B. Lu, M. Stocks, A. Blakers, K. Anderson, « Geographic information system algorithms to locate prospective sites for pumped hydro energy storage », Applied Energy, vol. 222, p. 300-312, 2018 ; M. Stocks, R. Stocks, B. Lu, C. Cheng, A. Blakers, « Global Atlas of Closed-Loop Pumped Hydro Energy Storage », Joule, vol. 5, p. 270-284, 2021 ; M. Gimeno-Gutiérrez, R. Lacal-Arántegui, « Assessment of the European potential for pumped hydropower energy storage based on two existing reservoirs », Renewable Energy, vol. 75, p. 856-868, 2015 ; N. Gilmore et al., « Continental-scale assessment of micro-pumped hydro energy storage using agricultural reservoirs », Applied Energy, vol. 349, 121715, 2023 (30 295 sites, 3,3 GWh, soit 0,11 MWh par site en moyenne).

<span id="note-8">[8]</span> A. Rogeau, R. Girard, G. Kariniotakis, « A generic GIS-based method for small Pumped Hydro Energy Storage (PHES) potential evaluation at large scale », Applied Energy, vol. 197, p. 241-253, 2017. Par rapport à cette étude nationale, l'article de 2026 change d'échelle (37 pays, avec le coût de chaque substitution de données mesuré sur la France, la Norvège et la Suède), ajoute trois filtres (marnage explicite des lacs, karst, plafond d'altitude), résout la sélection exactement au lieu d'une heuristique, étend l'analyse de sensibilité à huit paramètres et publie le code et les données.

<span id="note-9">[9]</span> Relief : FABDEM (L. Hawker et al., « A 30 m global map of elevation with forests and buildings removed », Environmental Research Letters, vol. 17, 024016, 2022), sauf en Norvège (Kartverket) et en Suède (Lantmäteriet), modèles lidar nationaux ramenés à 10 m. Détection des cuvettes par remplissage du relief (O. Planchon, F. Darboux, Catena, vol. 46, 2002 ; R. Barnes et al., Earth Surface Dynamics, vol. 9, 2021) : on garde les cuvettes de 2 500 m² à 1 km², de plus de 1 m de profondeur maximale et de plus de 20 kWh par mètre de chute. Lacs : classe « eau » de CORINE Land Cover 2018 (Agence européenne pour l'environnement), dont le volume est estimé par une relation topographique. Exclusions : aires protégées des catégories Ia, Ib et IV de l'UICN (base mondiale WDPA), surfaces artificielles de CORINE ; bassins plafonnés à 100 ha, lacs compris ; bassin haut sous 2 500 m. Une cuvette dont l'emprise est à 20 % ou plus dans un lac cartographié est retirée : c'est le plus souvent le même lac détecté une seconde fois. Le volume utile d'une cuvette aménagée est 90 % de son volume.

<span id="note-10">[10]</span> Les bassins sont les sommets d'un graphe, les couples candidats ses arêtes, pondérées par leur énergie ; on cherche un couplage de poids maximal (algorithme d'Edmonds, implémentation de la bibliothèque LEMON), résolu exactement composante connexe par composante connexe. La sélection exacte retient 1,4 % d'énergie de plus que l'heuristique gloutonne de 2017, sans changer le classement des paramètres de l'analyse de sensibilité.

<span id="note-11">[11]</span> France, à seuils identiques : RGE ALTI de l'IGN (25 m, lidar) 72 GWh, Copernicus GLO-30 (modèle de surface) 394 GWh, ramenés à 156 GWh seulement par un élagage calibré des cuvettes peu profondes, FABDEM 60 GWh. Norvège : sur les 163 dalles du pays, 61 321 cuvettes avec FABDEM contre 30 613 avec le lidar (−50 % en nombre, −67 % en volume) ; erreur quadratique moyenne de FABDEM de 4,9 m dans la dalle médiane. Dans la chaîne complète, le gisement norvégien passe de 328,7 à 92,1 GWh (−72 %) et le suédois de 67,3 à 18,5 GWh (−72 %), tandis que le volume utile des lacs varie de −0,4 % en Norvège et de +0,6 % en Suède. Les couples de deux lacs gagnent même 41 % en Norvège ; ceux qui contiennent une cuvette sèche s'effondrent, car dans un couple mixte c'est la cuvette qui fixe le volume transférable. Hors France, Norvège et Suède, aucun relief national n'a été utilisé : le gisement des cuvettes sèches y est une borne haute, en Finlande notamment.

<span id="note-12">[12]</span> Z. Chen et al., « The World Karst Aquifer Mapping project: concept, mapping procedure and map of Europe », Hydrogeology Journal, vol. 25, p. 771-785, 2017. Le test porte sur l'emprise de chaque bassin à construire ; la version soumise de l'article testait le point milieu du couple, plus permissif. Les deux règles concordent sur 98,9 % des couples de deux cuvettes ; passer à l'emprise coûte 7,1 % de l'énergie européenne sans changer le classement des pays. Selon la même carte (tableau 5), des roches carbonatées karstifiables sont présentes sous 21,6 % de la surface de l'Europe, dont 13,8 % à l'affleurement ; en France, 35,0 % du territoire à l'affleurement et 49,6 % en comptant les zones couvertes. Sur le mot et les formes du karst : Larousse, [« relief karstique »](https://www.larousse.fr/encyclopedie/divers/relief_karstique/63753) et [« doline »](https://www.larousse.fr/encyclopedie/divers/doline/44321) ; sur les sotchs, ministère de la Culture, [*Les Causses et les Cévennes, paysage culturel de l'agropastoralisme méditerranéen*](https://www.culture.gouv.fr/Media/Regions/Drac-Occitanie/Files/Doc-Ressources-documentaires/Doc-Publications/Doc-collection-DUO/Patrimoine-mondial/Les-Causses-et-les-Cevennes), 2015 ; Fontaine de Vaucluse (débit moyen d'environ 18 m³/s) : [UMR EMMAH](https://umremmah.fr/outils-experimentations/sites-experimentaux/fontaine-de-vaucluse-lsbb) et [syndicat mixte du bassin des Sorgues](https://www.lasorgue.fr/la-sorgue/la-fontaine-de-vaucluse/les-debits-385.html).

<span id="note-13">[13]</span> P. T. Milanović, *Water Resources Engineering in Karst*, CRC Press, 2004 ; O. Bonacci, J. Rubinić, « Water losses from a reservoir built in karst: the example of the Boljunčica reservoir (Istria, Croatia) », Environmental Geology, vol. 58, p. 339-345, 2008. Le gisement exclu au titre du karst est à 99,5 % sur des roches carbonatées (calcaires, dolomies) et à 0,5 % sur des évaporites (gypse, sel), dont la dissolution pendant l'exploitation pose des risques d'une autre ampleur. L'exclusion se justifie surtout dans le karst entièrement développé, de type dinarique, et elle est la plus prudente dans le karst couvert, où les dolines sèches sont rares (Belgique, nord de la France, Norvège). Vajont : [« Vajont Dam »](https://en.wikipedia.org/wiki/Vajont_Dam) (Wikipédia) et [« Vaiont Dam »](https://www.britannica.com/topic/Vaiont-Dam) (Encyclopædia Britannica) ; bilan officiel de 1 917 morts ; le rôle respectif de la pluie, des variations du niveau de la retenue et des séismes dans le déclenchement reste débattu.

<span id="note-14">[14]</span> Figure S8 du supplément de l'article. Cette illustration vient du calcul national français et classe un couple « sur karst » d'après son point milieu, la règle de cette étude nationale ; les 94 % sont donc une part calculée sur les données françaises et non sur la référence européenne, qui teste l'emprise de chaque bassin. L'étude de 2017 (note [\[8\]](#note-8)) n'avait pas de filtre du karst.

<span id="note-15">[15]</span> Chaque filtre est appliqué au graphe des couples candidats, puis la sélection est entièrement refaite : un bassin libéré par un couple écarté peut entrer dans un autre. Écran environnemental strict : un couple est écarté dès que l'emprise d'un de ses bassins touche un site Natura 2000 (version fin 2024) ou une aire protégée des catégories II à VI de l'UICN (WDPA, septembre 2026) ; −30 % de l'énergie et −31 % des sites. Sur le réseau complet d'OpenStreetMap, ruisseaux compris, le même tampon de 20 m retirerait 60 % de la référence, mais c'est une borne fixée par la cartographie inégale des petits cours d'eau d'un pays à l'autre plutôt que par l'hydrologie. Le rapport de la distance à la chute (L/H) est calculé avec la distance en ligne droite : le tracé réel d'une conduite est plus long, et ce filtre est donc optimiste. Avec L/H ≤ 15, il reste 5 231 sites et 117 GWh ; avec L/H ≤ 5, 759 sites et 25 GWh. Les trois écrans cumulés (environnement, rivières, L/H ≤ 10) laissent 1 375 sites et 0,03 TWh.

<span id="note-16">[16]</span> Consommation : Eurostat, [Electricity and heat statistics](https://ec.europa.eu/eurostat/statistics-explained/index.php?title=Electricity_and_heat_statistics), consommation finale d'électricité de l'UE-27 en 2024 : 2 378 TWh (somme des secteurs ; 2 464 TWh d'électricité disponible pour la consommation finale), soit 0,27 à 0,28 TWh par heure en moyenne ; 0,24 TWh en couvrent environ 50 minutes. Stockage utilisable des STEP de l'Union, 0,5 à 0,6 TWh contre 1,3 TWh souvent annoncés : note [\[2\]](#note-2). Parc de batteries : E. Quaranta et al., *Clean Energy Technology Observatory: Hydropower and Pumped Storage Hydropower in the European Union — 2025 Status Report*, JRC, 2025. Paires de réservoirs existants : Gimeno-Gutiérrez et Lacal-Arántegui (note [\[7\]](#note-7)). Pour le stockage saisonnier, les études de systèmes 100 % renouvelables se tournent vers l'hydrogène.

<span id="note-17">[17]</span> Analyse de sensibilité globale (indices de Sobol, estimateur de Jansen) : 4 000 lignes de base et 40 000 évaluations, chacune refaisant la sélection continentale exacte, intervalles par 500 rééchantillonnages. Indices totaux : distance maximale entre bassins 0,49, traitement du karst 0,48, distance maximale au réseau 0,14, plafond d'énergie par site 0,13, chute minimale 0,020, énergie minimale 0,025, marnage des lacs 0,004, plafond d'altitude 0,001. Sur l'ensemble du plan d'expérience, le total va de 0,8 à 2 277 GWh, avec une médiane de 148 GWh et 80 % des cas entre 19 et 636 GWh : c'est une enveloppe sur des plages de définition volontairement larges, pas un intervalle de confiance. Quatre des huit valeurs de référence sont en bord de plage : la sensibilité à ces quatre paramètres n'est mesurée que dans un sens.

<span id="note-18">[18]</span> Supplément de l'article, tableaux S4, S14 et S15. La carte CORINE voit 19 % des plans d'eau de la BD TOPO de l'IGN en nombre, mais 73 % dans la gamme de 25 à 100 ha qui nourrit le modèle. Natura 2000 ou aire protégée des catégories II à VI de l'UICN : 53,5 % de l'énergie française de la référence, 34,7 % pour l'ensemble des 37 pays ; ce sont des parts exposées, pas la perte après re-sélection. Postes électriques : couche `power=substation` d'OpenStreetMap, dont la complétude varie d'un pays à l'autre (90,6 % des sites français ont un poste à moins de 5 km). La proximité d'un poste ne dit rien de sa capacité d'accueil.

<span id="note-19">[19]</span> Le modèle compte cinq postes d'investissement et 34 paramètres, publiés avec le code (tableau S11 du supplément). Appliqué à un projet européen de 130 MW publié indépendamment, de chute proche de notre médiane, il retrouve son coût d'investissement à 7 % près ; c'est un contrôle de cohérence, pas une validation indépendante, car certains coûts unitaires sont calés sur ce même projet. La comparaison avec les grandes STEP européennes s'appuie sur le rapport du JRC cité en note [\[16\]](#note-16). Avec les mêmes variations de ±50 % des coûts unitaires, l'énergie sous 500 €/kWh passe de 67 GWh à une valeur comprise entre 17 et 161 GWh. Les bassins à aménager sont comptés comme des cuvettes naturelles : un terrassement de 5 € par m³ de volume utile (une fourchette de 2 à 15 €/m³ pour de nouveaux réservoirs hors rivière), une membrane de 15 € par m² d'emprise et un coût fixe par bassin ; aucune digue n'est comptée.

<span id="note-20">[20]</span> A. Morabito, P. Hendrick, « Pump as turbine applied to micro energy storage and smart water grids: A case study », Applied Energy, vol. 241, p. 567-579, 2019. Le rendement moyen du parc de l'Union (0,71) vient de la note [\[2\]](#note-2).
