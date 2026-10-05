---
title: "Fos-sur-Mer: what is hydrogen storage worth, and what does doing without gas cost?"
date: 2026-10-05
date_affichee: "5 October 2026"
lang: en
ref: cas-fos-h2-stockage
key: cas-fos-h2-stockage-en
permalink: /en/cas/fos-h2-stockage.html
cover: /assets/cas/fos-h2-stockage/figure_valeur_stockage_en.png
accroche: "If Fos-sur-Mer made its 83.5 kt of hydrogen a year entirely by electrolysis, the Manosque salt cavern would be worth €0.48/kg at €1,350/kW and €1.34/kg at €417/kW. Without a mandate it is worth nothing: the gas reformer already provides flexibility. A page to play with CAPEX, gas and the weather year."
tags: ["hydrogen", "electrolysis", "storage", "salt cavern", "Fos-sur-Mer", "POMMES", "electricity prices"]
---

<!-- Page engendrée par Communication/Cas/publier.py — ne pas éditer ici :
     modifier Communication/Cas/fos-h2-stockage/meta.yml, ou le cas lui-même dans https://git.persee.minesparis.psl.eu/energy-alternatives/pommes_studies/pommes-case-studies/-/tree/main/cas_fos_h2_stockage -->

<p class="linkedin-meta">published on 5 October 2026 · <a href="{{ site.baseurl }}/en/cas.html">all case studies</a></p>

The Fos-sur-Mer industrial zone uses **83.5 kt of hydrogen a year** (refining, methanol), made today by a natural-gas reformer, plus some by-product hydrogen from the chlorine plant. An electrolyser could make it instead, buying electricity at the hourly price. Two questions:

1. **What is a hydrogen storage worth** — the Manosque salt cavern, 110 km away — to that electrolyser, and how does that value depend on its investment cost (CAPEX)?
2. **What does it cost to do without the gas reformer** as a back-up, i.e. to impose 100 % electrolytic hydrogen?

Hourly French electricity prices come from a POMMES model of the 2030 European power system (11 weather years, three gas prices; PhD of Thibaut Knibiehly, PERSEE). The hub itself is a one-node hourly linear programme, the *reduced model*, which chooses the electrolyser and cavern sizes and their hourly operation at least annual cost. It reproduces the full POMMES modelling of Fos at every point POMMES solved.

## The interactive page

Choose the electrolyser CAPEX, the gas price (it sets the spread between expensive and cheap hours), the hydrogen volume and the cavern cap: the value of storage reads in €/kg, on average and for each of the 11 weather years. The second part imposes a growing share of electrolysis and shows the extra cost against the unconstrained hub. The sliders read grids precomputed by the reduced model; nothing is recomputed in the browser.

<p><a class="button button--primary button--rounded" href="{{ site.baseurl }}/assets/cas/fos-h2-stockage/page.html?lang=en" target="_blank" rel="noopener">Open the interactive page in its own tab</a></p>

<iframe src="{{ site.baseurl }}/assets/cas/fos-h2-stockage/page.html?lang=en" title="The interactive page" loading="lazy" scrolling="no" style="width:100%;height:1100px;border:1px solid #e1e0d9;" onload="var f=this;function h(){try{f.style.height=f.contentDocument.documentElement.scrollHeight+'px'}catch(e){f.scrolling='auto'}}h();new ResizeObserver(h).observe(f.contentDocument.body)"></iframe>

## The notebook

The full story, executed with its outputs: hourly prices, one run of the reduced model step by step, the check against the POMMES modelling, the two questions, a simplified rule that needs no solver, and what the case does not say.

<p><a class="button button--outline-primary button--rounded" href="{{ site.baseurl }}/assets/cas/fos-h2-stockage/notebook.html" target="_blank" rel="noopener">Read the executed notebook</a></p>

<small><a href="{{ site.baseurl }}/assets/cas/fos-h2-stockage/notebook.ipynb">download the .ipynb</a> · <a href="https://git.persee.minesparis.psl.eu/energy-alternatives/pommes_studies/pommes-case-studies/-/blob/main/cas_fos_h2_stockage/notebook.ipynb" target="_blank" rel="noopener">see it on GitLab</a></small>

## Figures

