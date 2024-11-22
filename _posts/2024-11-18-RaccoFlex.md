---
title: Valorisation technico-économique de la flexibilité de la production photovoltaïque dans les réseaux de distribution en France.   
key: photovoltaïque
tags: réseau de distribution d'électricité, coût renforcement, valeur de la flexibilité, photovoltaïque, transition, énergies renouvelables,
article_header:
  type: cover
  image:
    src: /assets/images/Posts/2024-11-18/Scenarios_PV_large.png
---

<span class="summary" style="display:block; text-align: justify">
Résumé -- Ce post présente une synthèse des résultats d'un projet qui a été mené par Yassine Abdelouadoud et coordonné par moi-même au centre PERSEE de MINES Paris PSL. Dans ce projet nous avons mis en place une méthode permettant d'évaluer les coûts de renforcement du réseau de distribution d'électricité pour l'intégration de centrales photovoltaïques (en basse tension et en HTA). Cette méthode combine deux types de modélisation. La première est une modélisation à la pointe qui permet d'estimer les besoins de renforcement liés à l'intégration du PV. La deuxième est une modélisation dynamique qui permet de calculer l'énergie qui sera effectivement écrêtée en cas d'utilisation de la flexibilité. Afin de limiter les besoins de calcul, cette approche est appliquée à une sélection de 150 départs HTA dont la représentativité a été validée. Cette méthode a été appliquée à différents niveaux de pénétration renouvelable (voir Figure ci-dessus), pour différentes combinaisons de types de centrales (grandes centrales au sol, grandes toitures, petites toiture), et avec ou sans l'utilisation de flexibilité. Ce projet a été financé par France Relance et par Roseau Technologies. Le rapport final sera publié prochainement.
Quelques points importants des résultats :
</span>
<!--more-->
- le coût pour des scénarios à 150 GWc reste en dessous de 150€/kW, c'est plus cher qu'aujourd'hui mais pour des grandes centrales au sol le coût total des projets est autour de 800 €/kW.
- La flexibilité est importante, elle permet de diviser les coûts par deux si l'on vise plus de 100 GWc
- Le coût dépend de ce que l'on installe et de où on installe les centrales. Avoir plus de grandes centrales au sol permet de limiter les coûts de renforcement contrairement à ce qu'on entend souvent.
- Monter à 250 GWc pourrait impliquer des coûts plus importants, mais nous pensons que des analyses complémentaires avec d'autres mix devraient être faites.



<span class="text" id="Figure1" style="display:block;text-align:center">
![Image]({{site.baseurl}}/assets/images/Posts/2024-11-18/cost_by_power_with_flexibility.png){:.border}
</span>

<span class="legendtext" id="CAPFigure1" style="display:block;text-align:center">
**Figure 1** --   Coûts unitaires obtenus en fonction des différents scénarios avec et sans flexibilité
</span>


## Généralités et contexte  

<span class="mytext">
Le développement du PV induit souvent des besoins de renforcement des réseaux électriques. Nous avons réalisé une étude au laboratoire PERSEE qui porte spécifiquement sur les installations PV raccordées au réseau de distribution (par opposition au réseau de transport) et sur les besoins de renforcement de ce réseau.
 </span>

