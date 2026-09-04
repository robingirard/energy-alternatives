---
title: A contribution to the debate on the national low-carbon strategy for buildings. Part 1 - Which heating systems by 2050?
key: low-carbon-strategy-buildings-heating-2050
ref: snbc-chauffage-2050
tags: Thermosensitivity consumption variability heating evolution
article_header:
  type: cover
  image:
    src: /assets/images/Posts/2020-03-22/DSCF7307c.jpg
---



<div class="summary" style="display:block; text-align: justify">
<em>
     I wrote a contribution to the public consultation on the "draft long-term strategy to mobilise investment in the renovation of the national stock of residential and commercial buildings, public and private" <a href= "http://www.consultations-publiques.developpement-durable.gouv.fr/projet-de-strategie-a-long-terme-pour-mobiliser-a2136.html"> [1]</a>. This contribution comes in two parts; the second part will come later and will address the question of the thermal renovation of buildings.
</em>
</div>
<!--more-->

<div class="summary" style="display:block; text-align: justify">
<em>
     In the introduction I recall the quantified objectives of the French national low-carbon strategy (SNBC) for buildings and for heating consumption. I discuss and quantify the power of the three levers: (i) reducing the heat requirement by improving the efficiency of buildings, (ii) increasing the efficiency of heating systems, mainly through the use of heat pumps (electric or hybrid), and (iii) using energy carriers whose greenhouse gas emissions are low enough. In this context I recall the important role of wood and of the electricity carrier, as well as the importance of the thermosensitivity constraint on electricity demand and the role that biogas can play with respect to it. I compare different ways of using gas to deliver this capacity service. I end with a conclusion including a few recommendations sent during the consultation, which closed on 10 March 2020. Note that I only deal with the heat end use in residential buildings, and that I set aside district heating and solar thermal (which are not negligible but are left out of the analysis). The first lever (thermal renovation of buildings) is deferred to the post that follows.

     The code and the data used to produce the graphs of this post are made freely available.
</em>
</div>



____________________________________


