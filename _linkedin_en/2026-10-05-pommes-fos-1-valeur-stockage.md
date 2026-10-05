---
title: "What is hydrogen storage worth? The Fos-sur-Mer case"
date: 2026-10-05
date_affichee: "5 October 2026"
lang: en
ref: linkedin-pommes-fos-1-valeur-stockage
key: linkedin-pommes-fos-1-valeur-stockage
permalink: /en/linkedin/2026-10-05-pommes-fos-1-valeur-stockage.html
linkedin: https://www.linkedin.com/feed/update/urn:li:share:7512780999789879296/
cover: /assets/linkedin/2026-10-05-pommes-fos-1-valeur-stockage/figure_valeur_stockage_en.png
accroche: "If Fos-sur-Mer had to make its 83.5 kt of hydrogen a year entirely by electrolysis, the Manosque salt cavern would be worth €0.48/kg with an electrolyser at €1,350/kW and gas at €30/MWh, €1.34/kg at €417/kW, and from €0.06 to €1.71/kg as gas goes from €15 to €65/MWh. Without a mandate, at the central electrolyser price, it is worth nothing: the gas reformer already provides flexibility."
tags: ["hydrogen", "electrolysis", "storage", "salt cavern", "Fos-sur-Mer", "POMMES", "electricity prices", "training"]
---

<!-- Page engendrée par Communication/Linkedin/publier.py — ne pas éditer ici :
     modifier meta.yml / texte_en.md dans Communication/Linkedin/2026-10-05_pommes-fos-1-valeur-stockage/ -->

<p class="linkedin-meta"><a href="https://www.linkedin.com/feed/update/urn:li:share:7512780999789879296/" target="_blank" rel="noopener"><i class="fab fa-linkedin"></i> See the post and its comments on LinkedIn</a> · published on 5 October 2026 · <a href="/en/linkedin.html">all posts</a></p>

<figure class="linkedin-figure">
<a href="{{ site.baseurl }}/assets/linkedin/2026-10-05-pommes-fos-1-valeur-stockage/figure_valeur_stockage_en.png" target="_blank"><img src="{{ site.baseurl }}/assets/linkedin/2026-10-05-pommes-fos-1-valeur-stockage/figure_valeur_stockage_en.png" alt="What is hydrogen storage worth? The Fos-sur-Mer case" style="max-width:100%;height:auto;"></a>
<figcaption><small>Two charts. Left, the value of the Manosque cavern in euros per kg of hydrogen, under a 100% electrolysis mandate, against electrolyser CAPEX from 200 to 2,000 €/kW, for three gas prices (15, 30 and 65 €/MWh): reduced-model curves, POMMES-modelling dots. With gas at €30/MWh, €1.34/kg at €417/kW and €0.48/kg at €1,350/kW. Right, at the three CAPEX levels solved by POMMES, the same value without a mandate (0.25, 0.03 and 0 €/kg) and under the mandate (1.34, 0.70 and 0.48 €/kg). Fos without the steel plant, 83.5 kt/yr of hydrogen, 2030 European power system, average of 11 weather years.</small></figcaption>
</figure>

> A textbook case, not a forecast. Electricity prices are exogenous: they do not react to the electrolyser. The cavern is capped at 200 GWh, a declared and not geological cap: the value is a lower bound. Fos is an isolated node, with no hydrogen network. The EU hourly-correlation rule (RFNBO) is not modelled.

## The text of the post

Producing hydrogen by electrolysing water is still more a plan than a reality today, yet people already talk about infrastructure to transport and store hydrogen. Until now, industries that use hydrogen have hardly needed any: in refineries, ammonia fertiliser plants or methanol plants. And for good reason: they make it continuously from gas, on site. In Europe, close to nine tenths of hydrogen is produced at the very site that consumes it.