<figure class="linkedin-figure">
<a href="{{ site.baseurl }}/assets/cas/fos-h2-stockage/figure_valeur_stockage_en.png" target="_blank"><img src="{{ site.baseurl }}/assets/cas/fos-h2-stockage/figure_valeur_stockage_en.png" alt="The value of the Manosque cavern against electrolyser CAPEX" style="max-width:100%;height:auto;"></a>
<figcaption><small>Left, the value of the cavern in €/kg of hydrogen, under a 100% electrolysis mandate, against electrolyser CAPEX, for three gas prices (15, 30 and 65 €/MWh): reduced-model curves, POMMES-modelling dots. Right, at the three CAPEX levels solved by POMMES, the same value without and with the mandate. Fos without the steel plant, 83.5 kt/yr, 2030 European power system, average of 11 weather years.</small></figcaption>
</figure>

## What the case does not say

- Electricity prices are **exogenous**: the electrolyser does not move them.
- The cavern is capped at **200 GWh**, a declared and not a geological cap: the value is a lower bound.
- Fos is an **isolated node**: a hydrogen network (to Lyon, Spain) would change the value of local storage.
- The EU hourly-correlation rule for renewable hydrogen (RFNBO) is not modelled.
- One power system (2030): the weather years change, the fleet does not. Replaying the case with the TYNDP 2026 scenarios is the natural next step.

## Posts about it

- [Hydrogen infrastructure: what is storage worth? (LinkedIn, 5 October 2026)](/en/linkedin/2026-10-05-pommes-fos-1-valeur-stockage.html)

## Data

- [donnees_valeur_stockage_pommes.csv]({{ site.baseurl }}/assets/cas/fos-h2-stockage/donnees_valeur_stockage_pommes.csv) — value of the cavern in the POMMES modelling, by CAPEX, gas price and mandate: mean, minimum and maximum over the 11 years.
- [donnees_valeur_stockage_modele_reduit.csv]({{ site.baseurl }}/assets/cas/fos-h2-stockage/donnees_valeur_stockage_modele_reduit.csv) — the same value in the reduced model, by CAPEX (200 to 2,000 €/kW), gas price, hydrogen volume and cavern cap.
- [hypotheses.yaml]({{ site.baseurl }}/assets/cas/fos-h2-stockage/hypotheses.yaml) — every assumption of the case: value, unit, source, status.

## Code

The code, the frozen data and the assumptions are in the public repository [pommes-case-studies](https://git.persee.minesparis.psl.eu/energy-alternatives/pommes_studies/pommes-case-studies/-/tree/main/cas_fos_h2_stockage).

To redo everything:

```bash
git clone https://git.persee.minesparis.psl.eu/energy-alternatives/pommes_studies/pommes-case-studies.git
git clone --branch regles-gelees-v2-2026-10-03 https://git.persee.minesparis.psl.eu/energy-alternatives/regles_parametriques.git
export REGLES_PARAMETRIQUES=$PWD/regles_parametriques OMP_NUM_THREADS=1
cd pommes-case-studies/cas_fos_h2_stockage
python grille.py stockage && python grille.py hybride   # le modèle réduit (HiGHS ; --solveur gurobi plus rapide)
python analyse.py && python figures.py && python build_page.py
jupyter nbconvert --to notebook --execute --inplace notebook.ipynb
```

The equations and costs of the reduced model are in the public module [regles_parametriques](https://git.persee.minesparis.psl.eu/energy-alternatives/regles_parametriques); the case calls them without copying them.

## Sources

- [POMMES, code source (GitLab PERSEE)](https://git.persee.minesparis.psl.eu/energy-alternatives/pommes)
- [The case: code, frozen data, assumptions (pommes-case-studies)](https://git.persee.minesparis.psl.eu/energy-alternatives/pommes_studies/pommes-case-studies/-/tree/main/cas_fos_h2_stockage)
- [Parametric rules: the reduced model and its costs (tag regles-gelees-v2-2026-10-03)](https://git.persee.minesparis.psl.eu/energy-alternatives/regles_parametriques)
- [MINES Paris – PSL Executive Education, Evolution of the power system in the context of the energy transition (30/11–04/12/2026, in French)](https://executive-education.minesparis.psl.eu/formations/evolution-du-systeme-electrique-dans-un-contexte-de-transition-energetique/)

<small>Case code and data under the MIT licence; texts and figures under CC BY 4.0; input data remain under their producer's licence.</small>
