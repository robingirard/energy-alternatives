---
title: Simulation énergétique des bâtiments à l’échelle des territoires, un outil open source calibré à l’échelle de la France.
key: bâtiments
tags: bâtiments, rénovation, consommation, énergie, territoires.
---

<span class="summary" style="display:block; text-align: justify">
*Résumé -- Nous publions aujourd’hui [un article dans la revue Energy and Building](https://www.sciencedirect.com/science/article/pii/S0378778823004358?via%3Dihub) sur la modélisation énergétique des bâtiments en France. L’occasion pour moi de présenter ici l’outil python de simulation open source [Building model](https://gitlab.com/energytransition/buildingmodel) qui est utilisé dans l’article, d’évoquer les possibilités de l’outil, quelques résultats obtenus, et notre recherche à venir ici.*
</span>
<!--more-->


## Introduction
<span class="mytext">
Les deux personnes qui ont le plus travaillé sur building model sont d’abord [Yassine Abdelouadoud](https://www.linkedin.com/in/yassine-abdelouadoud-a4b4831b9/) et ensuite [Martin Rit](https://www.linkedin.com/in/martin-rit/) (doctorant au CSTB). J’ai déjà publié ici des choses avec Yassine sur ce blog, il est l’auteur d’une base de données permettant d’évaluer le nombre de passoires thermiques en France que nous avions mis à disposition [ici](https://www.energy-alternatives.eu/2022/03/16/DPE-open-data.html). Cette base était obtenue en redressant la base des diagnostics de performance énergétique (DPE, l’ancienne génération) dont nous avions montré les défauts. Le redressement avait été présenté [dans un autre post](https://www.energy-alternatives.eu/2021/11/10/DPE-passoires.html). Il était entre autres basé sur l’utilisation des données du recensement de l’INSEE. Ici nous allons plus loin avec un modèle un peu plus complet, qui utilise en plus la [BD TOPO](https://geoservices.ign.fr/documentation/donnees/vecteur/bdtopo) de l’IGN. Ce modèle appelé Building Model est aussi un peu plus technique à l’usage, ça n’est pas une simple base de données mais bien un code de calcul branché sur un ensemble de bases de données (essentiellement la BD TOPO, recensement et DPE).
</span>

## Building Model, notre modèle de bâtiment open source.
<span class="mytext">
[Building Model](https://gitlab.com/energytransition/buildingmodel) est un outil de simulation énergétique des bâtiments open source. Sa vocation n’est pas de simuler parfaitement un bâtiment donné, mais de faire une simulation de la consommation énergétique d’un grand nombre de bâtiments, potentiellement toute la France, sur l’ensemble des vecteurs et avec une représentation de chaque bâtiment. Cela impose plusieurs choses importantes : (i) les données utilisées pour caractériser les bâtiments doivent être disponibles (en open data) sur toute la France, (ii) le modèle doit être assez simple pour tourner en un temps raisonnable sur toute la France.
</span>


<span class="mytext">
Le modèle développé est un modèle énergétique qui permet de simuler tous les usages de tous les logements d’un bâtiment, pour tous les vecteurs énergétiques (biomasse, gaz de ville, gaz bouteille, électricité, fioul). La consommation finale d’un logement pour un vecteur donné dépend de la surface du logement, du type de logement, du type et du nombre d’occupants, …  Le modèle le plus complexe concerne l’usage chauffage (oui, il y a du travail à faire encore sur l’usage froid, c’est prévu !). Le modèle correspondant est un modèle “d’ordre 1”, pour les connaisseurs il n’est pas si éloigné d’un modèle 3CL DPE. Les données d’entrée de ce modèle sont inférées (estimées) à partir de l’ensemble des bases de données mentionnées (BD TOPO, DPE, INSEE). Il tient compte des performances du logement, des apports solaires, des effets d’ombrage des bâtiments voisins et des adjacences entre bâtiments, tout cela grâce à l’apport de la BD TOPO. Si vous souhaitez en savoir plus, vous pouvez lire l’article, ou aller sur le git de Building Model. Il y a une documentation et le code python est ouvert.
</span>

## Résultats de l'article

<span class="mytext">
Dans [l'article](https://www.sciencedirect.com/science/article/pii/S0378778823004358?via%3Dihub) que nous venons de publier dans la revue Energy and Building, nous faisons deux choses :
</span>
<span class="mytext">
1- nous exposons Building Model avec plus de détails et nous l’appliquons à toute la France pour simuler la consommation de gaz et d’électricité du secteur résidentiel sur l’ensemble des IRIS de France. La [maille IRIS](https://www.insee.fr/fr/metadonnees/definition/c1523) est une maille géographique plus fine que la commune contenant de l’ordre de 2000 habitants.
</span>
<span class="mytext">
 2- Nous utilisons l’ensemble des données locales de l’énergie disponibles en open data https://www.statistiques.developpement-durable.gouv.fr/donnees-locales-de-consommation-denergie.   Ces données de consommation annuelle de gaz et d’électricité sont disponibles sur une bonne partie de la France à la maille IRIS, depuis 2017. Nous proposons une méthode statistique permettant de corriger le modèle Building Model.  Ce modèle utilise en entrée les sorties de Building Model mais aussi d’autres indicateurs statistiques comme le taux de pauvreté, l’âge moyen des habitants, …
</span>

<span class="mytext">
Les niveaux d'erreurs obtenus dans ces travaux sont présentés Figure 1 et 2.</span>
<span class="text" id="Figure9a" style="display:block;text-align:center">
![Image]({{site.baseurl}}/assets/images/Posts/2023-05-31/Erreur.jpg){:.border}
</span>

<span class="legendtext" id="CAPFigure9a" style="display:block;text-align:center">
**Figure 1** --   Distribution des erreurs relatives (exprimées en %) de simulation de l'énergie annuelle consommée sur l'ensemble des Iris de France pour le gaz et l'électricité, avant et après calibration.
</span>



## Travaux en cours/à venir
<span class="mytext">
1- Utilisation de Building Model couplé à un outil d’optimisation de la rénovation à l’échelle des territoires dont je parlerai prochainement ici (mis en place dans la [thèse de Antoine Rogeau](https://www.theses.fr/2020UPSLM014) et publié dans [cet article de la revue Applied Energy](https://www.sciencedirect.com/science/article/pii/S0306261920301513)) pour rejouer les PCAET de certains territoires (au programme pour l’instant quelques métropoles : Lille, Grenoble, Nantes, Toulouse). Si vous souhaitez assister à la présentation de Martin Rit au séminaire des doctorants le 8 juin 2023, c’est possible en visio via le [lien donné ici](https://www.linkedin.com/posts/activity-7061965584875319296-AQVv/?utm_source=share&utm_medium=member_desktop).
</span>

<span class="mytext">
2 - Mise en place d’une méthode statistique permettant d’ajuster les paramètres physiques du modèle (par exemple pour analyser comment la température de consigne dépend du taux de pauvreté) et d’analyser plus finement les interdépendances.  
</span>

<span class="mytext">
3 - Simulation et optimisation sur plusieurs années météo (pour l’instant nous avons travaillé avec une météo “moyenne” sur les années simulées.  
</span>

<span class="mytext">
4 - Amélioration du modèle sur des usages comme la climatisation (vaste sujet).
</span>


<span class="text" id="Figure9a" style="display:block;text-align:center">
![Image]({{site.baseurl}}/assets/images/Posts/2023-05-31/France_small.jpg){:.border}
</span>

<span class="legendtext" id="CAPFigure9a" style="display:block;text-align:center">
**Figure 2** --   Répartition spatiale des erreurs relatives (exprimées en %) pour la simulation de la consommation d'électricité à la maille IRIS avant et après calibration.
</span>
