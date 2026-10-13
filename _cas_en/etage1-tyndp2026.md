---
title: "Electricity and hydrogen prices in Europe in 2030, 2035 and 2040: the POMMES model on the TYNDP 2026 scenarios"
date: 2026-10-13
date_affichee: "13 October 2026"
lang: en
ref: cas-etage1-tyndp2026
key: cas-etage1-tyndp2026-en
permalink: /en/cas/etage1-tyndp2026.html
accroche: "Our European model (POMMES, 16 zones, 8,760 hours) on the National Trends+ scenario of TYNDP 2026: in 2030 it matches the ENTSO-E prices (55.7 against 57.2 €/MWh in France); in 2040 it is 18 €/MWh lower; the seasonal management of water and hydrogen storage explains most of the gap on expensive hours, not on the average price. Duration curves, 30 weather years, diagnostics and downloadable series."
tags: ["TYNDP 2026", "electricity prices", "hydrogen", "POMMES", "scenarios", "ENTSO-E"]
---

<!-- Page engendrée par Communication/Cas/publier.py — ne pas éditer ici :
     modifier Communication/Cas/etage1-tyndp2026/meta.yml, ou le cas lui-même dans https://cloud.minesparis.psl.eu/index.php/s/v6JCrh65WTTDHBW?path=%2Fetage1-tyndp2026%2F2026.10.1-draft -->

<p class="linkedin-meta">published on 13 October 2026 · <a href="{{ site.baseurl }}/en/cas.html">all case studies</a></p>

What hourly electricity and hydrogen prices do the TYNDP 2026 scenarios (National Trends+, June 2026 draft) give when run in another model, at least cost and with perfect foresight? And where do the gaps to the prices published by ENTSO-E come from?

The page compares our price duration curves with the NT+ ones in 2030, 2035 and 2040, shows the cloud of the 30 PECD 2026 climate years (the French 2035 q90 ranges from 41 to 121 €/MWh depending on the year), and the diagnostics that explain the gap. The prices on the page are our model's; TYNDP curves are drawn for comparison only.

## The interactive page

A self-contained page, in French and English, version 2026.10.1-draft: findings, method, duration curves at the TYNDP point and on the 17 gas price × demand combinations, cloud of the 30 climate years, diagnostics, assumptions of each scenario, downloads and a package to redo the calculations.

<p><a class="button button--primary button--rounded" href="{{ site.baseurl }}/assets/cas/etage1-tyndp2026/index.html?lang=en" target="_blank" rel="noopener">Open the interactive page in its own tab</a></p>

## What the case does not say

- Prices are marginal costs of a least-cost model with perfect foresight, not market prices.
- NT+ is a draft; prices will change with the final version.
- 16 zones: NO, SE, IT, DK and UK are aggregated.
- For the 27 climate years without NT+ outputs, demand is rebuilt from temperature.

## Code

The code, the frozen data and the assumptions are in the public repository [energycommons, etage1-tyndp2026 2026.10.1-draft](https://cloud.minesparis.psl.eu/index.php/s/v6JCrh65WTTDHBW?path=%2Fetage1-tyndp2026%2F2026.10.1-draft).

To redo everything:

```bash
# paquet energycommons etage1-tyndp2026/2026.10.1-draft : repro/scenarios/<scénario>/REFAIRE.md
zstd -dc <paquet>/repro/code/etude-<commit>.tar.zst | tar -x && cd etude-<commit>
zstd -dc <paquet>/repro/entrees/<jeu>.tar.zst | tar -x -C data/t26d/<jeu>/<année>
snakemake -s workflow/Snakefile1 --profile profiles/european_energy_system \
    --config config_workflow=<config.workflow.yaml> --cores 8 <cible dual.nc>
```

## Sources

- [TYNDP 2026 Scenarios, ENTSO-E & ENTSOG (draft, June 2026), CC BY 4.0](https://2026.entsos-tyndp-scenarios.eu/download/)
- [POMMES, code source (GitLab PERSEE)](https://git.persee.minesparis.psl.eu/energy-alternatives/pommes)
- [Our price series (energycommons, CC BY 4.0)](https://cloud.minesparis.psl.eu/index.php/s/v6JCrh65WTTDHBW?path=%2Fetage1-tyndp2026%2F2026.10.1-draft)

<small>Case code and data under the MIT licence; texts and figures under CC BY 4.0; input data remain under their producer's licence.</small>
