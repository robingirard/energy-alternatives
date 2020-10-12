---
title: Variabilité de la consommation électrique et thermosensibilité
key: variabilite-de-la-consommation-electrique-et-thermo-sensibilite
tags: Thermosensibilite consommation variabilite chauffage evolution
article_header:
  type: cover
  image:
    src: /assets/images/Posts/2019-05-24/Thermosens.jpg
---



<div class="summary" style="display:block; text-align: justify">
<em>
     Résumé -- Dans ce post je décris brièvement les phénomènes de variabilité de la consommation électrique en distinguant plusieurs causes et plusieurs échelles de temps. J’analyse en particulier le phénomène de thermosensibilité –sensibilité de la consommation à la température- important en France et problématique. Je montre l’évolution de cette thermosensibilité depuis 1996, on observe un doublement de l’amplitude du phénomène de 2000 à 2010.
     Dans d’autres posts je discuterai les causes de cette évolution, de la dispersion de ce phénomène sur le territoire ainsi que les évolutions possibles dans l’avenir.
</em>
</div>

<!--more-->

____________________________________


<div class="text" style="display:block; text-align: justify">
     Dans la plupart des régions du monde on a coutume de découper les variations intra-annuelles de la consommation électrique en variations journalières, hebdomadaires et saisonnières. Pour les variations intra-annuelles on peut distinguer grossièrement deux types de causes :
<ul> <li>l’emploi du temps des consommateurs qui fait varier la consommation au cours d’une journée et d’un jour de travail à un jour de congé. Cet emploi du temps peut aussi provoquer de légères variations saisonnières avec les grandes vacances d’été, surtout localement mais aussi à l’échelle du pays.</li>
  <li>la sensibilité de la consommation à la météorologie et plus particulièrement à la température -la thermosensibilité- qui a de légères conséquences sur les variations de la consommation à l’échelle journalières, des conséquences qui peuvent être importantes à l’échelle hebdomadaire, et surtout des conséquences très importantes à l’échelle saisonnière.</li>
</ul>
</div>

<span class="text" style="display:block; text-align: justify">
      Je vais étudier en détail les effets de ces deux types de causes. Puis je parlerai des évolutions sur le long terme (au-delà de l’échelle intra-annuelle) de la consommation et de sa thermosensibilité qui ont d’autres causes. Etudier la thermosensibilité est essentiel pour comprendre les contraintes qui agissent sur le système électrique, car de cette thermosensiblité va grandement dépendre le dimensionnement de notre système en puissance, mais nous verrons cela dans d'autres textes.
</span>

