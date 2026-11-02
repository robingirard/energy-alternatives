---
title: "Small pumped storage: 21,115 possible sites in Europe, and what karst changes"
date: 2026-11-02
date_affichee: "2 November 2026"
lang: en
ref: linkedin-micro-step
key: linkedin-micro-step
permalink: /en/linkedin/2026-11-02-micro-step.html
linkedin: https://www.linkedin.com/feed/update/urn:li:ugcPost:7522950533511454721/
cover: /assets/linkedin/2026-11-02-micro-step/figure_micro_step_carte_en.png
accroche: "21,115 sites of 5 to 100 MWh, 0.40 TWh of which 0.24 in the EU: the first European screening of small pumped-storage sites, published in Applied Energy. The post announcing the blog article."
titre_recherche: "How much small pumped hydro storage in Europe? A first continental screening"
tags: ["small pumped storage", "electricity storage", "pumped hydro", "karst", "Europe", "Applied Energy"]
---

<!-- Page engendrée par Communication/Linkedin/publier.py — ne pas éditer ici :
     modifier meta.yml / texte_en.md dans Communication/Linkedin/2026-11-02_micro-step/ -->

<p class="linkedin-meta"><a href="https://www.linkedin.com/feed/update/urn:li:ugcPost:7522950533511454721/" target="_blank" rel="noopener"><i class="fab fa-linkedin"></i> See the post and its comments on LinkedIn</a> · published on 2 November 2026 · <a href="/en/linkedin.html">all posts</a></p>

<figure class="linkedin-figure">
<a href="{{ site.baseurl }}/assets/linkedin/2026-11-02-micro-step/figure_micro_step_carte_en.png" target="_blank"><img src="{{ site.baseurl }}/assets/linkedin/2026-11-02-micro-step/figure_micro_step_carte_en.png" alt="Small pumped storage: 21,115 possible sites in Europe, and what karst changes" style="max-width:100%;height:auto;"></a>
<figcaption><small>Storable energy of the 21,115 small pumped-storage sites of the reference portfolio, in GWh per 1,000 km², on a 50 km grid. Sites of 5 to 100 MWh, hollows on karst excluded. Girard, Rogeau & Quaranta, Applied Energy, 2026.</small></figcaption>
</figure>

## The text of the post

Where can Europe still store electricity by pumping water uphill? The large sites are taken. What is left are the small ones: a lake and a natural depression, or two depressions, a few kilometres apart, with a few tens of metres of head.

With Antoine Rogeau and Emanuele Quaranta (JRC), we have just published in Applied Energy, open access, the first European inventory of these small pumped-storage sites. Across 37 countries, our method retains 21,115 sites of 5 to 100 MWh, which together would store 0.40 TWh. In the European Union, 0.24 TWh: a little less than one hour of electricity consumption, but of the order of half the truly usable storage of all the EU's large pumped-storage plants.

Three things I learned doing this work:

Karst. Our algorithm looks for closed depressions, and limestone plateaus are full of them. But a doline is closed because the water drains away through its floor. In 2017, our French study kept the depressions of the Grands Causses: they were dolines. Excluding reservoirs to be built on karst divides the resource by 2.5.

The elevation model. A surface model, which follows treetops and rooftops, invents depressions: in France, it gives five times the resource computed on the national IGN terrain model. And even a corrected model is not enough everywhere: in Norway and Sweden, switching to national lidar removes 72% of the energy.

Cost. About €1,150 per kWh of storage for the median site, by our indicative estimate: several times a large pumped-storage plant. And in our model, it is not the reservoir that costs, it is the pipes: kilometres of waterway for a few megawatts.

So this is a real resource, but an expensive one, often far from consumers, and one that field studies can only shrink: a tool for knowing where to look, not a promise. The data and code are open.

I explain all this, karst included, in a blog post (link in the comments). Paper: Girard, Rogeau and Quaranta, Applied Energy, 2026.

## The full article

[Small pumped storage: 21,115 possible sites in Europe, and what karst changes]({{ site.baseurl }}/en/2026/11/02/small-pumped-storage-europe.html)

## Sources

- [R. Girard, A. Rogeau, E. Quaranta, « Distributed small-reservoir pumped-storage hydropower in Europe: a GIS screening under drawdown and karst constraints », Applied Energy 427 (2027) 129193 (accès libre)](https://doi.org/10.1016/j.apenergy.2026.129193)
- [Données : couches de sites candidats par pays et résultats des scénarios (Zenodo)](https://doi.org/10.5281/zenodo.21326693)
- [Code : pipeline R/Snakemake (licence MIT)](https://git.persee.minesparis.psl.eu/energy-alternatives/Micro-Hydo-Pumped-Storage-EU)

## Code

To reproduce the figure:

```bash
# Script : Blog/atelier/micro-step/figures/cartes/figure_linkedin_carte_europe.R
# (dérivé de workflow/analysis/fig_grid_energy_map.R du dépôt MicroSTEP, commit 5030284)
MICROSTEP_BLOG_LANG=fr OUT_PNG=$PWD/figure_micro_step_carte_fr.png Rscript figure_linkedin_carte_europe.R   # ou en
```

The figure redraws Figure 4 of the article from the results archived on Zenodo; all figures of the article are detailed in the blog article itself.

All files of this post (figures, data, scripts) are in the folder [2026-11-02-micro-step](https://git.persee.minesparis.psl.eu/energy-alternatives/linkedinposts/-/tree/main/posts/2026-11-02-micro-step) of the public repository.

<small>Code under the MIT licence; texts and figures under CC BY 4.0; data remain under their producer's licence.</small>
