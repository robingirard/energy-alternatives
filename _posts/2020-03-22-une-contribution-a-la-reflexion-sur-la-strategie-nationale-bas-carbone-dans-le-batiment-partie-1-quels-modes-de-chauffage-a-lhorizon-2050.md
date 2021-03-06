---
title: Une contribution à la réflexion sur la stratégie nationale bas carbone dans le batiment. Partie 1 - Quels modes de chauffage à l’horizon 2050.
key: une-contribution-a-la-reflexion-sur-la-strategie-nationale-bas-carbone-dans-le-batiment-partie-1-quels-modes-de-chauffage-a-lhorizon-2050
tags: Thermosensibilite consommation variabilite chauffage evolution
article_header:
  type: cover
  image:
    src: /assets/images/Posts/2020-03-22/DSCF7307c.jpg
---



<div class="summary" style="display:block; text-align: justify">
<em>
     J’ai écrit une contribution à la consultation publique sur le « projet de stratégie à long terme pour mobiliser les investissements dans la rénovation du parc national de bâtiments à usage résidentiel et commercial, public et privé » <a href= "http://www.consultations-publiques.developpement-durable.gouv.fr/projet-de-strategie-a-long-terme-pour-mobiliser-a2136.html"> [1]</a>.  Cette contribution est en deux parties ; la seconde partie viendra plus tard et traitera de la question de la rénovation thermique de bâtiment.
</em>
</div>
<!--more-->

<div class="summary" style="display:block; text-align: justify">
<em>
     Je rappelle en introduction les objectifs chiffrés de la stratégie nationale bas carbone dans le bâtiment et vis-à-vis de la consommation de chauffage. Je discute et quantifie la puissance des trois leviers que sont : (i) la diminution du besoin de chaleur par l’amélioration de l’efficacité des bâtiments, (ii) l’augmentation de l’efficacité des systèmes de chauffage principalement en par l’utilisation de pompes à chaleur (électrique ou hybrides), et (iii) l’utilisation de vecteurs énergétiques qui impliquent des émissions de GES suffisamment faibles. Dans ce contexte, je rappelle le rôle important du bois et du vecteur électrique ainsi que l’importance de la contrainte de thermosensibilité sur la consommation électrique et le rôle que peut jouer le biogaz par rapport à celle-ci. Je compare différentes manières d’utiliser du gaz pour fournir ce service de puissance. Je termine par une conclusion incluant quelques préconisations envoyées lors de la consultation qui s’est terminée le 10 Mars 2020.  Notons que je ne traite que de l’usage chaleur dans le bâtiment résidentiel, et que je fais l’impasse sur les réseaux de chaleurs et du solaire thermique (qui ne sont pas négligeables mais écartés de l’analyse). Le premier levier (rénovation thermique de bâtiment) est reporté au post qui suivra.  

     Le code et les données permettant de faire les graphiques de ce post sont mis à disposition librement.
</em>
</div>



____________________________________