# Introduction: 2050 objectives of the national low-carbon strategy for buildings.
<span class="mytext">The French government recently published a new version of the national low-carbon strategy (SNBC) [[0](https://www.ecologique-solidaire.gouv.fr/strategie-nationale-bas-carbone-snbc)] for a public consultation whose first phase closed on 19 February 2020. This strategy sets itself the ambition of carbon neutrality by 2050 and, obviously, the detailed description of the levers to be deployed by then is still incomplete, but the orientations and quantifications already present in the current document have the merit of launching the debate. In addition, monitoring of our trajectory is planned in the coming years through the "carbon budget" mechanism. In this strategy the building sector plays an important role — on the construction side of course, but also as regards heat production. A dedicated public consultation [[1](http://www.consultations-publiques.developpement-durable.gouv.fr/projet-de-strategie-a-long-terme-pour-mobiliser-a2136.html)] was set up until 10 March 2020. At the same time, the French government is preparing the new thermal regulation for buildings, RE2020, which is to replace the former RT2012 in defining the rules applicable to new construction. RE2020 does not concern only heating, but heating plays a major role in it. This regulation is the subject of debate.
</span>

<span class="mytext">The quantified ambition of the national low-carbon strategy is shown in Figure 1. For buildings, it aims at a move from 85 MtCO2eq/year today to 5 MtCO2eq/year in 2050.
</span>

<span class="text" id="Figure1" style="display:block;text-align:center">
![Image]({{site.baseurl}}/assets/images/Posts/2020-03-22/SNBCChauffageFigure1ObjectifsSNBC.png){:.border}
</span>
<span class="legendtext" id="CAPFigure1" style="display:block;text-align:center">
**Figure 1** -- Ambition of the national low-carbon strategy.
</span>

<span class="mytext">Residential heating represents only part of the corresponding emissions, and that part is not given explicitly in the publicly available document. However, the current contribution of heating can be estimated from the publicly available heating consumption by energy carrier [[2](https://www.statistiques.developpement-durable.gouv.fr/les-menages-et-la-consommation-denergie.)] and the emission factors of ADEME's Base Carbone [[10](https://www.bilans-ges.ademe.fr/documentation/UPLOAD_DOC_FR/index.htm?gaz.htm)]. Some values will deserve a deeper discussion, especially for electricity and the wood/district categories. We defer those discussions to Section 3.
</span>

<span class="mytext">The corresponding calculation is presented in [Table 1](#CAPTable1) below.
</span>

|                             | Elec|   Gas| Fuel oil|  Wood| District| Total|
|:----------------------------|----:|-----:|-----:|-----:|------:|-----:|
|Consumption TWh/year          | 35| 122|  40| 85|   13| 300|
|Emissions gCO2eq/kWh         | 60| 240| 320| 50|  100| 186|
|Total emissions MtCO2eq/year |  2.1|  29.3|  12.8|  4.25|    1.3|  55.8|
{: .simple5 }
<span class="legendtext" id="CAPTable1" style="display:block;text-align:center">
**Table 1** -- Energy consumption for residential heating and associated emissions for different energy carriers. Source for the energy consumed: [[2](https://www.statistiques.developpement-durable.gouv.fr/les-menages-et-la-consommation-denergie.)]. For emissions, the source is the average values given by ADEME in the Base Carbone [[10](https://www.bilans-ges.ademe.fr/documentation/UPLOAD_DOC_FR/index.htm?gaz.htm)].
</span>

<span class="mytext">From this current value of 50 MtCO2eq/year for heating in buildings, a rule of three gives the 2050 objective: 3 MtCO2eq/year. Given that we are talking about a sector where it is not too difficult to reduce our emissions, that value is certainly rather an upper bound. Starting from this objective, the challenge of the national low-carbon strategy — and more generally of the energy transition — with respect to heating consumption is threefold. It is a matter of (i) reducing the heat requirement by improving the efficiency of buildings or by lowering set-point temperatures, (ii) increasing the efficiency of heating systems, mainly by using heat pumps (electric or hybrid, with COPs above 3) or solar thermal systems, and (iii) using energy carriers whose greenhouse gas emissions are low enough. For lever (ii) one also speaks of using (thermal) renewable energy. Variants of these three levers, compatible with the low-carbon strategy, are found in ADEME's 2035-2050 visions [[3](https://www.ademe.fr/lademe/priorites-strategiques-missions-lademe/scenarios-2030-2050)] and in the Negawatt scenarios [[4](https://negawatt.org/Scenario-negaWatt-2017-2050)]. The same kind of approach is found in other countries, such as Germany, which describes its strategy here [[5](https://www.bmwi.de/Redaktion/EN/Publikationen/energy-efficiency-strategy-buildings.pdf?__blob=publicationFile&v=7)].
</span>

<span class="mytext">The essential feature of the SNBC is that it rests on quantified objectives, which will therefore act as a constraint on our political decisions. The purpose of this post and of the one that follows is to quantify, very roughly, with public data and freely available code, how we can activate each of the three levers mentioned in the introduction in order to get closer to the SNBC's 3 MtCO2eq/year. It is also a matter of highlighting the advantages and drawbacks of the different solutions available to us.
</span>

<span class="mytext"> We will first discuss in a little more detail the energy carriers that must play a role in this transition. Then, in Section 3, we will talk about heat pumps, to stress the important role they can play as much as the electricity-demand thermosensitivity problem they induce. Finally, in Section 4, we will show why using biogas is an important building block among the set of solutions — important not with respect to the volumes involved but with respect to the service rendered (a capacity service). A future post will be dedicated to the thermal renovation of buildings.
</span>

# Using energy carriers whose CO2 emissions are low enough

<span class="mytext">When one speaks of using an energy carrier with low enough greenhouse gas emissions, one generally thinks first of electricity; yet wood and biogas are also carriers with low emissions. Thus, moving from an oil boiler to electric convectors or to a pellet stove divides the corresponding greenhouse gas emissions by more than 5. But these emissions and how they are computed are not always the reflection of a stable and indisputable reality. Some are falling, and all of them also involve drawbacks and volume constraints. We will survey these three carriers to illustrate a few of their advantages and imperfections. We do not deal with district heating, nor with solar thermal. For district heating, we refer the reader to this ADEME study from 2017 [[6](https://www.ademe.fr/avis-lademe-reseaux-chaleur-alimentes-energies-renouvelables-recuperation)].
</span>

## Electricity.

<span class="mytext">Electric heating is for now a French specificity, as is the thermosensitivity that accompanies it. In France, electricity has historically displaced other heating systems: geothermal systems, wood energy and district heating, which can have good environmental performance, but also others that are far worse, such as fuel oil. If one looks at a country like Germany, which has not yet developed electric heating much, one finds more district heating and more wood energy but also more fuel oil. Moreover, the German energy transition also aims at a substantial use of electricity for heating. Electricity is not the only low-carbon energy source for heating, but it must be acknowledged that, in annual volume at the scale of France, electricity must play a larger role than it does today. In that sense, since electric heating consumption in France represents only 15% of the requirement (40 TWh/year out of a total of 300 TWh/year), one cannot say that our lead is considerable.
</span>

<span class="mytext">The greenhouse gas emissions associated with electric heating are debated. First of all, the 60 gCO2eq/kWh used in ADEME's Base Carbone and in [Table 1](#CAPTable1) is a yearly average of all generation-related emissions. It does not reflect the real impact of electric heating, which corresponds rather to electricity consumed in winter when it is cold, and it does not include the impacts associated with the power network (the "grey" emissions of lines and transformers). If this thermosensitive electricity (consumed when it is cold) is produced by a gas plant burning natural gas, one ends up with emissions of the order of 400 gCO2eq/kWh instead of 60 gCO2eq/kWh. But thermosensitive demand is not covered only by gas in France, and the seasonal modulation of nuclear achieved "thanks to" the constraint of annual maintenance plays an important role. That seasonal modulation capability of nuclear is today pushed to its maximum and, if thermosensitivity increased in France, nuclear could not cover the additional modulation requirement. We will simply assume here that the 60 gCO2eq/kWh gives a lower bound on the current emissions associated with using electricity for heating. The E+C- experiment that is to prefigure the next regulation uses the figure of 210 gCO2eq/kWh, and in RE2020 the objective is to reduce that figure to 79 gCO2eq/kWh. As regards electricity, the SNBC envisages by 2050 a reduction in average emissions from 60 gCO2/kWh to 20 gCO2/kWh. That objective will go through the disappearance of coal, which is already secured, and through the use of a "relatively carbon-neutral" gas called biogas (methane or hydrogen), or through the disappearance of gas. Yet, as we shall see, the disappearance of gas is not compatible with the development of electric heating.
</span>
<span class="mytext">The volume of electricity consumed every year in France is around 500 TWh/year and covers many uses other than the 40 TWh/year of heating. Even assuming that this electricity only involves nuclear and hydro generation, which are low-carbon (thereby neglecting the thermosensitivity problem), one cannot consider the electricity resource to be "infinite". By 2050 most of the current nuclear fleet will have to be replaced, either by nuclear plants or by renewable plants accompanied by back-up capacity. Neither of these two options is neutral environmentally (resource use, waste, accident risk), nor simple in terms of acceptability: thousands of wind turbines and solar panels on one side, or some fifty times the Flamanville reactor on the other. The electricity resource will be no more infinite in 2050 than it is today.
</span>
<span class="mytext">The interest of electricity for heating, as we shall see, is that it allows the use of heat pumps, which are very efficient and will divide the requirement by 3.

## Biomass

<span class="mytext">Wood energy can also be low-carbon; that depends on the quality of combustion and on forest management. In its Base Carbone, ADEME gives a life-cycle content varying between 0 and 100 gCO2eq/kWh, depending on the origin of the wood and on whether it is logs, wood pellets, forest chips, sawdust and sawmill offcuts, crate and pallet shreds, straw, and so on. That is why we retained the value of 50 gCO2eq/kWh in [Table 1](#CAPTable1). If the wood comes from a sustainably managed forest — or better still from sawmill waste — and is not transported over long distances, emissions are even lower and widely compatible with the low-carbon strategy.
</span>
<span class="mytext">The important question, then, is that of the available volumes. A study [[7](https://www.ademe.fr/sites/default/files/assets/documents/biomasse-forestiere-populicole-et-bocagere-2009.pdf)] carried out for ADEME in 2009 makes it possible to understand the wood resource in volume terms. The horizon given was 2020. It distinguishes different origins of wood, and for each origin a sustainably available annual volume is determined:
</span>
<div class="text" style="display:block; text-align: justify">
<ul> <li>Wood for construction and furniture (BO), not used for heating,</li>
<li>Industrial wood / energy wood (BIBE), 60 $Mm^3$ available, of which 12 $Mm^3$ consumed by industry and 20 $Mm^3$ consumed for heating, hence 28 $Mm^3$ additional available,</li>
<li>Small wood (MB) from high forests that must be cut to favour the growth of large trees and that can be chipped, (8 $Mm^3$ available but unused today),</li>
<li> and sawmill by-products (PCS) used to make pellets or chips, whose availability is 40% of the volume of BO harvested (8 $Mm^3$ available).</li>
</ul>
</div>
<span class="mytext">That study uses precise models to estimate what can be recovered on a lasting basis, taking into account the difficulty of accessing the forest.
</span>
<span class="mytext">A stère of wood yields 2 MWh of heat; a cubic metre of wood gives 4.5 MWh. So the 20 $Mm^3$ of BIBE consumed for heating give 90 TWh/year, i.e. roughly the 85 TWh/year consumed today, which is what is found in the government statistics of [Table 1](#CAPTable1).
</span>
<span class="mytext">The additional resource is therefore composed of 28 $Mm^3$ of recoverable BIBE (126 TWh/year), 8 $Mm^3$ of recoverable MB (36 TWh/year), and 8 $Mm^3$ of PCS at current BO consumption (36 TWh/year), already partly exploited. Ultimately this gives an additional resource of between 150 and 200 TWh/year. One can therefore conclude that the current resource is largely under-exploited and that wood energy could play an important role in implementing the SNBC.
</span>
<span class="mytext">An important drawback of wood is the fine particle pollution it entails, but regulation now makes it possible to keep that problem under control [[17](https://www.ademe.fr/expertises/energies-renouvelables-enr-production-reseaux-stockage/passer-a-laction/produire-chaleur/dossier/bois-biomasse/bois-energie-qualite-lair)].
</span>

## Biogas, a coming reality

<span class="mytext">Gas can also be low-carbon if it is biogas. The prefix "bio" often concentrates a semantic discussion about its marketing counterpart. It must be said that biogas can have drawbacks if the subsidies that accompany it lead to perverse land use, with dedicated intensive crops competing with food [[8](https://decrypterlenergie.org/la-methanisation-est-elle-synonyme-dintensification-de-lagriculture-et-de-pollutions)]. Faced with these issues, the development of the sector is already a source of some tension [[9](https://www.bastamag.net/methanisation-lobby-gaz-vert-biogaz-agriculture-energetique-alimentaire)]. The only roughly neutral energy is the energy we do not consume, and no industrial project, however necessary for society, is safe from poor collective management. For wood the same rule applies, with the example of the Gardanne biomass plant, or the European subsidies granted a few years ago to German plants burning palm wood. For electricity, nuclear or renewable, the examples are no less numerous.
</span>
<span class="mytext">Biogas is nonetheless an important decarbonisation carrier for our energy systems, and we shall see that the capacity service it can render is essential and that it involves volumes far smaller than our current use of gas.
</span>
<span class="mytext">Today the term "biogas" gathers methane produced from very heterogeneous sources by three different techniques: anaerobic digestion, pyrogasification and methanation. These heterogeneous sources absolutely do not reduce to dedicated crops, as one sometimes hears. To date, only the emission factor computed for the wastewater treatment plant pathway is included in ADEME's Base Carbone [[10](https://www.bilans-ges.ademe.fr/documentation/UPLOAD_DOC_FR/index.htm?gaz.htm)], which gathers the "official" life-cycle assessments (LCA) in France; the associated emissions are 16 gCO2/kWh. The LCA emissions of the agricultural pathway are considered to be around 25-50 gCO2/kWh ([see here](https://www.grdf.fr/institutionnel/actualite/dossiers/biomethane-biogaz/etude-biomethane-gaz-effet-serre)), even if these figures are still debated and cannot be applied to the whole sector. In that sense I recommend here that ADEME's Base Carbone deepen its life-cycle assessment of biogas.
</span>
<span class="mytext">The biogas production potential in France varies according to sources between 150 TWh/year and 300 TWh/year (see the Afterres scenario [[11](https://afterres2050.solagro.org/a-propos/le-projet-afterres-2050/)]), to be compared with the 500 TWh/year of gas we consume today in France. It seems to me that, within the SNBC framework, a deeper assessment of this resource is also essential. One can thus imagine that in a decarbonised future, priority uses for gas will have to be defined. We believe these uses could be:
</span>
<div class="mytext">
<ul> <li>Industry, with say 60 TWh/year for processes requiring very high power,</li>
<li>the electricity generation sector, with another 60 TWh/year of gas that could produce 35 TWh/year of flexible electricity, necessary in strongly renewable scenarios but also, to a lesser extent, in a nuclear scenario,</li>
<li>the heating sector, with around 30 TWh/year for reasons we will explain in the next section; the corresponding flexibility could serve the electricity sector.</li>
<li>and possibly transport.</li>
</ul>
</div>

<span class="mytext">With 30 TWh/year reserved for heating, against 120 TWh/year consumed today, one can consider that decarbonisation requires a major reduction in the volume of gas consumed. But things must be analysed more precisely to understand that in the heating sector, as for electricity, gas will increasingly be called upon to play a major role of capacity supply, with reduced energy. Defining a minimum volume of biogas required by the SNBC for heating should in my view be considered in the coming years. That could be associated with a coupling in financing — for instance through an obligation, when setting up a wind project, to contribute to the setting up or financing of a biogas project.
</span>


# Increasing the efficiency of heating systems, mainly by using heat pumps.

## The heat pump, a very high-performing technology.

<span class="mytext">Heat pumps (HPs) use electricity and a thermodynamic process to extract energy from the heat of the environment. That environment may be the outside air (air-to-air or air-to-water systems) or water warming underground (shallow geothermal, water-to-water systems). These systems have the enormous advantage of reaching average coefficients of performance, or "seasonal COP" (the ratio between the heat delivered and the electrical energy supplied over a year), of 4 or even 5 for the best installations.
</span>
<span class="mytext">The performance of a heat pump depends on the technology (air-to-air, air-to-water, water-to-water), on the emitters (for air-to-water, performance is worse with high-temperature emitters) and on the weather (they work less well when it is cold). The heat pumps sold today run at variable speed and therefore adapt their output to the requirement for better performance, but an oversized heat pump generally does not perform best. That is why it is always preferable to renovate at the same time as installing and sizing a heat pump, rather than afterwards.
</span>
<span class="mytext">The investment cost of heat pumps is fairly high, but their efficiency (dividing consumption by 3) makes them economically profitable without subsidy in many cases. Our aim here is not to compare all existing systems; the trade-off between the various systems (air-to-air, low/medium/high-temperature air-to-water, water-to-water) cannot easily be reduced to a simple economic analysis, since air-to-water systems are generally more expensive but more pleasant and better suited to areas above 70 $m^2$ that already have a heat distribution network (by water, in dwellings formerly equipped with gas or oil). Each of these systems will have a different COP, but one can reasonably assume that among all the heat pumps that will be installed in future the COP will average 3.5. All these systems have varied costs that depend on the capacity (about €500/kW for entry-level air-to-air units, and rather €4000 + €500/kW for air-to-water systems) as well as on the distribution system and the emitters (in the case of an air-to-water heat pump). However, assuming an average unit cost of the order of €10k and a 20-year lifetime, one can see that the heat pump is a very effective decarbonisation carrier, profitable without subsidy in many cases. For example, replacing an oil boiler in a 100 $m^2$ dwelling consuming 170 kWh/$m^2$/year saves 12 MWh every year; at €150/MWh (the cost of electricity is higher than that today) that is €1800/year of savings and a system paid back in 6 years.
</span>
<span class="mytext">One can carry out a calculation at the scale of France using the number of households per heating energy obtained in Appendix 1, which we use in the rest of this post. Replacing the 5 million oil heating systems would save 14 MtCO2eq. This idea is developed at length in a study by Carbone 4 [[12](http://www.carbone4.com/les-pompes-a-chaleur/)], carried out in 2013. It is a recommendation that is hard not to endorse. The efficiency of heat pumps economically, energetically and environmentally is therefore an effective lever for the energy transition, but their deployment cannot happen while neglecting an important point: the thermosensitivity it induces in the power system.
</span>

## A thermosensitivity problem.

<span class="mytext">Deploying heat pumps is no doubt a necessary measure in the short term to reduce our greenhouse gas emissions, and the coming regulations (EPC, RE2020) will most likely give heat pumps significant weight. Yet, when heat pumps replace non-electric energies, they increase the thermosensitivity of electricity demand. We saw in a previous post [[13](https://www.energy-alternatives.eu/en/2019/05/24/electricity-demand-variability-and-thermosensitivity.html)] that electric heating consumption, network losses, and a few other temperature-correlated end uses induce a large thermosensitivity of demand at national level. It is 2.5 GW/°C in France, and more than doubled between 2000 and 2012. That problematic trend has not continued in recent years, and this is probably the result of a decline in the share of electric convectors in new buildings, which can be seen in Figure 2.
</span>

<span class="text" id="Figure2" style="display:block;text-align:center">
<img src="{{site.baseurl}}/assets/images/Posts/2020-03-22/RTE-1.png" width="49%" />
<img src="{{site.baseurl}}/assets/images/Posts/2020-03-22/RTE-2.png" width="49%" />
</span>
<span class="legendtext" id="CAPFigure2" style="display:block;text-align:center">
**Figure 2** -- Left: stock of main residences by heating energy. Right: new residential buildings by heating energy (source: RTE 2016 outlook, BatiEtude). The German move towards heat pumps happened earlier (see [[5](https://www.bmwi.de/Redaktion/EN/Publikationen/energy-efficiency-strategy-buildings.pdf?__blob=publicationFile&v=7)], Figure 10 p26).
</span>
<span class="mytext">
These 2.5 GW/°C are not entirely due to heating in the residential sector. Consumption data for different sectors are available (ENEDIS open data [[14](https://data.enedis.fr/explore/dataset/bilan-electrique-transpose/information/?flg=fr)]), and it can be shown (graph in Appendix 2) that the thermosensitivity of residential demand is of the order of 1.5 GW/°C, for an annual energy coverage which, let us recall, is of the order of 35 TWh/year (see Table 1). As already said, that consumption represents only a little more than 15% of total heating consumption, which is 293 TWh/year. One difficulty with the plan set out in [[15](https://jancovici.com/transition-energetique/electricite/50-ou-50/)] of converting the 15 million gas/oil heating systems to electric heating is that it would mean replacing 160 TWh/year of gas and oil consumption with about 46 TWh of electricity consumption (160 TWh/year to which we apply the heat pump COP). If 35 TWh/year of electricity dedicated to heating brings 1.5 GW/°C of thermosensitivity, then the 46 TWh/year resulting from converting gas/oil to electricity would add 2 GW/°C. Going by [[13](https://www.energy-alternatives.eu/en/2019/05/24/electricity-demand-variability-and-thermosensitivity.html)], that could represent about 40 GW of additional peak requirement in the power system — a far from negligible constraint.
</span>

<span class="mytext">
At this stage it is important to recall that thermosensitivity is not only a problem for supply-demand balance at the scale of France or Europe. Congestion problems in the distribution network would result from a massive deployment of heat pumps, for instance in a neighbourhood where gas is the rule today. If all the gas boilers of a neighbourhood are replaced by heat pumps, the electricity cables will locally no longer have sufficient capacity to deliver electricity to every household during a severe cold spell. That is not an insurmountable difficulty for the distribution system operator, but it requires a degree of anticipation and it has a non-negligible cost (that of changing the cables and, above all, of digging the trenches to do so).
</span>

## Heat pump COP during severe cold spells

<span class="mytext">
On top of this, heat pump performance during severe cold spells is lower than on average, for several reasons. First, heat pumps are equipped with a defrost system that starts up when it is cold and consumes energy; second, the COP of the heat pump is worse when the outside exchange fluid is too cold; and finally a heat pump is not sized for the coldest days, and when it is very cold heat pump users sometimes have a less efficient back-up convector plugged in somewhere. According to recent manufacturer data (see for example [[16](https://hal-mines-paristech.archives-ouvertes.fr/hal-01796759/document)], Figure 7 p249), the average COP of heat pumps during severe cold spells is not 3.5 but rather around 3. That question depends on the cold-spell temperature considered; going back to the temperature series I gave for France in my previous post [[13](https://www.energy-alternatives.eu/en/2019/05/24/electricity-demand-variability-and-thermosensitivity.html)] (1996-2019), we get the low quantiles of temperature shown in [Table 2](#CAPTable2).
</span>

|Frequencies                            |1%    |0.5%  |0.25% |0.1% |
|:-------------------------------------|:-----|:-----|:-----|:----|
|Temperature quantile [°C]          |-1.59 |-2.65 |-3.58 |-4.9 |
|Median COP of 3.5 kW air-to-air systems |3.5   |3.35  |3.2   |3.1  |
|Median COP of 7 kW air-to-air systems   |3.5   |3.2   |3.1   |2.9  |
 {: .mbtablestyle .wrapstyle .simple5}
 <span class="legendtext" id="CAPTable2" style="display:block;text-align:center">
 **Table 2** -- Low temperature quantiles for France (1996-2019) and the corresponding median COP of air-to-air heat pumps, from manufacturer data [[16](https://hal-mines-paristech.archives-ouvertes.fr/hal-01796759/document)].
 </span>

<span class="mytext">
This COP of 3 reflects data declared by manufacturers on air-to-air heat pumps, which have the best efficiencies and for which installation conditions are not as critical as for air-to-water heat pumps. One can imagine that, at the scale of France, an average COP of 2.5 would be reached during a severe cold spell. On this point, on-site observation campaigns are needed, especially regarding the performance of air-to-water heat pumps, whose performance depends greatly on the quality of installation and sizing. **These campaigns should be carried out; that is one of my recommendations here.** It must be kept in mind that as long as small electric convectors are not banned from sale, dwellings equipped with heat pumps will often have one or two of these heaters somewhere to cope with severe cold spells; this trend is observed today, with increased thermosensitivity during cold spells.
 </span>

## A few scenarios for the evolution of thermosensitivity depending on the heating systems deployed

<ul> <li> $X_1$: Thermosensitivity to be added to the current one, for a severe cold spell in France [GW/°C]</li>
<li>$X_2$: Change in the peak requirement on the French power system for a severe cold spell (-5°C)</li>
<li> Em: GHG emissions [MtCO2eq/year]</li>
</ul>


 |Scenarios                            |$X_1$    | $X_2$ |Em|
 |:------------------|:-----|:-----|:-----|
 |Gas+oil become HP     |2.8 GW/°C |+56 GW |10.6 |
 |Gas+oil+elec become HP |2.8-0.9 = 1.9 GW/°C   |+38 GW  |9.2   |
 |Gas+elec become HP, oil becomes wood   |(0.6+2.1)- 1.5 = 1.2 GW/°C   |+ 24 GW |10.4   |
|Gas+elec become HP, oil becomes wood, renovation, requirement halved   |(0.6+2.8)/2-1.5 = -0.15 GW/°C   |-3 GW |5.2   |
  {: .wrapstyle  .simple7}
<span class="legendtext" id="CAPTable3" style="display:block;text-align:center">
**Table 3** -- Impact of different heating-system change scenarios, at the scale of France and by 2050, on the evolution of thermosensitivity and on the associated peak requirement. We do not account for the growth in the number of dwellings between now and then, so what we have here is a lower bound. Thermosensitivity is computed assuming a COP of 2.5 for heat pumps during severe cold spells. The emissions used are those of [Table 1](#CAPTable1). They could fall if electricity emissions fall, but electricity emissions will hardly fall if the peak requirement stays the same. All the calculations are performed in the shared code with the data of Table 1 and Appendix 1. Note how very optimistic it is to assume the disappearance of "toaster"-type electric heating (the ones that are not heat pumps). Optimistic too to think that heat pumps can be installed everywhere (for reasons of space or of the external appearance of buildings).
  </span>

<span class="mytext">
[Table 3](#CAPTable3) shows us that the massive deployment of heat pumps has its limits, and that stabilising thermosensitivity is possible with increased use of wood and a substantial renovation campaign. Let us recall that renovations lose much of their value in this context if they are not carried out before, or at the same time as, the installation of heat pumps. Let us add that it could be worthwhile to reduce thermosensitivity relative to its current value. Note also that the reasoning described in Table 3 is a little too theoretical, for several reasons. It does not account for the growth of the requirement, nor for how difficult it would be to install heat pumps in every dwelling (visual constraints, size constraints, etc.), and above all to get rid of electric convectors entirely. It would be enough for 15% of the heat requirement covered by heat pumps in these scenarios to be in fact covered by electric convectors (added in flats) for there to be 30 TWh/year more and 1 GW/°C of additional thermosensitivity.
</span>

<span class="mytext">
We will see in the next section that gas (biogas, then) can be a good solution to help keep thermosensitivity under control without increasing emissions.
</span>

# Gas, a useful carrier for a capacity service

## How can thermosensitive demand be managed?
<span class="mytext">
In addition to the solutions mentioned in [Table 3](#CAPTable3) for lowering thermosensitivity, it is possible to use gas to provide a capacity service. We will now compare several approaches using methane, depending on whether it is used directly for heat production, for electricity production (which is then converted into heat), or for the cogeneration of electricity and heat.
</span>
<div class="mytext">
<ul> <li> the investment cost (€/kW),</li>
<li>the flexibility, i.e. how quickly the capacity can be made available,</li>
<li> how decentralised it is, i.e. its ability to relieve a local constraint on the electricity distribution network </li>
<li> the COPg of the gas-to-heat conversion, assuming that any electricity produced is then converted into heat by a heat pump with a COP of 3. </li>
</ul>
</div>
<span class="mytext">
In the perspective of a decarbonised system this gas should be biomethane, but it could also be hydrogen. Biomass could have a role here too. The corresponding fuel would therefore be very limited in volume, which is why the last criterion gives the quantity of methane consumed per kWh of heat delivered.
</span>

## Gas boiler
<span class="mytext"> The idea is not to keep using the 15 million gas boilers continuously through the winter for a consumption of 160 TWh of gas (see Appendix 1), but to install electric heat pumps for use 90% of the time. It is indeed possible to keep the existing boilers for a capacity service in cases where thermosensitivity is a problem for the balance of the power system. That is the principle of what is called a hybrid heat pump (sold today as a single HP+boiler unit by gas companies). Switching to the gas boiler can be done automatically, with a price signal, or directly at the request of the system operator, during a severe cold spell or when the generation available on the power system is not sufficient to cover demand (severe cold, low wind and sun). The hybrid heat pump consumes little gas because it runs on electricity most of the time, but it delivers a capacity service. The response time of a gas boiler is very short, and one can switch from the heat pump to the gas boiler in a minute. Adding the gas boiler to the heat pump does not necessarily imply an extra cost if the boilers are already there. A gas boiler is not very expensive per installed kW anyway: €125/kW. And for good reason — as already said, capacity and storage are far less of a problem with gas than with electricity. Finally, the gas boiler is decentralised and therefore relieves thermosensitivity-related constraints in the distribution network. The efficiency of a gas boiler is 90% for old boilers and about 100% for condensing boilers, so for the gas boiler we can say COPg=0.9, which, as we shall see, is rather poor. The advantage of the gas boiler is its cost (when a heat distribution system is already present).
</span>

## Electricity generation
<span class="mytext">  A centralised solution for managing the thermosensitivity problem using gas is electricity generation. By centralised we do not mean a system inside the dwelling but a few large power plants at the scale of France. Two families of technologies exist for this: on one side open-cycle gas turbines (OCGT) with an investment cost of the order of €600/kW and an efficiency of the order of 30-35%, and on the other combined-cycle gas plants, which are more expensive at €800/kW of investment but have efficiencies of the order of 55%. If the electricity produced is converted into heat with heat pumps having a COP of 3, the COPg over the whole gas-to-heat conversion chain is COPg=1.5 in the combined-cycle case and COPg=1 in the OCGT case. OCGTs are flexible and can start in less than 15 minutes, whereas it takes a few hours to start a combined cycle. This centralised electricity generation obviously does not relieve constraints in the electricity distribution network.
</span>
## Cogeneration of electricity and heat
<span class="mytext">When producing electricity from gas one can seek to recover the heat produced, which is normally lost. In the case of a centralised system this is called cogeneration, and the heat can be used in a district heating network or for an agricultural activity (essentially heating greenhouses, even if that does not seem compatible with a low-carbon society). In the case of a decentralised system (i.e. at the scale of a dwelling, but centralised within the dwelling) one speaks of micro-cogeneration. Several types of system exist, but micro-cogeneration is not suited to small dwellings and could rather be used for multi-family housing. The electricity/heat ratio (E/H) gives the ratio between the electricity and the useful heat produced. The cost of an individual system using a Stirling internal combustion engine is around €10-15k, offers an efficiency close to 100% and an E/H ratio of 1/6. That means COPg = 1/(5/6 + 1/6 × 1/3) = 1.125.
</span>

<span class="mytext">There are also systems using biomass (such as wood pellets, straw, etc.) rather than gas. Fuel cells use dihydrogen. A fuel cell consumes hydrogen and produces ½ electricity and ½ heat, with an efficiency that can approach 90%. Hydrogen can be produced from electricity with efficiencies of the order of 70-75%, and the interest of the fuel cell in a decarbonised context comes from the storage possibility offered by hydrogen. The fuel cell is not yet a mature technology; in Japan one finds 700 W models for €8k [18], i.e. more than €10,000/kW. The main advantage of the fuel cell is that it uses hydrogen rather than methane. Another advantage is that it has no moving parts, so it is quieter. Note that a cell can be fed indirectly with biogas (by coupling a reformer).
</span>

## Summary table

| |Cost [€/kW]   | Heat efficiency COPg|Centralised-decentralised| Flexibility|
|:------------------|:-----|:-----|:-----|:-----|
|Gas boiler     |150 |0.9|decentralised |1 minute|
|Gas OCGT     |150 |3*0.33= 1|semi-centralised |15 minutes|
|CCGT    |800 |3*1/2 = 1.5|centralised | 3 hours|
|Micro-cogeneration     |[2,3]*$10^3$ |1/(5/6+1/18)  = 1.125|decentralised |follows heat use|
|Fuel cell     |$10^4$ |No use of biogas|decentralised |1 second|
{: .wrapstyle  .simple7}
<span class="legendtext" id="CAPTable4" style="display:block;text-align:center">
**Table 4** -- For the second column, we assume that the electricity produced is used to generate heat in a heat pump with a COP of 3. These capacity costs should be set against the cost of the heat pump (€500-1000/kW for air-to-air, €4000 + €1000/kW for air-to-water) and the capacity cost of nuclear (€[3000-6500]/kW).
 </span>

<span class="mytext">[Table 4](#CAPTable4) summarises the technologies mentioned here. Note that the extra cost of a gas boiler (€125/kW against €1000 to €3000/kW for a heat pump) is not very large, but that if the biogas volume is a strong constraint it may be preferable to use a combined cycle. Gas boilers would bring greater flexibility during the heating season because they start very quickly and can relieve the distribution network, but the combined cycle would be available all year round. Gas boilers would complement solar energy (thermal or photovoltaic) well. Systems involving hydrogen are for now very expensive but these prices will fall. The interest of the hydrogen carrier compared with biogas is that it can be produced by electrolysis from low-carbon electricity at decent efficiencies (70%-75%), whereas the efficiency of producing biogas from electricity (by electrolysis then methanation) is not very good (around 50%). However, hydrogen is less convenient to store and transport; that is a vast question to which we will return.
 </span>
 <span class="mytext">We have already said that there is no transition in buildings without a major reduction in the volume of gas consumed; one can therefore add that there is no transition in buildings without a minimum volume of gas consumed, and perhaps without an increase in the installed capacity of gas boilers and of combined-cycle gas plants. Perhaps recycling existing gas boilers could be relevant to reduce thermosensitivity starting today. These aspects should increasingly be integrated into RTE's studies.
</span>
<span class="mytext">The value of these systems providing capacity support is not really integrated into today's support schemes or regulations, and the construction of new CCGT plants is forbidden by law. Indeed, there is no satisfactory mechanism that passes the thermosensitivity constraint through to investment, even though one of the objectives of the capacity market in the power system is to encourage consumers to keep it under control. That capacity market today reflects costs that are not investment costs (rather annual operating costs, or the cost of bringing a mothballed gas plant back online) and, even if that changes (for instance if heat pumps are deployed massively), one can well imagine that from an individual consumer's point of view there will never be a long-term signal reliable enough to trigger investment. In the case of a massive deployment of heat pumps that price signal will come too late (the gas boilers will already have disappeared). Note that the well-known factor of 2.58 applied today (but which will be reduced in RE2020) to final electricity consumption as a "penalty" is highly debatable physically (depending on whether one considers electric heating electricity to be produced from oil, gas or nuclear, or from a well-chosen combination of these three sources), but it is a safeguard against a future in which 15 million heat pumps would be deployed without regard for the laws of physics, which require supply and demand on the power system to balance at all times — even when it is cold.
</span>
<span class="mytext">Moreover, these hybrid systems could bring additional flexibility to the power system, globally reducing its costs, particularly in a strongly renewable system. Indeed, the capacity lever of using gas in boilers involves very low capacity costs, and CCGTs are also very competitive. Besides, it is not really desirable to try to control electric heating demand simply by switching it off for a few minutes or a few hours (as we try to do today), because that generally results in a temperature drop in the building and a demand peak on switch-on that can be more problematic than the one we sought to shed.
</span>

# Conclusion

<span class="mytext">We have recalled that the energy transition in buildings rests on (i) reducing the heat requirement by improving the efficiency of buildings, (ii) increasing the efficiency of heating systems, mainly through heat pumps (electric or hybrid) or solar thermal, and (iii) using energy carriers whose greenhouse gas emissions are low enough. We have thus been able to reaffirm the major role that renovation, the wood carrier, the electricity carrier and heat pumps must play in the energy transition of buildings. Table 3 shows us that the 3 MtCO2eq/year of emissions from residential heating are within our reach if all the levers are deployed. That means not starting only with the most economically profitable levers (heat pumps) but moving forward in parallel and right now on building renovation (perhaps even making heat pump deployment conditional on it), wood heating, and solar thermal.
</span>

<span class="mytext">We have also shown that hybrid systems, which couple the capacity service of gas with the efficiency of electric systems, are of interest in avoiding a very damaging increase in electrical thermosensitivity. These systems and the constraint they answer are known but often forgotten when the energy transition is discussed. We believe they should be developed and encouraged alongside heat pumps, wood energy and renovations. We believe this should be accompanied by a reasoned development of biogas, with volumes far smaller than those used today but playing an important capacity role. Note how very optimistic it is to assume the disappearance of "toaster"-type electric heating (the ones that are not heat pumps). Optimistic too to think that heat pumps can be installed everywhere (for reasons of space or of the external appearance of buildings) — but we believe that limiting their deployment as little as possible is very important.
</span>


<span class="mytext">Questions fortunately remain: how far should the various solutions be pushed? Should the building stock be flooded with heat pumps? With hybrid heat pumps? Wood stoves? Should the installed capacity of CCGT plants be increased? Should renovations aim only at low-consumption buildings (BBC)? What role can district heating play? What should be the role of wood energy? We have not answered all these questions precisely here, but we have shown the interest of the various avenues while advocating a diversity of solutions. The avenues given will be explored more quantitatively in later posts. In the next post we will try to put forward some estimates concerning building renovation.
</span>


<span class="mytext">We do not claim to have covered the whole question, and some things may have escaped us; we therefore hope that these analyses will help inform the debate and feed exchanges on the subject. Ultimately, it is about collectively giving credit and strength to the measures that will be taken to meet the SNBC's objectives, and doing so constructively (without saying "the government has no strategy"), without letting the complexity of the subject be derailed by this or that pressure from vested interests that would push us to let one carrier or one technology unreasonably take precedence over all the others.
</span>

# Bibliography

[0] [Stratégie nationale bas carbone](https://www.ecologique-solidaire.gouv.fr/strategie-nationale-bas-carbone-snbc)

[1] [Public consultation on the "draft long-term strategy to mobilise investment in the renovation of the national stock of residential and commercial buildings, public and private".](http://www.consultations-publiques.developpement-durable.gouv.fr/projet-de-strategie-a-long-terme-pour-mobiliser-a2136.html Du 17/02/2020 au 10/03/2020)

[2] [2017, Les ménages et la consommation d’énergie.](https://www.statistiques.developpement-durable.gouv.fr/les-menages-et-la-consommation-denergie)

[3] [2019, Visions de l’ADEME 2035-2050.](https://www.ademe.fr/lademe/priorites-strategiques-missions-lademe/scenarios-2030-2050)

[4] [2017, Scenario Negawatt horizon 2050.](https://negawatt.org/Scenario-negaWatt-2017-2050)

[5] https://www.bmwi.de/Redaktion/EN/Publikationen/energy-efficiency-strategy-buildings.pdf?__blob=publicationFile&v=7

[6] [2017, ADEME study on district heating networks](https://www.ademe.fr/avis-lademe-reseaux-chaleur-alimentes-energies-renouvelables-recuperation)

[7] [2009, BIOMASSE FORESTIERE, POPULICOLE ET BOCAGERE DISPONIBLE POUR L’ENERGIE A L’HORIZON 2020](https://www.ademe.fr/sites/default/files/assets/documents/biomasse-forestiere-populicole-et-bocagere-2009.pdf)

[8] [March 2020, décrypter l’énergie, La méthanisation est-elle synonyme d’intensification de l’agriculture et de pollutions ?](https://decrypterlenergie.org/la-methanisation-est-elle-synonyme-dintensification-de-lagriculture-et-de-pollutions)

[9] [February 2020, Bastamag "Produire de l’énergie plutôt que nourrir : comment le lobby du gaz « vert » transforme l’agriculture française."](https://www.bastamag.net/methanisation-lobby-gaz-vert-biogaz-agriculture-energetique-alimentaire)

[10] [ADEME Base Carbone.](https://www.bilans-ges.ademe.fr/documentation/UPLOAD_DOC_FR/index.htm?gaz.htm)

[11] [Afterres 2050 scenario.](https://afterres2050.solagro.org/a-propos/le-projet-afterres-2050/)

[12] [2013, Carbone 4 study on heat pumps.](http://www.carbone4.com/les-pompes-a-chaleur/)

[13] [2019, Electricity demand variability and thermosensitivity.](https://www.energy-alternatives.eu/en/2019/05/24/electricity-demand-variability-and-thermosensitivity.html)

[14] ENEDIS open data [« consommation journalière par catégorie de client »](https://data.enedis.fr/explore/dataset/bilan-electrique-transpose/information/?flg=fr)

[15] 2018, [50% ou 50%](https://jancovici.com/transition-energetique/electricite/50-ou-50/) post by Jean-Marc Jancovici.

[16] [2018 Air conditioners and comfort fans, Review of Regulation 206/2012](https://hal-mines-paristech.archives-ouvertes.fr/hal-01796759/document) and 626/2011 Final report

[17] [Wood energy and fine particle pollution.](https://www.ademe.fr/expertises/energies-renouvelables-enr-production-reseaux-stockage/passer-a-laction/produire-chaleur/dossier/bois-biomasse/bois-energie-qualite-lair)

[18] [Fuel cells sold in Japan.](https://fuelcellsworks.com/news/fcw-exclusive-tokyo-fuel-cell-expo-2019-300000-ene-farms/)

# Appendix 1: state of play of heating systems in France

<span class="mytext">
The information from the French census can be combined with the estimates of heating consumption by energy carrier given in the previous section (Table 1) to obtain the energy description of the French building stock given in Figure 3.
</span>

<span class="text" id="Figure3" style="display:block;text-align:center">
![Image]({{site.baseurl}}/assets/images/Posts/2020-03-22/SNBCChauffageFigureAnnexeParcBatiParClasse.png){:.border}
</span>
<span class="legendtext" id="CAPFigure3" style="display:block;text-align:center">
**Figure 3** -- Composition of the French stock of main residences with respect to heating. Source: INSEE 2016 census and data from Table 1 of the previous section. The "Other" category here is mostly wood.
</span>

<span class="mytext">Note that the importance of electric heating differs depending on whether one looks at the number of dwellings or at energy consumption. About 33% of French dwellings are indeed heated with electricity, but these dwellings, besides being more efficient on average, are smaller than the others, and in terms of final energy requirement electric heating represents less than 40 TWh out of a total of 300 TWh, i.e. less than 15% of the overall energy requirement. It should be recalled here that electricity as a heating mode was introduced into buildings following the nuclear programme, the 1973 oil shock and the first thermal regulations, so rather between 1980 and 2000. Buildings heated with electricity are therefore on average newer and more efficient than the others. Older buildings (those before 1980) heated with electricity do exist but are rather renovated buildings, or buildings where the heating was changed afterwards for economic reasons. Economically, gas has almost always been more favourable for larger and less efficient dwellings: gas heating involves low marginal costs but higher investment. Indeed, the price of a kWh of gas is much lower than that of a kWh of electricity, but gas involves boiler maintenance and investment in a heat distribution system and emitters. Before the arrival of air-to-water heat pumps, these fixed costs barely existed for electric heating. On top of that, the gas capacity delivered to the consumer is never limiting, whereas it is for electricity.
</span>

# Appendix 2: thermosensitivity across sectors

<span class="mytext"> In our discussion of thermosensitivity we focused on the residential sector of electricity demand, and we need to discuss the importance of that sector with respect to thermosensitivity. The ENEDIS open data [14] make it possible to obtain, between 2014 and 2019, the breakdown of daily consumption — and therefore of thermosensitivity — across 5 sectors: Residential, Professional, Large business, SME/SMI and other ("other" being the difference between the France-level data and the sum of the 4 ENEDIS sectors; the "other" sector therefore includes network losses and consumers connected directly to the transmission grid). For the definition of these sectors we refer to the ENEDIS website, but for now we simply wish to observe that residential thermosensitivity has been growing slowly since 2014 (mirroring total thermosensitivity) and that it went from 1.4 GW/°C in 2015 to about 1.5 GW/°C in 2019.
</span>

<span class="text" id="Figure4" style="display:block;text-align:center">
![Image]({{site.baseurl}}/assets/images/Posts/2020-03-22/ThSensParSecteurFigure1.png){:.border}
</span>
<span class="legendtext" id="CAPFigure4" style="display:block;text-align:center">
**Figure 4** --  Thermosensitivity by sector (from ENEDIS data and sectors [14])
</span>