<span class="mytext">
Les coûts associés à ces renforcements de réseau sont extrêmement élevés dans les scénarios de fort développement PV : [selon Enedis](https://www.enedis.fr/sites/default/files/documents/pdf/enedis-dossier-prospective-2050.pdf), dans le scénario “rupture” de l’étude “Futurs Énergétiques 2050” de RTE, il faudrait prévoir 6 à 8 MM€/an uniquement pour le raccordement des nouvelles installations PV au réseau exploité par Enedis. A titre de comparaison, Enedis investit actuellement ~4 MM€/an au total (tous besoins confondus) dans la modernisation, l’entretien et le développement du réseau de distribution d’électricité qu’il exploite en France. Il y a donc un enjeu majeur à maîtriser les investissements dans le réseau de distribution d’électricité qui seront rendus nécessaire par le développement de la production photovoltaïque.
</span>

<span class="mytext">
La flexibilité de la production photovoltaïque est fréquemment présentée comme une solution potentielle pour limiter ou différer ces investissements dans les infrastructures de distribution lorsque l’on y raccorde massivement des installations de production photovoltaïque. Les bénéfices que cette solution est susceptible d’apporter ont déjà été mis en évidence par différents moyens : études par simulation, démonstrateurs, et mises en œuvre en conditions réelles (cf rapport de la CRE “[évaluation de la performance des gestionnaires de réseaux sur le développement d'un réseau électrique intelligent](https://www.cre.fr/actualites/toute-lactualite/la-cre-publie-son-rapport-d-evaluation-de-la-performance-des-gestionnaires-de-reseaux-sur-le-developpement-d-un-reseau-electrique-intelligent.html)”). Il existe cependant aujourd’hui trop peu d’éléments objectifs, reposant sur une méthodologie ouverte et dont les résultats sont extrapolables à l’échelle nationale, permettant de répondre aux questions suivantes : serait-il pertinent, en France et dans les deux décennies à venir, de recourir massivement à la flexibilité de la production photovoltaïque (HTA et BT) pour limiter ou différer les investissements dans le réseau de distribution d’électricité ? De façon quantitative, quels coûts et quels bénéfices résulteraient d’une telle évolution ? Quelle part des 6 à 8 MM€/an d’investissements évalués par Enedis dans le scénario Rupture, notamment, pourrait être évitée ?
</span>

<span class="mytext">
Faute de tels éléments, l’incertitude domine, il n’émerge pas de consensus entre les différentes parties prenantes (Producteurs, Collectivités Concédantes, Gestionnaires de Réseau, Régulateur national, différents services de l’Etat…), et la flexibilité de la production photovoltaïque reste pratiquement inexploitée en France (3 PTF émises et acceptées en 2022 par Enedis, cf [rapport CRE](https://www.cre.fr/actualites/toute-lactualite/la-cre-publie-son-rapport-d-evaluation-de-la-performance-des-gestionnaires-de-reseaux-sur-le-developpement-d-un-reseau-electrique-intelligent.html), et aucune exploitation de la flexibilité pour éviter des contraintes dans les réseaux Basse Tension).
</span>

<span class="mytext">
Le travail réalisé au centre PERSEE visait à évaluer la pertinence technico-économique de cette solution à l’échelle de la France, et sur le même horizon de temps que les scénarios RTE (2050), afin de contribuer à dissiper les incertitudes qui entravent la prise de décision quant au rôle à donner à la flexibilité de la production photovoltaïque dans le réseau de distribution d’électricité français.
</span>

## Méthodologie

<span class="mytext">
On définit différents scénarios détaillés de déploiement du photovoltaïque en se basant sur une approche bottom-up qui tient compte des contraintes de mise en œuvre (toitures et terrains disponibles). Deux séries de scénarios sont sélectionnés : une qui permet d’évaluer l’impact des niveaux de pénétration envisagés par RTE dans l’étude “Futurs énergétiques 2050” et une qui permet de mesurer la sensibilité au type de centrale déployé (toiture résidentielles, industrielles et centrales au sol).
</span>

<span class="mytext">
On simule année après année l’impact de ce déploiement sur le réseau de distribution d’électricité, avec et sans recours à la flexibilité, et on détecte l’apparition de contraintes de tension, d’intensité dans les lignes et de puissance dans les transformateurs HTA/BT. Le cas échéant, on renforce progressivement le réseau jusqu’à ce que les contraintes disparaissent. Lorsque l’on recourt à la flexibilité de la production photovoltaïque, l’injection d’une installation de production n’est jamais limitée à une valeur inférieure à 70% de sa puissance nominale.
</span>

<span class="mytext">
On compare les coûts avec et sans recours à la flexibilité. En l’absence de flexibilité, on évalue les coûts d’investissement seuls, en se basant sur un modèle de coût unitaire qui dépend de l’opération à réaliser, du niveau de tension et du caractère urbain ou rural de la zone desservie. En présence de flexibilité, on évalue en outre la valorisation de l’énergie non-injectée par les installations de production en modélisant l’écoulement des flux dans le réseau heure par heure pour chaque année étudiée dans la simulation.
</span>


## Principaux résultats obtenus qui ne sont pas liés directement au sujet de la flexibilité  

<span class="mytext">
Avec ou sans recours à la flexibilité, la profondeur du réservoir de projets dont on dispose pour atteindre une certaine puissance-cible totale influence considérablement le montant à investir dans le réseau : les coûts unitaires (€/W) moyens de raccordement sont en effet extrêmement différents selon que l’on dispose d’un réservoir important de projets PV, et que l’on atteint la puissance-cible en ne réalisant que ceux pour lesquels le raccordement au réseau est favorable ; ou que l’on ne dispose pas d’un tel réservoir et que l’on doit, pour atteindre la puissance-cible, réaliser tous les projets PV dont on dispose, y compris ceux pour lesquels le raccordement au réseau est défavorable. Pour le scénario “rupture”, par exemple, renoncer à installer 15% du potentiel PV (17 GW) permettrait d’économiser 49% des coûts de renforcement (coût total de 42 MM€ pour 99GW, soit 0.42 €/W au lieu de 0.70€/W en raccordant la totalité des 116 GW du scénario “rupture”) tandis que renoncer à 34 % (39 GW) du potentiel PV permettrait d’économiser 79% des coûts (coût total de 17 MM€ pour 77GW, soit 0.22 €/W). **L’existence d’un vaste réservoir de projets PV, dépassant amplement la puissance-cible, est donc cruciale pour limiter les coûts d’investissement dans le réseau.**
</span>

<span class="mytext">
Dans tous les cas (avec ou sans recours à la flexibilité, et que l’on dispose ou non d’un vaste réservoir de projets PV), **les coûts unitaires (c’est-à-dire en €/W) de renforcement de réseau augmentent fortement dans les scénarios 3 (“expansion modérée”) et 4 (“rupture”) par rapport aux scénarios 1 ("continuité"") et 2 ("expansion limitée").**
</span>

<span class="mytext">
Le type d’installation de production (résidentiel, grande toiture ou centrale au sol) influence fortement la nature des renforcements à effectuer : impact majeur sur le réseau BT pour les scénarios avec fort développement du PV résidentiel ; impact majeur sur les postes HTA/BT pour les scénarios avec fort développement du PV sur grandes toitures ; et impact majeur sur le réseau HTA pour les scénarios avec fort développement des centrales au sol. De façon remarquable néanmoins, pour la capacité PV raccordée de l’ordre de 50 GW sur laquelle cette comparaison a été effectuée, on obtient des coûts totaux assez proches pour ces trajectoires de renforcement pourtant très différentes. **A puissance égale, les coûts d’investissement dans le réseau sont peu dépendants de la typologie d’installations photovoltaïques (résidentiel, grande toiture ou centrale au sol).**
</span>

## Principaux résultats obtenus sur le sujet spécifique de la flexibilité

<span class="mytext">
**La flexibilité de la production permet des gains d’investissement substantiels dans tous les cas étudiés**, c’est-à-dire quel que soit le scénario de déploiement étudié, et que l’on dispose ou non d’un vaste réservoir de projets PV. En ordre de grandeur, **la flexibilité permet de réduire d’au moins 30% et parfois de plus de 60%, les coûts de renforcement au prix d’un effacement de l’ordre de 1% du productible photovoltaïque**.
</span>

<span class="mytext">
Dans les scénarios à forte croissance de la capacité photovoltaïque, les ordres de grandeur de gain sont considérables ; la flexibilité de la production permet par exemple à **une économie de renforcement d’environ 11 MM€ (6 MM€ au lieu de 17 MM€ soit une réduction de coût de 65%) dans le scénario “rupture” et en supposant que l’on dispose d’un réservoir de projets suffisant pour que seuls ceux dont le coût de raccordement est inférieur à 0.8 €/W soient réalisés**. Cette hypothèse écarte 39 GW (33%) des 116 GW de capacité PV que l’on raccorderait au total, dans le scénario “rupture”, si l’on ne mettait pas de limite haute au coût de raccordement unitaire.
</span>

<span class="mytext">
**Les contraintes de tension (par opposition aux contraintes d’intensité), en HTA et en BT, constituent la très grande majorité des causes de renforcement ou création d’infrastructure.** Or les contraintes de tension sont justement celles pour lesquelles la mise en œuvre opérationnelle de la flexibilité est la plus facile, via un simple pilotage local de l’onduleur. **Il est donc possible de capter la majeure partie de la valeur de la flexibilité de la production photovoltaïque sans, a priori, grande difficulté de mise en œuvre.**
</span>

<span class="mytext">
**Dans tous les scénarios étudiés, la flexibilité apporte des bénéfices nets**, c'est-à-dire que les évitements d’investissements dans le réseau ont une valeur supérieure à l’énergie non injectée. **Ces bénéfices nets augmentent fortement avec le niveau de pénétration du PV.**
</span>

<span class="mytext">
**La mise en œuvre de la flexibilité est particulièrement favorable dans le cas des installations sur toitures résidentielles** (par opposition aux grandes toitures et aux centrales au sol). Ceci est dû à la fois à des évitements d’investissement plus importants (13 MM€ pour le scénario “résidentiel”, 7.8 MM€ pour le scénario “centrales au sol”, ces deux scénarios visant une même puissance-cible d’environ 50 GW) et une énergie écrêtée plus faibles (0.39% contre 1.53%) du fait d’une proximité plus grande avec la consommation.
</span>
<span class="mytext">
Les résultats techniques de l'étude et la description complète de la méthodologie seront publiés ultérieurement.
</span>

<span class="text" id="Figure2" style="display:block;text-align:center">
![Image]({{site.baseurl}}/assets/images/Posts/2024-11-18/repartition_infrastructures.png){:.border}
</span>

<span class="text" id="Figure2" style="display:block;text-align:center">
![Image]({{site.baseurl}}/assets/images/Posts/2024-11-18/logo_france_relance.png){:.border}
</span>
