---
title: Evaluer le coût économique de la production d'électricité
key: decomposition-lcoe
tags: mix-production intermittence evolution lcoe
article_header:
  type: cover
  image:
    src: /assets/images/Posts/2020-08-20/DSCF7793.jpg
---

<span class="summary" style="display:block; text-align: justify">
*Ce post vient en complément du post "energie et puissance" [[PostPrec](https://www.energy-alternatives.eu/2020/05/07/mix-de-production-delectricite-energie-et-puissance)] mais il peut être lu séparément. Il est même sans doute plus naturel de lire ce post en premier. Nous donnons une formule simple d'usage et assez classique pour le calcul du coût actualisé de l'électricité.  Elle repose sur un regroupement des coûts en plusieurs catégories : les coûts d'investissement, les coûts d'exploitation et de maintenance, les coûts marginaux. Pour chacun des différents moyens de production d'électricité qui existent dans les grandes classes utilisées dans le post précédent (nucléaire, gaz, charbon, éolien, solaire, hydraulique), nous donnons ces différents coûts et quelques précisions sur les éléments impactant le facteur de charge. Ceci nous permet en outre de donner des ordres de grandeur pour le coût actualisé et de retrouver les valeurs utilisées dans [[PostPrec](https://www.energy-alternatives.eu/2020/05/07/mix-de-production-delectricite-energie-et-puissance)].*
</span>
<!--more-->
<span class="mytext">
Dans un post précédent [[PostPrec](https://www.energy-alternatives.eu/2020/05/07/mix-de-production-delectricite-energie-et-puissance)], nous avons présenté une manière de modéliser les coûts économiques et environnementaux d’un système électrique à partir de la connaissance de l’énergie annuelle produite $E_i$ et de la puissance installée $P_i$ pour chaque moyen de production $i$ du système :
</span>
<span class="mytext">
$$ \sum_i \alpha_i^{cout} E_i+\beta_i^{cout} P_i$$
</span>
<span class="mytext">
Ceci nous a permis de retrouver des ordres de grandeur pour le coût de notre système actuel et d'en donner pour le coût à l’horizon 2050 d’un système fortement renouvelable et pour celui d’un système fortement nucléaire. Des valeurs pour les coefficients $\alpha_i^{cout}$ (en [€/MWh]) et $\beta_i^{cout}$ (en [€/kW/an]) ont été proposées sans que l'on explique ce qui permet de les obtenir. Le coefficient $\alpha_i^{cout}$ est appelé coût proportionnel, c’est la part du coût proportionnel à l’énergie produite, en première approche, il dépend du coût des combustibles, des taxes et du rendement de l’installation. Le coût fixe actualisé et annualisé $\beta_i^{cout}$ s’obtient à partir de données économiques comme l’actualisation, le coût d’investissement, les coût annuels d’exploitation d’une manière que nous allons détailler dans la première partie de ce post. Ceci nous permettra d’introduire le LCOE (levelized cost of energy) qui est très utilisé dans le domaine.
</span>
<span class="mytext">
Par ailleurs, nous avons considéré de grandes familles de technologies de production : « nucléaire », « charbon », « gaz », « hydraulique », « photovoltaïque », « éolien ». La précision des données économiques et des facteurs de charge pour chaque famille va nécessiter de donner quelques précisions sur la diversité des technologies y existants. Dans cette seconde partie, nous appliquerons à chaque famille la formule du LCOE donnée dans la première partie.
</span>


# Coût actualisé (LCOE).

## Introduction : actualisation

<span class="mytext">
Lorsque l’on compare le coût de systèmes de production d’électricité il y a deux grandes difficultés. La première est d’ordre économique, l’hétérogénéité de la répartition des dépenses dans le temps entre familles de moyens de production nécessite de ramener tous les coûts et revenus à une date unique pour les rendre comparable. La seconde grande difficulté vient du fait que l'on ne peut pas comparer directement un MWh produit avec un moyen de production pilotable et un MWh de production fatale (e.g. éolien, photovoltaique), mais nous en avons déjà parlé dans notre post précédent [[PostPrec](https://www.energy-alternatives.eu/2020/05/07/mix-de-production-delectricite-energie-et-puissance)].
</span>

<span class="mytext">
Afin de pallier au premier problème, les économistes qui réfléchissent à la question du coût et les ingénieurs qui développent des projets utilisent depuis très longtemps le modèle de l’actualisation.  Il repose sur une unique hypothèse plus simple à comprendre et à formuler qu’à discuter : l’argent $ x_{n} $ que l’on gagne ou que l’on dépense à l’année $n$, a plus de valeur que l’argent $x_{n+1}$ que l’on gagne ou dépense à l’année $n+1$. Le surcroit de valeur est $x_n \alpha$, où $\alpha$ est appelé taux d’actualisation, en effet, il permet "d’actualiser" la valeur de l’argent d’une année à l’autre. Ce modèle permet de rendre comparable $x_{n+1}/(1+\alpha)$ et $x_n$, mais aussi,  puisque $\alpha$  ne dépend pas de $n$, par récurrence,  $x_{n+1}/(1+\alpha)^n$ et $x_0$. En additionnant les dépenses actualisées et en divisant par les énergies produites et actualisées elles aussi, on calcule le coût actualisé de l’énergie actualisée, ou encore levelized cost of energy noté $LCOE$. Une formule est [disponible ici](https://fr.wikipedia.org/wiki/LCOE), dans la section suivante nous en donnerons une forme alternative, elle n'a rien de révolutionnaire mais elle a l'avantage d'être synthétique et plus facile à manipuler.
</span>

<span class="mytext">
Nous n'allons pas discuter plus profondément ce qui se cache derrière l'actualisation ici, c'est un très vaste sujet. Notons seulement que $\alpha$ est autour de 4-5% dans des projets portés par le public (ce taux est alors souvent encadré par la loi) et plutôt autour de 8-10% pour des projets portés par le privé. Si $\alpha$ est égal à l'inflation plus un taux de retour sur investissement, alors le LCOE correspond au tarif d'achat que le monteur de projet est susceptible de demander dans un appel d'offre (sauf dans le cas d'un contrat pour différence comme avec Hinkley Point où le prix est indéxé sur l'inflation qui ne doit pas être incluse dans le taux d'actualisation), voir [[Williams2019](https://www.sciencedirect.com/science/article/pii/S0301421518306645)].  Nous reportons quelques éléments de discussion autour de l'actualsiation en Annexe 1 : prise en compte des capitaux propres de l'entreprise, de l'inflation, du taux d'intérêt long terme, de la rentabilité du capital, de la croissance d'une entreprise, des frais bancaires, des intérêts intercallaires, actualisation et décroissance...
</span>

## Dépenses d'un projet
<span class="mytext">
Pour calculer le LCOE, il faut lister toutes les dépenses du projet, depuis la dépense des premiers euros, avant la mise en route de la centrale, jusqu'à ce que plus rien ne soit gagné ou dépensé, après l'arrêt , le démantèlement de la centrale, son recyclage et le traitement des déchets. C'est un travail complexe, et le but ici n’est pas de donner un exemple de calcul de LCOE détaillé mais plutôt une version simplifiée permettant à chacun de comprendre les facteurs importants. Dans le domaine de la production d’électricité (et dans beaucoup d’autres secteurs) il est pratique de classer les dépenses en 4 parties :
</span>
<div class="text" style="display:block; text-align: justify">
<ul> <li>Les coûts d’investissement $C_I$ exprimés en €/kW et comptabilisés à la date de livraison, c'est à dire la date où la centrale commence à produire de l’énergie. Une somme investie 10 ans avant le démarrage du projet aura un impact sur le coût à livraison beaucoup plus important, et lié à l’actualisation (ou plus directement aux intérêts intercalaires), qu’une somme déboursée au moment du démarrage (« à la livraison »). Je discute la prise en compte de la durée de construction dans les calculs en Annexe. </li>
<li>Les coûts annuels d’exploitation $C_F$ exprimés en €/kW/an, qui ne dépendent pas de l’énergie produite et qui correspondent plus à des coûts d’entretien, de gestion, pour la location d’un terrain, ou la rémunération du personnel. Ils sont dépensés chaque année pendant toute la durée de vie du projet, quel que soit la production. Ici nous supposerons qu'il ne dépendent pas de l'année $n$, même si il y a toujours une évolution dans les dépenses d'entretien liée aux besoin de remplacement de certains composants qui peuvent intervenir périodiquement. </li>
<li> Le coût proportionnel de production $C_M$ exprimé en €/MWh ,qui correspond à ce qu’il faut payer pour produire un MWh supplémentaire lorsque l’on produit déjà. Ces coûts sont payés à chaque fois que la centrale produit. Ils correspondent souvent à un simple coût de carburant éventuellement ajusté d'une taxe (e.g. taxe carbone) mais ils peuvent également inclure des coûts de démarrage au prorata lorsque ceux-ci sont significatifs.</li>
<li> le coût de démantèlement $C_D$ exprimé en €/kW, dans lequel on peut inclure les coûts qui surviennent après le projet (e.g gestion des déchets). $C_D$ peut aussi intégrer une valeur résiduelle de l’actif à la fin de la période considérée (dans ce cas un bénéfice, c’est-à-dire une valeur négative pour $C_D$).</li>
</ul>
</div>

<span class="mytext">
Notons que, pour la formule simplifiée du LCOE qui va suivre, toutes les dépenses sont soit annualisées (dans la catégorie "coût d'exploitation") ou ramenées à la date de démarrage du projet ou ramenées à la date de fin de fonctionnement. Il y a deux types d'hypothèses sous-jacentes.
</span>

<span class="mytext">
D'une part cela nécessite de supposer que certains facteurs ne varient pas d'une année sur l'autre comme le facteur de charge ou $C_F$. Ceci n'est évidemment jamais le cas mais si il n'y a pas d'asymétrie dans la distribution du coefficient en question année après année (e.g. une tendance à un facteur de charge plus important ou plus faible pour les premières années de fonctionnement),  on peut sans trop de scrupule utiliser une valeur moyenne. Le facteur de charge aura souvent une tendance à baisser au fil du temps sur certaines installations, soit par l'usage des machines, soit par un besoin accru de maintenances. A l'inverse les coûts d'exploitation auront tendance à augmenter avec les années. On pourra lire à ce sujet la discussion intéressante de [[Williams2019](https://www.sciencedirect.com/science/article/pii/S0301421518306645)]
</span>

<span class="mytext">
D'autre part, lorsque l'on parle d'un coût de construction, d'un coût de démantèlement, ou d'un coût de gestion des déchets, il s'y cache toujours une séries de dépenses intervenant à différents moments du projet, rassemblées par le biais d'une actualisation. Concernant le coût de construction, nous discutons ce sujet en Annexe.
</span>

## Formule simplifiée
<span class="mytext">
Avec cela, on peut montrer facilement que le LCOE d'une technologie donnée s’exprime comme une simple fonction de ces paramètres et du facteur de charge $FC$ ($P$ étant encore la puissance installée en GW et $E$ l’énergie annuelle produite en TWh )  :
</span>
<span class="mytext">
$$ LCOE =\beta*\frac{P}{E}+C_M=\frac{\beta }{FC\times 8,76}+C_M$$
</span>
<span class="mytext">
Où $ \beta $ est ce que l’on peut appeler le « coût capacitaire annuel moyen actualisé » exprimé en [€/kW/an] et donné par la formule :
</span>
<span class="mytext">
$$ \beta = \frac{C_c}{L^{\alpha}}+\frac{C_D}{(1+\alpha)^{L-1}}+C_F  $$
</span>
<span class="mytext">
On retrouve la formule du coût complet donnée en introduction et utilisée dans [[PostPrec](https://www.energy-alternatives.eu/2020/05/07/mix-de-production-delectricite-energie-et-puissance)], puisque pour une technologie $i$ le coût complet ramené à une année est :
</span>
<span class="mytext">
$$  LCOE_i*E_i =\beta_i*P_i+C_M*E_i=\beta^{cout}_i*P_i+\alpha^{cout}_i*E_i$$
</span>
<span class="mytext">
Ici $L$ est la durée de vie du projet, et $L^{\alpha}$ donné par la formule
</span>
<span class="mytext">
$$L^{\alpha}= \sum_{i=0}^{L-1}\frac{1}{(1+\alpha)^i}=\frac{1+\alpha}{\alpha}(1-(1+\alpha)^{-L}),$$
</span>
<span class="mytext">
est homogène à une durée de vie qui serait comme raccourcie (économiquement) par "l'effet de l’actualisation". Nous donnons dans [l’Annexe 1](annexe-1--table-pour-la-durée-de-vie-corrigée) une table de valeurs de $ L^{\alpha} $ en fonction de $\alpha$ et de la vraie durée de vie $L$. Ce qu’il faut retenir sur cette durée de vie "corrigée" est qu’elle est plus petite que la vraie durée de vie, et que plus $\alpha$ est petit (proche de zéro), plus $L^{\alpha}$ est proche de $L$. Notons que la formule simple proposée ressemble à l'approche donnée par [[NREL2018](https://www.nrel.gov/analysis/tech-lcoe-documentation.html)] et $L^{\alpha}$ n'est pas loin d'être l'inverse de ce qui est appellé le CRF (capital recovery factor). On peut donner $L^{\alpha}$ pour les cas emblématiques suivants :
</span>
<div class="text" style="display:block; text-align: justify">
<ul> <li> Avec une actualisation à 2%, une durée de 30 ans se corrige à 22, et une durée de 80 ans se corrige à 40 </li>
<li> Avec une actualisation à 4%, une durée de 30 ans se corrige à 22, et une durée de 80 ans se corrige à 40 </li>
<li> Avec une actualisation à 10%, cette durée est presque toujours entre 10 et 11 ans, même si la durée de vie est de 80 ans.</li>
</ul>
</div>
<span class="mytext">
On comprend dans quelle mesure les grandes valeurs de $\alpha$ correspondent à hypothéquer le futur. La réalité est évidemment bien plus complexe que ce que peut encadrer un modèle d’actualisation.
</span>
<span class="mytext">
Quel que soit le coût de démantèlement $C_D$ il est a un poids presque toujours négligeable du fait de l’actualisation. Ce poids sera d’autant plus négligeable que le démantèlement se fera sur une période très longue (comme dans le cas du nucléaire où des temps d’attente sont nécessaires pour laisser la radioactivité diminuer).
Dans les tables de la section suivante, nous donnons quelques valeurs typiques de $ C_c $ $C_F$ , $\beta$ et $C_M$.
</span>



# Quelques précisions sur la diversité cachée derrière ces grandes classes de moyens de production

<span class="mytext">
Dans cette section  nous allons parcourir les grandes classes de moyens de production d'électricité, et pour chacune d'entre elles nous allons discuter les différentes sortes de coûts pour donner des ordres de grandeur sur le LCOE. Nous ne parlons pas ici du coût du système électrique et nous renvoyons le lecteur à notre post précédent [[1](https://www.energy-alternatives.eu/2020/05/07/mix-de-production-delectricite-energie-et-puissance)].
</span>

## Centrales nucléaire

<span class="mytext">
En ce qui concerne le **nucléaire**, on distingue [plusieurs générations](https://fr.wikipedia.org/wiki/G%C3%A9n%C3%A9rations_de_r%C3%A9acteurs_nucl%C3%A9aires). La seconde génération est celle en activité aujourd’hui et construite entre le début des années 70 et la fin des années 80. Les nouvelles centrales que l’on construit aujourd’hui sont de la troisième génération. Parmi les nombreuses technologies déployées de manière commerciales aujourd’hui (seconde et troisième génération), les deux plus importantes sont les réacteurs à [eau bouillante](https://fr.wikipedia.org/wiki/R%C3%A9acteur_%C3%A0_eau_bouillante) (dit « REB ») des réacteurs à [eau pressurisé](https://fr.wikipedia.org/wiki/R%C3%A9acteur_%C3%A0_eau_pressuris%C3%A9e) (dit « REP »). Une liste plus exhaustive est donnée dans le lien sur les générations. La quatrième génération est prévue pour les décennies à venir (un projet pilote a vu le jour en Russie) ; il existe plusieurs propositions qui visent, par des évolutions technologiques importantes, à avoir des centrales qui n’utilisent plus le même combustible mais une forme d’uranium beaucoup moins rare, qui permettent de retraiter une partie des déchets à vie longue qui existent aujourd’hui, qui ne présentent pas de risque d’emballement, qui peuvent plus facilement moduler leur production sans pertes de rendement (nous reparlerons de la modulation des centrales nucléaires actuelles dans un post ultérieur, car certaines choses sont possibles mais pas tout et c’est un sujet important). En France le projet de recherche Astrid abandonné récemment était dans cette lignée, mais dans le monde d’autres projets se poursuivent dans cette direction. Enfin, une autre génération de nucléaire arrivera avec la fusion. Sur le fonctionnement des centrales nucléaires, je renvoie vers les [vidéos du réveilleur](https://www.youtube.com/watch?v=HMystmGbctw) (youtubeur effectuant un travail documenté et abordable et que je citerai souvent).
</span>

<span class="mytext">
Pour les coûts, la transparence en France a beaucoup progressé dans le cadre d'une analyse continue de la cours des comptes les 10 dernières années, sanctionnée par au moins 5 rapports [CDC2012](https://www.ccomptes.fr/fr/publications/les-couts-de-la-filiere-electro-nucleaire), [CDC2014](https://www.ccomptes.fr/fr/publications/le-cout-de-production-de-lelectricite-nucleaire-actualisation-2014), [CDC2016](https://www.ccomptes.fr/fr/publications/le-rapport-public-annuel-2016), [CDC2019](https://www.ccomptes.fr/fr/publications/laval-du-cycle-du-combustible-nucleaire), et [CDC2020](https://www.ccomptes.fr/fr/publications/larret-et-le-demantelement-des-installations-nucleaires). Je donne dans la table ci-dessous quelques coûts d’investissement et de fonctionnement en France avec les sources associées, la pluspart des chiffres viennent de [[CDC2014](https://www.ccomptes.fr/fr/publications/le-cout-de-production-de-lelectricite-nucleaire-actualisation-2014)] tableaux p11,14 et 24. Certaines valeurs et dicsussions sont complétées par d'autres rapports.
</span>

<div class="text" style="display:block; text-align: justify">
<ul> <li>Les coûts marginaux pris pour le nucléaire en France sont autour de 6 €/MWh.</li>
<li> Les coûts annuels d’exploitation sont de 120 €/kW/an (voir <a href="https://www.ccomptes.fr/fr/publications/le-cout-de-production-de-lelectricite-nucleaire-actualisation-2014"> table p14</a>), il faut y ajouter :
<ul><li> des coûts d'entretien "courant" de 16 €/kW/an. </li>
<li>  Les rénovations imposées par l'évolution de la réglementation suite à l'accident de Fukushima se chiffrent à 37 €/kW/an sur la période 2014-2025. </li>
<li> Pour le parc actuel, on rajoute dans les rapports de la cours des comptes, un "loyer économique" de 130 €/kW/an qui vise à payer les actionnaires et correspond d'une certaine manière à une rémunération du capital investi, qui devrait aussi permettre de futurs investissements. </li>
<li> le coût d'entretien a augmenté à l'approche des 30 ans du parc, et augmentera pour la prolongation à 50 ou 60 ans de durée de vie des centrales (que l'on nomme souvent "grand carénage"). Le coût additionnel dans le cas de l'extention de durée de vie (qui s'ajoute aux 16 €/kW/an) a été chifffré à 21 €/kW/an pour la période 2014-2025 puis 64 €/kW/an pour la période 2025-2033. </li>
</ul></li>
<li> Le coût de démentellement pour le cas du parc actuel peut être rammené à 20 €/kW/an (voir discussion <a href="#annexe-3--démentellement-et-gestion-des-déchets-nucléaires-"> Annexe 3 </a>).  Ce coût correspond à une charge brute autour de 300 €/kW. Même si elle est difficilement imputable à la future technologie EPR, le coût correspondant, si il intervient dans 80 ans est rendu nul par l'actualisation. Le coût de la gestion des déchets, même si il devrait être comptabilisé dans le coût proportionnel, est aujourd'hui évalué à 8 €/kW/an même si ce coût dépendra beaucoup de la politique énergétique future de la France (voir <a href ="#annexe-3--démentellement-et-gestion-des-déchets-nucléaires-"> Annexe 3 </a>).  </li>
<li> Nous négligeons ici les coûts liés à l'assurance et nous discutons cela dans l'annexe 4  </li>
</ul>
</div>

<span class="mytext">
Avec un facteur de charge de 75%, on peut donc évaluer les coûts suivants. Nous manquons d'élément pour chiffrer le coût d'exploitation de l'EPR, mais ces éléments donnent des ordres de grandeur et nous prendrons une valeur de 175 €/kW/an, le loyer économique peut sans doute être calculé à partir d'une actualisation plus importante, et nous avons donc dans la tableau ci-dessous une évaluation du coût intégrant ce "loyer économique" dans la ligne où l'actualisation est de 9% et qui permet d'obtenir pour Hinkley point C un ordre de grandeur au niveau de ce qui a été [obtenu par EDF au près des Anglais, 92,5 £/MWh (en monnaie 2012).](https://www.zonebourse.com/ELECTRICITE-DE-FRANCE-4998/actualite/Electricite-de-France-le-cout-d-Hinkley-Point-C-en-hausse-de-29-en-3-ans-29251492/) (c'est un contrat pour différence, CFD, le tarif est indexé sur l'inflation et donc cette dernière n'est pas incluse dans le calcul du taux d'actualisation, voir Annexe 1). On peut donc noter que l'électricité nucléaire, qui a le grand intérêt d'être à la fois pilotable et décarbonée, reste une énergie dont les coûts peuvent être maîtrisés à condition que son financement soit garanti par l’état (pour avoir des actualisations basses) et qu'elle soit développée massivement (effets d'échelle nécessaires pour la baisse des coûts et le maintien des compétences).
</span>

|Système                                         |CAPEX €/kW   |proportionnel  €/MWh    | Autre €/kW/an|Durée de vie| actualisation |  LCOE |
|:-----------------------------------------------|:------------|:------------------|:-------------|:-----------|:--------------|:------|
|Parc actuel moyen **sans** loyer                |0            |6                  | 201          |    x       |   5%          | 36   |
|Parc actuel moyen **avec** loyer                |0            |6                  | 331          |    x       |   5%          |    56   |
|Carrenage phase 1  **avec** loyer              |     0       |6                  | 352          |    x       |   5%          |    60   |
|Carrenage phase 2  **avec** loyer              |     0       |6                  | 411          |    x       |   5%          |    68   |
|Flamanville, Hinkley point (EPR)                |7000         |6                 | 175          |      80      |        5%   |     84  |
|Taishan (EPR)                                  |3500         | 6                |  175         |       80      |      5%    |     58  |  
|Flamanville, Hinkley point (EPR)                |7000         |6                 | 175           |    80      |   9%          |     120  |
|Taishan (EPR)                                   |3500         | 6                |  175         |    80      |   9%          |     76  |         
{: .mbtablestyle .wrapstyle .simple7}



## Gaz, fuel et charbon

### Types de centrales et coûts d'investissement
<span class="mytext">
Pour le gaz (et le fioul), on distingue plusieurs grandes catégories de centrales. La plus élémentaire est la [turbine à combustion](https://fr.wikipedia.org/wiki/Turbine_%C3%A0_gaz) (TAC, ou OCGT pour open cycle gaz turbine dans le cas du gaz) dans laquelle le gaz ou le fioul est mélangé à de l’eau et envoyé sous pression dans une turbine où il s’enflamme. Le principe de la TAC est très proche de celui du moteur d’avion. Dans la TAC la chaleur des gaz d’échappement est perdue mais l’on peut la récupérer de différentes manières. Une première solution est de faire chauffer de l’eau (dans une sorte de grande bouilloire) dont les vapeurs vont aller entrainer une seconde turbine connectée à celle de la TAC. C’est ce que l’on appelle un [cycle combiné](https://fr.wikipedia.org/wiki/Cycle_combin%C3%A9) (CCGT pour le cycle combiné gaz). Le rendement d’un CCG est donc meilleur : il peut monter autour de 55% (il y a même un record à 64% détenu par la centrale de Bouchain), alors que celui de la TAC est limité autour de 35-40% (sauf pour des technologies très particulières utilisant des fluides supercritiques). Le coût d’installation du CCG est plus élevé, et ce dernier demande quelques heures pour démarrer alors que la TAC n’a pas besoin de plus de 30 minutes. Une autre manière d’utiliser les gaz d’échappement de la TAC est d’en extraire directement la chaleur pour une autre application (réseau de chaleur, serres, …), c’est ce que l’on appelle la [cogénération](https://fr.wikipedia.org/wiki/Cog%C3%A9n%C3%A9ration). Dans ce cas le rendement global de l’installation est meilleur mais l’utilisation de la TAC est un peu asservie au besoin de chaleur : on est obligé de produire quand il fait froid et pas nécessairement seulement lorsqu’il y en a besoin.
</span>


<span class="mytext">
Dans une centrale à charbon on fait généralement chauffer de l’eau en brûlant du charbon, la vapeur sous pression ainsi générée est envoyée dans une turbine qui produit de l’électricité. Pour la production d’électricité à partir du charbon il existe plusieurs technologies plus ou moins efficaces selon le niveau de pression utilisé lors de la combustion du charbon. Les rendements correspondants peuvent varier entre 30 et 50%, et les impacts environnementaux varient eux aussi beaucoup selon la qualité de la combustion. L’industrie du charbon met en avant : l’augmentation des rendements de ses nouvelles centrales qui envoient dans la turbine des fluides « super-critiques » ; ainsi que la séquestration du carbone capturé en sortie de cheminée. Pourtant, le charbon reste à l’heure actuelle un moyen de production d’électricité parmi les plus polluants, et ce sur beaucoup de plans.
</span>

|Système                            |Rendement   |CAPEX €/kW   | Fixed O&M €/kW/an|
|:-------------------------------------|:-----|:-----|:-----|
|Gaz -- TAC        |35% |500 |15 |
|Gaz -- CCGT |54%  |900 | 20 |
|Coal – Subcritical   |40%  |1200   | 45 |
|Coal – Supercritical    |45%|1400 | 40 |
|Coal – Ultra-Supercritical |50%   |2000 | 30 |
{: .mbtablestyle .wrapstyle .simple6}

<span class="legendtext" id="CAPTable1" style="display:block;text-align:center">
**Table 1** -- moyens de production d’électricité au gaz et au charbon ainsi que leur efficacité et le coût d’investissement correspondant. Source pour le charbon et p le gaz : : [[Cost2013](https://econpapers.repec.org/paper/diwdiwddc/dd68.htm)]], source additionnelle pour le gaz : U.S. energy information administration [[EIA2016](https://www.eia.gov/analysis/studies/powerplants/capitalcost/pdf/capcost_assumption.pdf)]
</span>
<span class="mytext">
La production d’électricité à partir de **biomasse** ressemble assez à ce que l’on fait avec du charbon, combustion de la biomasse pour faire chauffer de l’eau et faire tourner une turbine à vapeur. La qualité de la combustion, le caractère renouvelable, les impacts environnementaux dépendent beaucoup de la biomasse utilisée, de sa nature et de sa provenance, ils peuvent être acceptables lors de l’utilisation de déchets ou d’une biomasse qui serait locale et tout de suite replacée mais aussi très mauvais lorsque par exemple on choisit de couper des forêts à l’autre bout du monde sans rien replanter.
</span>

### Coûts de carburant



<span class="mytext">
On distingue en générale l’électricité produite à partir d’un **charbon** de basse qualité -comme la lignite- de celle produite à partir de charbon noir. Il existe une grande variété de type de charbons liée à des niveaux de houillification différents. Ils se distinguent notamment par leur humidité, leur teneur en carbone ou leur pouvoir calorifique différents. Il n'existe pas de définition unique internationalement retenue permettant de classifier précisément les charbons mais on trouve une classification et quelques explications dans la base carbone de l’ADEME [[ADEMEGES](https://www.bilans-ges.ademe.fr/documentation/UPLOAD_DOC_FR/index.htm?solides3.htm)]. La Lignite est moins dense, sa combustion est moins bonne et donc plus polluante (pas vraiment sur le plan des émissions de GES cela dit voir table ci-dessous), son transport (ramené à la consommation d’énergie qu’il implique) est plus coûteux. Son extraction se fait souvent dans des mines à ciel ouvert qui peuvent avoir un avantage économique à court terme mais certainement pas un avantage environnemental. Pour ces raisons la Lignite continue d’être exploitée dans cas où c’est une ressource locale pour des raisons de coût, et parfois pour des questions de préservation d’une économie locale. L’Allemagne possède sur son territoire une ressource importante de lignite qui est utilisée pour la moitié de l’électricité produite à partir de charbon. Sur le plan économique, avec un coût de 5 €/MWhth (tableau ci-dessous) cela fait, pour une centrale avec un rendement de 40%, un coût proportionnel de moins de 15 €/MWh. Avec un tel coût proportionnel, ces centrales fonctionnent plutôt en base qu'en pointe. Avec un charbon de meilleurs qualité, importé pour l'Allemagne ou la France, on se retrouve avec un coût proportionnel entre 20 et 25  €/MWh. Une taxe carbone à 1 €/tCO2 rajoute ici à peu près 1 €/MWh, on comprend bien que sans taxe carbone le charbon a encore un avenir prometteur.
</span>




<table class="simple7">
<thead>
<tr>
  <th >Produits</th>
  <th >Emissions</th>
  <th >PCI</th>
  <th align="center" colspan="3" class="mb6">Share</th>
  <th  colspan="2">Cost [$/ton]</th>
  <th  colspan="2">Cost [€/MWhth]</th>
</tr>
<tr>
  <th></th>
  <th>gCO2eq/kWhth</th>
  <th>(kWhth/kg)</th>
  <th class="mb6"></th>
  <th></th>
  <th></th>
  <th>2017</th>
  <th>2017</th>
  <th>2017</th>
  <th>2017</th>
</tr>
<tr>
  <th></th>
  <th></th>
  <th>(TWhth/Mt)</th>
  <th class="mb6">US</th>
  <th>World</th>
  <th>DE</th>
  <th>US</th>
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
  <td >8.8</td>
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
  <td >7.7</td>
  <td >7</td>
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
  <td >3</td>
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
    <td >5</td>
    <td >5</td>
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
**Table 2** -- différentes sortes de charbon. Sources : U.S. EIA [[4](https://www.eia.gov/energyexplained/coal/prices-and-outlook.php)] et ADEME [[ADEMEGES](https://www.bilans-ges.ademe.fr/documentation/UPLOAD_DOC_FR/index.htm?solides3.htm)].
</span>


<span class="mytext">
Pour le gaz, il faut faire la différence entre le **Gaz** naturel liquéfié et non liquéfié. Le gaz non liquéfié se transporte essentiellement par pipline, son prix est donc homogène au sein d'un réseau interconnecté (même si des différences de prix peuvent exister lorsque les interconnections sont saturées comme cela arrive parfois entre le nord et le sud de la France). Le gaz liquéfié se transporte par bateau dans le monde entier, il est plus cher mais son cours est homogène sur la terre entière et donc plus stable. Le charbon (noir) et le gaz ont donc des prix qui varient dans le temps et dans l'espace, et qui sont liés aux cours du pétrole. Une représentation est données Figure 1. Tous ont connu un pic en 2008 puis un creu important. Ils connaissent aujourd'hui un creu important lié à la crise du COVID19.
</span>
<span class="text" id="Figure1" style="display:block;text-align:center">
![Image]({{site.baseurl}}/assets/images/Posts/2020-08-20/CoursGaz.png){:.border}
</span>
<span class="text" id="Figure1" style="display:block;text-align:center">
![Image]({{site.baseurl}}/assets/images/Posts/2020-08-20/CoursGazEEx.png){:.border}
</span>
<span class="legendtext" id="CAPFigure1" style="display:block;text-align:center">
**Figure 1-a** -- Evolution des cours du gaz depuis 2009 (avec 2008 pour l'Europe histoire d'illustrer le pic), données annuelles moyennes, puis données EEX Europe extraites en 2020.
</span>


<span class="text" id="Figure1b" style="display:block;text-align:center">
![Image]({{site.baseurl}}/assets/images/Posts/2020-08-20/CoalPrice.png){:.border}
</span>
<span class="legendtext" id="CAPFigure1b" style="display:block;text-align:center">
**Figure 1-b** -- Evolution des cours du charbon.
</span>
## Centrales hydrauliques

<span class="mytext">
Dans **l’hydraulique**, on produit de l’électricité en faisant passer de l’eau dans une turbine. Il existe une grande diversité de centrales hydrauliques, que l'on peut appréhender en regardant la puissance et le type de la turbine, la taille du réservoire supérieur si il existe et éventuellement la présence d'une pompe et d'un réservoir supérieur.
</span>
<span class="mytext">
La puissance délivrée peut aller de 22 GW pour le [barrage des trois gorges en Chine](https://fr.wikipedia.org/wiki/Barrage_des_Trois-Gorges), à quelques MW pour un **petit** hydraulique à quelques kW pour la **micro**-hydraulique au fond de votre jardin ou même quelques Watt à quelques centaines de Watt pour la **pico**-hydraulique [utilisée parfois dans des réseaux d'eau](https://www.encyclopedie-energie.org/les-pico-turbines-hydrauliques-application-aux-reseaux-de-distribution-deau-2/#:~:text=La%20d%C3%A9nomination%20pico%2Dturbine%20concerne,approvisionnement%20%C3%A9lectrique%20d'appareils%20autonomes.). Il existe un grand nombre de [type de turbines](https://fr.wikipedia.org/wiki/Turbine_hydraulique), dont les caractéristiques varient en fonction de la hauteur de chute et du débit d'eau, les trois les plus utilisées aujourd'hui sont les turbines Kaplan, Françis et Pelton. Il faut noter  l'existance d'un système permettant de faire fonctionner la turbine à vitesse variable, l’existence d’une pompe pour faire remonter l’eau comme dans une . De l’autre il s’agira de différentier l’hydraulique « au fil de l’eau » qui tire parti d’un fleuve ou d’une petite rivière sans bassin de stockage, et un grand barrage de vallée alpine qui récupère un faible débit d’eau mais peut garder en stock plusieurs jours de production à pleine puissance. Le fil de l’eau dans certaines grosses centrales de la vallée du Rhône permet tout de même de moduler la puissance de production sur une ou deux heures. Certains barrages sont équipés de pompes qui permettent de faire remonter l’eau et jouent ainsi un rôle de stockage d’électricité, c’est ce que l’on appelle les STEP ([Station de Transfert d'Electricité par Pompage](https://www.connaissancedesenergies.org/fiche-pedagogique/hydroelectricite-stations-de-transfert-d-energie-par-pompage-step) qui ont le même nom que les stations d’épuration). En France nous avons actuellement un peu moins de 5 GW de STEP dont certaines ont une capacité de stockage allant jusqu’à plusieurs jours (72 heures pour la plus grande). Le gisement Français d’hydraulique est assez saturé mais certains grands barrages pourraient être équipés de pompes pour augmenter la puissance disponible de stockage, on parle de 2GW supplémentaires. Il existe également un gisement de micro-STEP dont nous parlerons ultérieurement lorsqu’il sera plus précisément question du stockage.
</span>


<span class="mytext">
On trouve dans [IRENA2012](https://www.irena.org/documentdownloads/publications/re_technologies_cost_analysis-hydropower.pdf)
une source intéressante de coûts observés. Les CAPEX pour les systèmes avec stock (avec un bassin supérieur) varient essentiellement en fonction du terrassement et de la quantité de béton à couler. La turbine, l'approvisionnement en eau (conduites) coûtent autour de 400 €/kW là où le projet complet fait entre 900 €/kW et 3000 €/kW. Le prix augmente légèrement pour des petits systèmes et diminue en général avec la hauteur de chute. Le coût d'exploitation est de l'ordre de 2%CAPEX/an, donc autour de 30-60 €/kW/an. Le facteur de charge dépend beaucoup de l'hydrolicité du site, il peut varier de 25% à 90% et va donc être un des principaux éléments influençant le LCOE.
</span>

## Centrales solaires
<span class="mytext">
Pour le **solaire photovoltaïque** il est pertinent de distinguer les tailles de centrales : grandes centrales au sol occupant plusieurs hectares, centrales en toiture de centre commercial ou sur un parking (dites « ombrières » pour l’ombre qu’elles apportent aux voitures), et petites centrales de quelques kW sur le toit d’une maison. Pour les grosses centrales il faut distinguer les centrales avec des systèmes de tracking (système avec un axe ou deux axes, qui permet de suivre la position du soleil dans le ciel pour maximiser la production) de celles qui n’en ont pas.
</span>


<span class="text" id="Figure2" style="display:block;text-align:center">
![Image]({{site.baseurl}}/assets/images/Posts/2020-08-20/CAPEX-PV.png){:.border}
</span>
<span class="text" id="Figure2b" style="display:block;text-align:center">
![Image]({{site.baseurl}}/assets/images/Posts/2020-08-20/OPEXPV.png){:.border}
</span>
<span class="legendtext" id="CAPFigure2" style="display:block;text-align:center">
**Figure 2** -- Décomposition des coûts (CAPEX et OPEX) moyens observés dans les appel d’offre CRE, étude publiée en février 2019, [[CRE2019](https://www.cre.fr/Documents/Publications/Rapports-thematiques/Couts-et-rentabilites-du-grand-photovoltaique-en-metropole-continentale)].
</span>
<span class="mytext">
Finalement un facteurs qui déterminera de manière essentielle le facteur de charge d’un système de production photovoltaïques est la localisation de la centrale. Une centrale au sud de l’Espagne produira plus qu’une centrale au nord de l’Allemagne et surtout sa variabilité hiver/été sera beaucoup moins importante mais nous reparlerons de tout çà de manière quantitative lorsque nous parlerons de la variabilité de ces moyens de production. Sur le plan environnemental le lieu de construction des panneaux (et le mix électrique utilisé pour faire fonctionner les machines qui produisent les panneaux) peut aussi avoir de l’importance.  
</span>
<span class="mytext">
Pour les grandes centrales PV, on retrouve des LCOE entre 45 et 65 €/MWh ce qui correspond aux ordres de grandeur que l'on retrouve dans les réponses aux appels d'offre, comme en 2020
[[CRE2020PV](https://www.cre.fr/media/Fichiers/publications/appelsoffres/ao-centrale-au-sol-telecharger-le-rapport-de-synthese-version-publique-de-la-septieme-periode-de-candidature)] où le prix moyen des projets selectionnés était autour de 60 €/MWh pour les gros projets. Attention, le prix constaté dans les réponses aux appels d'offre n'est pas exactement un LCOE mêmes si il y est comparable. La durée pendant laquelle le tarif est assuré, et qui fixe l'évaluation économique n'est pas la durée de vie mais plutôt une durée de 15 ans. Certains montages financiers permettent aujourd'hui avoir des frais financiers limités et correpondent probablement à des taux d'actualisation inférieurs à 5%. Certains projets dans le monde descendent à des coûts remarquablement bas, comme au [Portugal en 2019](https://www.pv-tech.org/news/portugal-claims-spot-in-solar-history-with-record-low-auction-prices) et au [Qatar en 2020](https://www.pv-tech.org/news/qatar-utility-reveals-world-record-tariff-in-tender-for-800mw-park) autour de 15 €/MWh. Ces records illustrent la baisse continue des coûts du PV. Ces prix très bas s'expliquent aussi par un productible important (facteur de charge élevé), un effet d'échelle, des démarches administratives simplifiées, une main d'oeuvre peu chère. On peut penser que si un pays comme la France s'organisait pour mettre un place une industrie du PV comme nous l'avons fait avec le nucléaire, avec un standardisation, et des effets d'échelle, le coût du PV en pourrait encore bien baisser.
</span>
<span class="mytext">
Une classe à part de l’énergie solaire est le solaire à concentration : thermodynamique ou photovoltaïque. Le solaire thermodynamique permet de chauffer de l’eau (à plus ou moins haute température) pour l’utiliser directement pour le chauffage ou dans le cas du solaire à concentration thermodynamique faire tourner une turbine et permet donc de stocker l’énergie produite dans la journée pour la réutilisé le soir. Ce type de système est très développé en Espagne. On retrouvera une vidéo assez complète du réveilleur sur le sujet des différentes technos solaires [ici](https://www.youtube.com/watch?v=dykSjXQhSjM). Je n'ai pas pris le temps pour l'instant de récolter des données économiques sur ce sujet.
</span>
## Centrales éoliennes
<span class="mytext">
Pour **l’éolien**, les données sont nombreuses, et évoluent encore ces dernières années. Nous allons principalement nous référer à un rapport de 2019 de l'IRENA [[IRENA2019](https://www.irena.org/publications/2020/Jun/Renewable-Power-Costs-in-2019)]. Il faut avant tout distinguer l’éolien offshore (en mer) de l’éolien on shore (sur terre). L’éolien en mer peut être posé sur le fond de la mer ou flottant lorsque la mer est trop profonde. Que ce soit en mer ou sur terre il faut distinguer ce qui va influencer le facteur de charge et ce qui influence le coût de construction. Le coût de construction est principalement influencé par
</span>
<div class="text" style="display:block; text-align: justify">
<ul> <li>la taille de l'éolienne (le coût capacitaire baisse avec la taille) </li>
<li> le pays de construction, en particulier pour l'éolien en mer. Comme pour le nucléaire le coût de construction est plus bas en Chine, cela est du à la fois à une main d'oeuvre moins cher (que l'on peut quantifier en regardant la différence entre le coût du BTP en Europe et en Chine), des frais banquaires sans doute plus bas, des effets d'échelle plus importants, des durées de construction plus courtes. Sur ce dernier sujet dans le contexte de l'éolien offshore en Europe, voir l'aricle <a href="https://www.larevuedelenergie.com/impact-de-la-reglementation-sur-les-couts-de-production-de-leolien-en-mer-en-europe/"> [Peysson2019]</a>. D'une manière générale les contraintes administratives et les oppositions aux projets peuvent jouer sur les coûts et sont très différentes d'une région à une autre (parfois au sein d'un même pays) </li>
<li> ce qu'on appelle le toilage : le rapport entre la surface balayée par les pales et la puissance installée (en m^2/kW). Le toilage augmente le coût capacitaire mais aussi le facteur de charge. </li>
</ul>
</div>

<span class="mytext">
 Dans tous les cas, le facteur de charge va dépendre de la localisation (et le vent associé) de l'éolienne et de ses caractéristiques tehniques. Un facteur technique qui impacte de manière importante les performances est la hauteur de l’éolienne, la taille des pales et la puissance du moteur. La hauteur permet d’accéder à des vents plus forts, la surface balayée par les pales permet de collecter une puissance plus ou moins grande à vitesse de vent fixée, la puissance du moteur permet de définir quelle sera la puissance maximum transmise par l’éolienne. Ici aussi le toilage est important. Son évolution ces dernières années est illustré Figure 2, elle est très importante et rend difficile tout calcul sur des facteurs de charge anciens. Nous passerons du temps sur ce sujet dans un autre post.
</span>

<span class="text" id="Figure3" style="display:block;text-align:center">
![Image]({{site.baseurl}}/assets/images/Posts/2020-08-20/Toilage.png){:.border}
</span>
<span class="legendtext" id="CAPFigure3" style="display:block;text-align:center">
**Figure 3** -- Evolution du toilage moyen des éoliennes [$m^2/kW$] par pays en fonction de la date d'installation.
</span>


|Système                               |CAPEX quantile 5% €/kW  |CAPEX med €/kW | CAPEX quantile 95% €/kW   | Fixed O&M €/kW/an|
|:-------------------------------------|:-----------------------|:--------------|:--------------------------|:------------------|
|Eolien on-shore                       |850                     |1500           |1875                       | 40                |
{: .mbtablestyle .wrapstyle .simple7}

|Système                               |CAPEX Chine €/kW  |CAPEX Europe €/kW |  Fixed O&M €/kW/an|
|:-------------------------------------|:-----------------|:-----------------|:------------------|
|Eolien off shore                      |2500              |3300              | 75                |
{: .mbtablestyle .wrapstyle .simple7}

<span class="mytext">
Pour l'éolien on-shore, on retrouve des LCOE entre 50 et 70 €/MWh ce qui correspond aux ordres de grandeur que l'on retrouve dans les réponses aux appels d'offre, comme en 2020
[[AOCRE2020](https://www.cre.fr/media/Fichiers/publications/appelsoffres/ao-eolien-terrestre-telecharger-le-rapport-de-synthese-version-publique-de-la-cinquieme-periode-de-candidature)] où le prix moyen des projets selectionnés était de 62 €/MWh. On peut faire ici la même remarque que dans le cas du PV.
</span>
# Conclusion

<span class="mytext">
Nous avons donné une formule simple permettant de calculer le LCOE d'un moyen de production d'électricité à partir de coûts annualisés. Pour différentes familles de moyens de production, nous avons discuté les facteurs impactant les coûts. Ces coûts peuvent être utilisés pour alimenter un modèle d’estimation des coûts du système électrique comme nous l'avons fait dans un post précédent [[PostPrec](https://www.energy-alternatives.eu/2020/05/07/mix-de-production-delectricite-energie-et-puissance)]. Ces données peuvent servir de base à notre TP sur l'optimisation et la planification du système électrique dans un contexte de transition énergétique (et qui sera mis en ligne et en open source prochainement).
</span>
<span class="mytext">
Notons que le modèle d'actualisation est loin d’être parfait, mais il n'en existe pas de bien meilleur. Pour des durées de vie très longue une méthode est d'arrêter l'actualisation après un certain nombre d'années. Mon avis, sans doute plutôt personnel, est que les évaluations économiques sont nécessaires et éclairantes, il faut savoir les faires, et comprendre ce qui les sous-tend, il faut faire des analyses de sensibiltié et prendre du recul par rapport aux incertitudes sous-jacentes. Cependant, rammener des décisions aussi importantes que celles liées à notre futur énergétique à l'évaluation d'un indicateur unique me semble naif. Plus généralement, je pense qu'il y a là de la même naïveté qu'il y aurait à croire que toute activité humaine a un coût économique déterminable objectivementque l'on pourrait minimiser pour une société efficace.
</span>
<span class="mytext">
Nous avons rappelé que la comparaison des moyens de production sur la plan économique pose deux grandes difficultés. La première, d'ordre technique, impose de passer par une une vision du système électrique dans son ensemble, comme celle que nous avons entammé dans notre post précédent [[PostPrec](https://www.energy-alternatives.eu/2020/05/07/mix-de-production-delectricite-energie-et-puissance)], tant il est évident qu'un MWh non pilotable n'a pas la même valeur qu'un MWh pilotable. La seconde, sur le plan économique, impose de tenir compte de l'ensemble des coûts et de la temporalité associée. Nous avons rappelé quel était le cadre classique pour encadrer cette difficulté. Nous espérons par ce post, ouvrir un espace de discussion dans le débat démocratique autour de la transition énergétique qui soit scientifique, permettant la remise en question des modèles et des paramètres (comme l'actualisation) mais en évitant de comparer des choses qui ne sont pas comparables. Une démarche comme celle appliquée dans [Jancovici2018](https://jancovici.com/transition-energetique/renouvelables/100-renouvelable-pour-pas-plus-cher-fastoche/) qui ne consisterait à ne tenir compte que des coûts d'investissement sans tenir compte de l'actualisation, des coûts d'exploitation, des coûts de démantèlement, et des coûts marginaux, n'est pas adaptée à nos objectifs. C'est un sujet qui peut évoluer assez vite et sur lequel il est difficile de tout maîtriser, nous serons à l'écoute des remarques et propositions qui seront faites en commentaires. Autrement dit, les données et modèles proposés ici sont ouverts à discussion, et nous essaierons d'actualiser ce post à partir des commentaires constructifs qui seront faits et des évolutions au fil du temps.
</span>

<span class="mytext">
Dans un prochain post je complèterai celui ci en fournissant des données économiques pour le stockage batterie, des volants d'inerties, et des technologie de *power to gaz* (hydrogène ou méthane). Nous nous concentrerons également sur les aspects environnementaux dans un autre post.
</span>
# Bibliographie

[PostPrec] [Mai 2020, Mix de production d’électricité – énergie et puissance.](https://www.energy-alternatives.eu/2020/05/07/mix-de-production-delectricite-energie-et-puissance)

[NREL2018] [Simple Levelized Cost of Energy (LCOE) Calculator Documentation](https://www.nrel.gov/analysis/tech-lcoe-documentation.html)

[Williams2019] [Williams and Tuber, Energy Policy 2019  - Levelised cost of energy – A theoretical justification and critical assessment](https://www.sciencedirect.com/science/article/pii/S0301421518306645)

[CRE2019] [2019- Rapport de la CRE- Coûts et rentabilités du grand photovoltaïque en métropole continentale](https://www.cre.fr/Documents/Publications/Rapports-thematiques/Couts-et-rentabilites-du-grand-photovoltaique-en-metropole-continentale)

[CDC2012] [2012 Les coûts de la filière électro nucléaire](https://www.ccomptes.fr/fr/publications/les-couts-de-la-filiere-electro-nucleaire)

[CDC2014] [Le coût de production de l’électricité nucléaire actualisation 2014 ](https://www.ccomptes.fr/fr/publications/le-cout-de-production-de-lelectricite-nucleaire-actualisation-2014)

[CDC2016] [rapport public annuel de 2016, Tome I - La maintenance des centrales nucléaires : une politique remise à niveau, des incertitudes à lever](https://www.ccomptes.fr/fr/publications/le-rapport-public-annuel-2016)

[CDC2019] Juillet 2019 [rapport de la cours des comptes sur la gestion du combustible nucléaire](https://www.ccomptes.fr/fr/publications/laval-du-cycle-du-combustible-nucleaire)

[CDC2020] Mars 2020 [L’arrêt et le démantèlement des installations nucléaires](https://www.ccomptes.fr/fr/publications/larret-et-le-demantelement-des-installations-nucleaires)

[IRENA2012]IRENA 2012 - [Cost analysis of Hydropower](https://www.irena.org/documentdownloads/publications/re_technologies_cost_analysis-hydropower.pdf)

[RevEnergie2019] [LA RÉDUCTION DES COÛTS DE CONSTRUCTION DU NOUVEAU NUCLÉAIRE](https://www.larevuedelenergie.com/la-reduction-des-couts-de-construction-du-nouveau-nucleaire/) N°642 / janvier-février 2019 - par Michel Berthélemy Jean-Guy Devezeaux de Lavergne

[Cost2013] [Current and Prospective Costs of Electricity Generation until 2050](https://econpapers.repec.org/paper/diwdiwddc/dd68.htm)

[EIA2016] [Capital costs, U.S. energy information administration, 2916](https://www.eia.gov/analysis/studies/powerplants/capitalcost/pdf/capcost_assumption.pdf)

[Peysson2019] [2019 Pierre Peysson, IMPACT DE LA RÈGLEMENTATION SUR LES COÛTS DE PRODUCTION DE L’ÉOLIEN EN MER EN EUROPE](https://www.larevuedelenergie.com/impact-de-la-reglementation-sur-les-couts-de-production-de-leolien-en-mer-en-europe/)

[Jancovici2018] [Blog Jean-Marc Jancovici 2018. 100% renouvelable pour pas plus cher, fastoche ?](https://jancovici.com/transition-energetique/renouvelables/100-renouvelable-pour-pas-plus-cher-fastoche/)

[ADEMEGES] [Bilan des émissions de $CO_2$ du Charbon](https://www.bilans-ges.ademe.fr/documentation/UPLOAD_DOC_FR/index.htm?solides3.htm)

# Annexes

## Annexe 1- Taux d'actualisation, une discussion

<span class="mytext">
Discuter l’actualisation dépasse de très loin ce que je peux faire ici aujourd’hui sans vous ennuyer, on a là un pan entier de l’économie. Notons juste que 8% correspond à une vision court-termiste, même s’il y a pire (certains gestionnaires de capital voudront 10% voir 15%), mais que même à 4% on ne voit pas bien au-delà de 40 ans. Des discussions un peu tendues ont eu lieu sur cette question autour du rapport Stern sur les conséquences du changement climatique (prévues à l’époque pour dans longtemps). Il existe des méthodes qui consistent à ne plus actualiser au-delà d’une certaine durée, pour éviter d’écraser les coûts. Après, même dans un monde « en décroissance » ou avec une inflation nulle, l’actualisation peut difficilement se rapprocher de zéro. Ce petit modèle et la valeur de son unique paramètre soulèvent des questions de société importantes, et nous n'allons pas y apporter un éclairage déterminant ici. L'actualisation est le reflet de plusieurs éléments et nous allons en mentionner quelques uns.
</span>

<span class="mytext">
Le premier est **l'inflation**. En effet, avec une inflation $\tau_I$ l'argent $x_{n,n}$ obtenu à l'année $n$ en monnaie de l'année $n$ ne vaut plus que $x_{n,n+1}=x_{n,n}/(1+\tau_I)$ en monnaie de l'année $n+1$. Pour quelqu'un qui aurait emprunté l'argent $x_{0,0}$ à l'année $0$ et qui rembourserait $x_{n,n}$ chaque année avec un intérêt $\tau_N$ : $\sum_n x_{n,n}\times (1+\tau_N)^n =x_{0,0}$, le remboursement total exprimé en monnaie de l'année $0$ serait de $\sum_n x_{n,0}/(1+\tau_I)^n*(1+\tau_N)^n$. Cette somme ne sera supérieure à $x_{0,0}$ que si $\tau_N>\tau_I$.  On définit classiquement le taux d'intérêt "réel" $\tau_R=\tau_N-\tau_I$ par opposition au taux "naturel" $\tau_N$, et l'on fait souvent l'approximation suivante
</span>
<span class="mytext">
$$\sum_n x_{n,0}/(1+\tau_I)^n*(1+\tau_N)^n \approx \sum_n x_{n,0}\times (1+\tau_R)^n$$
</span>
<span class="mytext">
Ainsi, on comprend facilement que le taux naturel d'actualisation a en général un plancher au niveau de l'inflation, et que les périodes de forte inflation, comme celle que nous avons connu dans les années 70, sont propices à écraser des coûts d'investissement dans le calcul d'un LCOE. Ceci a joué un rôle important dans la construction du parc nucléaire actuel. Une inflation nulle n'implique pas nécessairement une actualisatioin nulle.
</span>

<span class="mytext">
Les autres facteurs importants sont dès lors liés au taux réel $\tau_R$. L'analyse de ce taux va dépendre du capital en notre possession que l'on peut dédier à l'investissement et de la capacité à emprunter. Si l'on est une entreprise avec du capital et que l'on cherche à en tirer le plus de profit possible il sera alors question de **rendement du capital** (lequel peut se calculer à une époque donnée en fonction de l'échéance et du risque que l'on est près à prendre), mais la valeur que l'on peut tirer du capital est aussi une question de stratégie d'entreprise et si il est question d'entrer dans un marché, d'écraser un concurrent ou si l'on table sur une croissance forte à venir de l'entreprise, on choisira  un taux réel plutôt bas. Si l'on ne possède pas le capital en question, le taux pourra refléter une combinaison du **taux d'intérêt** de différents prêts bancaires. Ainsi, on peut voir qu'un LCOE qui incluerait un taux réel relatif à un niveau de retour sur investissement minimum attendu correspond à un tarif d'achat demandé dans un appel d'offre. Dans le cas d'un contrat pour différence, comme c'est le cas pour [Hinkley Point](https://www.zonebourse.com/ELECTRICITE-DE-FRANCE-4998/actualite/Electricite-de-France-le-cout-d-Hinkley-Point-C-en-hausse-de-29-en-3-ans-29251492/), le tarif est indexé sur l'inflation et donc l'inflation ne doit pas être incluse dans le calcul du taux d'actualisation.
</span>

<span class="mytext">
Dans le cas où l'on actualise une dépense loingtaine, comme pour le démentellement ou la gestion des déchets, le raisonnement sous-jacent est que l’entreprise peut  mettre dès le début du projet une somme de côté (**provisionnement**) pour le démantèlement et que cet argent, s’il est bien placé, rapportera une somme d’argent liée à l’actualisation. Dans ce cas l’actualisation a un lien avec la rentabilité du capital. On demande aujourd'hui au nucléaire, de consolider le provisionnement pour le démentellement et la gestion des déchets, grâce à des investissements dans des **actifs dédiés**.  
</span>

<span class="mytext">
Dans le cas où l'on investi dans un nouveau moyen de production, mais que la durée de construction ne permet pas de rembourser tout de suite l'argent empruntée, il faut alors pays des frais supplémentaires, sous forme d'intérêt intercallaires. Les coûts d'investissement $C_I$ devraient intégrer cet aspect, et une réduction des temps de construction peut être dans beaucoup de cas, favorable à la diminution des coûts. C'est un sujet très important pour la fillière nucléaire
[RevEnergie2019](https://www.larevuedelenergie.com/la-reduction-des-couts-de-construction-du-nouveau-nucleaire/). Si l'on suppose que l'on dépense une somme $C_{I0}$ de manière uniforme sur une durée de construction $L_I$, avec une actualisation $\alpha$, alors on doit pouvoir retrouver $C_I$ (coût d'investissement à la date où la centrale commence à produire) à partir de la formule :
</span>
<span class="mytext">
$$C_I= C_{I0} * \frac{L_I^{\alpha}}{L_I}, \;\; \text{ où }   L_I^{\alpha}= \sum_{n=1}^{L_I}(1+\alpha)^n= \frac{1+\alpha}{\alpha}((1+\alpha)^{L_C}-1)$$
</span>
<span class="mytext">
Dans l'Annexe suivante, nous donnons une Table pour $L_I^{\alpha}/L_I$ en fonction de $\alpha$ et $L_{I}$ la durée de construction (la deuxième table dans l'annexe). On peut y voir qu'une durée de construction de 15 ans correspond à une multiplication par deux des coûts d'investissement.
</span>
## Annexe 2- Table pour la durée de vie corrigée
<span class="mytext">
Table de $L^\alpha$ en fonction de la durée de vie $L$ et de $\alpha$.
</span>

||1E-04|0.01|0.02|0.03|0.04|0.05|0.06|0.07|0.08|0.09|0.1|
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|15|14.99|14.004|13.106|12.296|11.563|10.899|10.295|9.745|9.244|8.786|8.367|
|20|19.981|18.226|16.678|15.324|14.134|13.085|12.158|11.336|10.604|9.95|9.365|
|25|24.97|22.243|19.914|17.936|16.247|14.799|13.55|12.469|11.529|10.707|9.985|
|30|29.957|26.066|22.844|20.188|17.984|16.141|14.591|13.278|12.158|11.198|10.37|
|35|34.941|29.703|25.499|22.132|19.411|17.193|15.368|13.854|12.587|11.518|10.609|
|40|39.922|33.163|27.903|23.808|20.584|18.017|15.949|14.265|12.879|11.726|10.757|
|45|44.901|36.455|30.08|25.254|21.549|18.663|16.383|14.558|13.077|11.861|10.849|
|50|49.878|39.588|32.052|26.502|22.341|19.169|16.708|14.767|13.212|11.948|10.906|
|55|54.852|42.569|33.838|27.578|22.993|19.565|16.95|14.916|13.304|12.005|10.942|
|60|59.823|45.405|35.456|28.506|23.528|19.876|17.131|15.022|13.367|12.042|10.964|
|65|64.792|48.103|36.921|29.306|23.969|20.119|17.266|15.098|13.409|12.066|10.978|
|70|69.759|50.67|38.249|29.997|24.33|20.31|17.368|15.152|13.438|12.082|10.986|
|75|74.723|53.113|39.451|30.593|24.628|20.459|17.443|15.19|13.458|12.092|10.991|
|80|79.685|55.437|40.539|31.107|24.872|20.576|17.5|15.218|13.471|12.099|10.995|
{: .mbtablestyle .wrapstyle .simple7}
<span class="mytext">
Table pour $L_I^{\alpha}/L_I$ en fonction de $\alpha$ et $L_{I}$ la durée de construction.
</span>

|  |     0.02|     0.04|     0.06|     0.08|      0.1|
|:--|--------:|--------:|--------:|--------:|--------:|
|1  | 1.020000| 1.040000| 1.060000| 1.080000| 1.100000|
|2  | 1.030200| 1.060800| 1.091800| 1.123200| 1.155000|
|3  | 1.040536| 1.082155| 1.124872| 1.168704| 1.213667|
|4  | 1.051010| 1.104081| 1.159273| 1.216650| 1.276275|
|5  | 1.061624| 1.126595| 1.195064| 1.267186| 1.343122|
|6  | 1.072381| 1.149716| 1.232306| 1.320467| 1.414529|
|7  | 1.083281| 1.173461| 1.271067| 1.376661| 1.490841|
|8  | 1.094329| 1.197849| 1.311414| 1.435945| 1.572435|
|9  | 1.105525| 1.222901| 1.353422| 1.498507| 1.659714|
|10 | 1.116872| 1.248635| 1.397164| 1.564549| 1.753117|
|11 | 1.128372| 1.275073| 1.442722| 1.634284| 1.853117|
|12 | 1.140028| 1.302237| 1.490178| 1.707941| 1.960226|
|13 | 1.151841| 1.330147| 1.539621| 1.785763| 2.074999|
|14 | 1.163815| 1.358828| 1.591141| 1.868008| 2.198034|
|15 | 1.175952| 1.388302| 1.644835| 1.954952| 2.329982|
{: .mbtablestyle .wrapstyle .simple5}

## Annexe 3- Compléments nucléaire
### Annexe 3-a. Démentellement et gestion des déchets nucléaires.
<span class="mytext">
L'évaluation des provisions pour le démentellement et les déchets est une tâche délicate dont les tenants et aboutissants sont assez bien expliqués dans deux rapports de la cours des comptes sur la Gestion du combustible nucléaire [[CDC2019](https://www.ccomptes.fr/fr/publications/laval-du-cycle-du-combustible-nucleaire)] et sur le démentellement des installations [[CDC2020](https://www.ccomptes.fr/fr/publications/larret-et-le-demantelement-des-installations-nucleaires)]. Ces rapports font suite aux rapports plus généraux [[CDC2012](https://www.ccomptes.fr/fr/publications/les-couts-de-la-filiere-electro-nucleaire)] et [[CDC2014](https://www.ccomptes.fr/fr/publications/le-cout-de-production-de-lelectricite-nucleaire-actualisation-2014)] sur le coût du nucléaire.
Pour bien comprendre les chiffres donnés par ces rapports, en ce qui concerne le démentellement aussi bien que pour la gestion des déchets, il faut faire la différences entre :
</span>
<div class="mytext">
<ul> <li>
les charges brutes (hors actualisation, en "€ d'aujourd'hui"),</li>
<li>  les sommes qu'il faudrait avoir provisionnées aujourd'hui si l'on ne voulait plus rien avoir à payer qui correspondent aux charges brutes actualisées à partir de la connaissance des échéances (en "€ d'aujourd'hui"), </li>
<li> les sommes provisionnées effecivement aujourd'hui, et un plan de provisionnement en [€/an] pour chaque année à venir. Ces sommes doivent permettre de compléter les provisons actuelles afin d'atteindre les charge brutes à temps.</li>
 </ul>
</div>
<span class="mytext">
Par ailleurs, il faut distinguer les sommes allouées à EDF et celles allouées à ORANO et au CEA. Faisons l'hypothèse (discutable) que celles allouées à EDF sont exactement celles liées à la production d'électricité d'origine nucléaire et nous ramenons des sommes données en € à la puissance installée de 63 GW pour obtenir  des montants en [€/kW]  et en [€/kW/an] (plus facile à interpréter vis à vis de l'ensemble de ce post).
</span>

<span class="mytext">
En ce qui concerne le **démentellement**, dans  on parle de 18.5 Mds d'€ pour les charges brutes ([[CDC2020](https://www.ccomptes.fr/fr/publications/larret-et-le-demantelement-des-installations-nucleaires)] p103).  Cela fait moins de 300 €/kW pour les charges brutes ramenées à la puissance installée, la cours des compte demande des analyses supplémentaires, les démentellements à venir viendront sans doute renforcer la méthode d'évaluation.   Dans [[CDC2020](https://www.ccomptes.fr/fr/publications/larret-et-le-demantelement-des-installations-nucleaires)] p117 sont donnés les montants provisionnés par EDF pour le démentellement des installations de production nucléaire entre 2013 et 2018. En faisant une moyenne et en rammenant à la puissance installée, on arrive à 8€/kW/an. Le planing de  provisionnement correspondant découle d'une hypothèse d'évolution du parc jugée un peu trop optimiste par la cours des comptes (voir [[CDC2020](https://www.ccomptes.fr/fr/publications/larret-et-le-demantelement-des-installations-nucleaires)] p118).
</span>

<span class="mytext">
Pour la **gestion des déchets**, on peut déduire de ce qui est écrit p89-90 du rapport [[CDC2019](https://www.ccomptes.fr/fr/publications/laval-du-cycle-du-combustible-nucleaire)]qu'en 2017 l'ensemble de ces charges brutes pour la gestion des déchets, représentaient pour EDF environ 45 Mds d'€ avant actualisation et 20 Mds d'€ après actualisation. Cela inclu notamment le projet Cigéo (25 Mds d'€ avant actualisation) pour lequel la cours encourage une réévaluation des coûts, qui est déjà discutée dans le rapport de 2012 [[CDC2012](https://www.ccomptes.fr/fr/publications/les-couts-de-la-filiere-electro-nucleaire)] p84. Rapporté au parc de production, cela signifie un peu plus de 700 €/kW, qui se réduisent à environ 310 €/kW "actuel" en tenant compte de l'actualisation. Notons que nous donnons ici les montants relativement aux puissances installées, là où il faudrait plutôt les ramener à l'énergie produite jusqu'à maintenant, ou produite sur la durée de vie des installations. Il faut noter que ces charges sont liées à des coûts futurs et n'incluent pas les investissements passés déjà amortis. Pour le provisionnement, le rapport de 2014 donne une valeur de 1.2 Mds d'€ en 2013 soit 19 €/kW/an [[CDC2014](https://www.ccomptes.fr/fr/publications/le-cout-de-production-de-lelectricite-nucleaire-actualisation-2014)].
</span>

<span class="mytext">
**Sensibilité des résultats**. Ces provisions dépendent dans tous les cas :
</span>
<div class="mytext">
 <ul> <li> du taux (nominal) d'actualisation utilisé qui découle en partie (de manière à peu près additive) du taux réel de rémunération du capital et du taux d’inflation prévisionnel de long terme. Il y a de nombreux débat sur ce taux car la baisse du taux en cours pèse sur les finances des énergéticiens voir déjà <a href="https://www.ccomptes.fr/fr/publications/le-cout-de-production-de-lelectricite-nucleaire-actualisation-2014"> [CDC2014] </a> p111. Récement, face à la chute du taux, un système de seuil a été introduit, voir <a href="https://www.ccomptes.fr/fr/publications/larret-et-le-demantelement-des-installations-nucleaires"> [CDC2020] </a> p119.  </li>
 <li> des échéances choisies pour chaque centrale : durée de construction, durée de vie, date de démentellement, fermeture des stockages.</li>
 </ul>
</div>
<span class="mytext">
 Pour les déchets, ces provisions dépendent aussi de beaucoup de paramètres relatifs à l'évolution future du cycle, et sur lesquels la cours des compte encourage à des éclaircissements :
  </span>
  <div class="mytext">
   <ul> <li>  quelles futures technologies déployées ?  EPR "moxé" ? IVeme génération ? </li>
    <li>  quels stratégie pour la fermetures des centrales de la première génération ? Les centrales 900MW moxées qui permettent un certain recyclage sont aussi les plus anciennes, </li>
    <li>  Quelles évolutions de la classification des substances radioactives ? elle détermine les traitements associés à une substance donnée.</li>
    </ul>
</div>

### Annexe 3-b. Coûts d'un accident nucléaire majeur
<span class="mytext">
A l'heure actuelle, les coûts liés à une assurance vis à vis d'un éventuel accident ne sont pas vraiment intégrés puisque l'assurance correspondante est plafonnée. Une évaluation est proposée <a href="https://www.irsn.fr/FR/connaissances/Installations_nucleaires/Les-accidents-nucleaires/cout-economique-accident/Pages/2-cout-economique-pour-2-scenarios.aspx#.XzqSgfgzbx4"> par l'IRSN,  </a> pour un coût de 420 Mds d'€ dans le cas d'un accident majeur en France. Une autre étude donne un coût de 120 Mds d'€ (celle utilisée par la cours des comptes dans ses arpports). Il semble très léger de vouloir associer une probabilité à ce type d'évenement, mais on peut par exemple dire que 400 GW de nucléaire ont été installé dans le monde avec une durée moyenne de fonctionnement autour de 30 ans. Cela a conduit à deux accidents majeurs, ce qui indique d'affecter au coût d'un accident majeur un poids de $1.6*10^{-10}/kW/an$, c'est à dire 70 €/kW/an. Cette évaluation ne tient pas compte du fonctionnement d'une assurance, et du placement de l'argent cotisé qui pourrait être fait et qui pourrait faire beaucoup baisser cette valeur. C'est ce qui est fait dans  <a href="https://www.ccomptes.fr/fr/publications/le-cout-de-production-de-lelectricite-nucleaire-actualisation-2014"> [CDC2014] </a> et qui donne lieu à des sommes négligeables, au pire quelques €/MWh. La détermination de ce poid et du coût associé soulève beaucoup de questions, le rapport de la cours des compte propose une autre approche avec un poids de 1 sur tout le parc français et un coût de 120 Mds d'€. La lecture du livre de Jean-Pierre Dupuy <a href="https://www.seuil.com/ouvrage/pour-un-catastrophisme-eclaire-jean-pierre-dupuy/9782020660464"> "Pour un catastrophisme éclairé"</a> est intéressante sur le sujet grand coût/petit poids, elle préfigure la notion de signe noir développée plus tard dans la monde de la finance. Quoi qu'il en soit, le coût de l'assurance n'est pas à l'origine d'une explosion des coûts, et même si il n'est pas non plus négligeable nous n'en tiendrons pas compte ici. Notons tout de même que ramener ce coût à un simple coût économique nous semble être une approche limitée.
</span>
