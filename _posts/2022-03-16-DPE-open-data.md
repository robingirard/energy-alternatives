---
title: Estimation de la Performance Énergétique du Parc Résidentiel
key: DPE
tags: bâtiment rénovation DPE transition évolution passoires énergétiques
article_header:
  type: cover
  image:
    src: /assets/images/Posts/2022-03-16/DPE_image.png
---

<span class="summary" style="display:block; text-align: justify">
*Résumé -- Dans un article précédent [[PostPassoires](https://www.energy-alternatives.eu/2021/11/10/DPE-passoires.html)], nous avons présenté avec [Yassine Abdelouadoud](mailto:yassine@abckpi.com) le diagnostic de performance énergétique (le DPE) et discuté son utilisation pour l’évaluation du nombre de passoires énergétiques en France. Nous avions proposé une nouvelle estimation du nombre de passoire autour de 7 millions assez différente de l’estimation officielle [[SDES-Sept2020](https://www.statistiques.developpement-durable.gouv.fr/le-parc-de-logements-par-classe-de-consommation-energetique)] qui est de 4.5 millions. La vraisemblance de ces résultats était confortée par une analyse de l’évolution depuis la précédente évaluation de 2013 qui comptait 8 millions de passoires et faisait consensus. La nouvelle estimation que nous proposons a été obtenue à partir d’une nouvelle méthode que nous allons présenter succinctement dans cet article et qui permet entre autres de corriger certains défauts de la base DPE. Une application possible des résultats présentés obtenus avec la méthodologie présentée dans ce post est une cartographie de l'estimation de la localisation des passoires en France*
</span>
<!--more-->

<iframe src="{{site.baseurl}}/assets/images/Posts/2022-03-16/carte passoire simple.html" height="400px" width="100%" style="border:none;"></iframe>


<span class="summary" style="display:block; text-align: justify">
**Mise à disposition des résultats.** La [description complète de la méthode](https://storage.googleapis.com/correction-base-dpe/Estimation%20Performance%20Energ%C3%A9tique%20Parc%20R%C3%A9sidentiel%20Fran%C3%A7ais%20v0_1_0.pdf) est mise à disposition, le texte ci-dessous en propose donc une synthèse.
Les [résultats détaillés complets à l’échelle du parc](https://www.data.gouv.fr/fr/datasets/structure-du-parc-de-residences-principales/) sont disponibles en Licence Ouverte/Open License sur le site data.gouv.fr.  
Le [taux et nombre de passoires énergétiques par IRIS](https://www.data.gouv.fr/fr/datasets/nombre-et-taux-de-passoires-energetiques-par-iris/) sont disponibles en Licence Ouverte/Open License sur le site data.gouv.fr.
Les [données complètes](https://storage.googleapis.com/correction-base-dpe/base_logement_complete.7z) (c’est-à-dire le fichier détail logement enrichi des données de performance énergétique) sont mises à disposition sous licence Open Licence / Licence Ouverte ([texte de la licence](https://www.etalab.gouv.fr/wp-content/uploads/2014/05/Licence_Ouverte.pdf)).
</span>

# Introduction : les limites de la base DPE
<span class="mytext">
[La base DPE mise en ligne par l’ADEME](https://data.ademe.fr/datasets/dpe-france) utilisée dans [[SDES-Sept2020](https://www.statistiques.developpement-durable.gouv.fr/le-parc-de-logements-par-classe-de-consommation-energetique)] mais aussi dans notre analyse [[PostPassoires](https://www.energy-alternatives.eu/2021/11/10/DPE-passoires.html)] contient l’ensemble des DPE réalisés depuis l’entrée en vigueur de l’obligation réglementaire. Bien que très riche, elle ne permet pas de directement estimer la performance énergétique du parc résidentiel pour deux raisons.
</span>

<div class="text" style="display:block; text-align: justify">
<ul> <li>
La présence de défauts liés à la réalisation des DPE : (a) manipulation des données d’entrée par les diagnostiqueurs quand le résultat du diagnostic est proche d’une limite de classe, (b) utilisation de la méthode facture qui possède un biais intrinsèque, et (c) le recours massif aux valeurs par défaut post RT 1974 entraînent une surestimation des performances énergétiques.
</li>
<li>
L’échantillon de logements sur lequel les DPE sont réalisés n’est pas représentatif (par exemple, surreprésentation des logements neufs) du fait des conditions dans lesquelles le DPE est obligatoire (mise en vente ou location).
</li>
</ul>
</div>

<span class="mytext">
La seconde limitation est contournée dans [[SDES-Sept2020](https://www.statistiques.developpement-durable.gouv.fr/le-parc-de-logements-par-classe-de-consommation-energetique)] par l’utilisation de la base Fideli [[Fidéli2021](Fichier démographique sur les logements et les individus (Fidéli))] qui n’est pas une base accessible à tous, et la première limitation n’est contournée que pour le problème causé par la méthode facture via l’utilisation du modèle Enerter de l’entreprise energie demain. De notre côté, nous avons développé une méthodologie en deux étapes détaillées dans les sections suivantes :
</span>

<div class="text" style="display:block; text-align: justify">
<ul> <li>
Nettoyage de la base DPE et correction des défauts liés à la réalisation et mentionnés ci-dessus.
</li>
<li>
Appariement avec le fichier détail logement issu du recensement pour redresser la non représentativité de l’échantillon
</li>
</ul>
</div>

# Nettoyage et correction de la base DPE

<span class="mytext">
Avant de présenter les 3 défauts (a,b,c) listés dans l’introduction et les méthodes de correction associées, quelques précisions préliminaires sont nécessaires. Tout d’abord, certains DPE ne peuvent pas être exploités du fait d’incohérences dans les données d’entrée ou parce qu’ils ne concernent pas le parc résidentiel, ceux-ci sont retirés (environ 5122000 DPE sont conservés). Ensuite, les résultats principaux des DPE peuvent être extraits directement de la base, mais certaines caractéristiques doivent être calculées à partir des tables pertinentes de la [[description de l’ancien DPE](http://www.rt-batiment.fr/IMG/pdf/annexe_methode_de_calcul_3cl-dpe_v1.3.pdf)]. Enfin, pour que chacune des analyses et corrections données ci-après soient appliquées sur des sous échantillons aussi homogènes que possible, les DPE sont groupés par classe d’année de construction, méthode de calcul, type de logement et combustible de chauffage. Dans chacune des sous-sections suivantes, nous donnons des représentations graphiques, certaines concernant un sous-ensemble de l’échantillon. L’ensemble des analyses et une description plus détaillée des méthodes d’ajustement sont disponibles dans [le rapport complet](https://storage.googleapis.com/correction-base-dpe/Estimation%20Performance%20Energ%C3%A9tique%20Parc%20R%C3%A9sidentiel%20Fran%C3%A7ais%20v0_1_0.pdf).
</span>

## Manipulation par les diagnostiqueurs des données d’entrée à proximité des limites de classe

<span class="mytext">
Le défaut le plus facile à mettre en évidence est la surreprésentation des consommations d’énergie primaire proche des limites hautes de classe énergétique accompagnée de la sous-représentation symétriques à proximité des limites basses, il peut être observé dans le graphique de la Figure 1.
</span>

<span class="text" id="Figure1" style="display:block;text-align:center">
![Image]({{site.baseurl}}/assets/images/Posts/2022-03-16/1946_1974_audit_house_oil_initial.svg){:.border}
</span>

<span class="legendtext" id="Figure1" style="display:block;text-align:center">
**Figure 1** --  Distribution des consommations d’énergie primaire obtenue par méthode 3CL pour les maisons individuelles chauffées au fioul construites entre 1946 et 1974. La ligne bleue représente une distribution beta approchant l’enveloppe de la distribution observée.
</span>


<span class="mytext">
La correction appliquée repose sur la distribution bêta correspondant au maximum de vraisemblance (en bleu dans le graphique ci-dessus). Cette distribution est utilisée pour identifier les intervalles de consommation surreprésentés et sous-représentés et déplacer une partie des DPE présents dans les premiers vers les seconds de manière à minimiser l’écart avec la distribution beta. Le résultat obtenu pour l’échantillon ci-dessus est donné dans le graphique de la Figure 2.
</span>

<span class="text" id="Figure2" style="display:block;text-align:center">
![Image]({{site.baseurl}}/assets/images/Posts/2022-03-16/1946_1974_audit_house_oil_step_0_result.svg){:.border}
</span>

<span class="legendtext" id="Figure2" style="display:block;text-align:center">
**Figure 2** --  Distribution des consommations d’énergie primaire obtenue après correction pour les maisons individuelles chauffées au fioul construites entre 1946 et 1974
</span>

## Utilisation de la méthode facture

<span class="mytext">
La méthode facture évalue, par construction, la combinaison de la performance intrinsèque du logement et du comportement énergétique des occupants sur un périmètre qui inclut, dans le cas de l’électricité notamment, des consommations non prises en compte par la méthode 3CL. Si les occupants sont en situation de précarité énergétique (5 millions de foyers [selon l’ONPE](https://onpe.org/sites/default/files/onpe_tableau-de-bord-de-la-precarite-energetique_2020_s2_0.pdf)), ils auront tendance à diminuer leur consommation d’énergie (notamment chauffage) pour limiter leur facture et ce, d’autant plus que leur logement a une faible performance énergétique. Cela se traduit par un transfert significatif des classes E, F et G vers les classes B, C et D qui est clairement visible dans la Figure 3 réalisée pour des logements construits dans la période 1940-1950.
</span>

<span class="text" id="Figure3" style="display:block;text-align:center">
![Image]({{site.baseurl}}/assets/images/Posts/2022-03-16/diff_3cl_facture.svg){:.border}
</span>

<span class="legendtext" id="Figure3" style="display:block;text-align:center">
**Figure 3** --  Différence, sur le sous-échantillon composé des logements construits dans la période 1940-1950, entre la distribution de consommations d’énergie pour les DPE 3CL et celle pour les DPE factures, une valeur positive indique donc la présence de plus de DPE 3CL
</span>


<span class="mytext">
Cette limitation de la méthode facture est compensée en appliquant un facteur correctif aux paramètres de la distribution bêta sous-jacente. Les facteurs de correction sont estimés pour chaque combustible et types de logement en comparant des échantillons de DPE facture et 3CL correspondant à des périodes de construction similaires.
</span>


## Valeurs par défaut surestimant les performances

<span class="mytext">
Dans le cas de l’application de la méthode 3CL, certaines valeurs des paramètres d’entrée peuvent être attribuées en fonction de l’année de construction si le diagnostiqueur juge qu’il lui est impossible de les relever. Cette manière de procéder repose sur l’entrée en vigueur de réglementations thermiques successives (RT 1974, 1982, 1988, 2000, 2005) imposant des niveaux de performances de plus en plus exigeants aux bâtiments. Cependant, les valeurs par défaut fixées indépendamment par éléments (mur, planchers, etc.) ne sont que des approximations limitées des exigences réglementaires qui ont, dès 1974, été basées sur des critères de performance globaux, prenant en compte notamment les surfaces des différentes parois relativement à la surface habitable. Chacune des RT ayant été associée à une exigence explicite d’amélioration de la performance (à l’exception de la RT 1988, voir ci-dessous), nous comparons dans la Figure 4 l’évolution de celle-ci avec celles des valeurs par défaut.
</span>

<span class="text" id="Figure4" style="display:block;text-align:center">
![Image]({{site.baseurl}}/assets/images/Posts/2022-03-16/evolution_u_perf.svg){:.border}
</span>

<span class="legendtext" id="CAPFigure4" style="display:block;text-align:center">
**Figure 4** --  comparaison de l’évolution, en fonction de l’année de construction, des performances de bâtiments associée aux réglementations thermiques (trait bleu) avec celle associée aux valeurs par défaut dans le DPE 3CL (toutes les couleurs sauf le bleu).
</span>

<span class="mytext">
On peut constater que les valeurs par défaut diminuent initialement plus rapidement que l’exigence de performance, avec un rattrapage partiel de la différence s’opérant à partir des RT des années 2000, ce qui implique une surestimation de la performance lorsque les valeurs par défaut sont appliqués à l’ensemble des parois d’un logement. Cet avantage se traduit par une augmentation très significative du recours aux valeurs par défaut pour les périodes de construction comprises entre 1975 et 2012 (entre 65 et 75% des DPE pour lesquels les valeurs par défaut ont été utilisées sur l’ensemble des parois) que l’on peut observer dans la Figure 5.  
</span>

<span class="text" id="Figure5" style="display:block;text-align:center">
![Image]({{site.baseurl}}/assets/images/Posts/2022-03-16/part_valeur_par_defaut.svg){:.border}
</span>

<span class="legendtext" id="CAPFigure4" style="display:block;text-align:center">
**Figure 5** --  Evolution de l’utilisation par les diagnostiqueurs, des valeurs par défaut, en fonction de la période de construction des bâtiments.
</span>


<span class="mytext">
L’impact de l’utilisation des valeurs par défaut de la méthode 3CL pour les périodes de construction comprises entre 1975 et 2012 est compensé en appliquant un facteur correctif aux paramètres de la distribution bêta sous-jacente. Les facteurs de correction sont estimés pour chaque combustible, types de logement et période de construction en comparant des échantillons de DPE à faible taux de valeur par défaut à des échantillons à taux élevé de valeurs par défaut.
</span>

# Appariement avec le fichier détail logement


<span class="mytext">
Les biais de sélection sont redressés en appariant la base DPE avec le fichier détail logement du recensement de l’INSEE, une description exhaustive du parc de logements géolocalisé à l’IRIS et contenant notamment des variables déterminantes pour la caractérisation énergétique des logements et communes avec la base DPE.
</span>

<div class="text" style="display:block; text-align: justify">
<ul> <li>
Type de logement (maison individuelle ou appartement)
</li>
<li>
Classe d’année de construction
</li>
<li>
Classe de surface habitable

</li>
<li>
Combustible principal de chauffage (électricité, gaz, fioul ou autre)
</li>
</ul>
</div>


<span class="mytext">
L’appariement consiste à affecter à chaque enregistrement du fichier détail logement un DPE présentant des caractéristiques similaires suivant les attributs ci-dessus. Du fait de la répartition géographique très inégale des DPE réalisés, il n’est pas possible de trouver un DPE correspondant à chaque enregistrement du fichier détail logement dans le même IRIS. Pour contourner cette limitation, l'appariement est réalisé à plusieurs échelles géographiques successives : IRIS, commune, EPCI, département, région, Pays. Le graphique de la Figure 6 présente le nombre d’enregistrements du recensement appariés à chaque niveau géographique.
</span>

<span class="text" id="Figure6" style="display:block;text-align:center">
![Image]({{site.baseurl}}/assets/images/Posts/2022-03-16/niveaux_appariemment.svg){:.border}
</span>

<span class="legendtext" id="CAPFigure6" style="display:block;text-align:center">
**Figure 6** --   Nombre d’enregistrements du recensement appariés à chaque niveau géographique
</span>


# Résultats

## Impacts comparés appariement recensement/correction DPE


<span class="mytext">
Afin d’illustrer l’impact de la correction de la base DPE et de l'appariement avec le recensement, nous présentons dans la Figure 7 le nombre de résidences principales totales par classe énergétique pour trois types de calcul :
</span>

<div class="text" style="display:block; text-align: justify">
<ul> <li>
Extrapolation directe de la base DPE brute (ie une règle de trois sur le nombre de logements est appliquée)
</li>
<li>
Appariement avec le recensement à partir de la base DPE brute
</li>
<li>
Appariement avec le recensement à partir de la base DPE corrigée
</li>
</ul>
</div>

<span class="text" id="Figure6" style="display:block;text-align:center">
![Image]({{site.baseurl}}/assets/images/Posts/2022-03-16/performance_parc_extrapolation_vs_redressement.svg){:.border}
</span>

<span class="legendtext" id="CAPFigure6" style="display:block;text-align:center">
**Figure 7** --   Nombre de résidences principales totales par classe énergétique pour les trois types de calcul.
</span>

<span class="mytext">
On peut ainsi constater que la conséquence principale à l’échelle du parc de l’appariement avec le recensement est de réduire la surreprésentation des logements neufs, qui constituent la majorité des logements très performants (A et B). La correction de la base DPE a, quant à elle, pour effet d’augmenter la part des logements peu performants (E, F et G).
</span>


# Sensibilité aux facteurs de correction

<span class="mytext">
Les facteurs de correction utilisés ont été obtenus en comparant des sous-échantillons de la base DPE et ne sont donc que des approximations des phénomènes à modéliser. Afin d’illustrer la sensibilité des résultats à ces facteurs, nous réalisons une étude de sensibilité consistant à faire varier séparément les facteurs “facture” et “3CL” par incrément de 10% entre 50 et 200% de leur valeur initiale. Le graphique ci-dessous présente le nombre de passoires énergétiques (résidences principales F et G) pour chacun des scénarios :
</span>

<span class="text" id="Figure8" style="display:block;text-align:center">
![Image]({{site.baseurl}}/assets/images/Posts/2022-03-16/etude_sensibilite.svg){:.border}
</span>

<span class="legendtext" id="CAPFigure8" style="display:block;text-align:center">
**Figure 8** --   Sensibilité du nombre de passoire au correctif appliqué sur la distribution beta.
</span>


<span class="mytext">
En ce qui concerne les facteurs de correction de la méthode facture, nous disposons d’un élément d’étalonnage externe : le nombre de passoires énergétiques parmi les logements construits avant 1948 obtenu dans l’étude du SDES de Septembre 2020, pour laquelle les DPE facture ont été remplacés par le modèle Enerter d’Energies Demain (environ 2.6 millions). Cette valeur correspond à une modulation de 160% des facteurs de correction de la méthode facture, aboutissant à un total de 6.9 millions de passoires énergétiques, que nous considérons comme référence pour la suite.
</span>

## Résultats détaillés

<span class="mytext">
Par construction de la méthodologie, celle-ci permet de produire des résultats à l’échelle du parc par classes de logements, comme illustré ci-dessous :
</span>

<span class="text" id="Figure9a" style="display:block;text-align:center">
![Image]({{site.baseurl}}/assets/images/Posts/2022-03-16/logements_par_classe_et_par_annee.svg){:.border}
</span>

<span class="legendtext" id="CAPFigure9a" style="display:block;text-align:center">
**Figure 9-a** --   Nombre de logements par classe énergétique et par classe d’année de construction
</span>

<span class="text" id="Figure9b" style="display:block;text-align:center">
![Image]({{site.baseurl}}/assets/images/Posts/2022-03-16/logements_par_classe_et_par_combustible.svg){:.border}
</span>

<span class="legendtext" id="CAPFigure9b" style="display:block;text-align:center">
**Figure 9-b** --   Nombre de logements par classe énergétique et par combustible de chauffage
</span>

<span class="text" id="Figure9c" style="display:block;text-align:center">
![Image]({{site.baseurl}}/assets/images/Posts/2022-03-16/logements_par_classe_et_par_surface.svg){:.border}
</span>

<span class="legendtext" id="CAPFigure9c" style="display:block;text-align:center">
**Figure 9-c** --   Nombre de logements par classe énergétique et classe de surface
</span>

<span class="summary" style="display:block; text-align: justify">
**Mise à disposition des résultats.** La [description complète de la méthode](https://storage.googleapis.com/correction-base-dpe/Estimation%20Performance%20Energ%C3%A9tique%20Parc%20R%C3%A9sidentiel%20Fran%C3%A7ais%20v0_1_0.pdf) est mise à disposition, le texte ci-dessous en propose donc une synthèse.
Les [résultats détaillés complets à l’échelle du parc](https://www.data.gouv.fr/fr/datasets/structure-du-parc-de-residences-principales/) sont disponibles en Licence Ouverte/Open License sur le site data.gouv.fr.  
Le [taux et nombre de passoires énergétiques par IRIS](https://www.data.gouv.fr/fr/datasets/nombre-et-taux-de-passoires-energetiques-par-iris/) sont disponibles en Licence Ouverte/Open License sur le site data.gouv.fr.
Les [données complètes](https://storage.googleapis.com/correction-base-dpe/base_logement_complete.7z) (c’est-à-dire le fichier détail logement enrichi des données de performance énergétique) sont mises à disposition sous licence Open Licence / Licence Ouverte ([texte de la licence](https://www.etalab.gouv.fr/wp-content/uploads/2014/05/Licence_Ouverte.pdf)).
</span>

# Perspectives

<span class="mytext">
L’existence d’un consensus large entre les acteurs de la rénovation énergétique sur l’état du parc est un préalable à l’établissement et à la mise en œuvre d’une politique de rénovation à la hauteur des enjeux. Cependant, la publication en Open Data de données brutes comme la base DPE de l’ADEME n’est pas suffisante pour asseoir un tel consensus, du fait de la non-reproductibilité et de l’opacité relative des méthodes de traitement utilisées par les différents acteurs.
</span>

<span class="mytext">
Une des manières de sortir de cette impasse est la mise en place d’une initiative Open Source (code de calcul + méthodologie documentée) d’estimation de la performance du parc faisant l’objet d’une gouvernance collégiale associant les différentes parties prenantes. Dans le but de favoriser l’émergence d’une telle structure, nous proposons d’utiliser la méthodologie présentée ici et le code associé comme brique initiale de la démarche.
</span>
