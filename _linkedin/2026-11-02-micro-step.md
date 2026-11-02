---
title: "Petites STEP : 21 115 sites de stockage possibles en Europe, et ce que le karst change"
date: 2026-11-02
date_affichee: "2 novembre 2026"
lang: fr
ref: linkedin-micro-step
key: linkedin-micro-step
permalink: /linkedin/2026-11-02-micro-step.html
linkedin: https://www.linkedin.com/feed/update/urn:li:ugcPost:7522950533511454721/
cover: /assets/linkedin/2026-11-02-micro-step/figure_micro_step_carte_fr.png
accroche: "21 115 sites de 5 à 100 MWh, 0,40 TWh dont 0,24 dans l'UE : le premier inventaire européen des petites STEP, publié dans Applied Energy. Le post qui annonce le billet de blog."
titre_recherche: "Combien de petites STEP en Europe ? Le premier inventaire européen"
tags: ["petites STEP", "stockage d'électricité", "STEP", "karst", "Europe", "Applied Energy"]
---

<!-- Page engendrée par Communication/Linkedin/publier.py — ne pas éditer ici :
     modifier meta.yml / texte_fr.md dans Communication/Linkedin/2026-11-02_micro-step/ -->

<p class="linkedin-meta"><a href="https://www.linkedin.com/feed/update/urn:li:ugcPost:7522950533511454721/" target="_blank" rel="noopener"><i class="fab fa-linkedin"></i> Voir le post et ses commentaires sur LinkedIn</a> · publié le 2 novembre 2026 · <a href="/linkedin.html">tous les posts</a></p>

<figure class="linkedin-figure">
<a href="{{ site.baseurl }}/assets/linkedin/2026-11-02-micro-step/figure_micro_step_carte_fr.png" target="_blank"><img src="{{ site.baseurl }}/assets/linkedin/2026-11-02-micro-step/figure_micro_step_carte_fr.png" alt="Petites STEP : 21 115 sites de stockage possibles en Europe, et ce que le karst change" style="max-width:100%;height:auto;"></a>
<figcaption><small>Énergie stockable des 21 115 sites de petites STEP de la référence, en GWh pour 1 000 km², sur une grille de 50 km. Sites de 5 à 100 MWh, cuvettes sur karst exclues. Girard, Rogeau & Quaranta, Applied Energy, 2026.</small></figcaption>
</figure>

## Le texte du post

Où peut-on encore stocker de l'électricité en remontant de l'eau, en Europe ? Les grands sites sont pris. Restent les petits : un lac et une cuvette naturelle, ou deux cuvettes, distants de quelques kilomètres, avec quelques dizaines de mètres de dénivelé.

Avec Antoine Rogeau et Emanuele Quaranta (JRC), nous venons de publier dans Applied Energy, en accès libre, le premier inventaire européen de ces petites STEP. Sur 37 pays, notre méthode retient 21 115 sites de 5 à 100 MWh, qui stockeraient ensemble 0,40 TWh. Dans l'Union européenne, 0,24 TWh : un peu moins d'une heure de consommation d'électricité, mais de l'ordre de la moitié du stockage réellement utilisable de toutes les grandes STEP de l'Union.

Trois choses que j'ai apprises en faisant ce travail :

Le karst. Notre algorithme cherche des cuvettes fermées, et les plateaux calcaires en sont pleins. Mais une doline est fermée parce que l'eau s'en va par le fond. En 2017, notre étude française retenait les cuvettes des Grands Causses : c'étaient des dolines. Écarter les bassins à construire sur du karst divise le gisement par 2,5.

Le relief numérique. Un modèle de surface, qui suit la cime des arbres et le toit des bâtiments, invente des cuvettes : en France, il donne cinq fois le gisement calculé sur le relief de l'IGN. Et même un modèle corrigé ne suffit pas partout : en Norvège et en Suède, passer au lidar national retire 72 % de l'énergie.

Le coût. Environ 1 150 € par kWh de stockage pour le site médian, selon notre estimation indicative : plusieurs fois une grande STEP. Et dans notre modèle, ce n'est pas le bassin qui coûte, ce sont les tuyaux : des kilomètres de conduite pour quelques mégawatts.

C'est donc un gisement réel, mais cher, souvent loin des consommateurs, et que les études de terrain ne pourront que réduire : un outil pour savoir où chercher, pas une promesse. Les données et le code sont ouverts.

J'explique tout cela, karst compris, dans un billet de blog (lien en commentaire). Article : Girard, Rogeau et Quaranta, Applied Energy, 2026.

## Le billet complet

[Petites STEP : 21 115 sites de stockage possibles en Europe, et ce que le karst change]({{ site.baseurl }}/2026/11/02/petites-STEP-europe.html)

## Sources

- [R. Girard, A. Rogeau, E. Quaranta, « Distributed small-reservoir pumped-storage hydropower in Europe: a GIS screening under drawdown and karst constraints », Applied Energy 427 (2027) 129193 (accès libre)](https://doi.org/10.1016/j.apenergy.2026.129193)
- [Données : couches de sites candidats par pays et résultats des scénarios (Zenodo)](https://doi.org/10.5281/zenodo.21326693)
- [Code : pipeline R/Snakemake (licence MIT)](https://git.persee.minesparis.psl.eu/energy-alternatives/Micro-Hydo-Pumped-Storage-EU)

## Code

Pour refaire la figure :

```bash
# Script : Blog/atelier/micro-step/figures/cartes/figure_linkedin_carte_europe.R
# (dérivé de workflow/analysis/fig_grid_energy_map.R du dépôt MicroSTEP, commit 5030284)
MICROSTEP_BLOG_LANG=fr OUT_PNG=$PWD/figure_micro_step_carte_fr.png Rscript figure_linkedin_carte_europe.R   # ou en
```

La figure redessine la figure 4 de l'article à partir des résultats archivés sur Zenodo ; toutes les figures du billet sont détaillées dans le billet lui-même.

Tous les fichiers de ce post (figures, données, scripts) sont dans le dossier [2026-11-02-micro-step](https://git.persee.minesparis.psl.eu/energy-alternatives/linkedinposts/-/tree/main/posts/2026-11-02-micro-step) du dépôt public.

<small>Code sous licence MIT ; textes et figures sous CC BY 4.0 ; les données restent sous la licence de leur producteur.</small>
