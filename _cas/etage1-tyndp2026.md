---
title: "Prix de l'électricité et de l'hydrogène en Europe en 2030, 2035 et 2040 : le modèle POMMES sur les scénarios du TYNDP 2026"
date: 2026-10-13
date_affichee: "13 octobre 2026"
lang: fr
ref: cas-etage1-tyndp2026
key: cas-etage1-tyndp2026
permalink: /cas/etage1-tyndp2026.html
accroche: "Notre modèle européen (POMMES, 16 zones, 8 760 heures) sur le scénario National Trends+ du TYNDP 2026 : en 2030, il colle aux prix de l'ENTSO-E (55,7 contre 57,2 €/MWh en France) ; en 2040, il est 18 €/MWh plus bas ; la gestion saisonnière des stocks d'eau et d'hydrogène explique l'essentiel de l'écart sur les heures chères, pas sur le prix moyen. Monotones, 30 années climatiques, diagnostics et séries téléchargeables."
tags: ["TYNDP 2026", "prix de l'électricité", "hydrogène", "POMMES", "scénarios", "ENTSO-E"]
---

<!-- Page engendrée par Communication/Cas/publier.py — ne pas éditer ici :
     modifier Communication/Cas/etage1-tyndp2026/meta.yml, ou le cas lui-même dans https://cloud.minesparis.psl.eu/index.php/s/v6JCrh65WTTDHBW?path=%2Fetage1-tyndp2026%2F2026.10.1-draft -->

<p class="linkedin-meta">mis en ligne le 13 octobre 2026 · <a href="{{ site.baseurl }}/cas.html">tous les cas</a></p>

Quels prix horaires de l'électricité et de l'hydrogène donnent les scénarios du TYNDP 2026 (National Trends+, version provisoire de juin 2026), quand on les fait tourner dans un autre modèle, à coût minimal et en anticipation parfaite ? Et d'où viennent les écarts avec les prix publiés par l'ENTSO-E ?

La page compare nos monotones de prix à celles de NT+ en 2030, 2035 et 2040, montre le nuage des 30 années climatiques du PECD 2026 (le q90 français de 2035 va de 41 à 121 €/MWh selon l'année), et les diagnostics qui expliquent l'écart. Les prix de la page sont ceux de notre modèle ; les courbes du TYNDP ne sont tracées que pour comparaison.

## La page interactive

Une page autonome, en français et en anglais, version 2026.10.1-draft : constats chiffrés, méthode, monotones au point TYNDP et sur les 17 combinaisons prix du gaz × demande, nuage des 30 années climatiques, diagnostics, hypothèses de chaque scénario, téléchargements et paquet pour refaire les calculs.

<p><a class="button button--primary button--rounded" href="{{ site.baseurl }}/assets/cas/etage1-tyndp2026/index.html?lang=fr" target="_blank" rel="noopener">Ouvrir la page interactive dans un onglet</a></p>

## Ce que le cas ne dit pas

- Les prix sont des coûts marginaux d'un modèle à coût minimal, en anticipation parfaite, pas des prix de marché.
- NT+ est une version provisoire ; les prix changeront avec la version finale.
- 16 zones : NO, SE, IT, DK et UK sont agrégées.
- Pour les 27 années climatiques sans sorties NT+, la demande est reconstruite à partir de la température.

## Code

Le code, les données gelées et les hypothèses sont dans le dépôt public [energycommons, etage1-tyndp2026 2026.10.1-draft](https://cloud.minesparis.psl.eu/index.php/s/v6JCrh65WTTDHBW?path=%2Fetage1-tyndp2026%2F2026.10.1-draft).

Pour tout refaire :

```bash
# paquet energycommons etage1-tyndp2026/2026.10.1-draft : repro/scenarios/<scénario>/REFAIRE.md
zstd -dc <paquet>/repro/code/etude-<commit>.tar.zst | tar -x && cd etude-<commit>
zstd -dc <paquet>/repro/entrees/<jeu>.tar.zst | tar -x -C data/t26d/<jeu>/<année>
snakemake -s workflow/Snakefile1 --profile profiles/european_energy_system \
    --config config_workflow=<config.workflow.yaml> --cores 8 <cible dual.nc>
```

## Sources

- [TYNDP 2026 Scenarios, ENTSO-E & ENTSOG (draft, juin 2026), CC BY 4.0](https://2026.entsos-tyndp-scenarios.eu/download/)
- [POMMES, code source (GitLab PERSEE)](https://git.persee.minesparis.psl.eu/energy-alternatives/pommes)
- [Nos séries de prix (energycommons, CC BY 4.0)](https://cloud.minesparis.psl.eu/index.php/s/v6JCrh65WTTDHBW?path=%2Fetage1-tyndp2026%2F2026.10.1-draft)

<small>Code et données du cas sous licence MIT ; textes et figures sous CC BY 4.0 ; les données d'entrée restent sous la licence de leur producteur.</small>
