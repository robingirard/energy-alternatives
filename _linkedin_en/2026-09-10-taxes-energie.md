---
title: "Energy taxes in France: the whole picture"
date: 2026-09-10
date_affichee: "10 September 2026"
lang: en
ref: linkedin-taxes-energie
key: linkedin-taxes-energie
permalink: /en/linkedin/2026-09-10-taxes-energie.html
linkedin: https://www.linkedin.com/feed/update/urn:li:activity:7503706312531410944/
cover: /assets/linkedin/2026-09-10-taxes-energie/figure_facture_fr_mwh_2024_paysage_en.png
accroche: "What a consumer pays per MWh of electricity, gas, wood or fuel, and what the State takes from it: energy taxation follows neither carbon nor energy content."
tags: ["taxation", "energy prices", "electricity", "gas", "wood", "fuels", "France"]
---

<!-- Page engendrée par Communication/Linkedin/publier.py — ne pas éditer ici :
     modifier meta.yml / texte_en.md dans Communication/Linkedin/2026-09-10_taxes-energie/ -->

<p class="linkedin-meta"><a href="https://www.linkedin.com/feed/update/urn:li:activity:7503706312531410944/" target="_blank" rel="noopener"><i class="fab fa-linkedin"></i> See the post and its comments on LinkedIn</a> · published on 10 September 2026 · <a href="/en/linkedin.html">all posts</a></p>

<figure class="linkedin-figure">
<a href="{{ site.baseurl }}/assets/linkedin/2026-09-10-taxes-energie/figure_facture_fr_mwh_2024_paysage_en.png" target="_blank"><img src="{{ site.baseurl }}/assets/linkedin/2026-09-10-taxes-energie/figure_facture_fr_mwh_2024_paysage_en.png" alt="Energy taxes in France: the whole picture" style="max-width:100%;height:auto;"></a>
<figcaption><small>France, 2024, euros per MWh delivered, all taxes included. Four components per energy carrier and customer type: energy and supply, network, excise and other taxes, VAT. The percentage at the end of each bar is the share of levies (excise + VAT) in the price; the network is not counted as a levy.</small></figcaption>
</figure>

## The same figure, to explore

Choose the year, the unit and, above all, the reading: per MWh delivered, as in the figure, or per MWh of useful heat depending on the use, in euros or in CO₂. With a heat pump, one MWh of electricity makes three MWh of heat, and the comparison with gas turns around. Hover a bar for the detail; the "table" view gives the numbers. The chart is generated from the CSV below by `build_interactif.py`.

<iframe src="{{ site.baseurl }}/assets/linkedin/2026-09-10-taxes-energie/interactif_facture.html?lang=en" title="The same figure, to explore" loading="lazy" style="width:100%;height:640px;border:0;"></iframe>

<small><a href="{{ site.baseurl }}/assets/linkedin/2026-09-10-taxes-energie/interactif_facture.html?lang=en" target="_blank">Open the chart in its own tab</a></small>

> The vintage is 2024, the last year for which grid-injected biomethane and international bunker kerosene are published. The 2025 version of the figure, without those two bars, is produced by the same command without `--annee 2024`: household electricity is then at 262 €/MWh including 77 of levies (the excise, being restored after the tariff shield, rises from 25 to 37 €/MWh), gas at 136 including 40.

## The text of the post

Energy taxes in France: a whole-picture view that points to a few imbalances.

I spent part of the summer preparing an introductory energy course for the new I-BE³, the PSL International Bachelor of Environmentally Engaged Engineering, and I will try to share some remarks and figures here as I go. The aim of this one was to make clear that the price of energy generally contains taxes (VAT and others), a network cost and an energy cost. Some taxes are proportional to the price (like VAT), others are "fixed" (proportional to the volume), like the excise duty recently introduced on electricity.

What is striking is how much the taxes differ between energy carriers: energy taxation in France follows neither carbon content nor energy content. It follows the history of each tax, carrier by carrier, and it is also (above all? that will be the next post) tied to the weight that the corresponding energy bill can represent in household budgets.

Gas is taxed very little, especially compared with electricity. The level on kerosene is of course almost revolting, the result of difficult international coordination, but I also find it rather singular that wood is taxed so little, no doubt because of many short supply chains that are hard to trace. And is it logical that biomethane should be taxed so much more than wood?

For electricity and gas these are "average" values, since there are many kinds of contracts. For oil products it is also an average, over time.

Sources: Eurostat (nrg_pc_204_c and 205_c) for electricity and gas, the European Commission's Weekly Oil Bulletin for fuels, the SDES energy balance for wood.

## Sources

- [Eurostat, prix de l'électricité pour les ménages par composante (nrg_pc_204_c)](https://ec.europa.eu/eurostat/databrowser/view/nrg_pc_204_c/default/table)
- [Eurostat, prix du gaz pour les ménages par composante (nrg_pc_205_c) ; séries 202_c et 203_c pour les industriels](https://ec.europa.eu/eurostat/databrowser/view/nrg_pc_205_c/default/table)
- [Commission européenne, Weekly Oil Bulletin (carburants et fioul, prix avec et hors taxes)](https://energy.ec.europa.eu/data-and-analysis/weekly-oil-bulletin_en)
- [SDES, Bilan énergétique de la France (bois de chauffage : dépense et fiscalité des ménages)](https://www.statistiques.developpement-durable.gouv.fr/bilan-energetique-de-la-france-en-2025-donnees-provisoires)
- [Code des impositions sur les biens et services, art. L. 312-9 et suivants (champ de l'accise sur les énergies)](https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000044595989/LEGISCTA000044598327/)

## Data

- [`facteurs_co2.csv`]({{ site.baseurl }}/assets/linkedin/2026-09-10-taxes-energie/facteurs_co2.csv) — The emission factors used by the interactive chart (kg CO₂e per MWh, ADEME Base Empreinte, upstream included), with their LHV/GCV basis and source.
- [`donnees_facture_fr_mwh_2024_2025.csv`]({{ site.baseurl }}/assets/linkedin/2026-09-10-taxes-energie/donnees_facture_fr_mwh_2024_2025.csv) — The twelve bars of the figure, 2024 and 2025 vintages, in €/MWh: energy, network, excise, VAT, price incl. taxes, levies and their share.

## Code

The code that produces the figure is in the public repository [linkedinposts](https://git.persee.minesparis.psl.eu/energy-alternatives/linkedinposts/-/tree/main/energy_taxes), folder `energy_taxes`.

To reproduce the figure:

```bash
cd energy_taxes
python3 prepare_eurostat.py      # électricité et gaz, API Eurostat
python3 prepare_carburants.py    # carburants et fioul, Weekly Oil Bulletin
python3 prepare_bilan_sdes.py    # bois de chauffage, bilan SDES
python3 plot_facture.py --unite mwh --paysage --lang fr --annee 2024
python3 plot_facture.py --unite mwh --paysage --annee 2024   # version anglaise
```

The three `prepare_*` scripts download the sources and write the CSV files in `data/processed/`; those are in the repository, so `plot_facture.py` runs straight away.

All files of this post (figures, data, scripts) are in the folder [2026-09-10-taxes-energie](https://git.persee.minesparis.psl.eu/energy-alternatives/linkedinposts/-/tree/main/posts/2026-09-10-taxes-energie) of the public repository.

<small>Code under the MIT licence; texts and figures under CC BY 4.0; data remain under their producer's licence.</small>
