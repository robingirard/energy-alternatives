---
title: Mix de production d’électricité – énergie et puissance.
key: mix-de-production-delectricite-energie-et-puissance
ref: mix-energie-puissance
tags: mix-production intermittence evolution
article_header:
  type: cover
  image:
    src: /assets/images/Posts/2020-05-07/DSCF8920c.jpg
---



<div class="summary" style="display:block; text-align: justify">
<em>
     L’objectif de ce post est d’introduire une base simple permettant la description du mix de production d’électricité d’un pays. Cela passe par une segmentation des moyens de production en grandes familles : « nucléaire », « charbon », « gaz », « hydraulique », « photovoltaïque », « éolien », ou « biomasse ». La place que tient chacune de ces classes dans le mix est résumée par deux indicateurs simples, importants et complémentaires que sont d’un côté l’énergie annuelle produite et de l’autre la puissance installée. La puissance installée est décomposée entre une puissance installée pilotable et une qui ne l’est pas. Ce qui lie l’énergie annuelle produite à la puissance installée est le facteur de charge. Nous donnons une première analyse grossière des éléments qui l’influencent pour les différents moyens permettant de produire de l’électricité. Enfin, nous expliquons en quoi la puissance installée et énergie annuelle produite sont de bons paramètres pour estimer le coût économique et en termes de GES d’un système électrique. Nous donnons les paramètres permettant ces estimations dans un tableur partagé et nous l’utilisons pour estimer l’ordre de grandeur du coût (économique et en termes de GES) d’un futur mix fortement renouvelable et de celui d’un futur mix fortement nucléaire. En définitive le paramètre primordial pour l’estimation des impacts économiques et environnementaux n’est pas la puissance installée mais bien l’énergie produite. Nous ne donnons ici que des estimations grossières mais nous montrons en quoi le mix nucléaire implique des émissions de GES plus faibles que le mix fortement renouvelable mais que tous deux sont compatibles avec la stratégie nationale bas carbone visant la neutralité carbone à l’échelle de la France, pour l’horizon 2050.
