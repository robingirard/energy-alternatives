---
title: Simulation énergétique des bâtiments à l’échelle des territoires : un outil open source calibré à l’échelle de la France.
key: bâtiment
tags: bâtiment, rénovation, consommation, énergie, territoires.
article_header:
  type: cover
  image:
    src: /assets/images/Posts/2023-06-01/France.jpg
---

<span class="summary" style="display:block; text-align: justify">
*Résumé -- Nous publions aujourd’hui [un article dans la revue Energy and Building](https://www.sciencedirect.com/science/article/pii/S0378778823004358?via%3Dihub) sur la modélisation énergétique des bâtiments en France. L’occasion pour moi de présenter ici l’outil python de simulation open source [Building model](https://gitlab.com/energytransition/buildingmodel) qui est utilisé dans l’article, d’évoquer les possibilités de l’outil, quelques résultats obtenus, et notre recherche à venir ici.*
</span>
<!--more-->


## Introduction
<span class="mytext">
Les deux personnes qui ont le plus travaillé sur building model sont d’abord Yassine Abdelouadoud et ensuite Martin Rit (doctorant au CSTB). J’ai déjà publié ici des choses avec Yassine ici, il est l’auteur d’une base de données permettant d’évaluer le nombre de passoires thermiques en France que nous avions mis à disposition [ici](https://www.energy-alternatives.eu/2022/03/16/DPE-open-data.html). Cette base était obtenue en redressant la base des diagnostics de performance énergétique (DPE, l’ancienne génération) dont nous avions montré les défauts. Le redressement avait été présenté [dans un autre post](https://www.energy-alternatives.eu/2021/11/10/DPE-passoires.html). Il était entre autres basé sur l’utilisation des données du recensement de l’INSEE. Ici nous allons plus loin avec un modèle un peu plus complet, qui utilise en plus la [BD TOPO](https://geoservices.ign.fr/documentation/donnees/vecteur/bdtopo) de l’IGN. Ce modèle appelé Building Model est aussi un peu plus technique à l’usage, ça n’est pas une simple base de données mais bien un code de calcul branché sur un ensemble de bases de données (essentiellement la BD TOPO, recensement et DPE).
</span>

## Building Model, notre modèle de bâtiment open source.
<span class="mytext">
[Building Model](https://gitlab.com/energytransition/buildingmodel) est un outil de simulation énergétique des bâtiments open source. Sa vocation n’est pas de simuler parfaitement un bâtiment donné, mais de faire une simulation de la consommation énergétique d’un grand nombre de bâtiments, potentiellement toute la France, sur l’ensemble des vecteurs et avec une représentation de chaque bâtiment. Cela impose plusieurs choses importantes : (i) les données utilisées pour caractériser les bâtiments doivent être disponibles (en open data) sur toute la France, (ii) le modèle doit être assez simple pour tourner en un temps raisonnable sur toute la France.
</span>

<span class="mytext">
Les prix de marché de l’électricité pour l’hiver prochain sont à des niveaux jamais atteints, plus de 1000 €/MWh, soit 10 fois supérieurs aux prix pré-crise. Ces prix très élevés reflètent le coût que sont prêts à payer certains consommateurs, notamment industriels, pour éviter une rupture d’approvisionnement en électricité. A contrario, le tarif réglementé de vente de l’électricité pour les particuliers, calculé à partir du coût moyen de production et limité par les mesures dites de « bouclier tarifaire », a peu augmenté : +7% entre 2020 et 2022.
</span>


<span class="mytext">
Le modèle développé est un modèle énergétique qui permet de simuler tous les usages de tous les logements d’un bâtiment, pour tous les vecteurs énergétiques (biomasse, gaz de ville, gaz bouteille, électricité, fioul). La consommation finale d’un logement pour un vecteur donné dépend de la surface du logement, du type de logement, du type et du nombre d’occupants, …  Le modèle le plus complexe concerne l’usage chauffage (oui, il y a du travail à faire encore sur l’usage froid, c’est prévu !). Le modèle correspondant est un modèle “d’ordre 1”, pour les connaisseurs il n’est pas si éloigné d’un modèle 3CL DPE. Les données d’entrée de ce modèle sont inférées (estimées) à partir de l’ensemble des bases de données mentionnées (BD TOPO, DPE, INSEE). Il tient compte des performances du logement, des apports solaires, des effets d’ombrage des bâtiments voisins et des adjacences entre bâtiments, tout cela grâce à l’apport de la BD TOPO. Si vous souhaitez en savoir plus, vous pouvez lire l’article, ou aller sur le git de Building Model. Il y a une documentation et le code python est ouvert.
</span>

## Résultats de l'article

<span class="mytext">
Dans l’article que nous venons de publier, nous faisons deux choses :
</span>
<div class="text" style="display:block; text-align: justify">
<ul> <li>
1- nous exposons Building Model avec plus de détails et nous l’appliquons à toute la France pour simuler la consommation de gaz et d’électricité du secteur résidentiel sur l’ensemble des IRIS de France. La [maille IRIS](https://www.insee.fr/fr/metadonnees/definition/c1523) est une maille géographique plus fine que la commune contenant de l’ordre de 2000 habitants.
</li>
<li>
2- nous utilisons l’ensemble des données locales de l’énergie disponibles en open data https://www.statistiques.developpement-durable.gouv.fr/donnees-locales-de-consommation-denergie.   Ces données de consommation annuelle de gaz et d’électricité sont disponibles sur une bonne partie de la France à la maille IRIS, depuis 2017. Nous proposons une méthode statistique permettant de corriger le modèle Building Model.  Ce modèle utilise en entrée les sorties de Building Model mais aussi d’autres indicateurs statistiques comme le taux de pauvreté, l’âge moyen des habitants, …
</li>
</ul>
</div>

## Travaux en cours/à venir

<div class="text" style="display:block; text-align: justify">
<ul> <li>
Utilisation de Building Model couplé à un outil d’optimisation de la rénovation à l’échelle des territoires dont je parlerai prochainement ici (mis en place dans la [thèse de Antoine Rogeau](https://www.theses.fr/2020UPSLM014) et publié dans [cet article de la revue Applied Energy](https://www.sciencedirect.com/science/article/pii/S0306261920301513)) pour rejouer les PCAET de certains territoires (au programme pour l’instant quelques métropoles : Lille, Grenoble, Nantes, Toulouse). Si vous souhaitez assister à la présentation de Martin Rit au séminaire des doctorants le 8 juin 2023, c’est possible en visio via le [lien donné ici](https://www.linkedin.com/posts/activity-7061965584875319296-AQVv/?utm_source=share&utm_medium=member_desktop).
</li>
<li>
Mise en place d’une méthode statistique permettant d’ajuster les paramètres physiques du modèle (par exemple pour analyser comment la température de consigne dépend du taux de pauvreté) et d’analyser plus finement les interdépendances.  
</li>
<li>
Simulation et optimisation sur plusieurs années météo (pour l’instant nous avons travaillé avec une météo “moyenne” sur les années simulées.  
</li>
<li>
Amélioration du modèle sur des usages comme la climatisation (vaste sujet).
</li>
</ul>
</div>
