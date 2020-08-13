---
title: Décomposition du coût du mix de production de l'électricité
tags: mix-production intermittence evolution
article_header:
  type: cover
  image:
    src: /assets/images/Posts/2020-05-07/DSCF8920c.jpg
---

<div class="summary" style="display:block; text-align: justify">
<em>
L’objectif de ce post est d’introduire une base simple permettant la description du mix de production d’électricité d’un pays.
</em>
</div>
<!--more-->
<span class="mytext">
Dans un post précédent [1], nous avons présenté une manière de modéliser les coûts économiques et environnementaux d’un système électrique à partir de la connaissance de l’énergie produite $E_i$ et de la puissance installée $P_i$ pour chaque moyen de production $i$ du système :
</span>
<span class="mytext">
$$ \sum_i \alpha_i^{cout} E_i+\beta_i^{cout} P_i$$
</span>
<span class="mytext">
Ceci nous a permis de retrouver une estimation du coût de notre système actuel et de donner une estimation du coût à l’horizon 2050 d’un système fortement renouvelable et de celui d’un système fortement nucléaire. Des valeurs pour les coefficients $\alpha_i^{cout}$ (en [€/MWh]) et $\beta_i^{cout}$ (en [€/kW/an]) ont été proposées sans donner beaucoup de détails sur les calculs et les sources permettant de les obtenir. Le coût marginal $\alpha_i^{cout}$ est en général connu et facile à trouver, mais le coût fixe actualisé et annualisé $\beta_i^{cout}$ s’obtient à partir de données économiques comme l’actualisation, le coût d’investissement, les coût annuels d’exploitation d’une manière que nous allons détailler ici. Ceci nous permettra d’introduire le LCOE (levelized cost of energy) qui est très utilisé dans le domaine.
Par ailleurs, nous avons considéré de grandes familles de technologies de production : « nucléaire », « charbon », « gaz », « hydraulique », « photovoltaïque », « éolien », ou « biomasse ». La précision des données de coût (économiques et environnementaux) va nécessiter de donner quelques précisions sur la diversité des technologies existantes dans ces familles. C’est ce que nous allons faire dans une première partie qui nous permettra aussi d’introduire les données économiques propres à chaque familles de technologies.
</span>

# Quelques précisions sur la diversité cachée derrière ces grandes classes de moyens de production

## introduction : différentes sortes de coûts
<span class="mytext">
Nous n’allons pas détailler ici toutes variations existantes au sein de chacune des familles de technologies, ou des carburants utilisés, il y aura presque dans chaque cas un post futur plus détaillé mais pour que le niveau de détail choisi jusqu’à maintenant ne paraisse pas trop arbitraire, et pour comprendre certains enjeux autour du facteur de charge, du rendement, des émissions de GES, ainsi que du coût il est déjà utile d’avoir conscience de quelques sous-catégories. Aussi, pour chacun des moyens de production nous allons chercher à donner les variables suivantes :
</span>
<div class="text" style="display:block; text-align: justify">
<ul> <li>Les coûts d’investissement $C_I$ exprimés en €/kW (kW installé) et dépensé au moment juste avant que le projet ne commence à produire de l’énergie. Une somme investie 10 ans avant le démarrage du projet aura un impact sur le coût à livraison beaucoup plus important, et lié à l’actualisation, qu’une somme déboursée au moment du démarrage (« à la livraison »).</li>
<li>Les coûts annuels d’exploitation $C_F$ exprimés en €/kW/an (kW installé)  qui ne dépendent pas de l’énergie produite et qui correspondent plus à des coûts d’entretien, de gestion, la location d’un terrain, ou la rémunération du personnel. Ils sont payés pendant toute la durée de vie du projet. Ils sont dépensés chaque année pendant toute la durée de vie du projet, quel que soit la production.</li>
<li>Le coût marginal de production $C_M$ exprimé en €/MWh qui correspond à ce qu’il faut payer pour produire un MWh supplémentaire lorsque l’on produit déjà (et qui inclus d’une certaine manière des coûts de démarrage). Ces coûts sont payés à chaque fois que la centrale produit et sont donc proportionnels à l’énergie produite. Ils correspondent souvent à un simple coût de carburant, auxquels il faut rajouter par exemple la taxe carbone.</li>
<li> Emissions de GES $E_{ges}$ exprimées en /MWh.</li>
</ul>
</div>




