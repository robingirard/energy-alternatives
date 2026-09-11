---
title: "PFAS, heat pumps and air conditioning: an accurate headline that misleads"
date: 2026-09-09
date_affichee: "9 September 2026"
lang: en
ref: linkedin-pfas-pompes-a-chaleur
key: linkedin-pfas-pompes-a-chaleur
permalink: /en/linkedin/2026-09-09-pfas-pompes-a-chaleur.html
linkedin: https://www.linkedin.com/feed/update/urn:li:activity:7503181960106647552/
cover: /assets/linkedin/2026-09-09-pfas-pompes-a-chaleur/figure_pfas_emissions_europe_en.png
accroche: "Of 68,000 tonnes of PFAS emitted each year in Europe, close to 39,000 come from refrigerant fluorinated gases. But that total aggregates uses that have almost nothing in common. The post announcing the blog article."
tags: ["PFAS", "heat pumps", "air conditioning", "refrigerants", "TFA", "European regulation"]
---

<!-- Page engendrée par Communication/Linkedin/publier.py — ne pas éditer ici :
     modifier meta.yml / texte_en.md dans Communication/Linkedin/2026-09-09_pfas-pompes-a-chaleur/ -->

<p class="linkedin-meta"><a href="https://www.linkedin.com/feed/update/urn:li:activity:7503181960106647552/" target="_blank" rel="noopener"><i class="fab fa-linkedin"></i> See the post and its comments on LinkedIn</a> · published on 9 September 2026 · <a href="/en/linkedin.html">all posts</a></p>

<figure class="linkedin-figure">
<a href="{{ site.baseurl }}/assets/linkedin/2026-09-09-pfas-pompes-a-chaleur/figure_pfas_emissions_europe_en.png" target="_blank"><img src="{{ site.baseurl }}/assets/linkedin/2026-09-09-pfas-pompes-a-chaleur/figure_pfas_emissions_europe_en.png" alt="PFAS, heat pumps and air conditioning: an accurate headline that misleads" style="max-width:100%;height:auto;"></a>
<figcaption><small>Annual PFAS emissions in Europe by use, in tonnes per year, from the opinions of ECHA's Risk Assessment Committee (RAC), 2025-2026. In blue, the uses where the PFAS is a refrigerant.</small></figcaption>
</figure>

## The text of the post

"Heat pumps and air conditioning are the leading source of PFAS emissions in Europe." That was the headline of a column in Le Monde last June. The headline is accurate. And yet it misleads. That is what I explain in this new article on my blog.

Two regulations now overlap on the same fluids. The "F-gas" regulation targets the climate: it reasons in terms of warming potential, and therefore lets through the HFOs, in which manufacturers have invested and which degrade into TFA. The PFAS restriction targets persistence and calls that choice into question. Both are necessary. But applied without staging, they squeeze the energy transition at the very moment when heat pumps must be deployed on a large scale to move away from gas and oil, and air conditioning to withstand heat waves.

Of 68,000 tonnes of PFAS emitted each year in Europe, close to 39,000 come from refrigerant fluorinated gases. Except that this total aggregates uses that have almost nothing in common. Three things change when you look at the detail:

Counting tonnes of gas or counting the TFA actually formed (the molecule that causes the problem) does not give the same ranking, and the reversal is really very large.

R32, which equips most recent air conditioners and heat pumps, is not a PFAS and does not produce TFA.

The first lever is not the refrigerant of new machines.

ECHA's Risk Assessment Committee itself writes that a ban without derogation "is probably not applicable". The real debate of the next two years is therefore about calibrating the derogations, use by use. That is what I discuss in the article. I am also preparing more "quantitative" work.

## The full article

[PFAS, heat pumps and air conditioning: an accurate headline that misleads]({{ site.baseurl }}/en/2026/09/04/PFAS-heat-pumps.html)

## Sources

- [ECHA, restriction des PFAS : dossier, avis du RAC et évaluations sectorielles](https://echa.europa.eu/fr/registry-of-restriction-intentions/-/dislist/details/0b0236e18663449b)
- [ECHA, page thématique PFAS](https://echa.europa.eu/fr/hot-topics/perfluoroalkyl-chemicals-pfas)
- [J.-B. Fressoz, « Pompes à chaleur et climatisation sont la première source d'émissions de PFAS en Europe », Le Monde, 6 juin 2026](https://www.lemonde.fr/idees/article/2026/06/06/pompes-a-chaleur-et-climatisation-sont-la-premiere-source-d-emissions-de-pfas-en-europe_6696594_3233.html)

## Code

The script [fig_emissions_pfas_europe.py]({{ site.baseurl }}/assets/linkedin/2026-09-09-pfas-pompes-a-chaleur/fig_emissions_pfas_europe.py) produces the figure on its own.

To reproduce the figure:

```bash
python3 fig_emissions_pfas_europe.py fr   # ou `en`
```

The tonnages are entered in the script itself, each with its source; there is no other data to download. All figures of the article are detailed in the article itself.

All files of this post (figures, data, scripts) are in the folder [2026-09-09-pfas-pompes-a-chaleur](https://git.persee.minesparis.psl.eu/energy-alternatives/linkedinposts/-/tree/main/posts/2026-09-09-pfas-pompes-a-chaleur) of the public repository.

<small>Code under the MIT licence; texts and figures under CC BY 4.0; data remain under their producer's licence.</small>