Hydrogen networks do already exist: private networks, built by industrial gas companies, linking several steam reformers to several customers: refineries, petrochemicals, ammonia. They also collect by-product hydrogen from chlor-alkali plants and steam crackers, and the reason for building them, beyond pooling and economies of scale, is often reliability: if one unit stops, another takes over through the pipeline. Pure hydrogen has even been stored in salt caverns since 1972 at Teesside (about 25 GWh) and since 1983 in Texas, where three caverns are now in service, one of them over 120 GWh. But these are back-up reserves for petrochemicals, not arbitrage between expensive and cheap hours, and this infrastructure stays at the scale of one industrial basin. In Europe, only one tenth of hydrogen travels, by pipeline, mostly between Rotterdam, Antwerp and northern France, or by truck.

In fact, and this is a first-order point, hydrogen infrastructure only has value if hydrogen is to be made almost exclusively by electrolysis. Yet the largest electrolyser being built in France today, whose start-up should already have been announced, Air Liquide's (200 MW, the Normand'Hy project), will be connected to Air Liquide's local network, hybridised with its reformers, but with no storage, and the e-SAF projects under discussion today all plan to go without hydrogen storage and without infrastructure.

Yet the value is undeniable, provided that (1) hybridisation and the use of methane are abandoned altogether (which comes at an extra cost and, in the short term, does not necessarily mean decarbonisation) and (2) electrolyser CAPEX falls. With 100% electrolysis and today's CAPEX, the cost reduction that storage brings is around 15%. With lower CAPEX, it can rise to 20 to 40%.

In the hands-on sessions of the course week I teach in December (registration link in the comments), you will be able to use our tool POMMES and its AI assistant to model the economic value of storage in several configurations. You can also look at the web page that presents the results of an open-access notebook if you are interested! Links in the comments.

## Sources

- [Le cas complet : page interactive, notebook, données et code (section « Cas d'étude » du blog)](https://www.energy-alternatives.eu/cas/fos-h2-stockage.html)
- [POMMES, code source (GitLab PERSEE)](https://git.persee.minesparis.psl.eu/energy-alternatives/pommes)
- [MINES Paris – PSL Executive Education, Évolution du système électrique dans un contexte de transition énergétique (30/11–04/12/2026)](https://executive-education.minesparis.psl.eu/formations/evolution-du-systeme-electrique-dans-un-contexte-de-transition-energetique/)
- [Règles paramétriques simples : le modèle réduit et ses coûts (module regles, étiquette regles-gelees-v2-2026-10-03)](https://git.persee.minesparis.psl.eu/energy-alternatives/regles_parametriques)

## Data

- [`donnees_valeur_stockage_pommes.csv`]({{ site.baseurl }}/assets/linkedin/2026-10-05-pommes-fos-1-valeur-stockage/donnees_valeur_stockage_pommes.csv) — The value of the cavern in the POMMES modelling, by electrolyser CAPEX, gas price and mandate (0 or 100%): mean, minimum and maximum over the 11 weather years. These are the dots and bars.
- [`donnees_valeur_stockage_modele_reduit.csv`]({{ site.baseurl }}/assets/linkedin/2026-10-05-pommes-fos-1-valeur-stockage/donnees_valeur_stockage_modele_reduit.csv) — The value of the cavern in the reduced model, by CAPEX (200 to 2,000 €/kW), gas price, hydrogen volume and cavern cap: mean, minimum and maximum over the 11 years. These are the curves, and the interactive page.

## Code

To reproduce the figure:

```bash
cd pommes-case-studies/cas_fos_h2_stockage
python grille.py stockage          # le modèle réduit, ≈ 3 500 LP horaires (HiGHS)
python analyse.py                  # les chiffres du post : results/chiffres.json
python figures.py                  # la figure, les deux langues
```

The reduced model is a one-node hourly linear programme (electrolyser, cavern, flat demand) that reproduces the POMMES modelling at the points it solved. Its equations and costs are in the regles_parametriques module.

All files of this post (figures, data, scripts) are in the folder [2026-10-05-pommes-fos-1-valeur-stockage](https://git.persee.minesparis.psl.eu/energy-alternatives/linkedinposts/-/tree/main/posts/2026-10-05-pommes-fos-1-valeur-stockage) of the public repository.

<small>Code under the MIT licence; texts and figures under CC BY 4.0; data remain under their producer's licence.</small>
