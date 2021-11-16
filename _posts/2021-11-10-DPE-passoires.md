---
title: Sur le nombre de passoires énergétiques en France
key: DPE
tags: bâtiment rénovation DPE transition évolution passoires énergétiques
article_header:
  type: cover
  image:
    src: /assets/images/Posts/2021-11-15/DPE_image.png
---

<span class="summary" style="display:block; text-align: justify">
*Résumé -- Dans cet article, co-écrit avec Yassine Abdelouadoud, nous discutons le rôle du diagnostic de performance énergétique  (DPE) dans la transition énergétique et en particulier des estimations qu'il a permis du nombre de passoires énergétiques. Nous cherchons à expliquer l'origine les différences entre deux estimations faites par le gouvernement : celle de 2013 (8,8 millions) et celle de 2020 (4,8 millions). Une partie de cette différence s'explique par la dynamique du parc (destructions/rénovations), mais nous montrons que c'est surtout un ensemble de défauts dans la base DPE utilisée en 2020 qui cause cette différence et nous proposons une méthode pour corriger ces défauts qui aboutit à une estimation de 7 millions de passoires. Nous discutons de l'importance de ces chiffrages vis à vis de nos objectifs de moyen et long terme dans le contexte de la transition énergétique.*
</span>
<!--more-->