# Introduction : objectifs 2050 de la stratégie nationale bas carbone dans le bâtiment.
<span class="mytext">Le gouvernement français a récemment publié une nouvelle version de la stratégie nationale bas carbone (SNBC) [[0](https://www.ecologique-solidaire.gouv.fr/strategie-nationale-bas-carbone-snbc)]. pour une consultation publique dont la première phase s’est terminée le 19 février 2020. Cette stratégie se fixe pour ambition une neutralité carbone à l’horizon 2050, et évidemment la description détaillée des leviers à mettre en œuvre à cet horizon est encore incomplète, mais les orientations et quantifications déjà présentes dans le document actuel ont le mérite de lancer le débat. En outre, un suivi de notre trajectoire est prévu dans les années à venir via le mécanisme des « budget carbone ». Dans cette stratégie le secteur du bâtiment joue un rôle important, du côté de la construction évidement, mais aussi en ce qui concerne la production de chaleur. Une consultation publique dédiée [[1](http://www.consultations-publiques.developpement-durable.gouv.fr/projet-de-strategie-a-long-terme-pour-mobiliser-a2136.html)]. a été mise en place jusqu’au 10 mars 2020. Dans le même temps, le gouvernement français prépare la nouvelle réglementation thermique du bâtiment, la RE2020 qui doit remplacer l’ancienne RT2012 pour définir les règles applicables à la construction de bâtiments neufs. La RE2020 ne concerne pas seulement le chauffage mais on peut dire qu’il y joue un rôle majeur. Cette réglementation fait débat.
</span>

<span class="mytext">L’ambition chiffrée de la stratégie nationale bas carbone est représentée Figure 1. En ce qui concerne le bâtiment, elle vise un passage de 85 MtCO2eq/an actuellement à 5 MtCO2eq/an en 2050.
</span>

<span class="text" id="Figure1" style="display:block;text-align:center">
![Image]({{site.baseurl}}/assets/images/Posts/2020-03-22/SNBCChauffageFigure1ObjectifsSNBC.png){:.border}
</span>
<span class="legendtext" id="CAPFigure1" style="display:block;text-align:center">
**Figure 1** -- Ambition de la stratégie nationale bas carbone.
</span>

<span class="mytext">Le chauffage résidentiel ne représente qu’une partie des émissions correspondantes, et celle-ci n’est pas donnée de manière explicite dans le document disponible publiquement. On peut cependant les estimer la contribution actuelle du chauffage à partir des consommations de chauffage par vecteur énergétique disponibles publiquement [[2](https://www.statistiques.developpement-durable.gouv.fr/les-menages-et-la-consommation-denergie.)] et des émissions de la Base Carbone de l’ADEME [[10](https://www.bilans-ges.ademe.fr/documentation/UPLOAD_DOC_FR/index.htm?gaz.htm)]. Certaines valeurs mériteront une discussion plus approfondie, surtout pour l’électricité et les catégories bois/urbain. Nous reportons ces discussions à la Section 3.
</span>

<span class="mytext">Le calcul correspondant est présenté dans la [Table 1](#CAPTable1) ci-dessous.
</span>

|                             | Elec|   Gaz| Fioul|  Bois| Urbain| Total|
|:----------------------------|----:|-----:|-----:|-----:|------:|-----:|
|Consommation TWh/an          | 35| 122|  40| 85|   13| 300|
|Emissions gCO2eq/kWh         | 60| 240| 320| 50|  100| 186|
|Emissions totales MtCO2eq/an |  2.1|  29.3|  12.8|  4.25|    1.3|  55.8|
{: .simple5 }

<span class="legendtext" id="CAPTable1" style="display:block;text-align:center">
**Table 1** -- Consommation d’énergie pour l’usage chauffage résidentiel et émissions associées pour différents vecteurs énergétiques. Source pour les énergies consommées [[2](https://www.statistiques.developpement-durable.gouv.fr/les-menages-et-la-consommation-denergie.)]. Pour les émissions source valeurs moyennes données par l’ADEME dans la base carbone [[10](https://www.bilans-ges.ademe.fr/documentation/UPLOAD_DOC_FR/index.htm?gaz.htm)].
</span>

<span class="mytext">De cette valeur actuelle de 50 MtCO2eq/an pour le chauffage dans le bâtiment, on peut déduire par une règle de trois l’objectif de 2050 : 3 MtCO2eq/an. Vu que l’on parle ici d’un secteur où il n’est pas trop difficile de réduire nos émissions, cette valeur est certainement plutôt une borne supérieure. A partir de cet objectif, l’enjeu de la stratégie nationale bas carbone et plus généralement de la transition énergétique vis-à-vis de la consommation de chauffage est triple. Il s’agit (i) de diminuer le besoin de chaleur en améliorant l’efficacité des bâtiments ou en diminuant les températures de consigne, (ii) d’augmenter l’efficacité des systèmes de chauffage, principalement en utilisant des pompes à chaleur (électrique ou hybrides qui ont des COP supérieurs à 3) ou des systèmes solaires thermiques, et (iii) utiliser des vecteurs énergétiques qui impliquent des émissions de GES suffisamment faibles. Pour le levier (ii) on parle aussi d’utilisation d’énergie (thermique) renouvelable. On retrouve des déclinaisons de ces trois leviers compatibles avec la stratégie bas carbone dans les visions de l’ADEME 2035-2050 [[3](https://www.ademe.fr/lademe/priorites-strategiques-missions-lademe/scenarios-2030-2050)], dans les scénarios Negawatt [[4](https://negawatt.org/Scenario-negaWatt-2017-2050)]. On retrouve ce type de démarche dans d’autres pays comme en Allemagne qui décrit sa stratégie ici [[5](https://www.bmwi.de/Redaktion/EN/Publikationen/energy-efficiency-strategy-buildings.pdf?__blob=publicationFile&v=7)].
</span>

<span class="mytext">Le caractère essentiel de la SNBC est qu’elle repose sur des objectifs chiffrés qui vont donc agir comme une contrainte sur nos décisions politiques. L’objectif de ce post et de celui qui suivra est de quantifier de manière très grossière, avec des données publiques et un code mis à disposition librement, la manière dont nous pouvons activer chacun des trois leviers mentionnés dans l’introduction pour nous rapprocher des 3 MtCO2eq/an de la SNBC. Il s’agira également de mettre en lumière les avantages et inconvénients des différentes solutions qui s’offrent à nous.
</span>

<span class="mytext"> Nous allons dans un premier temps discuter avec un peu plus de détail les vecteurs énergétiques qui doivent jouer un rôle dans cette transition. Ensuite, dans la Section 3, nous parlerons des pompes à chaleur, pour insister sur le rôle important qu’elles peuvent jouer autant que sur le problème de thermosensibilité de la consommation électrique qu’elles induisent. Enfin, nous montrerons dans la Section 4 en quoi l'utilisation de biogaz est une brique importante dans l'ensemble des solutions, importante non pas vis à vis des volumes en jeux, mais vis à vis du service rendu (service de puissance).  Un prochain post sera dédié à la rénovation thermique du bâtiment.
</span>

# Utiliser des vecteurs énergétiques qui impliquent des émissions de CO2 suffisamment faibles

<span class="mytext">Lorsque l’on parle d’utiliser un vecteur énergétique qui implique des émissions de GES suffisamment faibles on pense en général en premier lieu à l’électricité, pourtant le bois et le biogaz sont également des vecteurs qui induisent des émissions faibles. Ainsi, lorsque l’on passe d’une chaudière au fioul à des convecteurs électriques ou à un poêle à granulé cela divise par plus de 5 les émissions de GES correspondantes. Mais ces émissions et leurs calculs ne sont pas toujours le reflet d’une réalité stable et indiscutable. Certaines évoluent à la baisse, toutes impliquent également des défauts, des contraintes de volume. Nous allons faire un tour d’horizon de ces trois vecteurs pour illustrer quelques avantages et imperfections de ceux-ci. Nous ne traitons pas les réseaux de chaleur, ni le solaire thermique. Pour les réseaux de chaleur, nous renvoyons le lecteur à cette étude de l’ADEME faite en 2017 [[6](https://www.ademe.fr/avis-lademe-reseaux-chaleur-alimentes-energies-renouvelables-recuperation)].
</span>

## Electricité.

<span class="mytext">Le chauffage électrique est pour l’instant une spécificité française, tout comme la thermosensibilité qui l’accompagne. L’électricité en France a historiquement pris le pas sur d’autres systèmes pour le chauffage : des systèmes de géothermie, du bois énergie et des réseaux de chaleur qui peuvent avoir de bonnes performances environnementales, mais également sur d’autres qui sont bien moins bonnes, comme le fioul. Si l’on regarde un pays comme Allemagne qui n’a pas encore beaucoup développé le chauffage électrique, on y trouve plus de réseaux de chaleur, plus de bois énergie mais également plus de fioul. En outre la transition énergétique allemande vise elle aussi un usage important de l’électricité dans le chauffage. L’électricité n’est pas la seule source d’énergie faiblement carbonée pour le chauffage, mais il faut admettre qu’en volume annuel à l’échelle de la France l’électricité doit jouer un rôle plus important que le rôle actuel. Dans ce sens, la consommation de chauffage électrique en France ne représentant que 15% des besoins (40 TWh/an sur un total de 300 TWh/an), on ne peut pas dire que notre avance soit considérable.
</span>

<span class="mytext">Les émissions de GES liées à l’utilisation du chauffage électrique font débat. Tout d’abord les 60 gCO2eq/kWh utilisées dans la base carbone de l’ADEME et dans la [Table 1](#CAPTable1) sont une moyenne sur l’année de toutes les émissions liées à la production. Elles ne reflètent pas le réel impact du chauffage électrique qui correspond plutôt à une électricité consommée en hiver lorsqu’il fait froid et n’intègre pas les impacts liés au réseau électrique (les émissions “grises” liées aux lignes électriques et aux transformateurs). Si cette électricité thermosensible (consommée lorsqu’il fait froid) est produite par une centrale à gaz utilisant du gaz naturel on se retrouve avec des émissions de l’ordre de 400 gCO2eq/kWh au lieu de 60 gCO2eq/kWh. Mais la consommation thermosensible n’est pas seulement couverte par du gaz en France et la modulation saisonnière du nucléaire faite « grâce » à la contrainte des maintenances annuelles joue un rôle important. Cette capacité de modulation saisonnière du nucléaire est aujourd’hui poussée à son maximum et si la thermosensibiltié augmentait en France le nucléaire ne pourrait pas couvrir le besoin additionnel de modulation. Nous supposerons ici simplement que les 60 gCO2eq/kWh donnent une borne inférieure sur les émissions actuelles liées à l’utilisation de l’électricité pour le chauffage. L’expérimentation E+C- qui doit préfigurer la prochaine réglementation utilise le chiffre de 210 gCO2eq/kWh, et dans la RE2020 l’objectif est de diminuer ce chiffre pour arriver à 79 gCO2eq/kWh. Concernant l’électricité, la SNBC envisage à l’horizon 2050 une réduction des émissions moyennes de 60 gCO2/kWh à 20 gCO2/kWh. Cet objectif passera par la disparition du Charbon qui est déjà acquise et par l’utilisation d'un gaz "relativement neutre en carbone" appelé biogaz (méthane ou hydrogène), ou par la disparition du gaz. Or nous allons le voir la disparition du gaz n’est pas compatible avec le développement du chauffage électrique.
</span>
<span class="mytext">Le volume d’électricité consommé tous les ans en France est autour de 500 TWh/an, et couvre bien d’autres usages que les 40 TWh/an de chauffage. Même si l’on suppose que cette électricité implique seulement une production nucléaire et hydraulique qui sont faiblement carbonées (en négligeant donc le problème de la thermosensibilité), on ne peut pas considérer que le gisement électrique est « infini ». A l’horizon 2050 la majorité du parc nucléaire actuel devra être remplacé, par des centrales nucléaires ou, par des centrales renouvelables accompagnées d’une puissance de secours. Aucune de ces deux options n’est neutre sur le plan environnemental (utilisation de ressources, déchets, risque d’accident), ni simple sur le plan de l’acceptabilité : des milliers d’éoliennes, de panneaux photovoltaïques d’un côté, ou une cinquantaine de fois le réacteur de Flamanville, de l’autre. Le gisement électrique ne sera pas plus infini en 2050 qu’il ne l’est aujourd’hui.
</span>
<span class="mytext">L’intérêt de l’électricité vis-à-vis du chauffage, nous allons le voir, est qu’elle permet d’utiliser des pompes à chaleurs qui sont très efficaces et vont permettre de diviser le besoin par 3.

## Biomasse

<span class="mytext">Le bois-énergie peut également être faiblement carboné, cela dépend de la qualité de la combustion et de la gestion des forêts. L’ADEME donne dans sa base carbone un contenu ACV variable entre 0 et 100 gCO2eq/kWh, selon la provenance du bois et selon qu’il s’agit de bois bûche, de granulés bois, de plaquettes forestières, de sciures et chutes de scieries, de broyats de cagettes et de palettes, de paille … C’est pour cela que nous avons retenu la valeur de 50 gCO2eq/kWh dans la [Table 1](#CAPTable1). S’il s’agit d’une forêt exploitée de manière durable, ou mieux encore de déchets de scierie et que le bois n’est pas transporté sur de longues distances les émissions sont encore plus faibles, et largement compatibles avec la stratégie bas carbone.
</span>
<span class="mytext">La question importante, dès lors, est celle des volumes disponibles. Une étude [[7](https://www.ademe.fr/sites/default/files/assets/documents/biomasse-forestiere-populicole-et-bocagere-2009.pdf)] réalisée pour le compte  de l’ADEME en 2009 permet de comprendre le gisement de bois en termes de volumes. L’horizon donné était 2020. On y trouve la distinction entre différentes origines du bois, et pour chaque origine un volume annuel disponible durablement est déterminé :
</span>
<div class="text" style="display:block; text-align: justify">
<ul> <li>Le bois pour la construction et les meubles, bois d’oeuvre BO, non utilisé pour le chauffage,</li>
<li>Le bois industrie/bois énergie (BIBE), 60 $Mm^3$ disponibles, dont 12 $Mm^3$ consommés par l’industrie et 20 $Mm^3$ consommés pour le chauffage, donc 28 $Mm^3$ supplémentaires disponibles,</li>
<li>Le Menu Bois (MB) issu des futaies qu’il faut couper pour favoriser la croissance des grands arbres et qui peut être déchiqueté pour faire des plaquettes, (8 $Mm^3$ disponibles mais inutilisé aujourd’hui),</li>
<li> et les produits connexes de scierie (PCS) utilisés pour faire des pellets ou plaquettes et dont la disponibilité est 40% du volume de BO exploité (8 $Mm^3$ disponibles).</li>
</ul>
</div>
<span class="mytext">Dans cette étude sont pris en compte des modèles précis pour estimer ce qu’il est possible de récupérer de manière pérenne, avec une prise en compte des difficultés d’accès à la forêt.
</span>
<span class="mytext">Un stère de bois permet d’obtenir 2 MWh de chaleur, un mètre cube de bois donne 4,5 MWh. Ainsi les 20 $Mm^3$ de BIBE consommés pour le chauffage donnent 90 TWh/an, c’est à dire à peu près les 85 TWh/an consommés aujourd’hui et que l’on retrouve dans les statistiques du gouvernement de la [Table 1](#CAPTable1).
</span>
<span class="mytext">Le gisement supplémentaire est donc composé de 28 $Mm^3$ BIBE récupérable (126 TWh/an), 8 $Mm^3$ de MB récupérable (36 TWh/an), 8 $Mm^3$ de PCS avec la conso de BO actuelle (36 TWh/an) déjà en partie exploité. En définitive cela donne un gisement supplémentaire entre 150 et 200 TWh/an. On peut donc conclure que le gisement actuel est largement sous-exploité et que le bois énergie pourrait jouer un rôle important dans la mise en œuvre de la SNBC.
</span>
<span class="mytext">Un défaut important du bois est la pollution aux particules fines qu’il implique, mais la réglementation permet aujourd'hui de maitriser ce problème [[17](https://www.ademe.fr/expertises/energies-renouvelables-enr-production-reseaux-stockage/passer-a-laction/produire-chaleur/dossier/bois-biomasse/bois-energie-qualite-lair)].
</span>

## Biogaz, une réalité à venir

<span class="mytext">Le gaz peut aussi être faiblement carboné s’il s’agit de biogaz. Le terme « bio » concentre souvent une discussion sémantique sur son pendant marketing. Il faut dire que le biogaz peut avoir des défauts si les subventions qui l’accompagnent provoquent une utilisation des sols perverse avec des cultures dédiées intensives en concurrence avec l’alimentaire [[8](https://decrypterlenergie.org/la-methanisation-est-elle-synonyme-dintensification-de-lagriculture-et-de-pollutions)]. Face à ces problématiques, le développement de la filière est déjà source de quelques tensions [[9](https://www.bastamag.net/methanisation-lobby-gaz-vert-biogaz-agriculture-energetique-alimentaire)]. La seule énergie à peu près neutre est celle que l’on ne consomme pas, et aucun projet industriel, même nécessaire pour la société, n’est à l’abri d’une mauvaise gestion collective. Pour le bois la même règle s’applique avec l’exemple de la centrale biomasse de Gardanne, ou avec les subventions Européennes attribuées il y a quelques années au centrales Allemande brûlant du bois de palme. Pour l’électricité, nucléaire ou renouvelable, les exemples ne sont pas moins nombreux.
</span>
<span class="mytext">Le biogaz est tout de même un vecteur de décarbonation important de nos systèmes énergétiques, et nous allons voir que le service de puissance qu’il peut rendre est essentiel et qu’il implique des volumes très nettement réduits par rapport à l’utilisation que nous faisons du gaz aujourd’hui.
</span>
<span class="mytext">On rassemble aujourd’hui sous l’appellation “biogaz” du méthane produit à partir de sources très hétérogènes par trois techniques différentes : la méthanisation, la pyrogazéification et la méthanation. Ces sources hétérogènes ne se réduisent absolument pas à des cultures dédiées comme on l’entend parfois. A ce jour, seul le facteur d’émission calculé pour la filière STEU (stations d’épuration) est intégré dans la base carbone de l’ADEME [[10](https://www.bilans-ges.ademe.fr/documentation/UPLOAD_DOC_FR/index.htm?gaz.htm)] qui rassemble les analyses de cycle de vie (ACV) « officielles » en France, les émissions associées sont de 16 gCO2/kWh.  On considère que les émissions en ACV de la filière agricole sont autour de 25-50 gCO2/kWh ([voir ici](https://www.grdf.fr/institutionnel/actualite/dossiers/biomethane-biogaz/etude-biomethane-gaz-effet-serre)) même si ces chiffres font encore débat et ne peuvent s’appliquer à toute la filière. Dans ce sens je préconise ici un approfondissement de la base carbone de l’ADEME sur l’évaluation en analyse de cycle de vie du biogaz.
</span>
<span class="mytext">Le potentiel de production de biogaz en France varie selon les sources entre 150 TWh/an et 300 TWh/an (voir le scénario Afterre [[11](https://afterres2050.solagro.org/a-propos/le-projet-afterres-2050/)]) qu’il faut comparer aux 500 TWh/an de gaz que l’on consomme aujourd’hui en France. Il me semble que dans le cadre de la SNBC un approfondissement de ce gisement est également essentiel. Ainsi on peut imaginer que dans un futur décarboné il faille définir des usages prioritaires du gaz. Nous pensons que ces usages pourraient être :
</span>
<div class="mytext">
<ul> <li>L’industrie, avec disons 60 TWh/an pour les processus nécessitant de très fortes puissances,</li>
<li>le secteur de la production d’électricité, avec encore 60 TWh/an de gaz qui pourraient faire 35 TWh/an d’électricité flexible nécessaire dans les scénarios fortement renouvelable mais également, dans une moindre mesure, avec un scénario nucléaire,</li>
<li>le secteur du chauffage, avec autour de 30 TWh/an pour des raisons que nous allons expliquer dans la section suivante, la flexibilité correspondante pourrait servir au secteur de l’électricité.</li>
<li>et éventuellement celui du transport.</li>
</ul>
</div>

<span class="mytext">Avec 30 TWh/an réservés au chauffage, contre 120 TWh/an consommés aujourd’hui, on peut considérer que la décarbonation passe par une réduction majeure du volume de gaz consommé mais il faut analyser plus précisément les choses pour comprendre que dans le secteur du chauffage comme pour l’électricité le gaz va de plus en plus être appelé à jouer un rôle majeur de fourniture de puissance, à énergie réduite. La définition d’un volume minimal de biogaz nécessaire à la SNBC pour le chauffage devrait à mon avis être envisagée dans les années à venir. Cela pourrait être associé à un couplage dans le financement, par exemple via une obligation lors du montage d'un projet éolien, de contribuer au montage ou au financement d'un projet biogaz.
</span>


# Augmenter l’efficacité des systèmes de chauffage principalement en utilisant des pompes à chaleur.

## La pompe à chaleur, une technologie très performante.

<span class="mytext">Les pompes à chaleur (PAC) utilisent de l’électricité et un procédé thermodynamique pour extraire de l’énergie de la chaleur de l’environnement. Cet environnement peut être l’air extérieur (système air-air ou air-eau) ou de l’eau se réchauffant sous terre (géothermie de surface, système eau-eau). Ces systèmes ont l’énorme avantage d’atteindre des coefficients de performance moyen ou « COP saisonnier » (rapport entre la chaleur fournie et l’énergie électrique fournie sur une année) de 4 voir 5 pour les meilleures installations.
</span>
<span class="mytext">Les performances de la PAC dépendent de la technologie (air-air, air-eau, eau-eau), des émetteurs (pour les air-eau, les performances sont moins bonnes avec des émetteurs haute température) et de la météo (elles fonctionnent moins bien lorsqu’il fait froid). Les PAC vendues aujourd’hui fonctionnent à vitesse variable et adaptent donc leur puissance au besoin pour de meilleures performances mais une PAC surdimensionnée n’a en général pas les meilleures performances. C’est pour cela qu’il est toujours préférable de faire une rénovation en même temps que l’installation et le dimensionnement d’une PAC et non après.
</span>
<span class="mytext">Le coût des PAC est assez élevé à l’investissement mais leur efficacité (division par 3 de la consommation) permet une rentabilité économique sans aide dans beaucoup de cas. Notre objectif n’est pas ici de comparer tous les systèmes existants, l’arbitrage entre les différents systèmes (air-air, air-eau basse/moyenne/haute température, eau-eau) ne peut pas facilement se réduire à une simple analyse économique car les systèmes air-eau sont en général plus chers mais plus agréables et mieux adaptés pour des surfaces de plus de 70 $m^2$ ayant déjà un réseau de distribution de chaleur (par l’eau, systèmes anciennement équipés au gaz ou au fioul). Chacun de ces systèmes aura un COP différent mais on peut raisonnablement supposer que parmi toutes les PAC qui seront posées à l’avenir le COP sera en moyenne de 3,5. Tous ces systèmes ont des coûts variés qui dépendent de la puissance (environ 500 €/kW pour les air-air d’entrée de gamme, et plutôt 4000€+500€/kW pour le système air-eau) ainsi que du système de distribution et des émetteurs (dans le cas de la PAC air-eau). Cependant, si l’on suppose un coût unitaire moyen de l’ordre de 10 k€ et une durée de vie de 20 ans on peut comprendre que la PAC est un vecteur de décarbonation très efficace et rentable sans subvention dans beaucoup de cas. Par exemple, si l’on remplace une chaudière au fioul dans un logement de 100 $m^2$ consommant 170 kWh/$m^2$/an on économise chaque année 12 MWh, à 150 €/MWh (le coût de l’électricité est plus élevé que cela aujourd’hui) cela fait 1800 euros/an d’économie et un système remboursé en 6 ans.
</span>
<span class="mytext">On peut faire un calcul à l’échelle de la France en utilisant le nombre de foyers par énergie de chauffage obtenu en Annexe 1 que nous utiliserons dans la suite de ce post. Si l’on remplace les 5 millions de chauffages au fioul cela permettra une économie de 14 MtCO2eq. Cette idée est très largement développée dans une étude de Carbone 4 [[12](http://www.carbone4.com/les-pompes-a-chaleur/)], faite en 2013. C’est une préconisation à laquelle il est difficile de ne pas s’associer. L’efficacité des PAC sur le plan économique, énergétique et environnemental est donc un levier efficace pour la transition énergétique mais son développement ne peut se faire sans négliger un point important : la thermosensibilité qu’il implique sur le système électrique.
</span>

## Un problème de thermosensibilité.

<span class="mytext">Le développement des PAC est sans doute une mesure nécessaire à court terme pour la réduction de nos émissions de GES et les réglementations à venir (DPE, RE2020) vont vraisemblablement donner aux PAC un poids important. Pourtant, lorsque les PAC viennent en remplacement d’énergies non électriques, elles font augmenter la thermosensibiltié de la consommation électrique. Nous avons vu dans un post précédent [[13](https://www.energy-alternatives.eu/2019/05/24/variabilite-de-la-consommation-electrique-et-thermo-sensibilite.html)] que la consommation de chauffage électrique, les pertes réseau, et quelques autres usages corrélés à la température, induisent une thermosensibilité importante de la consommation à l’échelle nationale. Elle est de 2,5 GW/°C en France, et a plus que doublé entre 2000 et 2012. Cette évolution problématique ne s’est pas poursuivie ces dernières années et ceci est probablement le résultat d’une baisse de la proportion de convecteurs électriques dans le neuf, que l’on peut observer sur la Figure 2.
</span>

<span class="text" id="Figure2" style="display:block;text-align:center">
<img src="{{site.baseurl}}/assets/images/Posts/2020-03-22/RTE-1.png" width="49%" />
<img src="{{site.baseurl}}/assets/images/Posts/2020-03-22/RTE-2.png" width="49%" />
</span>
<span class="legendtext" id="CAPFigure2" style="display:block;text-align:center">
**Figure 2** -- A gauche : parc de résidences principales selon l’énergie de chauffage. A droite : résidentiel neuf selon l’énergie de chauffage (source bilan prévisionnel RTE 2016, BatiEtude). L’évolution Allemande vis-à-vis des PAC a été plus précoce (voir [[5](https://www.bmwi.de/Redaktion/EN/Publikationen/energy-efficiency-strategy-buildings.pdf?__blob=publicationFile&v=7)] Figure 10 p26).
</span>
<span class="mytext">
Ces 2,5 GW/°C ne sont pas intégralement liés au chauffage dans le secteur résidentiel. On dispose des données de consommation dans différents secteurs (open data ENEDIS  [[14](https://data.enedis.fr/explore/dataset/bilan-electrique-transpose/information/?flg=fr)]), et l’on peut montrer (graphique en Annexe 2) que la thermo-sensibilité de la consommation résidentielle est de l’ordre de 1,5 GW/°C, pour une couverture en énergie annuelle qui est, je le rappelle, de l’ordre de 35 TWh/an (cf Table 1). Nous l’avons déjà dit, cette consommation ne représente qu’un peu plus de 15% du total de consommation de chauffage qui est de 293 TWh/an. Une difficulté avec le projet développé dans [[15](https://jancovici.com/transition-energetique/electricite/50-ou-50/)] de remplacer les 15 millions de chauffage au gaz/fioul en chauffage électrique est que cela impliquerait de remplacer 160 TWh/an de consommation de gaz et de fioul par environ 46 TWh de consommation d’électricité (160 TWh/an auxquels nous appliquons le COP des PAC). Si 35 TWh/an d’électricité dédié au chauffage apportent 1,5GW/°C de thermosensibilité alors les 46 TWh/an issus de la conversion du gaz/fioul en électricité ajouteraient 2 GW/°C. Si l’on se réfère à [[13](https://www.energy-alternatives.eu/2019/05/24/variabilite-de-la-consommation-electrique-et-thermo-sensibilite.html)] cela pourrait représenter environ 40 GW de besoin de pointe supplémentaire dans le système électrique, soit une contrainte non négligeable.
</span>

<span class="mytext">
A ce stade il est important de rappeler que la thermosensibilité n’est pas seulement un problème vis à vis de l’équilibre offre-demande à l’échelle de la France ou de l’Europe. En effet, des problèmes de congestion dans le réseau de distribution résulteraient d’un développement massif des pompes à chaleur, par exemple dans un quartier où le gaz est la règle aujourd’hui. Par exemple, si l’on change toutes les chaudières gaz d’un quartier pour des PAC, les câbles électriques n’auront plus localement une capacité suffisante pour acheminer l’électricité à tous les foyers en période de grand froid. Ce n’est pas une difficulté insurmontable pour le gestionnaire du réseau de distribution mais elle nécessite une certaine anticipation et elle a un coût non négligeable (celui de changer les câbles, et surtout de creuser des tranchées pour le faire).
</span>

## COP des PAC en période de grand froid

<span class="mytext">
En plus de cela les performances des PAC en période de grand froid sont plus faibles qu’en moyenne pour plusieurs raisons. Tout d’abord les PACs sont équipées d’un système de dégivrage qui se met en route lorsqu’il fait froid et consomme de l’énergie, ensuite le COP de la PAC est moins bon lorsque le fluide d’échange extérieur est trop froid, et enfin une PAC n’est pas dimensionnée pour les jours de grand froid et lorsqu’il fait très froid les utilisateurs de PAC ont parfois, branché quelque part, un convecteur d’appoint moins performant. D’après les données récentes de constructeurs (voir par exemple [[16](https://hal-mines-paristech.archives-ouvertes.fr/hal-01796759/document)] Figure 7 p249), le COP moyen des PAC en période de grand froid n’est pas 3,5 mais plutôt autour de 3. Cette question dépend de la température de grand froid considérée, si l’on reprend la série de températures que j’ai donné pour la France dans mon post précédent [[13](https://www.energy-alternatives.eu/2019/05/24/variabilite-de-la-consommation-electrique-et-thermo-sensibilite.html)] (1996-2019), on a les quantiles bas de la [Table 2](#CAPTable2) sur la température.
</span>

|Fréquences                            |1%    |0.5%  |0.25% |0.1% |
|:-------------------------------------|:-----|:-----|:-----|:----|
|Quantile de température [°C]          |-1.59 |-2.65 |-3.58 |-4.9 |
|COP médian des systèmes air-air 3.5kW |3.5   |3.35  |3.2   |3.1  |
|COP médian des systèmes air-air 7kW   |3.5   |3.2   |3.1   |2.9  |
 {: .mbtablestyle .wrapstyle .simple5}
 <span class="legendtext" id="CAPTable2" style="display:block;text-align:center">
 **Table 2** -- Consommation d’énergie pour l’usage chauffage résidentiel et émissions associées pour différents vecteurs énergétiques. Source pour les énergies consommées [[2](https://www.statistiques.developpement-durable.gouv.fr/les-menages-et-la-consommation-denergie.)]. Pour les émissions source valeurs moyennes données par l’ADEME dans la base carbone [[10](https://www.bilans-ges.ademe.fr/documentation/UPLOAD_DOC_FR/index.htm?gaz.htm)].
 </span>

<span class="mytext">
Ce COP de 3 reflète des données déclarées par les constructeurs sur des PAC air-air qui ont les meilleurs rendements et pour lesquelles les conditions d’installation ne sont pas aussi essentielles que pour les PAC air-eau. On peut imaginer qu’à l’échelle de la France, un COP moyen de 2,5 soit atteint en période de grand froid. Sur ce point des campagnes d’observation sur site sont nécessaires, surtout vis à vis des performances des PAC air-eau dont les performances dépendent beaucoup de la qualité de la pose et du dimensionnement. **Ces campagnes devraient être mises en œuvre, c’est une de mes préconisations ici**. Il faut garder à l’esprit que tant que les petits convecteurs électriques achetés ne seront pas interdits à la vente, les logements équipés de PAC auront souvent quelque part un ou deux de ces chauffages pour faire face aux périodes de grand froid, on observe aujourd’hui cette tendance avec une thermosensibilité accrue en période de grand froid.
 </span>

## Quelques scénarios d'évolution de la thermosensibilité en fonction des modes de chauffage développés

<ul> <li> $X_1$ : Thermo-sensibilité à additionner à l’actuelle, pour une période de grand froid en France [GW/°C]</li>
<li>$X_2$ : Évolution du besoin de pointe en   France sur le système électrique pour une période de grand froid (-5°C)</li>
<li> Em : Emissions GES [MtCO2eq/an]</li>
</ul>


 |Scenarios                            |$X_1$    | $X_2$ |Em|
 |:------------------|:-----|:-----|:-----|
 |Gaz+Fioul devient PAC     |2.8 GW/°C |+56 GW |10.6 |
 |Gaz+Fioul+Elec devient PAC |2.8-0.9 = 1.9 GW/°C   |+38 GW  |9.2   |
 |Gaz+Elec devient PAC, Fioul devient Bois   |(0.6+2.1)- 1.5 = 1.2 GW/°C   |+ 24 GW |10.4   |
|Gaz+Elec devient PAC Fioul devient Bois Renovation, besoin divisé par deux   |(0.6+2.8)/2-1.5 = -0.15 GW/°C   |-3 GW |5,2   |
  {: .wrapstyle  .simple7}
<span class="legendtext" id="CAPTable3" style="display:block;text-align:center">
**Table 3** -- Impact de différents scénarios de changement de mode de chauffage, à l’échelle de la France et à l’horizon 2050, sur l’évolution de la thermosensibilité et l’évolution du besoin de pointe associé. Nous ne tenons pas compte de la croissance du nombre de logements d’ici là, nous avons donc ici une borne inférieure. La thermosensibilité est calculée en supposant un COP de 2,5 pour les PAC en période de grand froid. Les émissions prises sont celles de la [Table 1](#CAPTable1). Elles pourraient baisser si l’électricité baisse, mais les émissions de l’électricité baisseront difficilement si le besoin de pointe reste le même. Tous les calculs sont effectués dans le code partagé avec les données de la Table 1 et de l’Annexe 1. Il faut noter le caractère très optimiste qu'il y a à supposer la disparition des chauffages électriques de type "grille pain" (ceux qui ne sont pas des PAC). Optimiste également de penser que l'on peut mettre des PAC partout (pour des raisons de place ou d'esthétique extérieur de bâtiment)
  </span>

<span class="mytext">
La [Table 3](#CAPTable3) nous montre que le déploiement massif de PAC a ses limites, et que la stabilisation de la thermosensibilité est possible avec un accroissement de l’usage du bois et une campagne de rénovation importante. Rappelons que les rénovations perdent beaucoup de leur valeur dans ce contexte si elles ne sont pas faites avant ou au même moment que l’installation des PAC. Ajoutons qu’il pourrait être opportun de réduire la thermosensibilité par rapport à sa valeur actuelle. Notons également que le raisonnement décrit dans la Table 3 est un peu trop théorique pour plusieurs raisons. Il ne tient pas compte de la croissance du besoin, de la difficulté qu’il y aurait à installer des PAC dans tous les logements (contraintes visuelles, contraintes de taille, …), mais surtout à se débarrasser complètement des convecteurs électriques. Il suffirait que 15% du besoin de chaleur couvert par des PAC dans ces scénarios soit en fait couvert par des convecteurs électriques (rajoutés dans les appartements) pour avoir 30 TWh/an de plus et 1GW/°C de thermo-sensibilité en plus.
</span>

<span class="mytext">
Nous allons voir dans la section suivante que le gaz (biogaz donc) peut être une bonne solution pour contribuer à la maîtrise de la thermosensibilité sans augmenter les émissions.
</span>

# Le gaz, un vecteur utile pour un service de puissance

## Comment gérer la conso thermosensible ?  
<span class="mytext">
En plus des solutions évoquées dans la [Table 3](#CAPTable3) pour faire baisser la thermosensibilité, il est possible d’utiliser le gaz pour fournir un service de puissance. Nous allons maintenant comparer plusieurs approches utilisant du méthane selon que celui-ci est utilisé directement pour la production de chaleur, pour la production d’électricité (qui sera ensuite transformée en chaleur), ou enfin pour la cogénération d’électricité et de chaleur.
</span>
<div class="mytext">
<ul> <li> le coût d’investissement (€/kW),</li>
<li>la flexibilité, c’est à dire la rapidité avec laquelle la puissance peut être rendue disponible,</li>
<li> le caractère décentralisé, c’est à dire leur capacité à soulager une contrainte locale sur sur le réseau de distribution d’électricité </li>
<li> le COPg de la conversion de gaz en chaleur, en supposant que toute électricité produite est ensuite convertie en chaleur grâce à une PAC ayant un COP de 3. </li>
</ul>
</div>
<span class="mytext">
Dans la perspective d’un système décarboné ce gaz devrait être du biométhane, mais pourra également être de l’hydrogène. La biomasse pourrait avoir un rôle ici également. Le combustible correspondant serait donc en volume très limité, c’est pourquoi le dernier critère donne la quantité de méthane consommé par kWh de chaleur fourni.
</span>

## Chaudière gaz
<span class="mytext"> Il ne s’agit pas de continuer à utiliser les 15 millions de chaudières à gaz en continu l’hiver pour une consommation de 160 TWh de gaz (cf Annexe 1) mais bien d’installer des PAC électrique pour une utilisation 90% du temps. Il est en effet possible de garder les chaudières existantes pour un service de puissance dans les cas où la thermo-sensibiltié est un problème pour l’équilibre du système électrique. C’est le principe de ce que l’on appelle une PAC hybride (et qui est vendue aujourd’hui en un bloc PAC+chaudière par les gaziers). Le passage à l’utilisation de la chaudière gaz peut se faire de manière automatique, avec un signal prix ou directement à la demande du gestionnaire du système, en période de grand froid ou lorsque les moyens de production disponibles sur le système électrique ne sont pas suffisants pour couvrir la demande (grand froid, vent et soleil faibles). La PAC hybride consomme peu de gaz car elle fonctionne la majorité du temps sur l’électricité, mais elle fournit un service de puissance. Le temps de réponse d’une chaudière gaz est très court, et en une minute on peut passer de la PAC à la chaudière gaz. L’ajout de la chaudière gaz à la PAC n’implique pas nécessairement un surcoût si celles-ci sont déjà présentes. Une chaudière gaz ne coûte de toute façon pas très cher à la puissance installée : 125€/kW. Et pour cause, nous l’avons déjà dit, la puissance et le stockage sont bien moins un problème avec le gaz qu’avec l’électricité. Finalement la chaudière gaz est décentralisée et permet donc de lever des contraintes liées à la thermo-sensibilité dans le réseau de distribution. Le rendement de la chaudière gaz est de 90% pour les anciennes chaudières et d’environ 100% pour les chaudières à condensation, ainsi pour la chaudière gaz nous pouvons dire que COPg=0.9, ce qui est, nous allons le voir, plutôt mauvais. L’avantage de la chaudière gaz est son coût (lorsqu’un système de distribution de chaleur est déjà présent).
</span>

## Production d’électricité
<span class="mytext">  Une solution centralisée, pour gérer le problème de la thermosensibilité en utilisant du gaz, est la production d’électricité. Par centralisé nous ne pensons pas ici à un système dans le logement mais bien à quelques grosses centrales électriques à l’échelle de la France. Il existe pour cela deux familles de technologies : d’un côté les turbines à combustion (TAC) avec un coût d’investissement de l’ordre de 600 €/kW, un rendement de l’ordre de 30-35%, et de l’autre des centrales à cycle combiné gaz qui sont plus chères 800 €/kW à l’investissement mais ont des rendements de l’ordre de 55%. Si l’électricité produite est transformée en chaleur avec des PAC ayant un COP de 3, le COPg sur toute la chaîne de conversions gaz-chaleur est de COPg=1.5 dans le cas du cycle combiné et de COPg=1 dans le cas des TAC. Les TAC sont flexibles et peuvent démarrer en moins de 15 minutes alors qu’il faut quelques heures pour démarrer un cycle combiné. Cette production d’électricité centralisée ne permet évidemment pas de lever des contraintes dans le réseau de distribution d’électricité.
</span>
## Cogénérations d’électricité et de chaleur
<span class="mytext">Lors de la production d’électricité à partir de gaz on peut chercher à récupérer la chaleur produite et normalement perdue. Dans le cas d’un système centralisé on parle de cogénération et la chaleur peut être utilisée dans un réseau de chaleur ou pour une activité agricole (essentiellement pour chauffer des serres, même si cela ne semble pas compatible avec une société bas carbone). Dans le cas d’un système décentralisé (donc à l’échelle d’un logement, mais centralisé dans le logement) on parle de micro-cogénération. Il existe plusieurs types de systèmes mais la micro-cogénération n’est pas adapté à des petits logements et pourrait plutôt être utilisée pour des logements collectifs. Le ratio électricité / chaleur (E/C), donne le rapport entre l’électricité et la chaleur utile produite. Le coût d’un système individuel utilisant un moteur à combustion interne Stirling est autour de 10-15 k€, offre un rendement proche de 100% et un rapport E/C de 1/6. Cela signifie que COPg=1/(5/6+1/6*1/3)  = 1.125.
</span>

<span class="mytext">Il existe également des systèmes utilisant de la biomasse (comme des granulés bois, de la paille, …) plutôt que du gaz. Les piles à combustible (PiAC) utilisent elles du dihydrogène. La pile à combustible permet de consommer de l’hydrogène et produit ½ d’électricité et ½ de chaleur avec un rendement qui peut approcher les 90%. L’hydrogène peut être produit à partir d’électricité avec des rendements de l’ordre de 70-75% et l’intérêt de la PiAC dans un contexte décarboné vient de la possibilité de stockage offerte par l’hydrogène. La pile à combustible n’est pas encore une technologie mature, on trouve au Japon des modèles de 700W pour 8k€ [18], soit plus de 10000 €/kW.  Le principal avantage de la PiAC est qu’elle utilise de l’hydrogène plutôt que du méthane. Un autre avantage est qu’elle n’a pas de partie mobile, elle est donc moins bruyante. Notons qu’il est possible d’utiliser une pile alimentée indirectement par du biogaz (en couplant un reformeur).
</span>

## Table de synthèse

| |Coût [€/kW]   | Rendement chaleur COPg|Centralisé-décentralisé| Flexibilité|
|:------------------|:-----|:-----|:-----|:-----|
|Chaudiere gaz     |150 |0.9|décentralisé |1 minute|
|TAC Gaz     |150 |3*0.33= 1|semi-centralisé |15 minutes|
|CCG    |800 |3*1/2 = 1.5|centralisé | 3 heures|
|Micro-cogé     |[2,3]*$10^3$ |1/(5/6+1/18)  = 1.125|décentralisé |adaptation usage chaleur|
|PiAC     |$10^4$ |Pas d’utilisation du biogaz|décentralisé |1 seconde|
{: .wrapstyle  .simple7}
<span class="legendtext" id="CAPTable4" style="display:block;text-align:center">
**Table 4** -- Pour la deuxième colonne, nous faisons l’hypothèse que l’électricité produite est utilisée pour générer de la chaleur dans une PAC ayant un COP de 3. Ces coûts capacitaires sont à mettre en regard du cout de la PAC (500-1000 euros/kW pour la PAC air-eau, 4000€+1000€/kW pour la PAC air-eau), et du coût capacitaire du nucléaire [3000-6500] euros/kW)
 </span>

<span class="mytext">La [Table 4](#CAPTable4) donne une synthèse des technologies mentionnées ici. Il faut observer que le surcoût d’une chaudière gaz (125 euros/kW contre 1000 à 3000 euros/kW pour la PAC) n’est pas très important mais que si le volume de biogaz est une contrainte forte il sera peut-être préférable d’utiliser un cycle combiné. Les chaudières gaz amèneraient une flexibilité plus importante pendant les périodes de chauffe car elles démarrent très rapidement et qu’elles peuvent alléger le réseau de distribution, mais le cycle combiné serait lui disponible toute l’année. Les chaudières gaz auraient une bonne complémentarité avec l’énergie solaire (thermique ou photovoltaïque). Les systèmes impliquant l’utilisation d’hydrogène sont pour l’instant très chers mais ces prix vont baisser. L’intérêt du vecteur hydrogène par rapport au biogaz est qu’il est possible, par électrolyse, de le produire à partir d’électricité faiblement carbonée à des rendements corrects (70%-75%) alors que le rendement de production de biogaz à partir d’électricité (par électrolyse puis méthanation) n’est pas très bon (autour de 50%). Cependant l’hydrogène est moins pratique à stocker et à transporter, c’est une vaste question sur laquelle nous reviendrons.
 </span>
 <span class="mytext">Nous avons déjà dit qu’il n’y a pas de transition dans le bâtiment sans réduction majeure du volume de gaz consommé, on peut donc rajouter qu’il n’y a pas de transition dans le bâtiment sans un minimum de volume de gaz consommé et peut-être sans une augmentation de la puissance de chaudières gaz installées, des cycles combinés gaz installés. Peut-être qu’un recyclage des chaudières gaz existantes pourrait être pertinent pour réduire dès aujourd’hui la thermosensibilité. Ces aspects devraient de plus en plus être intégrés dans les études de RTE.
</span>
<span class="mytext">La valeur de ces systèmes fournissant un soutient en puissance, n’est pas vraiment intégrée aux systèmes d’aides ou aux réglementations aujourd’hui, et la construction de nouvelles centrales CCG est interdite par la loi. En effet, il n’existe pas de mécanisme satisfaisant qui fasse remonter la contrainte de thermosensibilité dans les investissements, même si c’est un des objectifs du marché de capacité dans le système électrique que d’inciter les consommateurs à la maîtriser. Ce marché de capacité reflète aujourd’hui des coûts qui ne sont pas des coûts d’investissement (plutôt des coûts annuels de fonctionnement/sortie de mise sous cocon d’une centrale à gaz) et même si cela change (par exemple si l’on développe massivement des PAC) on peut bien imaginer que du point de vue du consommateur particulier il n’y aura jamais là un signal assez fiable sur le long terme pour déclencher des investissements. Dans le cas d’un développement massif des PAC ce signal prix arrivera trop tard (les chaudières gaz auront déjà disparu). Il est à noter que le fameux facteur 2.58 appliqué aujourd’hui (mais qui va être réduit dans la RE2020) à la consommation d’énergie finale électrique comme une « pénalité », est très discutable sur le plan physique (selon que l’on considère que l’électricité du chauffage électrique est produit à partir de fioul, de gaz ou de nucléaire, ou d’une combinaison bien choisie de ces trois sources) mais c’est un garde-fou contre une évolution dans laquelle 15 millions de PAC se développeraient sans tenir compte des lois de la physique qui imposent l’équilibre entre l’offre et la demande sur le système électrique à tout moment, même lorsqu’il fait froid.
</span>
<span class="mytext">Par ailleurs ces systèmes hybrides pourraient apporter une flexibilité supplémentaire dans le système électrique permettant globalement de réduire ses coûts, en particulier dans le cas d’un système fortement renouvelable. En effet le levier en puissance de l’utilisation du gaz dans des chaudières implique des coûts capacitaires très faibles, et les CCG sont également très compétitives. Par ailleurs, il n’est pas vraiment souhaitable de chercher à piloter une demande sur un chauffage électrique juste en l’éteignant quelques minutes ou quelques heures (comme nous cherchons à le faire aujourd’hui) car cela résulte en générale par une baisse de température dans le bâtiment et un pic de consommation au rallumage qui peut être plus problématique que celui que l’on a cherché à effacer.
</span>

# Conclusion

<span class="mytext">Nous avons rappelé que la transition énergétique dans le bâtiment repose sur (i) la diminution du besoin de chaleur par l’amélioration de l’efficacité des bâtiments, (ii) l’augmentation de l’efficacité des systèmes de chauffage principalement en par l’utilisation de pompes à chaleur (électrique ou hybrides) ou de solaire thermique, et (iii) l’utilisation de vecteurs énergétiques qui impliquent des émissions de GES suffisamment faibles. Nous avons donc pu réaffirmer le rôle majeur que doivent jouer la rénovation, le vecteur bois, le vecteur électricité, et les pompes à chaleur dans la transition énergétique du bâtiment. La Table 3 nous montre que les 3 MtCO2eq/an d’émissions dues au chauffage résidentiel sont à notre portée si tous les leviers sont déployés. Cela implique de ne pas commencer seulement par les leviers les plus rentable économiquement (les PAC) mais d’avancer en parallèle et dès maintenant sur la rénovation de bâtiments (peut-être même de conditionner le développement des PAC à celle-ci), le chauffage au bois, et le solaire thermique.  
</span>

<span class="mytext">Nous avons également montré que les systèmes hybrides permettant de coupler le service de puissance du gaz à l’efficacité des systèmes électriques sont intéressant pour éviter un accroissement très préjudiciable de la thermosensibilité électrique. Ces systèmes et la contrainte à laquelle ils répondent sont connus mais souvent oubliés lorsque l’on parle de transition énergétique. Nous pensons qu’ils devraient être développés et encouragés en parallèle des PAC, du bois-énergie et des rénovations. Nous pensons que cela devrait s’accompagner d’un développement raisonné du biogaz, avec des volumes beaucoup plus faibles que ceux utilisés aujourd’hui mais jouant un rôle de puissance important. Il faut noter le caractère très optimiste qu'il y a à supposer la disparition des chauffages électriques de type "grille pain" (ceux qui ne sont pas des PAC). Optimiste également de penser que l'on peut mettre des PAC partout (pour des raisons de place ou d'esthétique extérieur de bâtiment), mais nous pensons qu'une limitation au maximum de leur développement est très important.
</span>


<span class="mytext">Des questions persistent heureusement : savoir jusqu’à quel point il faut pousser les différentes solutions, faut-il inonder le parc de bâtiments de PAC ? de PAC hybrides ? Poêles à bois ? augmenter la capacité installée de centrales CCG ? faut-il faire seulement des rénovations pour obtenir des bâtiments basse consommation (BBC) ? quel peut-être le rôle des réseaux de chaleur ? quel doit être le rôle du bois énergie ? Nous n’avons pas répondu précisément à toutes ces questions ici mais nous avons montré l’intérêt des différentes pistes tout en prônant la diversité des solutions. Les pistes données seront exploitées de manière plus quantitative dans des posts ultérieurs. Dans le post suivant nous essaierons d’avancer quelques estimations concernant la rénovation de bâtiment.
</span>


<span class="mytext">Nous n’avons pas la prétention d’avoir fait le tour de la question et certaines choses auront pu nous échapper, aussi, nous espérons que ces analyses contribueront à éclairer le débat et nourriront des échanges sur le sujet. En définitive, il s’agit de donner collectivement crédit et force aux mesures qui seront prises pour atteindre les objectifs de la SNBC, et ce de manière constructive (sans dire « le gouvernement n’a pas de stratégie »), sans se laisser dérouter de la complexité du sujet par telle ou telle pression liée à des intérêts particuliers qui nous pousseraient à laisser un vecteur ou une technologie prendre le pas sur toutes les autres de manière déraisonnée.
</span>

# Bibliographie

[0] [Stratégie nationale bas carbone](https://www.ecologique-solidaire.gouv.fr/strategie-nationale-bas-carbone-snbc)

[1] [Consultation publique sur le « projet de stratégie à long terme pour mobiliser les investissements dans la rénovation du parc national de bâtiments à usage résidentiel et commercial, public et privé ».](http://www.consultations-publiques.developpement-durable.gouv.fr/projet-de-strategie-a-long-terme-pour-mobiliser-a2136.html Du 17/02/2020 au 10/03/2020)

[2] [2017, Les ménages et la consommation d’énergie.](https://www.statistiques.developpement-durable.gouv.fr/les-menages-et-la-consommation-denergie)

[3] [2019, Visions de l’ADEME 2035-2050.](https://www.ademe.fr/lademe/priorites-strategiques-missions-lademe/scenarios-2030-2050)

[4] [2017, Scenario Negawatt horizon 2050.](https://negawatt.org/Scenario-negaWatt-2017-2050)

[5] https://www.bmwi.de/Redaktion/EN/Publikationen/energy-efficiency-strategy-buildings.pdf?__blob=publicationFile&v=7

[6] [2017, étude de l’ADEME sur les réseaux de chaleur](https://www.ademe.fr/avis-lademe-reseaux-chaleur-alimentes-energies-renouvelables-recuperation)

[7] [2009, BIOMASSE FORESTIERE, POPULICOLE ET BOCAGERE DISPONIBLE POUR L’ENERGIE A L’HORIZON 2020](https://www.ademe.fr/sites/default/files/assets/documents/biomasse-forestiere-populicole-et-bocagere-2009.pdf)

[8] [Mars 2020, décrypter l’énergie, La méthanisation est-elle synonyme d’intensification de l’agriculture et de pollutions ?](https://decrypterlenergie.org/la-methanisation-est-elle-synonyme-dintensification-de-lagriculture-et-de-pollutions)

[9] [Février 2020, Bastamag « Produire de l’énergie plutôt que nourrir : comment le lobby du gaz « vert » transforme l’agriculture française. »](https://www.bastamag.net/methanisation-lobby-gaz-vert-biogaz-agriculture-energetique-alimentaire)

[10] [Base Carbone de l’ADEME.](https://www.bilans-ges.ademe.fr/documentation/UPLOAD_DOC_FR/index.htm?gaz.htm)

[11] [Scenario Afterre 2050.](https://afterres2050.solagro.org/a-propos/le-projet-afterres-2050/)

[12] [2013, étude de Carbone 4 sur les pompes à chaleur.](http://www.carbone4.com/les-pompes-a-chaleur/)

[13] [2019, variabilité de la consommation électrique et thermo-sensibilité.](https://www.energy-alternatives.eu/2019/05/24/variabilite-de-la-consommation-electrique-et-thermo-sensibilite.html)

[14] open data ENEDIS [« consommation journalière par catégorie de client »](https://data.enedis.fr/explore/dataset/bilan-electrique-transpose/information/?flg=fr)

[15] 2018, [50% ou 50%](https://jancovici.com/transition-energetique/electricite/50-ou-50/) post de Jean-Marc Jancovici.

[16] [2018 Air conditioners and comfort fans, Review of Regulation 206/2012](https://hal-mines-paristech.archives-ouvertes.fr/hal-01796759/document) and 626/2011 Final report

[17] [Bois énergie et pollution aux particules fines.](https://www.ademe.fr/expertises/energies-renouvelables-enr-production-reseaux-stockage/passer-a-laction/produire-chaleur/dossier/bois-biomasse/bois-energie-qualite-lair)

[18] [Piles à combustibles vendues au Japon.](https://fuelcellsworks.com/news/fcw-exclusive-tokyo-fuel-cell-expo-2019-300000-ene-farms/)

# Annexe 1 : Etat des lieux des moyens de chauffage en France

<span class="mytext">
On peut combiner les informations du recensement français avec les estimations de consommation de chauffage par vecteur énergétique, données à la section précédente (Table 1), pour obtenir la description énergétique du parc de bâtiments français donnée à la Figure 3.
</span>

<span class="text" id="Figure3" style="display:block;text-align:center">
![Image]({{site.baseurl}}/assets/images/Posts/2020-03-22/SNBCChauffageFigureAnnexeParcBatiParClasse.png){:.border}
</span>
<span class="legendtext" id="CAPFigure3" style="display:block;text-align:center">
**Figure 3** -- Composition du parc de résidences principales français vis-à-vis du chauffage. Source : recensement INSEE 2016 et données de la Table 1 de la section précédente. La catégorie « Autre » correspond ici majoritairement au bois.
</span>

<span class="mytext">On note que l’importance du chauffage électrique diffère selon que l’on regarde le nombre de logements ou la consommation d’énergie. Il y a bien 33% environ des logements français qui sont chauffés à l’électricité, mais ces logements, en plus d’être plus performants en moyenne, sont moins grands que les autres et en termes de besoin énergétique final le chauffage électrique représente moins de 40 TWh sur un total de 300 TWh, soit moins de 15% du besoin énergétique global. Il faut ici rappeler que l’électricité comme mode de chauffage a été intégrée dans les bâtiments à la suite du programme nucléaire, du choc pétrolier de 1973, et des premières réglementations thermiques, donc plutôt entre 1980 et 2000. Ainsi les bâtiments chauffés à l’électricité sont en moyenne plus récents et plus performant que les autres. Les bâtiments plus vieux (ceux d’avant 1980) chauffés à l’électricité existent mais sont plutôt des bâtiments rénovés ou pour lesquels un changement de chauffage a été fait après coup pour des raisons économiques. Or, sur le plan économique le gaz a presque toujours été plus favorable pour des logements plus grands et moins performants : le chauffage au gaz implique des coûts marginaux faibles mais des investissements plus élevés. En effet, le prix du kWh de gaz est beaucoup moins important que celui du kWh électrique mais le gaz implique un entretien de la chaudière, un investissement dans un système de distribution de chaleur et des émetteurs. Avant l’arrivée des pompes à chaleur air-eau ces coûts fixes n’existaient presque pas pour le chauffage électrique.  En plus de cela la puissance de gaz délivrée au consommateur n’est jamais limitante alors qu’elle l’est pour l’électricité.
</span>

# Annexe 2 : la thermosensibilité dans différents secteurs

<span class="mytext"> Dans notre discussion autour de la thermosensibilité, nous nous sommes concentrés sur le secteur résidentiel de la consommation électrique et il nous faut discuter l’importance de ce secteur vis-à-vis de la thermosensibilité. Les données open data de ENEDIS [14] permettent d’obtenir entre 2014 et 2019 la décomposition de la consommation journalière et donc de la thermosensibilité entre 5 secteurs : Résidentiel, Professionnel, Entreprise, PME/PMI et autre (autre étant la différence entre les données à la maille France et la somme des 4 secteurs de ENEDIS, ainsi le secteur « autre » contient notamment les pertes, les consommateurs branchés directement sur le réseau de transport). Pour la définition de ces secteurs nous renvoyons au site de ENEDIS, mais pour l’heure nous souhaitons simplement observer que la thermosensibilité résidentielle est en croissance lente depuis 2014 (à l’image de la thermosensibilité totale) et qu’elle est passée de de 1.4 GW/°C en 2015, à 1.5 GW/°C environ en 2019.
</span>

<span class="text" id="Figure4" style="display:block;text-align:center">
![Image]({{site.baseurl}}/assets/images/Posts/2020-03-22/ThSensParSecteurFigure1.png){:.border}
</span>
<span class="legendtext" id="CAPFigure4" style="display:block;text-align:center">
**Figure 4** --  Thermosensibilité par secteur (d'après données et secteurs ENEDIS [14])
</span>