## Centrales pilotables
<span class="mytext">
En ce qui concerne le **nucléaire**, on distingue [plusieurs générations](https://fr.wikipedia.org/wiki/G%C3%A9n%C3%A9rations_de_r%C3%A9acteurs_nucl%C3%A9aires). La seconde génération est celle en activité aujourd’hui et construite entre le début des années 70 et la fin des années 80. Les nouvelles centrales que l’on construit aujourd’hui sont de la troisième génération. Parmi les nombreuses technologies déployées de manière commerciales aujourd’hui (seconde et troisième génération), les deux plus importantes sont les réacteurs à [eau bouillante](https://fr.wikipedia.org/wiki/R%C3%A9acteur_%C3%A0_eau_bouillante) (dit « REB ») des réacteurs à [eau pressurisé](https://fr.wikipedia.org/wiki/R%C3%A9acteur_%C3%A0_eau_pressuris%C3%A9e) (dit « REP »). Une liste plus exhaustive est donnée dans le lien sur les générations. La quatrième génération est prévue pour les décennies à venir (un projet pilote a vu le jour en Russie) ; il existe plusieurs propositions qui visent, par des évolutions technologiques importantes, à avoir des centrales qui n’utilisent plus le même combustible mais une forme d’uranium beaucoup moins rare, qui permettent de retraiter une partie des déchets à vie longue qui existent aujourd’hui, qui ne présentent pas de risque d’emballement, qui peuvent plus facilement moduler leur production sans pertes de rendement (nous reparlerons de la modulation des centrales nucléaires actuelles dans un post ultérieur, car certaines choses sont possibles mais pas tout et c’est un sujet important). En France le projet de recherche Astrid abandonné récemment était dans cette lignée, mais dans le monde d’autres projets se poursuivent dans cette direction. Enfin, une dernière génération de nucléaire arrivera avec la fission. Sur le fonctionnement des centrales nucléaires, je renvoie vers les [vidéos du réveilleur](https://www.youtube.com/watch?v=HMystmGbctw) (youtubeur effectuant un travail documenté et abordable et que je citerai souvent). Pour les coûts, je donne dans la table ci-dessous quelques coûts d’investissement avec les sources associées.
</span>

<span class="mytext">
Pour le gaz (et le fioul), on distingue plusieurs grandes catégories de centrales. La plus élémentaire est la turbine à combustion (TAC, ou OCGT pour open cycle gaz turbine dans le cas du gaz) dans laquelle le gaz ou le fioul est mélangé à de l’eau et envoyé sous pression dans une turbine où il s’enflamme. Le principe de la TAC est très proche de celui du moteur d’avion. Dans la TAC la chaleur des gaz d’échappement est perdue mais l’on peut la récupérer de différentes manières. Une première solution est de faire chauffer de l’eau (dans une sorte de grande bouilloire) dont les vapeurs vont aller entrainer une seconde turbine connectée à celle de la TAC. C’est ce que l’on appelle un cycle combiné (CCGT pour le cycle combiné gaz). Le rendement d’un CCG est donc meilleur : il peut monter autour de 55% (il y a même un record à 64% détenu par la centrale de Bouchain), alors que celui de la TAC est limité autour de 35-40% (sauf pour des technologies très particulières utilisant des fluides supercritiques). Le coût d’installation du CCG est plus élevé, et ce dernier demande quelques heures pour démarrer alors que la TAC n’a pas besoin de plus de 30 minutes. Une autre manière d’utiliser les gaz d’échappement de la TAC est d’en extraire directement la chaleur pour une autre application (réseau de chaleur, serres, …), c’est ce que l’on appelle la cogénération. Dans ce cas le rendement global de l’installation est meilleur mais l’utilisation de la TAC est un peu asservie au besoin de chaleur : on est obligé de produire quand il faut froid et pas nécessairement seulement lorsqu’il y en a besoin.
</span>

<span class="mytext">
Dans une centrale à charbon on fait généralement chauffer de l’eau en brûlant du charbon, la vapeur sous pression ainsi générée est envoyée dans une turbine qui produit de l’électricité. Pour la production d’électricité à partir du charbon il existe plusieurs technologies plus ou moins efficaces selon le niveau de pression utilisé lors de la combustion du charbon. Les rendements correspondants peuvent varier entre 30 et 50%, et les impacts environnementaux varient eux aussi beaucoup selon la qualité de la combustion. L’industrie du charbon met en avant : l’augmentation des rendements de ses nouvelles centrales qui envoient dans la turbine des fluides « super-critiques » ; ainsi que la séquestration du carbone capturé en sortie de cheminée. Pourtant, le charbon reste à l’heure actuelle un moyen de production d’électricité parmi les plus polluants, et ce sur beaucoup de plans.
</span>

|Système                            |Rendement   |CAPEX €/kW   |
|:-------------------------------------|:-----|:-----|
|Gaz -- TAC        |35% |600 |
|Gaz -- CCGT |54%  |970 |
|Coal – Subcritical   |40%  |1200   |
|Coal – Supercritical    |45%|-2.65 |
|Coal – Ultra-Supercritical |50%   |3.35  |
|Nuke - Moyenne parc français actuel  | 33%   |3.2   |
|Nuke - Flamanville Hinckley point (EPR)  |33%    |3.2   |
|Nuke - Taishan (EPR) |33%    |3.2   |
{: .mbtablestyle .wrapstyle .simple5}
<span class="legendtext" id="CAPTable1" style="display:block;text-align:center">
**Table 1** -- moyens de production d’électricité au gaz et au charbon ainsi que leur efficacité et le coût d’investissement correspondant. Source pour le charbon : [1], pour le gaz : U.S. energy information administration [[2](https://www.eia.gov/analysis/studies/powerplants/capitalcost/pdf/capcost_assumption.pdf)]
</span>
<span class="mytext">
La production d’électricité à partir de biomasse ressemble assez à ce que l’on fait avec du charbon, combustion de la biomasse pour faire chauffer de l’eau et faire tourner une turbine à vapeur. La qualité de la combustion, le caractère renouvelable, les impacts environnementaux dépendent beaucoup de la biomasse utilisée, de sa nature et de sa provenance, ils peuvent être acceptables lors de l’utilisation de déchets ou d’une biomasse qui serait locale et tout de suite replacée mais aussi très mauvais lorsque par exemple on choisit de couper des forêts à l’autre bout du monde sans rien replanter.
</span>
<span class="mytext">
On distingue en générale l’électricité produite à partir d’un charbon de basse qualité -comme la lignite- de celle produite à partir de charbon noir. Il existe une grande variété de type de charbons liée à des niveaux de houillification différents. Ils se distinguent notamment par leur humidité, leur teneur en carbone ou leur pouvoir calorifique différents. Il n'existe pas de définition unique internationalement retenue permettant de classifier précisément les charbons mais on trouve une classification et quelques explications dans la base carbone de l’ADEME [[3](https://www.bilans-ges.ademe.fr/documentation/UPLOAD_DOC_FR/index.htm?solides3.htm)]. La Lignite est moins dense, sa combustion est moins bonne et donc plus polluante (pas sur le plan des émissions de GES cela dit voir table ci-dessous), son transport (ramené à la consommation d’énergie qu’il implique) est plus coûteux. Son extraction se fait souvent dans des mines à ciel ouvert qui peuvent avoir un avantage économique à court terme mais certainement pas un avantage environnemental. Pour ces raisons la Lignite continue d’être exploitée dans cas où c’est une ressource locale pour des raisons de coût, et parfois pour des questions de préservation d’une économie locale. L’Allemagne possède sur son territoire une ressource importante de lignite qui est utilisée pour la moitié de l’électricité produite à partir de charbon.  
</span>


<table class="simple7">
<thead>
<tr>
  <th >Produits</th>
  <th >Emissions</th>
  <th >PCI</th>
  <th align="center" colspan="3" class="mb6">Share</th>
  <th  colspan="2">Cost [$/ton]</th>
</tr>
<tr>
  <th>(kWh/kg)</th>
  <th>gCO2eq/kWhth</th>
  <th></th>
  <th class="mb6"></th>
  <th></th>
  <th></th>
  <th>2017</th>
  <th>2017</th>
</tr>
<tr>
  <th>(TWh/Mt)</th>
  <th>(TWh/Mt)</th>
  <th></th>
  <th class="mb6">US</th>
  <th>World</th>
  <th>DE</th>
  <th>US</th>
  <th>DE</th>
</tr>
</thead>
<tbody>
<tr>
  <td >Anthracite (hard/black coal)</td>
  <td >384</td>
  <td >9 à 10</td>
  <td >1</td>
  <td >14</td>
  <td >-</td>
  <td >93</td>
  <td ></td>
</tr>
<tr>
  <td >Bituminous</td>
  <td >374</td>
  <td >5 à 9</td>
  <td >46</td>
  <td >76</td>
  <td >-</td>
  <td >55</td>
  <td >50</td>
</tr>
<tr>
  <td >subbituminous</td>
  <td >377</td>
  <td >4 à 5</td>
  <td >45</td>
  <td >-</td>
  <td >-</td>
  <td >14</td>
  <td ></td>
</tr>
  <tr>
    <td >Lignite (brown coal)</td>
    <td >393</td>
    <td >2 à 3</td>
    <td >9</td>
    <td >14</td>
    <td >100</td>
    <td >19</td>
    <td >20</td>
  </tr>
</tbody>
</table>


<!-- | Produits                   |	Emissions    |	PCI	   |      | Share|      | Cost | [\$/ton]   |
|	(kWh/kg) 		               |	gCO2eq/kWhth |	       |      |      |      |  2017|	2017|
|	(TWh/Mt)	                 | (TWh/Mt) 	   |         |US    |	World| DE	  |US	   | DE   |
|:---------------------------|:--------------|:--------|:-----|:-----|:-----|:-----|:-----|
|Anthracite (hard/black coal)|	384          |	9 à 10 |	1   |	14   |	-	  | 93	 |      |
|Bituminous                  |	374          |	5 à 9  |	46  |	76	 |	-	  | 55	 |  50  |
|subbituminous               |	377          |	4 à 5  |	45  |	-    |	-	  | 14	 |      |
|Lignite (brown coal)        |	393          |	2 à 3  |	9   |	14   |	100	| 19	 |  20  |
{: .mbtablestyle .center}
-->
  <span class="legendtext" id="CAPTable2" style="display:block;text-align:center">
  **Table 2** -- différentes sortes de charbon. Sources : U.S. EIA [[4](https://www.eia.gov/energyexplained/coal/prices-and-outlook.php)] et ADEME [[3](https://www.bilans-ges.ademe.fr/documentation/UPLOAD_DOC_FR/index.htm?solides3.htm)].
    </span>

<span class="mytext">
Dans **l’hydraulique**, on fait de l’électricité en faisant passer de l’eau dans une turbine. On différenciera une centrale hydraulique selon des caractéristiques techniques et naturelles. D’un côté on regardera le type de turbine, la possibilité de faire fonctionner la turbine à vitesse variable, l’existence d’une pompe pour faire remonter l’eau. De l’autre il s’agira de différentier l’hydraulique « au fil de l’eau » qui tire parti d’un fleuve ou d’une petite rivière sans bassin de stockage, et un grand barrage de vallée alpine qui récupère un faible débit d’eau mais peut garder en stock plusieurs jours de production à pleine puissance. Le fil de l’eau dans certaines grosses centrales de la vallée du Rhône permet tout de même de moduler la puissance de production sur une ou deux heures. Certains barrages sont équipés de pompes qui permettent de faire remonter l’eau et jouent ainsi un rôle de stockage d’électricité, c’est ce que l’on appelle les STEP (station de transfert d’énergie par pompage, qui ont le même nom que les stations d’épuration). En France nous avons actuellement un peu moins de 5 GW de STEP dont certaines ont une capacité de stockage allant jusqu’à plusieurs jours (72 heures pour la plus grande). Le gisement Français d’hydraulique est assez saturé mais certains grands barrages pourraient être équipé de pompes pour augmenter la puissance disponible de stockage, on parle de 2GW supplémentaires. Il existe également un gisement de micro-STEP dont nous parlerons ultérieurement lorsqu’il sera plus précisément question du stockage.
</span>

## Electricité d’origine renouvelable
<span class="mytext">
Pour le **solaire photovoltaïque** il est pertinent de distinguer les tailles de centrales : grandes centrales au sol occupant plusieurs hectares, centrales en toiture de centre commercial ou sur un parking (dites « ombrières » pour l’ombre qu’elles apportent aux voitures), et petites centrales de quelques kW sur le toit d’une maison. Pour les grosses centrales il faut distinguer les centrales avec des systèmes de tracking (système avec un axe ou deux axes, qui permet de suivre la position du soleil dans le ciel pour maximiser la production) de celles qui n’en ont pas.
</span>


<span class="text" id="Figure1" style="display:block;text-align:center">
![Image]({{site.baseurl}}/assets/images/Posts/2020-08-20/CAPEX-PV.png){:.border}
</span>
<span class="legendtext" id="CAPFigure1" style="display:block;text-align:center">
**Figure 1** -- Décomposition des coûts d’investissement moyens observés dans les appel d’offre CRE, étude publiée en février 2019, [[1](https://www.cre.fr/Documents/Publications/Rapports-thematiques/Couts-et-rentabilites-du-grand-photovoltaique-en-metropole-continentale)].
</span>
<span class="mytext">
Finalement un facteurs qui déterminera de manière essentielle les performances d’un système de production photovoltaïques est la localisation de la centrale. Une centrale au sud de l’Espagne produira plus qu’une centrale au nord de l’Allemagne et surtout sa variabilité hiver/été sera beaucoup moins importante mais nous reparlerons de tout çà de manière quantitative lorsque nous parlerons de la variabilité de ces moyens de production. Sur le plan environnemental le lieu de construction des panneaux (et le mix électrique utilisé pour faire fonctionner les machines qui produisent les panneaux) peut aussi avoir de l’importance. Finalement, une classe à part de l’énergie solaire est le solaire à concentration : thermodynamique ou photovoltaïque. Le solaire thermodynamique permet de chauffer de l’eau (à plus ou moins haute température) pour l’utiliser directement pour le chauffage ou dans le cas du solaire à concentration thermodynamique faire tourner une turbine et permet donc de stocker l’énergie produite dans la journée pour la réutilisé le soir. Ce type de système est très développé en Espagne. On retrouvera une vidéo assez complète du réveilleur sur le sujet des différentes technos solaires [ici](https://www.youtube.com/watch?v=dykSjXQhSjM).
</span>
<span class="mytext">
Pour **l’éolien**, la localisation de la centrale est aussi fondamentale. Mais il faut avant tout distinguer l’éolien offshore (en mer) de l’éolien on shore (sur terre). L’éolien en mer peut être posé sur le fond de la mer ou flottant lorsque la mer est trop profonde. Dans tous les cas un facteur qui impact de manière importante les performances est la hauteur de l’éolienne, la taille des pales et la puissance du moteur. La hauteur permet d’accéder à des vents plus forts, la surface balayée par les pales permet de collecter une puissance plus ou moins grande à vitesse de vent fixée, la puissance du moteur permet de définir quelle sera la puissance maximum transmise par l’éolienne. Un facteur important dont nous reparlerons est le toilage de l’éolienne : le rapport entre la surface balayée par les pales et la puissance installée (en m^2/kW).  
</span>
<span class="mytext">
J’ai omis des sources de production d’électricité plus rares comme l’énergie des vagues ou des courants marins, dont je parlerai sans doute plus tard.
</span>

# Puissance et énergie dans le coût actualisé de l’énergie (LCOE)

## LCOE pour une technologie

<span class="mytext">
Lorsque l’on compare le coût de systèmes de production d’électricité il y a deux grandes difficultés. La première est d’ordre économique : il est impossible de ramener objectivement un projet quel qu’il soit à un seul coût et un seul revenu. En effet, on dépense de l’argent à différents moments de la durée de de vie du projet : pour sa construction un certain nombre d’années avant de produire, pour assurer le fonctionnement, payer du personnel, puis au bout de quelques années pour remplacer certaines parties du système, pour son démantèlement, et peut-être plusieurs années après encore lorsqu’il faut gérer des déchets. De même, les bénéfices que l’on tire de ce projet vont s’étaler de manière plus ou moins variable sur toute sa durée de vie.
</span>
<span class="mytext">
Afin de pallier à ce problème, les économistes qui réfléchissent à la question du coût et les ingénieurs qui développent des projets utilisent le modèle de l’actualisation. Ce modèle est loin d’être parfait mais il est très utilisé et il faut donc connaitre son fonctionnement et ses limites. Il repose sur une unique hypothèse plus simple à comprendre et à formuler qu’à discuter : l’argent $ x_{n} $ que l’on gagne ou que l’on dépense à l’année $ n$  a plus de valeur que l’argent $x_{n+1}$  que l’on gagne ou dépense à l’année $ n$. Le surcroit de valeur est $x_n \alpha$, où $\alpha$ est appelé taux d’actualisation (car il permet d’actualiser la valeur de l’argent d’une année à l’autre). Ainsi, avec ce modèle, on peut comparer $x_{n+1}/(1+\alpha) $ à $x_n$  et par récurrence $x_{n+1}/(1+alpha)^n$  à $x_0$. En additionnant les dépenses actualisées et en divisant par les énergies produites et actualisées elle aussi, on calcule le coût actualisé de l’énergie actualisée, ou encore levelized cost of energy noté LCOE. Une formule est donnée en Annexe 1 et il n’est pas très important de la comprendre complètement ici car nous allons en donner une forme beaucoup plus simple. Je ne vais pas discuter $ \alpha$ ici mais l’on peut dire que $ \alpha$ est autour de 4% dans des projets portés par le public et plutôt autour de 8-10% pour des projets portés par le privé.
</span>
<span class="mytext">
Pour ce faire il faut lister les dépenses du projet. Lister toutes les dépenses d’un projet sur sa durée de vie est un travail complexe, et le but ici n’est pas de donner un exemple de calcul de LCOE très précis mais plutôt une version simplifiée permettant à chacun de comprendre les facteurs importants. Dans le domaine de la production d’électricité (et dans beaucoup d’autres secteurs) on peut classifier les dépenses en 4 parties :
</span>
<div class="text" style="display:block; text-align: justify">
<ul> <li>Les coûts d’investissement $C_I$ exprimés en €/kW et dépensé au moment juste avant que le projet ne commence à produire de l’énergie. Une somme investie 10 ans avant le démarrage du projet aura un impact sur le coût à livraison beaucoup plus important, et lié à l’actualisation, qu’une somme déboursée au moment du démarrage (« à la livraison »).</li>
<li>Les coûts annuels d’exploitation $C_F$ exprimés en €/kW/an qui ne dépendent pas de l’énergie produite et qui correspondent plus à des coûts d’entretien, de gestion, la location d’un terrain, ou la rémunération du personnel. Ils sont payés pendant toute la durée de vie du projet. Ils sont dépensés chaque année pendant toute la durée de vie du projet, quel que soit la production.</li>
<li>	Le coût marginal de production $C_M$ exprimé en €/MWh qui correspond à ce qu’il faut payer pour produire un MWh supplémentaire lorsque l’on produit déjà (et qui inclus d’une certaine manière des coûts de démarrage). Ces coûts sont payés à chaque fois que la centrale produit. Ils correspondent souvent à un simple coût de carburant.</li>
<li>	On peut ajouter à ceci les coûts de démantèlement $C_D$ exprimé en €/kW, dans lequel on peut inclure les coûts qui surviennent après le projet (e.g gestion des déchets). $C_D$ peut aussi intégrer une valeur résiduelle de l’actif à la fin de la période considérée (dans ce cas un bénéfice, c’est-à-dire une valeur négative pour $C_D$).</li>
</ul>
</div>
<span class="mytext">
Avec cela, le LCOE s’exprime finalement comme une simple fonction de ces paramètres et du facteur de charge FC (P étant encore la puissance installée en GW et E l’énergie annuelle produite en TWh )  :
</span>
<span class="mytext">
$$ LCOE =\beta*\frac{P}{E}+C_M=\frac{\beta }{FC\times 8,76}+C_M$$
</span>
<span class="mytext">
Où $ \beta $ est ce que l’on peut appeler le « coût capacitaire annuel moyen actualisé » exprimé en [€/kW] et donné par la formule :
</span>
<span class="mytext">
$$ \beta = \frac{C_c}{L^{\alpha}}+\frac{C_D}{(1+\alpha)^{L-1}}+C_F  $$
</span>
<span class="mytext">
Ici $ L $ est la durée de vie du projet et $ L^{\alpha} $ la durée de vie corrigée de l’actualisation qui est définie par une formule donnée dans l’annexe 1, qui contient également une table de valeurs de $ L^{\alpha} $ en fonction de $\alpha$ et de la vraie durée de vie $ L $. Ce qu’il faut retenir sur cette durée de vie corrigée est qu’elle est plus petite que la vraie durée de vie, et que plus $ \alpha $ est petit (proche de zéro), plus $ L^{\alpha} $ est proche de $ L $. Dans les cas extrêmes on a les valeurs suivantes :
</span>
<div class="text" style="display:block; text-align: justify">
<ul> <li>Avec une actualisation à 2% une durée de 30 ans se corrige à 22 et une durée de 80 ans se corrige à 40 </li>
<li>Avec une actualisation à 4% une durée de 30 ans se corrige à 22 et une durée de 80 ans se corrige à 40 </li>
<li>Avec une actualisation à 10%, cette durée est presque toujours entre 10 et 11 ans, même si la durée de vie est de 80 ans.</li>
</ul>
</div>
<span class="mytext">
On comprend dans quelle mesure les grandes valeurs de $ \alpha$ correspondent à hypothéquer le futur. La réalité est souvent bien plus complexe que ce modèle d’actualisation. Le premier élément singulier qu’il faut comprendre est qu’un acteur privé qui a des fonds propres importants peut décider d’investir dans un projet qu’il considère stratégique pour son entreprise en tablant sur une actualisation relativement faible, au risque de laisser passer des projets qui amèneraient un retour sur investissement plus rapide.
</span>
<span class="mytext">
Quel que soit le coût de démantèlement $ C_D $ il est a un poids presque toujours négligeable du fait de l’actualisation. Ce poids sera d’autant plus négligeable que le démantèlement se fera sur une période très longue (comme dans le cas du nucléaire où des temps d’attente sont nécessaire pour laisser la radioactivité diminuer). Le raisonnement sous-jacent est que l’entreprise peut ici mettre dès le début du projet une somme de côté (provisionnement) pour le démantèlement et que cet argent, s’il est bien placé, rapportera une somme d’argent liée à l’actualisation. Dans ce cas l’actualisation a un lien avec la rentabilité du capital. Le même raisonnement s’applique à la gestion des déchets.
Dans la table suivante, nous donnons quelques valeurs typiques de $ C_c $ $ C_F  $ , $ \beta  $ et $ C_M $. Nous discutons les sources de ces valeurs dans l’annexe 2.
</span>
<span class="mytext">
Discuter l’actualisation dépasse de très loin ce que je peux faire ici aujourd’hui sans vous ennuyer, on a là un pan entier de l’économie. Notons juste que 8% correspond à une vision court-termiste, même s’il y a pire (certains gestionnaires de capital voudront 10% voir 15%), mais que même à 4% on ne voit pas bien au-delà de 40 ans. Des discussions un peu tendues ont eu lieu sur cette question autour du rapport Stern sur les conséquences du changement climatique (prévues à l’époque pour dans longtemps). Il existe des méthodes qui consistent à ne plus actualiser au-delà d’une certaine durée, pour éviter d’écraser les coûts. Après, même dans un monde « en décroissance » ou avec une inflation nulle, l’actualisation peut difficilement se rapprocher de zéro. Vous l’avez compris, ce petit modèle et la valeur de son unique paramètre soulèvent des questions de société importantes. Nous allons maintenant parler de la deuxième grande difficulté
</span>

## LCOE du système
<span class="mytext">
La deuxième grande difficulté, lorsque l’on compare le coût de systèmes de production d’électricité, est technique : il faut s’assurer que les systèmes fournissent des services techniques équivalents. La comparaison ne se fait jamais sur la puissance installée mais sur l’énergie produite, ainsi nous allons voir que le coût actualisé de l’énergie. Pourtant nous  Le LCOE donne un coût en euros/MWh et de ramène un coût de production à une énergie produite il permet donc de comparer des moyens de production qui ont des facteurs de charge différents comme un système éolien+gaz et un système nucléaire. Cependant il ne tient pas compte de la pilotabilité des moyens de production et il faut donc s’assurer que l’on compare deux systèmes offrant à peu près la même pilotabilité, on ne peut pas par exemple comparer un système éolien à un système nucléaire sur cette base. Deux systèmes ne seront jamais exactement comparables, certains seront plus rapide à construire, d’autres auront peut-être une utilisation du territoire plus importante, des impacts environnementaux différents.
</span>