## Les variations intra-annuelles de la consommation d'origine non météorologique
<span class="text" style="display:block; text-align: justify">
Les variations journalières peuvent différer en fonction de la saison. C’est le cas par exemple en France où l’on consomme toujours plus la journée que la nuit mais le pic journalier est atteint vers 19h en hiver et plutôt vers 14h en été ([Figure 1](#Figure1)). A l’inter-saison le pic du soir se déplace légèrement avec l’évolution de la luminosité qui joue non seulement sur notre consommation de lumière mais aussi sur notre mode de vie.
</span>

<span class="text" id="Figure1" style="display:block;text-align:center">
![Image]({{site.baseurl}}/assets/images/Posts/2019-05-24/VarConsoFigure1.png){:.border}
</span>
<span class="legendtext" id="CAPFigure1" style="display:block;text-align:center">
**Figure 1** -- Type de profil de consommation électrique (exprimée en GW une unité de puissance) pour une journée froide de l’hiver 2012 et une journée chaude de l’été en France. Attention, les échelles des deux graphiques sont très différentes ! (Source : données de consommation France RTE)
</span>

<span class="text" style="display:block; text-align: justify">
Sur cet exemple particulier de la [Figure 1](#Figure1), la différence entre le creux de la nuit et le pic de la journée ou du soir est d’environ 15 GW, et la différence n’est pas plus marquée en hiver. Nous allons étudier la distribution générale de ces pics au cours de l’année. On peut diviser ces variations en deux parties comme cela est fait Figure 2 : une variation à la baisse (entre la moyenne journalière et le creux) et une variation à la hausse (entre la moyenne journalière et le pic). La Figure 2 donne la distribution de ces variations en puissance pour la période 2012-2018, période pendant laquelle elles n’ont quasiment pas évolué. Ces variations sont plus importantes à la baisse (autour de 9-10 GW en moyenne et jusqu’à 16 GW au maximum) qu’à la hausse (autour de 7GW en moyenne et jusqu’à 12GW au maximum). La température (période chaude ou froide) a une influence assez faible sur les variations. Pour les variations à la hausse, la moyenne hivernale n’est que quelques centaines de MW plus grande que pendant la saison chaude. Cette définition des variations est simple et pratique et elle sera traduite en un besoin de modulation dans des posts ultérieurs. Il existe évidemment d’autre manières d’appréhender cette variabilité, et l’on pourra par exemple consulter [[Heggarty2018](https://www.sciencedirect.com/science/article/pii/S0306261919302107?via%3Dihub)] pour les définitions proposées à plusieurs échelles de temps et les références qui s’y trouvent.
</span>

<span class="text" id="Figure2" style="display:block;text-align:center">
![Image]({{site.baseurl}}/assets/images/Posts/2019-05-24/VarConsoFigure2.v2.png){:.border}
</span>
<span class="legendtext" id="CAPFigure2" style="display:block;text-align:center">
**Figure 2** -- Une définition des variations extremales à la hausse ou à la baisse (à gauche) et leurs distributions sur la période 2012-2018 en fonction du moment de l’année (période d’utilisation du chauffage ou non). Source des données : consommation France RTE
</span>

<span class="text" style="display:block; text-align: justify">
Les variations hebdomadaires peuvent être liées aux deux causes mentionnées en introduction de ce post. En ce qui concerne la sensibilité de la consommation à la température à l'échelle hebdomadaire, l’arrivée d’une vague de froid peut faire augmenter la consommation de quelques dizaines de GW en un jour ou deux, nous étudierons ce phénomène dans la section suivante. Pour ce qui est de l’emploi du temps des consommateurs, ce sont essentiellement les variations entre le week end ou les jours de congés et la semaine de travail, qui causent des variations de consommation. En général la consommation est plus faible le week end.
</span>

<span class="text" style="display:block; text-align: justify">
On peut produire pour ces de variations hebdomadaires la même analyse que pour les variations journalières en définissant une variation à la baisse (ou à la hausse) entre la moyenne hebdomadaire et la plus petite (ou la plus grande) consommation moyenne journalière. C’est ce qui est fait Figure 3 où l’on observera que ces variations sont plus importantes à la baisse. Ceci s’explique par le fait que la consommation est plus faible seulement les jours de week end et donc, que la moyenne hebdomadaire reflète plutôt un jour de semaine.
</span>

<span class="text" id="Figure3" style="display:block;text-align:center">
![Image]({{site.baseurl}}/assets/images/Posts/2019-05-24/VarConsoFigure3.v2.png){:.border}
</span>
<span class="legendtext" id="CAPFigure3" style="display:block;text-align:center">
**Figure 3** --  Distributions sur la période 2012-2018 des variations hebdomadaires extremales à la hausse ou à la baisse leurs en fonction du moment de l’année (période d’utilisation du chauffage ou non). Source des données : consommation France RTE. La variation hebdomadaire est construite à partir des consommations moyennes journalières (voir texte).
</span>

<span class="text" style="display:block; text-align: justify">
Au sein d’une année, la variation la plus importante est la variation saisonnière. Le pic peut dépasser les 100 GW en hiver comme lors de la vague de froid de 2012 alors qu’en été il est autour de 50 GW. L’existence et l’ampleur (presque 50 GW) de la différence entre ces pointes hivernales et les points estivales est principalement due à la sensibilité de la consommation à la température. En hiver plus il fait froid et plus nous consommons d’électricité, c’est ce que l’on appelle la **thermosensibilité** sur laquelle je vais donner plus de détails dans la section suivante.
</span>

## Sensibilité de la consommation à la température, définition de la thermosensibilité

<span class="text" style="display:block; text-align: justify">
La thermosensibilité permet de quantifier la variation de la consommation avec la température. On peut voir sur la Figure 4 cette relation entre la consommation française moyenne journalière et la température moyenne journalière. Pour des températures inférieures à 15°C elle est assez bien décrite par une droite. La pente de cette droite donne les MW additionnels de consommation qu’engendre une baisse de 1°C, c’est de cette manière que l’on quantifie la thermosensibilité. En dessous de la température seuil (ici 15 °C) la consommation dépend de la température, aussi ce seuil est parfois appelé « température de chauffage ». On peut imaginer en première approximation qu’il s’agit ici d’une température extérieure à partir de laquelle en moyenne les français se mettent à chauffer à l'électricité.
</span>

<span class="text" id="Figure4" style="display:block;text-align:center">
![Image]({{site.baseurl}}/assets/images/Posts/2019-05-24/VarConsoFigure4.png){:.border}
</span>
<span class="legendtext" id="CAPFigure4" style="display:block;text-align:center">
**Figure 4** --  Une définition de la thermosensibilité : pente de la droite de régression linéaire entre la moyenne journalière de la consommation et celle de la température, sur une plage de température où la relation est linéaire. Ici sur les données de consommation France de 2012 (source RTE) et avec les données de température issue de la pondération spatiale de stations météorologiques proposée par RTE.
</span>

<span class="text" style="display:block; text-align: justify">
Plusieurs définitions existent mais toutes reposent sur un modèle linéaire entre des données de consommation électrique et une température pour un sous-ensemble bien choisi des observations. Ce sous-ensemble est ici composé des données pour lesquelles la température est en dessous de 15°, mais il peut aussi être définit par des dates délimitant une période, ou bien par une combinaison des deux. La consommation est ici une moyenne journalière mais elle peut également être prise au maximum de la journée ou à une heure précise. Il existe plusieurs manières de définir une température nationale. Vous pouvez tester différentes définitions de la thermosensibilité en utilisant le code et les données partagées (cf sous le résumé). La thermosensibilité est finalement la pente de la droite de régression linéaire et se mesure donc en GW/°C.
</span>

<span class="text" style="display:block; text-align: justify">
La sensibilité de la consommation électrique à la température est différente selon les pays. Dans certains pays il y a aussi une température chaude au-dessus de laquelle la consommation dépend à nouveau de la température à cause de l’utilisation de climatiseurs. C’est le cas par exemple des Etats-Unis ou de l’Italie, ou dans certains endroits très particuliers de la France. A l’échelle de la France il n’y a pas de thermosensibilité estivale.  Entre ces plages de température (“température de chauffage” et “température de climatisation” si elle existe) la consommation est relativement indépendante de la température. Dans certaines communes du sud de la France, localement, l’effet de la thermosensibilité estivale combiné à des migrations estivales peut impliquer que les pointes de consommation annuelles locales aient lieu en été.
</span>

<span class="text" style="display:block; text-align: justify">
Pour l’hiver en France, la thermosensibilité était autour de 2.3 GW/°C (l’équivalent de deux tranches nucléaires par degré) en 2013. La température de non chauffage est autour de 15°C. La relation linéaire entre consommation et température explique qu’il puisse y avoir une différence de presque 50 GW entre la consommation d’une journée d’été et celle d’une journée de grand froid où la température moyenne nationale descend au-dessous de -5°C comme cela est arrivé en 2012. La [Figure 5](#Figure5) illustre ce phénomène dans différents pays, il est très prononcé en France : la thermosensibilité européenne, de l’ordre de 5 GW/°C est presque pour moitié française. Cela est essentiellement du à l'utilisation du chauffage électrique qui est pour l'instant une spécificité française. Dans le contexte de la transition énergétique nous aurons tendance à utiliser de plus en plus l'électricité comme moyen de chauffage, mais également à consommer moins grâce à l'efficacité.
</span>

<span class="text" id="Figure5" style="display:block;text-align:center">
![Image]({{site.baseurl}}/assets/images/Posts/2019-05-24/VarConsoFigure3.png){:.border}
</span>
<span class="legendtext" id="CAPFigure5" style="display:block;text-align:center">
**Figure 5** --  Thermosensibilité de quatre pays européens (Allemagne, Royaume-Uni, Espagne et France) le pic journalier de la consommation est représenté en fonction de la température nationale pour l’année 2015. Les données de températures sont obtenues à partir de la base de données MERRA (NASA) et les données de consommation à partir de ENTSOE.
</span>

<span class="text" style="display:block; text-align: justify">
Le fait de prendre une température moyenne journalière et une consommation moyenne journalière est préféré ici à l’étude des variations horaires. Cela permet de ne pas intégrer des effets liés l’emploi du temps des consommateurs (surplus de consommation à 19h) et qui ne sont pas dus à la température mais qui lui sont corrélés. Par ailleurs si la température moyenne journalière a une influence importante sur la consommation moyenne journalière (plus de 2GW/°C), ce qu’ajoutent les variations infra-journalières à cette dépendance est moins important. Pour être plus précis si l’on étudie les variables :
</span>

<div class="text" style="display:block; text-align: justify">
<ul> <li> X : la différence entre la pointe de consommation journalière et sa moyenne journalière</li>
<li>   Et Y : la différence entre la température au moment du pic et sa moyenne journalière</li>
  </ul>
</div>

<span class="text" style="display:block; text-align: justify">
on obtient entre elles une faible corrélation et un coefficient directeur de la régression linéaire autour de 0.2 GW/°C (donc beaucoup plus faible que les 2 GW/°C) sans réelle évolution depuis 1996. Le code mis à disposition pour ce post permet de reproduire cette analyse.  Nous reviendrons sur ce point lorsque nous parlerons de la principale cause de la thermosensibilité, le chauffage électrique, et de l’inertie relative à cet usage.  
</span>

## Evolution passée de la thermosensibilité en France.

<span class="text" style="display:block; text-align: justify">
La consommation annuelle électrique depuis la création d’EDF au lendemain de la seconde guerre mondiale a augmenté de presque 5 TWh/an jusqu’au milieu des années 1990. Cette croissance est liée à la croissance économique et aux changements du mode de vie des français. Ces augmentations sont plus liées à une évolution dans le secteur résidentiel et tertiaire qu'à celui de l’industrie mais nous discuterons les évolutions par secteur dans un autre post. Cette croissance a ensuite connu un ralentissement jusqu’à la crise de 2008 après laquelle on ne détecte pas pour l’instant d’augmentation significative.
</span>

<span class="text" style="display:block; text-align: justify">
Durant les années 2000 à 2012 pourtant, alors même que la consommation annuelle ralentissait un phénomène est notable : les pics de consommation annuels ont beaucoup augmenté. Il n’est pas évident de dire dans quelle mesure ce phénomène est nouveau car les données de consommation heure par heure avant 1996 ne sont pas rendues disponibles par le gestionnaire du réseau de transport RTE. Les pics ont augmenté deux fois plus vite que la consommation moyenne et cela correspond à une augmentation d’environ 30% en 10 ans, soit à peu près 2 GW par an (Figure 6).
</span>

<span class="text" id="Figure6" style="display:block;text-align:center">
![Image]({{site.baseurl}}/assets/images/Posts/2019-05-24/VarConsoFigure6.png){:.border}
</span>
<span class="legendtext" id="CAPFigure6" style="display:block;text-align:center">
**Figure 6** --  Consommation horaire française de 1996 à 2019. Entre 2000 et 2012, alors que l’énergie annuelle consommée stagne, on observe une augmentation d’environ 30% des pointes de consommation (Source RTE).
</span>

<span class="text" style="display:block; text-align: justify">
La thermosensibilité est presque entièrement à l’origine de l’augmentation des pointes puisqu’elle a triplé entre 2000 et 2012 passant de 0.8 GW/°C à 2,4 GW/°C. Cela correspond en moyenne à plus de 0.1 GW/°C de plus chaque année. Une température d’un peu moins que 13°C en dessous des normales saisonnières provoquait une augmentation de la consommation de 10 GW en 2000 et de l’ordre de 30 GW en 2012. Ainsi, la légère augmentation de la consommation annuelle et le grand froid de 2012 expliquent presque totalement l’évolution des pics présentés à la Figure 4. La Figure 7 illustre l’évolution du phénomène de thermosensibilité de 2000 à 2012. Par ailleurs, on peut noter que les pics de consommation sont de plus en plus une conséquence directe des variations de la température (évolution de la variance expliquée par la régression linéaire, qui tourne autour de 70% ces dernières années).
</span>

<span class="text" id="Figure7" style="display:block;text-align:center">
![Image]({{site.baseurl}}/assets/images/Posts/2019-05-24/VarConsoFigure7.png){:.border}
</span>
<span class="legendtext" id="CAPFigure7" style="display:block;text-align:center">
**Figure 7** --  Evolution de la thermosensibilité de la consommation électrique française pendant 20 ans (de 1996 à 2019), 100MW/°C de plus chaque année : pente de la relation “conso moyenne journalière”=f(Température moyenne journalière).
</span>

<span class="text" style="display:block; text-align: justify">
On observe donc une augmentation substantielle de la thermosensibilité. Il semble que cette augmentation ait commencé en 2000 mais les données de consommation horaires avant 1996 manquent ici à l’analyse. On peut tout de même penser que le phénomène des années 2000-2010 est nouveau dans le sens où l’évolution de la consommation d’énergie électrique annuelle depuis 1970 a connu un ralentissement progressif. La tendance d’évolution de la thermosensibilité n’est pas confirmée par les années 2012-2018 (cf Figure 7). Il est intéressant d’essayer de comprendre d’une part les conséquences de cette thermosensibilité sur le coût du système électrique et d’autre part ce qui est à l’origine des évolutions passées et futures de la thermosensibilité pour bien la modéliser dans une démarche prospective. C’est ce que nous ferons dans des posts ultérieurs. En ce qui concerne les évolutions futures, dans un contexte de transition énergétique, elles seront guidées par un facteur d'augmentation, l'électrification du chauffage, et un facteur de baisse, l'augmentation de l'efficacité des systèmes de chauffage et de l'isolation des bâtiments. Nous discutons cela [dans ce post](https://www.energy-alternatives.eu/2020/03/22/une-contribution-a-la-reflexion-sur-la-strategie-nationale-bas-carbone-dans-le-batiment-partie-1-quels-modes-de-chauffage-a-lhorizon-2050.html).
</span>

## Conclusion

<span class="text" style="display:block; text-align: justify">
Nous avons analysé les variations de la consommation à plusieurs échelles de temps et selon plusieurs causes. Nous avons donné une définition de la thermosensibilité, c‘est un concept simple utilisé depuis longtemps par les gestionnaires des réseaux électrique français (transport et distribution) et depuis encore plus longtemps par les gaziers. Nous aurons l’occasion de revenir dessus dans des posts futurs. Nous étudierons notamment les causes de la thermosensibilité (essentiellement le chauffage électrique), ainsi que les conséquences sur la gestion et la planification du système électrique des différentes formes de variations. Nous étudierons aussi la variabilité de la production renouvelable et nous montrerons également comment celle-ci impact le système électrique : son fonctionnement et son dimensionnement.
</span>
