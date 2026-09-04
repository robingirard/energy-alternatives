---
title: Building energy simulation at territorial scale, an open source tool calibrated for the whole of France.
key: buildings
ref: building-model
tags: buildings, renovation, consumption, energy, territories.
---

<span class="summary" style="display:block; text-align: justify">
*Summary -- Today we are publishing [an article in the journal Energy and Buildings](https://www.sciencedirect.com/science/article/pii/S0378778823004358?via%3Dihub) on building energy modelling in France. This is a good opportunity to present here the open source Python simulation tool [Building model](https://gitlab.com/energytransition/buildingmodel), which is used in the article to simulate all residential energy consumption of every dwelling in every IRIS district of France. The model is then calibrated against the consumption data observed at that scale (the French local energy data). This post is also a chance to discuss what the tool can do, to show a few results, and to outline some ongoing research topics.*
</span>
<!--more-->


## Introduction
<span class="mytext">
Some time ago I presented here a database for assessing the number of energy sieves (very poorly insulated dwellings) in France, which we had made available [here](https://www.energy-alternatives.eu/en/2022/03/16/epc-open-data.html). That database was obtained by correcting the database of energy performance certificates (EPC, the previous generation), whose shortcomings we had documented. The correction method was presented [in another post](https://www.energy-alternatives.eu/en/2021/11/10/energy-sieves.html). Among other things, it relied on data from the INSEE census. Here we go further, with a somewhat more complete model that additionally uses IGN's [BD TOPO](https://geoservices.ign.fr/documentation/donnees/vecteur/bdtopo). This model, called Building Model, is also a little more technical to use: it is not a simple database but a computation code plugged into a set of databases (essentially BD TOPO, the census and the EPCs).
</span>

## Building Model, our open source building model.
<span class="mytext">
[Building Model](https://gitlab.com/energytransition/buildingmodel) is an open source building energy simulation tool. Its purpose is not to simulate one given building perfectly, but to simulate the energy consumption of a very large number of buildings — potentially all of France — across all energy carriers and with a representation of each individual building. That imposes several important requirements: (i) the data used to characterise the buildings must be available (as open data) for the whole of France, and (ii) the model must be simple enough to run in a reasonable time over the whole of France.
</span>


<span class="mytext">
The model we developed is an energy model that simulates every end use of every dwelling in a building, for every energy carrier (biomass, mains gas, bottled gas, electricity, fuel oil). The final consumption of a dwelling for a given carrier depends on the floor area, the type of dwelling, the type and number of occupants, and so on. The most complex sub-model concerns heating (yes, there is still work to do on cooling — it is planned!). That sub-model is a "first-order" model; for those who know the field, it is not so far from a 3CL EPC model. Its input data are inferred (estimated) from all the databases mentioned above (BD TOPO, EPC, INSEE). It accounts for the thermal performance of the dwelling, solar gains, the shading effects of neighbouring buildings and adjacencies between buildings, all thanks to BD TOPO. If you want to know more, you can read the article or go to the Building Model git repository. There is documentation, and the Python code is open.
</span>

## Results from the article

<span class="mytext">
In the [article](https://www.sciencedirect.com/science/article/pii/S0378778823004358?via%3Dihub) we have just published in Energy and Buildings, we do two things:
</span>
<span class="mytext">
1- we describe Building Model in more detail and apply it to the whole of France to simulate residential gas and electricity consumption across all IRIS districts. The [IRIS unit](https://www.insee.fr/fr/metadonnees/definition/c1523) is a geographical unit finer than the municipality, containing of the order of 2000 inhabitants.
</span>
<span class="mytext">
 2- We use all the local energy data available as open data at https://www.statistiques.developpement-durable.gouv.fr/donnees-locales-de-consommation-denergie. These annual gas and electricity consumption data are available for a good part of France at IRIS level, since 2017. We propose a statistical method to correct the Building Model output. That method takes as inputs the outputs of Building Model but also other statistical indicators such as the poverty rate, the average age of inhabitants, and so on.
</span>

<span class="mytext">
The error levels obtained in this work are shown in Figures 1, 2 and 3. On average, for the electricity carrier and with the calibrated model, the error is 16%. It is somewhat larger for the gas carrier.  </span>
<span class="text" id="Figure9a" style="display:block;text-align:center">
![Image]({{site.baseurl}}/assets/images/Posts/2023-05-31/Erreur.jpg){:.border}
</span>

<span class="legendtext" id="CAPFigure9a" style="display:block;text-align:center">
**Figure 1** --   Distribution of the relative errors (in %) in the simulation of annual energy consumption across all IRIS districts of France, for gas and electricity, before and after calibration.
</span>



## Ongoing and upcoming work
<span class="mytext">
The two people who have worked most on Building Model are, first, [Yassine Abdelouadoud](https://www.linkedin.com/in/yassine-abdelouadoud-a4b4831b9/) and then [Martin Rit](https://www.linkedin.com/in/martin-rit/) (PhD student at CSTB). We are still working with Yassine and Martin on various topics.
</span>

<span class="mytext">
1- Using Building Model coupled with a territorial-scale renovation optimisation tool, which I will write about here soon (developed in [Antoine Rogeau's PhD thesis](https://www.theses.fr/2020UPSLM014) and published in [this article in Applied Energy](https://www.sciencedirect.com/science/article/pii/S0306261920301513)), to replay the climate-air-energy plans (PCAET) of some territories — currently a few metropolitan areas: Lille, Grenoble, Nantes, Toulouse. If you would like to attend Martin Rit's presentation at the PhD students' seminar on 8 June 2023, you can join online via the [link given here](https://www.linkedin.com/posts/activity-7061965584875319296-AQVv/?utm_source=share&utm_medium=member_desktop).
</span>

<span class="mytext">
2 - Developing a statistical method to adjust the physical parameters of the model (for instance to analyse how the heating set point depends on the poverty rate) and to analyse the interdependencies in more detail.
</span>

<span class="mytext">
3 - Simulation and optimisation over several weather years (so far we have worked with an "average" weather over the simulated years).
</span>

<span class="mytext">
4 - Improving the model for end uses such as air conditioning (a vast subject).
</span>

<span class="mytext">
5 - Plugging Building Model into the electricity distribution network planning tools developed by [Roseau Technologies](https://www.roseautechnologies.com/), to assess the future costs of distribution network evolution as well as the value of flexibility in that network.
</span>


<span class="text" id="Figure9a" style="display:block;text-align:center">
![Image]({{site.baseurl}}/assets/images/Posts/2023-05-31/France_small.jpg){:.border}
</span>

<span class="legendtext" id="CAPFigure9a" style="display:block;text-align:center">
**Figure 2** --   Spatial distribution of the relative errors (in %) for the simulation of electricity consumption at IRIS level, before and after calibration.
</span>
<span class="text" id="Figure9a" style="display:block;text-align:center">
![Image]({{site.baseurl}}/assets/images/Posts/2023-05-31/erreur2.jpg){:.border}
</span>

<span class="legendtext" id="CAPFigure9a" style="display:block;text-align:center">
**Figure 3** --   Relative errors (in %) as a function of the complexity of the model used.
</span>