</em>
</div>
<!--more-->
<span class="mytext">
[Le code et les données permettant de faire les graphiques de ce post sont mis à disposition librement.](https://git.persee.mines-paristech.fr/robin.girard/energy-alternatives/blob/master/2020-04-01-Puissance-Energie-LCOE.R)
</span>

____________________________________


# Description d’un système électrique

## Puissance installée et énergie annuelle consommée.

<span class="mytext">
On combine sur un territoire (une île, un pays ou un continent) différentes sortes de moyens de production et de stockage d’électricité et l’ensemble formé par ceux-ci est appelé le mix de production d’électricité. Si l’on y ajoute le réseau de transport et de distribution d’électricité dont nous parlerons dans un autre texte, il s’agit alors du système électrique. Le mix de production d’électricité en France est composé essentiellement de centrales nucléaires et de centrales hydrauliques, mais il comprend aussi des centrales à gaz, des éoliennes, des panneaux photovoltaïques, des usines marémotrices, …
</span>
<span class="mytext">
Les deux premières grandeurs qu’il faut apprendre à distinguer pour appréhender le mix de production d’électricité d’un pays sont, d’un côté l’énergie annuelle produite qui est une énergie “finale” (par opposition à une énergie primaire) qui s’exprime le plus souvent en TWh (ou GWh, ou MWh, ou kWh), et de l’autre la puissance installée qui se donne en GW (ou MW, ou kW). Comme nous le verrons dans la section 3, l’intérêt qu’il y a à décrire un système électrique à partir des puissances installées et des énergies produites est que celles-ci se traduisent assez simplement en termes de coûts économique et d’émissions de gaz à effet de serre (GES).
</span>
<span class="mytext">
On peut voir dans le graphique ci-dessous la décomposition entre puissance et énergie pour les différents moyens de production en France et en Allemagne en 2018. Les moyens de production sont regroupés en grandes classes selon la source d’énergie utilisée : nucléaire, gaz, pétrole (oil), charbon, éolien (Wind), photovoltaïque (Solar PV). Nous avons ici rassemblé les moyens de production sous différentes grandes classes (éolien, PV, nucléaire, gaz, charbon, …) derrière lesquelles se cachent des variantes importantes que nous détaillerons prochainement, vis à vis des capacités techniques, des coûts, et des impacts environnementaux. …
</span>

<span class="text" id="Figure1" style="display:block;text-align:center">
![Image]({{site.baseurl}}/assets/images/Posts/2020-05-07/ElecMixFig1.png)
</span>
<span class="legendtext" id="CAPFigure1" style="display:block;text-align:center">
**Figure 1** -- Energie produite par an et puissance installée pour différentes classes de moyens de production en France et en Allemagne en 2018. Les moyens de production pilotables sont à gauche de la zone verte, les moyens de production fortement carbonés sont à gauche de la zone rouge (Oil, Gaz et Coal). Source de données ENTSOE [[1](https://www.entsoe.eu/data/)]
</span>

## Puissance installée pilotable et non pilotable
<span class="mytext">
La puissance installée (ou capacité installée) n’a pas la même valeur selon qu’elle est pilotable (gaz, charbon, nucléaire, hydraulique) ou relative à une production non pilotable (éolien, photovoltaïque) dont la disponibilité n’est pas le résultat d’un choix. On ne peut produire avec les éoliennes et les panneaux photovoltaïque que lorsqu’il y a du vent ou du soleil. En France la capacité pilotable est atour de 110 GW, alors qu’en Allemagne elle est un peu plus faible, autour de 100GW (on peut lire ces chiffres sur la Figure 1 en totalisant les puissances installées des moyens de production se trouvant à gauche de la zone bleue de l’hydraulique).
</span>
<span class="mytext">
Cette dichotomie est utile mais quelques nuances doivent être évoquées. Un moyen de production pilotable n’a jamais une disponibilité de 100% du fait de la nécessité de maintenances ou de certaines contraintes de fonctionnement, mais les maintenances à l’origine des indisponibilités correspondantes sont le plus souvent le résultat d’un choix qui peut être utilement optimisé. C’est par exemple le cas en France avec le nucléaire dont les maintenances sont optimisées pour adapter la production à la variation saisonnière de la consommation due à sa thermosensibilité, nous en avons déjà parlé [[2](https://www.energy-alternatives.eu/2020/03/22/une-contribution-a-la-reflexion-sur-la-strategie-nationale-bas-carbone-dans-le-batiment-partie-1-quels-modes-de-chauffage-a-lhorizon-2050/)]. Une partie de l’hydraulique au fil de l’eau n’est que partiellement pilotable (avec des flexibilités de quelques dizaines de minutes). Un moyen de production non pilotable peut être partiellement piloté, par exemple en faisant de la régulation à la baisse pour gérer une contrainte réseau, ou pour gérer un surplus de production sur le système. C’est ce que l’on appelle parfois l’effacement de production, le bridage (pour l’éolien) ou en anglais le curtailement.
</span>

<span class="mytext">
La capacité pilotable donne un ordre de grandeur de la consommation instantanée maximale qu’il est possible de couvrir mais cette question requiert une analyse plus complexe tenant compte d’autres facteurs comme d’un côté les besoins de maintenance des centrales pilotables, les besoins de réserve du système électrique qui diminuent la capacité pilotable disponible et de l’autre les variations de la consommation conjointement avec celles de la production intermittente, l’existence et la disponibilité de capacités de stockage, d’interconnexion et de demande flexible qui peuvent permettre de revoir à la baisse le besoin de puissance pilotable. Il n’est pas nécessaire à ce stade de comprendre ce qui se cache derrière tous ces termes, c’est un enjeu important sur lequel nous reviendrons. En France, nous avons couvert, lors de l’hiver très froid de 2012, une consommation de 110 GW.
</span>

##  Exemples de mix électriques dans le monde

<span class="mytext">
La place occupée par un moyen de production peut être décrite en termes de puissance pilotable installée, ou bien, en termes d’énergie annuelle produite. Ces deux choses sont en général différentes. Par exemple, le nucléaire contribue à environ 3/4 de la production d’énergie électrique en France mais ne représente qu’un peu plus de la moitié de la capacité pilotable (avec 63 GW installés). A l’inverse, toujours en France, la capacité hydraulique pilotable tient une place importante en puissance (de l’ordre de 25 GW) mais beaucoup moins en énergie. En Allemagne les énergies éoliennes et photovoltaïques ont une puissance installée importante qui représente la moitié du mix en termes de puissance installée, ce sont des puissances non pilotables qui représentent moins d’un tiers pour ce qui est de l’énergie produite. Mais nous allons voir que le rapport entre puissance installée et énergie produite est relativement stable au sein d’une technologie (c’est le facteur de charge dont nous parlons à la section suivante). Aussi nous donnons dans la [Figure 2](#CAPFigure2) une description des volumes d’électricité produits par différentes technologies pour différents pays dans le monde
</span>

<span class="text" id="Figure2" style="display:block;text-align:center">
![Image]({{site.baseurl}}/assets/images/Posts/2020-05-07/ElecMixFig2-World2.png)
</span>
<span class="legendtext" id="CAPFigure2" style="display:block;text-align:center">
**Figure 2** -- Énergie annuelle (électrique) produite en 2018 par pays et par technologie.
</span>

<span class="mytext">
Les données ont des origines variées mais elles sont toutes publiques, mon travail a été de les rassembler pour vous dans ce document. On peut noter que la Chine a donc une production d’énergie électrique 10 fois plus importante que l’Allemagne qui a elle-même une production deux fois plus importante que l’Espagne. C’est en France que la production bas carbone est la plus importante mais l’Espagne, l’Allemagne et l’Angleterre ont une part significative de production bas carbone.
</span>

# Facteur de charge
## Définition
<span class="mytext">
On passe de la puissance installée d’une centrale ou d’un groupe de centrales à une énergie annuelle par le facteur de charge qui est un élément essentiel pour décrire les moyens de production du mix électrique. Il se définit comme l’énergie produite pendant une certaine période (une heure, un mois, un an, …) rapportée à l’énergie que l’on aurait produit en tournant tout le temps à pleine puissance. Le facteur de charge annuel est exprimé soit en proportion soit en nombre d’heures annuelles (obtenu en multipliant la proportion par le nombre d’heures d’une année : 8760). Si l’on note  $E$  l’énergie annuelle produite en TWh/an et $P$ la puissance installée en GW, on a alors un facteur de charge annuel donné par :
</span>
<span class="mytext">
$$FC=\frac{E}{P\times 8760 \times 10^{−3}}=\frac{E}{P\times 8.76}$$
</span>
<span class="text" id="Figure3" style="display:block;text-align:center">
![Image]({{site.baseurl}}/assets/images/Posts/2020-05-07/ElecMixFig3-CapacityFactors.png)
</span>
<span class="legendtext" id="CAPFigure3" style="display:block;text-align:center">
**Figure 3** -- distribution des facteurs de charge pour différentes technologies sur la période 2008-2018 et dans les différents pays considérés dans la Figure 2. Ces distributions sont représentées avec des boîtes à moustache, le rectangle contient la moitié des valeurs et le trait plein 90% des valeurs, les points sont des valeurs extrêmes ou aberrantes vis à vis des autres observations. Un point représente le facteur de charge de tout un parc pour toute une année dans un pays.
</span>
<span class="mytext">
On peut voir [Figure 3](#CAPFigure3) la distribution des facteurs de charge des différentes classes des technologies sur la période 2008-2018 et dans les différents pays considérés Figure 2. Ce ne sont donc pas les facteurs de charge des centrales qui sont représentés ici mais ceux de groupes cohérents de centrales dans différents pays et pour différentes années. Ces valeurs ne sont pas pondérées par la taille des différents pays et l’on ne peut pas dire que les pays choisis soient exactement représentatifs de la diversité existante dans le monde, aussi ces valeurs sont données ici à titre d’exemple, surtout pour illustrer le panel de valeurs possibles et la tendance par type de moyen de production. Nous allons maintenant donner quelques explications sur l’origine de ces valeurs.
</span>
## Ce qui influence le facteur de charge
<span class="mytext">
Plusieurs éléments qui ne sont pas du même ordre peuvent influencer le facteur de charge d’un moyen de production d’électricité :

<span class="mytext">
**La météo** — La production photovoltaïque dépend de l’ensoleillement, l’éolien dépend du vent, et l’hydraulique au fil de l’eau qui dépend de l’hydraulicité et donc de la pluie. Par ailleurs nous avons déjà vu que la température influence la consommation et donc elle influence également la production qui est mise en face.
</span>
<span class="mytext">
**Les contraintes techniques de fonctionnement** — Donnons quelques exemples. Les indisponibilités pour recharge des centrales nucléaires qui sont d’à peu près un mois tous les ans, deux mois tous les trois ans et 3 mois tous les dix ans. Pour le nucléaire en bord de fleuve le débit et la température de l’eau peuvent-être limitants, et donc les périodes de sécheresse sont problématiques ce qui est une réelle difficulté dans un contexte de changement climatique. Pour l’hydraulique, le stock hydraulique de nos grands barrages ou le respect de l’utilisation des cours d’eau pour le tourisme ou vis-à-vis de la flore qui y grandit, peuvent être limitants. Des contraintes de flux sur le réseau électrique peuvent imposent de limiter une partie de la production localement pour certaines heures, c’est le cas par exemple assez souvent aujourd’hui dans le nord de l’Allemagne où est concentrée une grande quantité d’éoliennes qui ne sont pas assez bien reliées au sud de l’Allemagne.
</span>
<span class="mytext">
**La structure de coût des moyens de production** – Nous allons voir que les coûts d’un moyen de production peuvent être décomposés en coûts fixes qui apparaissent dès que l’on construit et maintient en activité une centrale et coûts variables (ou marginaux) qui n’apparaissent que lorsque la centrale produit (essentiellement des coûts de carburant). L’importance relative de ces deux postes de dépenses pour un moyen de production impacte la fonction qu’il va jouer dans le mix électrique pour satisfaire l’équilibre offre-demande (base vs pointe). Par exemple certaines centrales installées pour leur faible coût d’investissement (comme certaines centrales à gaz) fonctionnent peu souvent parce qu’elles ont un coût marginal élevé et ne sont donc utilisées que lorsque le reste du mix électrique n’est pas suffisant pour couvrir la consommation. Elles sont tout de même installées car leur coût capacitaire (eu €/kW installé) est faible. On parle alors de moyen de production de pointe. A l’opposé, le nucléaire a un coût variable faible et un coût d’investissement élevé, on l’utilise en base et son facteur de charge doit être le plus élevé possible, essentiellement pour des raisons économiques.
</span>

<span class="mytext">
Dans un système chaque moyen de production peut impacter le facteur de charge des autres de par ses caractéristiques économiques, la variabilité de la consommation impacte également le facteur de charge. Il faut aussi noter qu’un faible facteur de charge n’est pas en soi le reflet d’une difficulté technique, mais que c’est plutôt la variabilité et la non pilotabilité des moyens de production qui pourra l’être, comme avec les EnR intermittentes (éolien/PV).
</span>

<span class="mytext">
Un faible facteur de charge n’est pas non plus à l’origine d’un faible intérêt économique ou environnemental. En effet, si un système A produit quatre fois moins d’énergie qu’un système B à puissance installée égale, mais que le système B est quatre fois plus cher, le coût à l’énergie produite pour A, toutes choses égales par ailleurs, est le même que pour B. C’est pour cela que l’on ramène souvent le coût économique à l’énergie produite [€/MWh] ce qui permet a priori des comparaisons économiques indépendantes du facteur de charge. Nous allons maintenant formaliser un peu cette remarque, et donner des quantifications tant pour la partie économique que vis-à-vis des émissions de GES.  
</span>

# Énergie et puissance : deux facteurs pour expliquer les coûts économiques et les émissions de GES
<span class="mytext">
La puissance installée et l’énergie annuelle produite – ou de manière équivalente la puissance installée et le facteur de charge- permettent assez bien d’estimer les coûts économiques du système de production d’électricité ainsi que ses émissions de GES.
</span>

## Coûts économiques
<span class="mytext">
On estime les dépenses annuelles associées à la production d’électricité (en M€/an) d’un pays par une relation linéaire (somme sur les moyens de production) du type
</span>

<span class="mytext">
$$ \sum_i \alpha_i^{cout} E_i+\beta_i^{cout} P_i$$
</span>

<span class="mytext">
En effet, une partie des coûts est directement proportionnelle à l’énergie produite (  $E$  est exprimée en [TWh/an]), elle contient le plus souvent des coûts de carburant, ces coûts sont appelés « coûts marginaux », ils sont donnés ici par  $\alpha_i^{cout}$  et exprimés en [€/MWh]. D’autre part la puissance installée (  $P$ est exprimée en GW) induit des coûts fixes d’investissement et d’entretien, des coûts de personnel, des taxes, … certains de ces coûts sont payés seulement à l’investissement, d’autres sont payés tous les ans. Ces coûts sont proportionnels à la capacité installée et une pratique est de les ramener sur une base annuelle :  $\beta_i^{cout}$  exprimé pour le moyen de production  $i$  en [€/kW/an]. Sur le plan économique cette partie est souvent importante, mais son importance varie selon les moyens de production : le nucléaire et les renouvelables ont des coûts fixes élevés mais des coûts marginaux faibles alors que pour le gaz le fioul ou le charbon c’est plutôt le contraire. Mais au sein de chaque type de centrale, il y a un panel de cas possibles que nous ne détaillons pas ici.
</span>

<span class="mytext">
Rassembler tous les coûts sur une base temporelle commune et intelligible est très pratique, ici nous utiliserons une base annuelle comme souvent dans l’énergie. Cette simplification peut être à l’origine de quelques difficultés et malentendus qu’il faut évoquer.
</span>

<span class="mytext">
Tout d’abord les coûts fixes n’interviennent pas d’une manière uniforme sur la durée de vie du projet. On peut distinguer trois temps dans le projet. Ce sont les mêmes que pour l’achat d’une maison : une grande somme d’argent est dépensée à l’investissement, puis après une durée plus ou moins importante le projet passe dans une phase d’exploitation et de remboursement. Tout au long du projet, on peut avoir à remplacer des équipements selon leur vieillissement, cela ne signifie pas que le projet est en fin de vie mais juste qu’il faut renouveler certains investissements. Une fois l’investissement initial remboursé le projet passe dans une phase d’exploitation sans remboursement, on dit que l’investissement est amorti. Cette dernière période est souvent une période de rémunération des actionnaires.
</span>

<span class="mytext">
Une conséquence de cela est que les dépenses d’une année donnée ne reflètent pas toujours les dépenses moyennes passées ou futures. Dans la Table 1 nous donnons quelques valeurs pour le coûts économiques et les émissions de GES, le coût du nucléaire « ramené à l’année 2018 » n’y intègre pas de coût d’investissement puisque les centrales françaises sont déjà amorties, il ne reflète donc pas un coût futur du nucléaire. Pour l’obtenir, il faut y ajouter le coût de la rénovation de centrales actuelles ou celui de la construction de nouveaux EPR. A l’inverse le coût du photovoltaïque a beaucoup baissé ces quinze dernières années mais comme nous payons encore les centrales installées à un coût très élevé avant 2010, le coût indiqué dans la Table 1 est bien plus élevé que le coût des centrales qui s’installent en 2018. Sur la Figure 4 nous donnons les dépenses d’investissement dans les énergies renouvelables, on peut y observer le pic de dépenses pour le PV lié à des tarifs subventionnés très élevés avant le moratoire de 2010 et qui pèsent encore aujourd’hui sur le coût de l’électricité, même si la filière est maintenant beaucoup plus intéressante économiquement.
</span>


<span class="text" id="Figure4" style="display:block;text-align:center">
![Image]({{site.baseurl}}/assets/images/Posts/2020-05-07/EvolutionCouts.png)
</span>
<span class="legendtext" id="CAPFigure4" style="display:block;text-align:center">
**Figure 4** -- Évolution des dépenses d’investissement dans les énergies renouvelables et de récupération, voir [[3](https://www.statistiques.developpement-durable.gouv.fr/chiffres-cles-des-energies-renouvelables-edition-2019)] p11. Ce ne sont pas ici les subventions mais les dépenses d’investissements. On voit que les dépenses pour les pompes à chaleur dont nous avons parlé [[2](https://www.energy-alternatives.eu/2020/03/22/une-contribution-a-la-reflexion-sur-la-strategie-nationale-bas-carbone-dans-le-batiment-partie-1-quels-modes-de-chauffage-a-lhorizon-2050/)] sont déjà importantes depuis longtemps et ont, elles, aussi connu un pic autour de 2008.
</span>

<span class="mytext">
Dans tous les cas l’annualisation pose un problème économique fondamental. C’est un problème politique et philosophique par certains de ses aspects. En effet, il est impossible de comparer objectivement une somme d’argent dépensée maintenant et une somme d’argent dépensée dans le futur. En conséquence on ne peut pas simplement diviser un investissement par la durée de vie du projet pour annualiser les coûts correspondants. La solution préconisée par les économistes est d’utiliser le modèle de l’actualisation pour rendre comparables les revenus et dépenses des différentes années : l’argent dépensé à l’année 𝑛 a une valeur proportionnelle à celui dépensé à l’année $n+1$ le coefficient de proportionnalité est $1+A$ où $A$ est le taux d’actualisation. Nous présenterons et discuterons cette méthode et ses implications dans un post futur ([ici](https://www.energy-alternatives.eu/2020/08/20/decomposition-lcoe.html)). Notons juste ici que cette méthode revient formellement à réduire la durée de vie des projets dans le calcul des revenus, et ce, d’autant plus que les projets ont une durée de vie longue. Ce paramètre a un impact très important sur les résultats mais il n’est pas simple à discuter, dans la table 1 ci-dessous nous avons pris une actualisation à 4%, ce qui est plutôt un taux faible mais sans doute pas le plus bas possible. Nous mettrons prochainement à disposition un fichier Excel dans lequel il sera possible de changer ce taux.
</span>

## Émissions de GES et synthèse pour le mix actuel Français
<span class="mytext">
Il est important de rappeler que la partie environnementale ne se résume pas aux émissions de GES même si nous nous y bornons ici. Nous allons parler d’éolien, de photovoltaïque et de nucléaire et ces trois sources d’énergie, bien qu’elles soient faiblement carbonées, posent tout un tas d’autres problèmes (ressources, utilisation du territoire, déchets, risques d’accident, …) dont nous ne parlons pas ici. Nous insistons donc comme nous l’avons déjà fait par le passé sur le fait que ces sources d’énergie ne sont pas neutres et que comme nous l’entendons assez souvent : « la meilleure énergie est celle que l’on ne consomme pas ».
</span>
<span class="mytext">
Sur le plan des émissions de GES liées au système électrique, la partie la plus importante est aujourd’hui le résultat de l’utilisation de combustibles fossile (gaz, charbon, pétrole) dans la phase de production d’énergie. Elle correspond donc à des émissions directement proportionnelles à l’énergie produite, que l’on pourrait appeler « émissions marginales » par analogie avec la partie économique. Si l’on fait la somme des émissions correspondantes on retrouve en ordre de grandeur ce qui est donné dans le document de la stratégie nationale bas carbone (SNBC) dont nous avons parlé en introduction du post sur le chauffage [[2](https://www.energy-alternatives.eu/2020/03/22/une-contribution-a-la-reflexion-sur-la-strategie-nationale-bas-carbone-dans-le-batiment-partie-1-quels-modes-de-chauffage-a-lhorizon-2050/)], à savoir environ 20 MtCO2eq/an associés au secteur de la production d’électricité, c’est ce que l’on peut voir dans la Table 1 ci-dessous.
</span>
<span class="mytext">
Dans le même esprit qu’avec l’analyse économique, on peut aussi tenir compte des émissions liées à la construction de la centrale ou à celles qui ne sont pas des « émissions marginales » mais sont liées à l’exploitation de la centrale. On parle alors d’une analyse en cycle de vie : une analyse qui tient compte des émissions du berceau à la tombe (de la construction au démantèlement de l’installation). Cette analyse se fait sur un périmètre qui doit être bien défini (par exemple ici nous ne tenons pas compte du réseau), mais alors elle n’est plus forcément compatible avec une analyse à la maille France comme celle de la SNBC puisqu’elle implique des émissions d’une autre année, dans d’autres secteurs et bien souvent également dans d’autres pays. S’il faut éviter d’oublier quelque chose (comme les émissions liées à une production à l’étranger) il faut également éviter de compter deux fois la même chose (comme la production d’acier pour produire l’armature d’un bâtiment qui servira à la production d’électricité mais qui relève de l’industrie de l’acier et est utilisée dans le secteur du bâtiment avant que le bâtiment soit utilisé pour la production d’électricité). Si l’on garde cette analyse en cycle de vie, les émissions du mix de production d’électricité peuvent être données par une formule très similaire à celle donnée pour le coût.
</span>

<span class="mytext">
$$ Emissions[MtCO_2/an]=\sum_i \alpha_i^{emissions} E_i + \beta_i^{emissions} P_i$$
</span>
<span class="mytext">
Cette formule implique une annualisation, contient des coûts fixes et des coûts variables. Des valeurs sont données dans la Table 1. A l’échelle du mix les coûts fixes sont beaucoup plus faibles que les « coûts variables » qui correspondent aux émissions lors de la combustion de gaz ou de charbon.
</span>
<style type="text/css">
	table.tableizer-table {
		font-size: 12px;
		border: 1px solid #CCC;
		font-family: Arial, Helvetica, sans-serif;
	}
	.tableizer-table td {
		padding: 4px;
		margin: 3px;
		border: 1px solid #CCC;
	}
	.tableizer-table th {
		background-color: #104E8B;
		color: #FFF;
		font-weight: bold;
	}
</style>

<table>
<thead><tr><th></th><th>&nbsp;</th><th>&nbsp;</th><th>Charbon</th><th>Gaz</th><th>Fioul</th><th>Old Nuke</th><th>Eolien</th><th>BioE</th><th>PV</th><th>Total</th></tr></thead><tbody>
 <tr><td>Système</td><td>P</td><td>Puissance installée [GW]</td><td>3</td><td>12</td><td>3</td><td>63</td><td>15,1</td><td>2</td><td>8,5</td><td>106,6</td></tr>
 <tr><td>&nbsp;</td><td>E</td><td>Production [TWh/an]</td><td>6</td><td>31,0</td><td>2,0</td><td>400,0</td><td>30,0</td><td>10,0</td><td>10,0</td><td>489,0</td></tr>
 <tr><td>&nbsp;</td><td>FC</td><td>Facteur de Charge [%]</td><td>22,83</td><td>29,49</td><td>7,61</td><td>72,48</td><td>22,68</td><td>57,08</td><td>13,43</td><td>&nbsp;</td></tr>
 <tr><td>Coût </td><td>beta</td><td>[€/kW/an]</td><td>110</td><td>90</td><td>60</td><td>200</td><td>150</td><td>110</td><td>350</td><td>&nbsp;</td></tr>
 <tr><td>&nbsp;</td><td>alpha</td><td>[€/MWh]</td><td>10</td><td>40</td><td>30</td><td>6</td><td>0</td><td>10</td><td>0</td><td>&nbsp;</td></tr>
 <tr><td>&nbsp;</td><td>Total</td><td>[€/MWh]</td><td>65</td><td>74,8</td><td>120,0</td><td>37,5</td><td>75,5</td><td>32,0</td><td>297,5</td><td>48,1</td></tr>
 <tr><td>&nbsp;</td><td>&nbsp;</td><td>[Milliards €/an]</td><td>0,4</td><td>2,3</td><td>0,2</td><td>15,0</td><td>2,3</td><td>0,3</td><td>3,0</td><td>23,5</td></tr>
 <tr><td>Emissions</td><td>beta</td><td>[gCO2eq/W/an]</td><td>30</td><td>25</td><td>30</td><td>50</td><td>20</td><td>25</td><td>50</td><td>&nbsp;</td></tr>
 <tr><td>&nbsp;</td><td>Marg</td><td>[MtCO2eq/an] marginal</td><td>5</td><td>16</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>24</td></tr>
 <tr><td>&nbsp;</td><td>alpha</td><td>[gCO2eq/kWh]</td><td>900</td><td>500</td><td>700</td><td>2</td><td>0</td><td>40</td><td>0</td><td>60</td></tr>
 <tr><td>&nbsp;</td><td>Total</td><td>[gCO2/kWh]</td><td>915</td><td>510</td><td>745</td><td>10</td><td>10</td><td>45</td><td>43</td><td>57</td></tr>
 <tr><td>&nbsp;</td><td>&nbsp;</td><td>[MtCO2eq/an]</td><td>5,5</td><td>15,8</td><td>1,5</td><td>4,0</td><td>0,3</td><td>0,5</td><td>0,4</td><td>27,9</td></tr>
</tbody></table>
{: .mbtablestyle .center .wrapstyle }

<span class="legendtext" id="CAPTable1" style="display:block;text-align:center">
**Table 1** -- Émissions de GES et coûts moyens (grossièrement approchés) associées aux grandes classes françaises. On retrouve approximativement le contenu carbone lié à la production d’électricité aujourd’hui en France. Données 2018. Attention ces émissions ne tiennent pas compte des impacts liés au réseau de transport et de distribution d’électricité et des importations. [Fichier Excel.](Fichier Excel.)
</span>
<span class="mytext">
Dans la perspective d’un mix électrique bas carbone, qui pourrait reposer sur des moyens comme le nucléaire, le biogaz, le PV, l’éolien, la part fixe des émissions serait prépondérante. Dans un tel contexte ou dans une démarche prospective visant la neutralité carbone, on comprend qu’il devient important de tenir compte du lieu de fabrication des moyens de production. Notons qu’ici aussi il faudrait pour être rigoureux, « actualiser » les émissions (tenir compte du fait que des émissions maintenant et des émissions dans dix ans n’ont pas le même impact sur le réchauffement à un horizon donné), mais l’effet est mineur et n’est à ma connaissance jamais pris en compte dans la littérature.
</span>

# Possibles futurs mix « bas carbones »
## Quelques enjeux autour de la SNBC pour le secteur de la production d’électricité

<span class="mytext">
Le gouvernement Français construit aujourd’hui une vision long terme de la transition énergétique à travers la stratégie nationale bas carbone (SNBC) qui vise la neutralité carbone en 2050. Cette neutralité passe par une réduction des émissions marginales de 20 MtCO2eq/an à 2 MtCO2eq/an. Les émissions du mix de production Français sont déjà faibles grâce au nucléaire et nous ne sommes pas si loin d’atteindre cet objectif. Il reste une difficulté.
</span>

<span class="mytext">
L’enjeu majeur en France est lié au vieillissement du parc nucléaire. En effet même s’il faut sans doute prolonger la durée de vie des centrales (ou éviter de fermer un peu trop vite comme on le fait avec Fessenheim) en investissant dans la rénovation, la majorité des centrales existantes seront très probablement fermées en 2050-2060. C’est qu’au vu du temps qu’il faut pour construire quelques GW, il serait très risqué d’avoir un mix entier de plus de 60 ans d’âge moyen. C’est « l’effet falaise » dont parle la SFEN [4] Figure 4. Dans sa réponse à la stratégie nationale bas carbone, sur le sujet de l’évolution du système électrique, le Shift Projet [0] rappelait récemment que « ce système est très inertiel et que le vieillissement du parc nucléaire va soulever la question de son remplacement d’ici 2050» . Ainsi, il s’agit de construire un nouveau mix électrique décarboné et on ne peut faire cela du jour au lendemain. Il n’est pas trop tôt de s’y atteler aujourd’hui. Il y a pour cela deux grandes alternatives, toutes deux délicates : construire des milliers d’éoliennes et de panneaux PV avec la puissance pilotable qui l’accompagne ou bien bâtir environ cinquante fois Flamanville. La réalité sera probablement quelque part au milieu de tout ça. Afin de quantifier le coût économique et en termes de GES de ces mix alternatifs, nous avons ici utilisé les précédentes équations, les résultats sont donnés dans la Table 2 qui est aussi disponible sous forme d’un fichier Excel dans lequel vous pourrez modifier les hypothèses à votre guise.
</span>

<span class="mytext">
Un autre enjeu est celui de l’utilisation du gaz. Il sera difficile de se passer complètement du peu de gaz restant dans le système électrique Français aujourd’hui, car même si les volumes en énergie sont très faibles comparés à ceux de la production nucléaire, la puissance installée correspondante est significative, et utile à couvrir une consommation comme la consommation de chauffage thermosensible dont nous avons déjà parlé [[2](https://www.energy-alternatives.eu/2020/03/22/une-contribution-a-la-reflexion-sur-la-strategie-nationale-bas-carbone-dans-le-batiment-partie-1-quels-modes-de-chauffage-a-lhorizon-2050/)]. L’utilisation du nucléaire pour des facteurs de charge très faibles impliquerait des coûts trop élevés. Une voie importante sur ce point est celle du biogaz dont nous avons déjà parlé. Il s’agit de petites quantités d’énergie (60TWh de gaz au maximum, donc autour de 30 TWh/an d’électricité en provenance du gaz) mais d’une puissance importante, surtout dans le cas d’un mix renouvelable. Le biogaz sera beaucoup plus cher que le gaz naturel, mais les émissions correspondantes, sont bien plus faibles (autour de 25 gCO2eq/kWh même si ce sujet mériterait des analyses bien plus poussées, voir post sur le chauffage [[2](https://www.energy-alternatives.eu/2020/03/22/une-contribution-a-la-reflexion-sur-la-strategie-nationale-bas-carbone-dans-le-batiment-partie-1-quels-modes-de-chauffage-a-lhorizon-2050/)]). Dans tous les cas on parle ici de volumes en énergie qui sont faibles et puisque le coût capacitaire du gaz est faible, cela impacte peu la facture énergétique.
</span>


<table>
<thead><tr><th></th><th>&nbsp;</th><th>&nbsp;</th><th>Future</th><th>Nuke</th><th>&nbsp;</th><th>&nbsp;</th><th>Future</th><th>EnR</th><th>&nbsp;</th><th>&nbsp;</th><th>&nbsp;</th><th>&nbsp;</th></tr></thead><tbody>
 <tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>EPR</td><td>Gaz</td><td>Hydro</td><td>Total</td><td>Gaz</td><td>Eolien</td><td>Hydro</td><td>PV</td><td>Bat.</td><td>Total</td></tr>
 <tr><td>Système</td><td>P</td><td>Puissance installée [GW]</td><td>63</td><td>6</td><td>25</td><td>94</td><td>35</td><td>170</td><td>25</td><td>90</td><td>10</td><td>330</td></tr>
 <tr><td>&nbsp;</td><td>E</td><td>Production [TWh/an]</td><td>400,0</td><td>15,0</td><td>68,0</td><td>483,0</td><td>30,0</td><td>300,0</td><td>68,0</td><td>95,0</td><td>X</td><td>493,0</td></tr>
 <tr><td>&nbsp;</td><td>FC</td><td>Facteur de Charge [%]</td><td>72,48</td><td>28,54</td><td>31,05</td><td>&nbsp;</td><td>9,78</td><td>20,15</td><td>31,05</td><td>12,05</td><td>X</td><td>&nbsp;</td></tr>
 <tr><td>Coût </td><td>beta</td><td>[€/kW/an]</td><td>500</td><td>90</td><td>110</td><td>&nbsp;</td><td>90</td><td>140</td><td>110</td><td>85</td><td>150</td><td>&nbsp;</td></tr>
 <tr><td>&nbsp;</td><td>alpha</td><td>[€/MWh]</td><td>6</td><td>100</td><td>0</td><td>&nbsp;</td><td>100</td><td>0</td><td>0</td><td>0</td><td>0</td><td>&nbsp;</td></tr>
 <tr><td>&nbsp;</td><td>Total</td><td>[€/MWh]</td><td>84,8</td><td>136,0</td><td>40,4</td><td>80,1</td><td>205,0</td><td>79,3</td><td>40,4</td><td>80,5</td><td>X</td><td>84,9</td></tr>
 <tr><td>&nbsp;</td><td>&nbsp;</td><td>[Milliards €/an]</td><td>33,9</td><td>2,0</td><td>2,8</td><td>38,7</td><td>6,2</td><td>23,8</td><td>2,8</td><td>7,7</td><td>1,5</td><td>41,9</td></tr>
 <tr><td>Emissions</td><td>beta</td><td>[gCO2eq/W/an]</td><td>50</td><td>25</td><td>20</td><td>&nbsp;</td><td>25</td><td>20</td><td>20</td><td>50</td><td>60</td><td>&nbsp;</td></tr>
 <tr><td>&nbsp;</td><td>Marg</td><td>[MtCO2eq/an] marginal</td><td>0,8</td><td>0,8</td><td>0,0</td><td>1,6</td><td>1,5</td><td>0,0</td><td>0,0</td><td>0,0</td><td>X</td><td>1,5</td></tr>
 <tr><td>&nbsp;</td><td>alpha</td><td>[gCO2eq/kWh]</td><td>2</td><td>50</td><td>0</td><td>11,08</td><td>50</td><td>0</td><td>0</td><td>0</td><td>0</td><td>23,88</td></tr>
 <tr><td>&nbsp;</td><td>Total</td><td>[gCO2/kWh]</td><td>10</td><td>60</td><td>7</td><td>11</td><td>79</td><td>11</td><td>7</td><td>47</td><td>X</td><td>24</td></tr>
 <tr><td>&nbsp;</td><td>&nbsp;</td><td>[MtCO2eq/an] </td><td>4,0</td><td>0,9</td><td>0,5</td><td>5,4</td><td>2,4</td><td>3,4</td><td>0,5</td><td>4,5</td><td>1,0</td><td>11,8</td></tr>
</tbody></table>
{: .wrapstyle  .simple7}

<span class="legendtext" id="CAPTable2" style="display:block;text-align:center">
**Table 2** -- Mix fortement nucléaire ou fortement renouvelable pour l’horizon 2050.  [Fichier Excel.](Fichier Excel.)
</span>

<span class="mytext">
On comprend en regardant ces mix qu’ils ont des coûts comparables. Les valeurs de alpha et beta seront discutées dans un post ultérieur ([ici](https://www.energy-alternatives.eu/2020/08/20/decomposition-lcoe.html)). Pour ce qui pourrait donner lieu aux discussions les plus importantes : le nucléaire est ici à moins de 85 €/MWh, c’est-à-dire moins que ce que coûtent des centrales comme Flamanville en France ou Hinckley Point [[5](https://www.zonebourse.com/ELECTRICITE-DE-FRANCE-4998/actualite/Electricite-de-France-le-cout-d-Hinkley-Point-C-en-hausse-de-29-en-3-ans-29251492/)] en Grande Bretagne qui sont des têtes de série, mais une valeur plus proche de celle que l’on obtiendrait en applicant les coûts d’investissement de la centrale de Taishan en Chine. Le PV et l’éolien apparaissent dans la Table 2 à des prix autour de 80 €/MWh, ce qui est moins que les projets construits dans les années 2010, mais beaucoup plus que certains projets qui se construisent aujourd’hui entre 50 et 60 €/MWh (voir [[6](https://www.cre.fr/Documents/Publications/Rapports-thematiques/Couts-et-rentabilites-du-grand-photovoltaique-en-metropole-continentale)] pour le PV, [[7](https://www.cre.fr/media/Fichiers/publications/appelsoffres/Eolien-Telecharger-le-rapport-de-synthese-version-publique-de-la-troisieme-periode-de-candidature)] pour l’éolien). La discussion pourrait être longue sur ce sujet épineux et très discuté et l’idée est seulement de montrer ici que l’on peut difficilement imaginer (sauf à vraiment tordre les chiffres) qu’il y ait une différence très importante entre les deux mix. Bien sûr, on pourra changer les hypothèses économiques, discuter l’équilibre offre-demande, pour faire gagner un système ou l’autre mais les incertitudes sur ce type d’horizon sont grandes, et en fin de compte les enjeux et difficultés ne sont pas seulement économiques et sont très nombreux, vis-à-vis du développement des EnR comme vis-à-vis du développement du nouveau nucléaire, nous en reparlerons.
</span>
<span class="mytext">
Il semble qu’à l’échelle de la terre (échelle à considérer in fine lorsqu’il s’agit de relever les défis imposés par le changement climatique), celles-ci peuvent prendre différentes formes. Dans beaucoup de cas les deux formes d’énergie peuvent jouer un rôle, qui dépendra sans doute beaucoup des régions, des pays. Nous ne pensons pas qu’il y ait matière ici à discréditer l’une ou l’autre des solutions. Sur le plan des émissions de GES pour le cas de la France les deux systèmes sont compatibles avec la SNBC avec des émissions « marginales » qui passent de 20 MtCO2eq/an à moins de 2 MtCO2eq/an dans les deux cas.
</span>

## Puissance pilotable du mix renouvelable

<span class="mytext">
Il n’est pas possible de comparer sur le plan économique ou environnemental, un moyen de production pilotable comme le nucléaire à un moyen de production intermittent comme le photovoltaïque ou l’éolien. En effet ces moyens ne fournissent pas des services équivalents. La méthodologie adaptée dans ce cas est de comparer un système nucléaire à un système renouvelable avec des moyens de backup suffisants (biogaz, stockage, hydraulique, …) i.e. qui permet d’assurer l’équilibre offre demande à n’importe quel instant et en tout point du réseau. C’est ce que l’on appelle le coût système et c’est ce que nous donnons ici dans la Table 2, même si c’est une version un peu simplifiée.
</span>
<span class="mytext">
Nous discuterons dans un autre post le caractère suffisant des moyens de backup proposés dans la Table 2 pour le mix renouvelable. Pour l’heure nous pouvons indiquer le calcul simple suivant : si l’on considère que 3% de la puissance éolienne installée à l’échelle du pays est disponible 100% du temps, cela fait (avec le gaz, l’hydraulique et le stockage batterie) 75 GW de puissance pilotable dans le mix renouvelable. Une analyse supplémentaire sera exposée pour montrer que cette puissance est suffisante, et que les 30 TWh/an d’électricité à partir de biogaz le sont également. Il faut comprendre que ces systèmes sont ici très simplifiés car il faudrait tenir compte des interconnexions avec les pays voisins, de la possibilité de gestion de la demande, le contrôle à la baisse de la production renouvelable (dont nous tenons compte en volume, en diminuant les facteurs de charge des renouvelables dans le Table 2) des variantes de chaque moyen de production, les interactions avec le réseau de gaz, avec des systèmes hydrogènes. Notons que le gestionnaire de transport d’électricité RTE prépare actuellement une étude sur ce sujet. Ce que nous donnons permet d’obtenir des ordres de grandeur concernant la production d’électricité mais ne vise certainement pas à définir un mix futur. La seule chose que nous voulons illustrer, c’est que le coût du système de production dépend beaucoup plus de l’énergie produite que de la puissance installée : le mix renouvelable a une puissance installée presque 4 fois plus grande que celle du mix nucléaire, mais des coûts comparables. Dans les deux cas les impacts GES marginaux sont réduits de manière satisfaisante (i.e. compatible avec la SNBC).
</span>

## Emissions de GES liées à la construction, l’entretien, …
<span class="mytext">
Il reste des émissions liées à la phase de construction de la centrale, ou de son démantèlement. Dans la SNBC ces émissions (et les valeurs de beta associées) doivent être réduites dans le secteur industriel, de la construction et le secteur des transports. Le secteur de la construction contient par exemple la production de béton, le secteur industriel contient l’extraction de minerais de fer, ou de cuivre et la production d’acier ou d’aluminium. Car ces matériaux sont très utilisés ici et produits avec des sources d’énergies très carbonées. Le secteur du transport concerne le transport des matières premières, des éléments et des personnes.
</span>
<span class="mytext">
Sur le périmètre de ces émissions « hors émissions marginales », il faut noter que bien que les deux systèmes (nucléaire/renouvelable+backup) soient compatibles avec la SNBC, le système nucléaire est deux fois moins carboné que le système renouvelable. Il y a plusieurs raisons à cela, mais une raison importante est la durée de vie des centrales prise pour les calculs (60 ans pour le nucléaire, alors que 20 ans seulement sont considérés pour les éoliennes et les panneaux PV). On peut penser que ces durées vont augmenter avec le temps, les centrales éoliennes arrivées au-delà de leurs 20 années de vie sont nombreuses aujourd’hui et les retours d’expérience, comme ceux qui permettent d’allonger la durée de vie initialement prévue des centrales nucléaires en place aujourd’hui, permettent des évolutions importantes. En outre les centrales sont souvent démantelées pour des raisons économiques qui ne seront plus valables dans quelques années : les nouvelles centrales sur le marché sont plus performantes et il vaut souvent mieux construire une nouvelle centrale pour obtenir de nouvelles subventions sur un site déjà acquis que de continuer à faire tourner une vieille centrale. Surtout, la question sous-jacente est celle de la décarbonation du secteur de l’industrie. Lorsque l’on regarde le secteur de l’électricité, cet enjeu ne semble pas très important car les émissions associées sont faibles comparées aux émissions actuelles, mais dans un futur décarboné, les calculs et les optimisations vis-à-vis de ces émissions seront, nous l’espérons, plus poussés.
</span>

# Conclusion
<span class="mytext">
Nous avons proposé des outils pour analyser simplement les mix de production d’électricité à partir des puissances installées et des énergies annuelles produites. Nous avons montré pourquoi l’énergie produite, plus que la puissance installée, est le facteur explicatif des émissions de GES et des coûts économiques.
</span>
<span class="mytext">
Nous avons rappelé qu’un enjeu important dans le contexte de la stratégie nationale bas carbone est le renouvellement du parc nucléaire Français à l’horizon 2050-2060. Nous avons donné des ordres de grandeur qui indiquent en quoi les systèmes caricaturaux « tout renouvelables » ou « tout nucléaire » ont des coûts comparables pour ce renouvellement et sont compatibles avec la stratégie nationale bas carbone. En fin de compte les enjeux ne sont pas seulement économiques, et sont très nombreux vis-à-vis du développement des EnR comme vis à vis du développement du nouveau nucléaire, nous en reparlerons. Il semble qu’à l’échelle de la Terre (échelle à considérer in fine lorsqu’il s’agit de changement climatique), les problèmes posés par ces deux options peuvent prendre différentes formes. Dans beaucoup de cas les deux formes d’énergie (nucléaire/renouvelable) peuvent jouer un rôle, qui dépendra sans doute beaucoup des régions, des pays. Nous ne pensons pas qu’il y ai matière dans ce texte à discréditer l’une ou l’autre des solutions. Il est à noter que les affrontements sur sujet ne laissent pas augurer d’une transition simple du système Français à l’horizon 2050. Pour l’heure l’acceptabilité est une difficulté importante, d’un côté comme de l’autre en France, alors l’important est de ne surtout pas croire que l’électricité est une ressource infinie et parfaitement propre ou simple à déployer.
</span>
<span class="mytext">
Sur le plan des émissions de GES pour le cas de la France les deux systèmes sont compatibles avec la SNBC avec des émissions « marginales » qui passent de 20 MtCO2eq/an à moins de 2 MtCO2eq/an dans les deux cas.
</span>

<span class="mytext">
Lorsque l’on regarde les émissions liées au secteur de la production d’électricité, la partie de ces émissions liée à la phase de construction de la centrale, ou du démantèlement, ne semblent pas être un enjeu majeur, car elles sont faibles comparées aux émissions actuelles du secteur de l’électricité. Pour le système nucléaire les émissions correspondantes, ramenées à l’énergie produite, sont moins importantes que pour le système renouvelable.
</span>
<span class="mytext">
Mais dans un futur moins carboné, les calculs et les optimisations vis-à-vis de ces émissions seront, nous l’espérons, plus poussés. Dans cette perspective, la prise en compte des émissions liées aux secteurs de l’industrie et du transport, sur lesquels repose la construction des moyens de production d’électricité, va devenir de plus en plus importante. Concernant l’industrie, on pense ici à la production de métaux, de béton, à l’extraction de matières premières. On peut donc imaginer qu’un jour, être compatible avec la stratégie nationale bas carbone impliquera une certaine provenance des matériaux utilisés pour la construction, minimisant les émissions associées.
</span>
<span class="mytext">
Dans ce post nous avons évoqué plusieurs sujets qui feront l’objet de posts futurs : l’évolution du système électrique, les sous-classes de moyens de production (qui se cachent derrière les grandes classes utilisées ici), la variabilité de la production EnR et les moyens de la gérer, les impacts environnementaux autres que le changement climatique, le calcul de coûts annualisés (et la fameuse actualisation), la gestion de la demande, la SNBC dans le transport et l’industrie, …
</span>

# Bibliographie

[0] [Réponse du shift projet à la SNBC ](https://www.entsoe.eu/data/)

[1] [ENTSOE Transparency Platform](https://www.entsoe.eu/data/)

[2] [Une contribution à la réflexion sur la stratégie nationale bas carbone dans le bâtiment — Partie 1 : Quels modes de chauffage à l’horizon 2050. Posté sur ce site en Mars 2020.](https://www.energy-alternatives.eu/2020/03/22/une-contribution-a-la-reflexion-sur-la-strategie-nationale-bas-carbone-dans-le-batiment-partie-1-quels-modes-de-chauffage-a-lhorizon-2050/)

[3] [Chiffres clés des énergies renouvelables](https://www.energy-alternatives.eu/2020/05/07/mix-de-production-delectricite-energie-et-puissance/%C2%AB%20les%20chiffres%20cle%CC%81%20des%20e%CC%81nergies%20renouvelable%202019%20%C2%BB) – Edition 2019. Graphique p11

[4] [Revue générale du nucléaire](https://www.sfen.org/rgn/rte-alerte-securite-approvisionnement-france), Figure 4. Novembre 2019.  

[5] [Tarif obtenu pour Hinckley Point en Grande Bretagne](https://www.zonebourse.com/ELECTRICITE-DE-FRANCE-4998/actualite/Electricite-de-France-le-cout-d-Hinkley-Point-C-en-hausse-de-29-en-3-ans-29251492/) 2019.

[6] [Coûts et rentabilités du grand photovoltaïque en métropole continentale.](https://www.cre.fr/Documents/Publications/Rapports-thematiques/Couts-et-rentabilites-du-grand-photovoltaique-en-metropole-continentale) Etude de la CRE février 2019 sur les réponses aux appels d’offre.

[7] [Résultat des appels d’offre du 3eme trimestre 2019 pour l’éolien en France](https://www.cre.fr/media/Fichiers/publications/appelsoffres/Eolien-Telecharger-le-rapport-de-synthese-version-publique-de-la-troisieme-periode-de-candidature) (CRE).