# Le DPE, un outil clé de la politique énergétique.
<span class="mytext">
Dans le secteur du bâtiment, la transition vers la neutralité carbone passera par la rénovation de bâtiments autant que par l’évolution des modes de chauffage. D’après la seconde version de la SNBC [[SNBC2](https://www.ecologie.gouv.fr/sites/default/files/2020-03-25_MTES_SNBC2.pdf)]: “dans le secteur du résidentiel, le rythme de rénovation atteint environ 370 000 rénovations complètes équivalentes en moyenne sur la période 2015-2030 puis augmente pour atteindre environ 700 000 rénovations complètes équivalentes en moyenne sur la période 2030-2050.”
</span>

<span class="mytext">
Cette stratégie sera mise à jour prochainement, mais l’on peut déjà noter que l’ambition affichée est grande et que sa mise en œuvre sera complexe. Complexe parce que le nombre de bâtiments est grand, complexe parce qu’il est difficile de standardiser la rénovation, complexe parce que le parc de bâtiment est très hétérogène en termes de performances, et en termes de typologie, difficile parce que cela va toucher à l’espace privatif des français. Il est donc important d’avancer avec un instrument qui permette de mesurer l’état du parc à tout moment et de fixer des objectifs de long terme ainsi qu’une trajectoire réaliste et contrôlable pour les atteindre. De communiquer sur des objectifs clairs et connus de tous longtemps à l’avance.
</span>

<span class="mytext">
Cet instrument existe déjà en partie : c’est le diagnostic de performance énergétique (DPE) qui permet d’affecter à un logement donné une estimation du besoin de chauffage, des consommations énergétiques pour l’eau chaude sanitaire et la cuisson. Dans sa forme la plus synthétique, il se résume à une étiquette entre A et G qui permet en outre de donner une définition claire à ce qu’est une “passoire énergétique” : un bâtiment avec une étiquette F ou G. Ces étiquettes permettent de définir des politiques énergétiques. A court terme la loi resilience climat [[LoiResilienceClimat-juillet2021](https://www.ecologie.gouv.fr/loi-climat-resilience)] va imposer le gel des loyers des passoires énergétiques dès 2023, et l’Interdiction de mettre en location les logements mal isolés : les étiquettes G à compter de 2025, les F en 2028 et les E en 2034. Avec le temps, le DPE va donc jouer le rôle d’un contrôle technique pour les performances énergétique d’un bâtiment.
</span>

<span class="mytext">
Ce diagnostic peut être vu comme un outil permettant de sonder un bâtiment du parc. Comme le DPE est obligatoire aujourd’hui lors de la mise en location ou de la vente d’un bâtiment, il est de fait une méthode d’observation appliquée à grande échelle qui permet de se faire une idée des performances de l’ensemble du parc. D’autant que l’intégralité des données obtenues dans ces DPE, qui sont nombreuses pour chaque bâtiment, sont mises à disposition en open data [[baseDPE2021](https://data.ademe.fr/datasets/dpe-france)].
</span>

<span class="mytext">
Notons à ce stade que le DPE combine des mesures simples sur site, quelques valeurs par défaut (plus ou moins selon les pratiques des diagnostiqueurs), et l’utilisation d’un modèle le “3CL”. Il permet d’estimer une consommation conventionnelle reflétant la performance du bâti dans un climat moyen associé à sa localisation. Elle ne peut être confondue avec la consommation réelle qui reflète en plus la manière dont le bâti est occupé et la variabilité du climat d’une année sur l’autre. En outre, ces consommation réelles peuvent assez largement dépendre, surtout pour des bâtiments peu performants, des conditions d’utilisation (taux d’occupation du bâtiment, température de consigne pour le chauffage, aération,...) et l’outil DPE n’est pas fait pour quantifier l’attitude des consommateurs en situation de précarité énergétique.
</span>

# Méthodes existantes pour l’évaluation du nombre de passoires énergétiques et défauts du DPE

<span class="mytext">
Deux estimations de la performance du parc français dans son ensemble ont été publiées par les services statistiques du CGDD à partir d’un ensemble de DPE. La première [[SDES2012](https://www.statistiques.developpement-durable.gouv.fr/logements-en-france-metropolitaine-en-2012-plus-de-la-moitie-des-residences-principales-ont-une)] a été réalisée en 2013 sur le parc de 2012 à partir de 2400 DPE réalisés par Bureau Veritas dans le cadre de l’enquête Phébus [[Phebus](https://www.statistiques.developpement-durable.gouv.fr/enquete-performance-de-lhabitat-equipements-besoins-et-usages-de-lenergie-phebus)]. La seconde a été réalisée en 2020 [[SDES-Sept2020](https://www.statistiques.developpement-durable.gouv.fr/le-parc-de-logements-par-classe-de-consommation-energetique)] à partir d’un échantillon des DPE réalisés dans le cadre de l’obligation légale pour les logements construits après 1948 [[baseDPE2021](https://data.ademe.fr/datasets/dpe-france)] et sur le modèle Enerter de Energie Demain pour les autres bâtiments plus anciens.
</span>

<span class="mytext">
Dans tous ces cas, pour obtenir un nombre de bâtiments dans chaque classe énergétique à l’échelle de la France, il est nécessaire d’effectuer un redressement statistique de la base DPE avec une description exhaustive ou représentative du parc adossée à des variables présentes dans le DPE : le type et l’âge du bâtiment ainsi que la zone climatique dans laquelle il se trouve. En effet, les DPE ne sont pas issus d’un plan d’échantillonnage qui permette de déduire directement la distribution des performances de l’ensemble des bâtiments de France, et par exemple, les bâtiments neufs sont sur-représentés car depuis 2012 le DPE est obligatoire à la construction. Dans la première méthode, le redressement statistique a été effectué avec le recensement de la population de 2011 [[RecensementINSEE](https://www.insee.fr/fr/information/2008354)], dans la seconde, il a été effectué avec Fidéli [[Fidéli2021](https://www.insee.fr/fr/metadonnees/source/serie/s1019)].
</span>

<span class="mytext">
Ces deux méthodologies ont abouti à des écarts significatifs dans l’estimation du nombre de passoires énergétiques : 8.8 millions et 4.9 millions respectivement. Ces différence peuvent avoir plusieurs origines :
la dynamique du parc (rénovation/destruction) entre les deux périodes analysées : (2011-2012) pour la première et (2016-2018) pour la seconde. Cela pourrait expliquer guère plus qu’une différence de l’ordre de 1 000 000 de passoires.
la différence entre le recensement utilisé dans le 1er cas et la base Fidéli dans le 2nd cas pour inférer les performances à l’échelle du parc à partir de l’échantillon retenu. Ici on peut expliquer une différence d’environ 500 000 passoires.
Utilisation de deux campagnes de DPE faite dans des conditions et avec des objectifs différents. Nous allons montrer que la plus grosse différence vient de là.
</span>


<span class="mytext">
Les détails techniques qui soutiennent nos affirmations pour les quantifications des points 1, 2 sont donnés en Annexe. Nous allons donc donner plus de détails sur le quatrième point : la différence entre les 2400 DPE de l'enquête Phebus utilisés dans l’évaluation de 2013 et les DPE réalisés dans le cadre de l’obligation réglementaire, utilisés dans l’étude de 2020. Les premiers ont été produits de manière homogène par un seul organisme (bureau Veritas) qui était payé pour prendre le temps de bien faire le travail en évitant par exemple d’utiliser trop de valeurs par défaut. Le commanditaire (l’état) n’avait pour sa part pas d’intérêt à obtenir une classe énergétique reflétant un logement performant. A l’inverse, les DPEs de la base utilisée dans l’étude de 2020 sont beaucoup plus nombreux mais ont été commandés par les particuliers, qui ont intérêt à ce que la classe énergétique soit celle d’un logement performant. Ils ont été réalisés par un grand nombre de bureaux d’études dont certains ont pu vouloir gagner du temps dans la réalisation en utilisant des valeurs par défaut voir satisfaire le client en ajustant les observations faites sur le terrain. La distribution des performances issues de cette seconde base de DPE est représentée Figure 1. Elle ne permet pas de mesurer l’ensemble des déformations induites par les problèmes que nous venons d’évoquer, mais elle reflète clairement le fait qu’un nombre significatif de tricheurs ont eu des scrupules et ont voulu positionner le résultat du DPE parmi les moins performants de la classe. On peut noter que l’utilisation qu’on pu faire les diagnostiqueurs  de valeurs par défaut ont certainement causé aussi des sous-estimations des performances en particulier pour les bâtiments récents.
</span>

<span class="text" id="Figure1" style="display:block;text-align:center">
![Image]({{site.baseurl}}/assets/images/Posts/2021-11-15/DPE_sans_corrections.png){:.border}
</span>

<span class="legendtext" id="CAPTable1" style="display:block;text-align:center">
**Figure 1** --  Distribution des consommations d’énergie simulées pour l’échantillon de 5,2 millions de DPE présents dans la base [[baseDPE2021](https://data.ademe.fr/datasets/dpe-france)] utilisée dans l’étude de 2020 [[SDES-Sept2020](https://www.statistiques.developpement-durable.gouv.fr/le-parc-de-logements-par-classe-de-consommation-energetique)].
</span>



<span class="mytext">
Il y a un autre élément de fond sur lequel les deux campagnes divergent significativement, c’est le traitement des bâtiments construits avant 1948. Même si celui-ci n’est pas à l’origine d’une différence dans les résultats entre les deux études (voir table section suivante), il est utile de le mentionner ici. Jusqu’à juillet dernier, date à laquelle la méthode DPE a été changée, les bâtiments construits avant 1948 faisaient l’objet d’un DPE reposant sur l’analyse des factures d’énergie en lieu et place de l'application de la méthode 3CL. Cette méthode dite “facture”, ne mesurait pas la consommation conventionnelle et, dans le cas de passoires énergétiques occupées par des personnes n’ayant pas les moyens de payer des consommations élevées, ces DPE facture sur-estimaient largement les performances des bâtiments. En outre, un certain nombre de bâtiments avec des âges proches de 1948 ont vraisemblablement triché sur la date, pour pouvoir faire un DPE facture. C’est pour cela que le SDES a fait appel au modèle Enerter de l’entreprise Energie Demain. Les descriptions de ce modèle mettent en évidence une prise en compte du phénomène de précarité énergétique évoqué précédemment. Par ailleurs, nous observons que les résultats de ce modèle sur les bâtiments construits avant 48 sont en cohérence avec les données issues de l’enquête Phébus (voir table section suivante).
</span>

<span class="mytext">
Nous ne préconisons pas un retour à la base Phebus qui est trop ancienne et de trop petite taille pour bien caractériser la queue de la distribution des performances dans le parc bâti français. Une mise à jour et un enrichissement régulier de Phebus pourrait être une piste finalement peu coûteuse au regard des sommes qu’il va falloir engager dans cette transition, mais nous pensons qu’il est possible de reprendre la méthode [[SDES-Sept2020](https://www.statistiques.developpement-durable.gouv.fr/le-parc-de-logements-par-classe-de-consommation-energetique)] en corrigeant les problèmes intrinsèques aux DPE réalisés dans le cadre de l’obligation légale.
</span>

#  Notre correction de la base DPE

<span class="mytext">
Nous avons proposé une méthode pour corriger les défauts mentionnés dans la section précédente présents dans la base des DPE utilisée dans l’étude de 2020.  Rappelons que l’analyse du [[SDES-Sept2020](https://www.statistiques.developpement-durable.gouv.fr/le-parc-de-logements-par-classe-de-consommation-energetique)] repose sur l’utilisation de Fidéli, et nous avons de notre côté utilisé le recensement de l’INSEE qui est plus facile à obtenir. La différence entre ces deux bases est discutée en annexe.
</span>

<span class="mytext">
Nous ne sommes pas capables pour l’instant de détecter une fraude ou un abus d’utilisation de valeurs par défaut sur un DPE en particulier, mais nous pouvons corriger la distribution des performances énergétiques, afin de faire disparaître les pics et de combler les creux observables dans les sauts de classe à partir du passage à la classe D. Plus généralement, nous avons mis en place une méthode qui permet de corriger la distribution des performances. Cette correction est effectuée tranche d’âge par tranche d’âge. La distribution obtenue et agrégée sur tous les DPE est donnée par la figure suivante. Nous publierons prochainement un rapport complet de description de la méthodologie, et pour en savoir plus, vous pouvez contacter directement [Yassine Abdelouadoud](mailto:yassine@abckpi.com) (yassine@abckpi.com) qui a implémenté la méthodologie et qui réalise l'étude détaillée.
</span>


<span class="text" id="Figure1" style="display:block;text-align:center">
![Image]({{site.baseurl}}/assets/images/Posts/2021-11-15/DPE_corrige.png){:.border}
</span>

<span class="legendtext" id="CAPTable1" style="display:block;text-align:center">
**Figure 2** --  Distribution de l’ensemble des DPE de [[baseDPE2021](https://data.ademe.fr/datasets/dpe-france)]  après correction des défauts.
</span>

|      |Correction défauts |Corrections factures | <1918 | [1919,1945] | [1946,1970] | [1971,1990] | [1991,2005] | >2006 |
|:----------|:---------------|:---------------|:-----------|:------------|:------------|:------------|:------------|:------------|
|DPE "brut"        |        |                | 18.68      | 18.77        | 18.67     | 12.49         |3.58         | 1.03|
|SDES 2020          |       |      X          | 42.4      | 35.8       | 16.8     | 12.6         |3.8        | 1.16|
|notre correction  |    X    |     X           | 41.45      | 40.96       | 35.72     | 24.18        |5.6        | 1.33|
{: .mbtablestyle .wrapstyle .simple7}
<span class="legendtext" id="CAPTable1" style="display:block;text-align:center">
**Table 1** --  Taux de passoires énergétiques (classes F et G) par tranche d’âge dans la base  [[baseDPE2021](https://data.ademe.fr/datasets/dpe-france)] selon le type de corrections appliquées. La correction des fraudes a un impact essentiel.
</span>

<span class="mytext">
**Avec cette méthode de correction de la base DPE [[baseDPE2021](https://data.ademe.fr/datasets/dpe-france)], nous avons obtenu environ 7 millions de passoires énergétiques.**
</span>

# Sur le nouveau DPE et sa mise à jour

<span class="mytext">
Une nouvelle version de la méthode 3CL a été publiée en juillet 2021. C’est une méthode robuste qui semble satisfaire les experts les plus exigeants du domaine [[Sidler-Sept2021](https://www.actu-environnement.com/blogs/olivier-sidler/346/non-methode-calcul-dpe-pas-fausse-475.html)]. En outre, cette méthode permet un traitement des bâtiments construits avant 1948. Les exigences sur les logiciels utilisables par les diagnostiqueurs sont plus importantes, et le DPE est maintenant un document opposable qu’un acheteur pourrait utiliser pour casser une vente. Il semble clair que les pratiques passées des diagnostiqueurs, entre l’envie de faire vite, ou l’envie de faire plaisir au client, n’y trouveront leur place de la même manière. Les premières remontées de terrain sont beaucoup trop peu nombreuses pour y voir une mesure fiable mais le nombre de passoires remontées n’était pas en accord avec l’étude [[SDES-Sept2020](https://www.statistiques.developpement-durable.gouv.fr/le-parc-de-logements-par-classe-de-consommation-energetique)] et correspond, comme on peut le voir dans la Table 2, plutôt à notre évaluation.
</span>

|      |SDES 2020 |Phebus | Retour terrain 2021 | Notre méthode |
|:----------|:---------------|:---------------|:-----------|:------------|
|Proportions de passoires | 27,5%  |    42,5%            | 38,6%     | 38,2%       |
{: .mbtablestyle .wrapstyle .simple7}
<span class="legendtext" id="CAPTable1" style="display:block;text-align:center">
**Table 2** : remontées de terrain [Remonte2021] (voir aussi [[Sidler-Sept2021](https://www.actu-environnement.com/blogs/olivier-sidler/346/non-methode-calcul-dpe-pas-fausse-475.html)]) sur le taux de passoires énergétiques parmi l’ensemble des bâtiments construits avant 1974. Nous y avons ajouté les résultats de notre méthode.
</span>

<span class="mytext">
Notons que le ministère du logement a décidé avec la DGEC de modifier à la marge le DPE publié en mars 2021 par un arrêté d’octobre 2021 [[DPE-MiseAjourOct2021](https://www.legifrance.gouv.fr/download/pdf?id=7hpbVyq228foxHzNM7WleDImAyXlPNb9zULelSY01V8=)]. Il sera possible de juger de l’impact de cette réforme lorsque les données. Le gouvernement nous annonce des impacts mineurs et des corrections à la marge, mais dans le même temps cette réforme a été mise en place suite, entre autres, à une surreprésentation des passoires dans les retours de terrain de 2021 incompatible avec l’estimation de 2020. Les paramètres modifiés incluent le taux de renouvellement de l’air qui peut avoir un impact significatif sur les résultats. L’explication donnée par le gouvernement est que cette modification permettra une adaptation du paramètre “renouvellement de l’air” aux observations de terrain (présence de joints sur les fenêtres) mais ces paramètres de perméabilité à l’air ne correspondent pas à une réalité physique mesurable facilement, et vu leur impact, on notera surtout que ces choix vont avoir pour conséquence de faire gagner des classes à un nombre incertains de logements.
</span>

# Conclusion : sur les conséquences de ces erreurs.

<span class="mytext">
Vis à vis des modifications apportées sur le nouveau DPE en octobre 2021, deux scénarios sont possibles : (1) le nombre de passoires diminue mais reste proche de notre estimation à 7 millions, (2) la modification ramène le nombre de passoires à l’estimation donnée dans l’étude de 2020 (5 millions). Il sera possible de savoir laquelle de ces tendances reflète la réalité lorsque les remontées de terrain du nouveau DPE seront rendues publiques par l’ADEME d’ici quelques mois.
</span>

<span class="mytext">
Dans le premier scénario, la situation du mois de septembre 2021 se reproduira : le gouvernement et les la filière du bâtiment réaliseront que le nombre de passoires impactées à court terme par les restrictions de la loi de résilience climat [[LoiResilienceClimat-juillet2021](https://www.ecologie.gouv.fr/loi-climat-resilience)] est plus importants que celui envisagés dans l’étude de 2020. Les alternatives seront les mêmes qu’en septembre 2021 : revoir à la hausse les moyens alloués à la rénovation énergétique, ou modifier à nouveau le DPE par un arrêté. Choisir à nouveau la seconde option impactera la crédibilité du DPE et rendra certainement nos objectifs de long terme (neutralité carbone) hors de portée. Dans le second scénario, le DPE facilitera l’atteinte des objectifs de court terme (suppression du nombre de passoires) au détriment de la crédibilité du DPE et des objectifs de long terme en repoussant à 2034 une part trop importante des rénovations. En outre, dans ces cas, les foyers directement impactés seront ceux en situation de précarité énergétique dans le parc privé locatif qui pourront voir la rénovation de leur logement repoussée à 2034.
</span>

<span class="mytext">
Au-delà des questions techniques relatives au DPE, qui connaît vraiment les mesures prises par la loi climat ? A-t-on envoyé une lettre à tous les logements ayant un DPE F ou G pour les informer (les adresses sont connues et publiques dans la base DPE) ? Aux maires des villes qui sont susceptibles d’abriter ces logements ? Ou est-ce que chacun attend dans son coin que la date fatidique arrive pour se plaindre de ne pas avoir été prévenu et demander un peu plus de temps ? Mal mesurer aujourd’hui, c’est ne pas allouer suffisamment d’argent public pour accompagner les rénovations et se préparer à accepter de revenir sur les objectifs de court et long terme ou de mettre en difficulté des propriétaires dans le besoin qui n’ont pas aujourd’hui conscience de ce qui les attend.
</span>

# Annexe : détails sur l’impact de la dynamique du parc et des rénovations, et du choix de la base Fideli

<span class="mytext">
Nous discutons ici des facteurs qui peuvent justifier le passage de 8.8 millions de passoires en 2013 aux 7 millions environ que nous obtenons avec notre méthode.
1 - la dynamique du parc (rénovation/destruction) entre les deux périodes analysées : (2011-2012) pour la première et (2016-2018) pour la seconde. Cela pourrait expliquer guère plus qu’une différence de l’ordre de 1 000 000 de passoires.
2 - la différence entre le recensement utilisé dans le 1er cas et la base Fidéli dans le 2nd cas pour inférer les performances à l’échelle du parc à partir de l’échantillon retenu. Ici on peut expliquer une différence d’environ 500 000 passoires.  
</span>

<span class="mytext">
Concernant le point 1, on peut séparer destruction et rénovation. D’après les recensements de l’INSEE [RecensementINSEE] effectués pour les années comprises entre 2013 et 2017, la destruction de bâtiment représente environ 150 000 logements par an (voir Figure 1 ci-dessous), c’est à dire environ 750 000 logements entre le parc de 2012 et celui de 2018. Parmi les bâtiments construits avant 1918, 40% sont des passoires énergétiques, en supposant prudemment que plus de la moitié des 750 000 logements détruits étaient des passoires cela donne 400 000 passoires détruites.  
</span>

<span class="mytext">
D’après l'enquête TREMI  [[TREMI2017](https://librairie.ademe.fr/urbanisme-et-batiment/1666-travaux-de-renovation-energetique-des-maisons-individuelles-enquete-tremi-9791029710223.html)] réalisée en 2017 sur la période 2014-2016, 260 000 logements ont eu une rénovation leur permettant de gagner deux classes énergétiques ou plus et 1 040 000  logements on eut une rénovation leur permettant de gagner une classe énergétique. Il est très optimiste de penser que tous ces bâtiments étaient à l’origine des passoires énergétiques. Supposer que 600 000 passoires ont ainsi disparu nous semble raisonnable.  
</span>

<span class="mytext">
Concernant le point 2, la comparaison directe entre Fideli et le recensement n’est pas évidente car les deux évaluations sont faites sur des segments différents. On peut tout de même constater que pour les bâtiments d’avant 1945, les plus susceptibles d’être des passoires (puisque dans cette tranche d’âge 40% sont de classe F ou G) la différence est d’environ 500 000 logements. Sur les logements construits entre 1945 et 2005 la différence est d’environ 3 millions de logements. Si l’on applique les taux donnés dans  [[SDES-Sept2020](https://www.statistiques.developpement-durable.gouv.fr/le-parc-de-logements-par-classe-de-consommation-energetique)], on peut imaginer que sur tous ces bâtiments la différence entre Fidéli et le recensement soit responsable d’une sous-estimation d’environ 500 000 logements.  
</span>
