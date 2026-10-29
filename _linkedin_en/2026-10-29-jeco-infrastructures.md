---
title: "Energy transition: building infrastructure without losing agility"
date: 2026-10-29
date_affichee: "29 October 2026"
lang: en
ref: linkedin-jeco-infrastructures
key: linkedin-jeco-infrastructures
permalink: /en/linkedin/2026-10-29-jeco-infrastructures.html
linkedin: https://www.linkedin.com/feed/update/urn:li:ugcPost:7521482055902302208/
cover: /assets/linkedin/2026-10-29-jeco-infrastructures/figure_jeco_document_en.png
accroche: "My op-ed for the 2026 Jéco in Lyon, as a two-page document: the transition is a matter of infrastructure, to build and to close. Risk is not shared (the State carries supply, on the demand side everyone waits), we must move through options and share roles between markets and long-term policy. Panel on Tuesday 3 November, 2 pm, at emlyon."
titre_recherche: "What transition for energy infrastructure? Jéco 2026 op-ed"
tags: ["infrastructure", "electricity grid", "electrification", "hydrogen", "planning", "electricity markets", "gas network", "Jéco"]
---

<!-- Page engendrée par Communication/Linkedin/publier.py — ne pas éditer ici :
     modifier meta.yml / texte_en.md dans Communication/Linkedin/2026-10-29_jeco-infrastructures/ -->

<p class="linkedin-meta"><a href="https://www.linkedin.com/feed/update/urn:li:ugcPost:7521482055902302208/" target="_blank" rel="noopener"><i class="fab fa-linkedin"></i> See the post and its comments on LinkedIn</a> · published on 29 October 2026 · <a href="/en/linkedin.html">all posts</a></p>

<figure class="linkedin-figure">
<a href="{{ site.baseurl }}/assets/linkedin/2026-10-29-jeco-infrastructures/figure_jeco_document_en.png" target="_blank"><img src="{{ site.baseurl }}/assets/linkedin/2026-10-29-jeco-infrastructures/figure_jeco_document_en.png" alt="Energy transition: building infrastructure without losing agility" style="max-width:100%;height:auto;"></a>
<figcaption><small>First page of the document: op-ed "Energy transition: building infrastructure without losing agility", Robin Girard, first published in the Mag des Jéco 2026 (Lyon).</small></figcaption>
</figure>

## The text of the post

Next Tuesday, 3 November, I will be at the Journées de l'économie (Jéco) in Lyon, for a panel: "What transition for energy infrastructure?". For the occasion I wrote an op-ed, published in the Mag des Jéco.

The starting point is simple: the energy transition is largely a matter of infrastructure. The infrastructure needed to produce, transport and consume low-carbon electricity, and the infrastructure that serves fossil fuels and will have to be closed. Climate investment in France reached €102 billion in 2024, and it would need almost to double by 2030 (I4CE).

But the difficulty is not only money. It is coordinating a supply and a demand that wait for each other. On the supply side, the State carries the risk, through long-term contracts for renewables and the financing of new nuclear. On the consumption side, everyone waits for everyone else: electrolysers struggle to find customers, manufacturers who want to electrify their heat first seek to secure their electricity, and grid connection lead times are lengthening.

To move forward, there are options, in the literal sense: investing without closing doors. Faster grid connections in exchange for power that is not guaranteed in all circumstances. Electrolysers hybridised with existing steam reformers, as Air Liquide is doing with Normand'Hy, rather than waiting for a "hydrogen backbone".

That leaves sharing the roles: to short- and medium-term markets "the commissariat", to borrow Jean-Pierre Dupuy's word; to a long-term European and French policy, the direction. A policy that can also correct its mistakes, such as the hydrogen volumes targeted by REPowerEU, and support the losers: the gas distribution network, whose fixed costs weigh on fewer and fewer customers, is the clearest example.

I will debate this with François Chaumont (RTE Auvergne-Rhône-Alpes) and Minh Ha-Duong (CNRS, CIRED), moderated by Simon Brigode (Regards croisés sur l'économie), on Tuesday 3 November, 2:00-3:30 pm, at the emlyon auditorium.

The full text is on my blog and below! The blog post also gives the source of every figure (I4CE, CRE, 2027 Finance Bill, Air Liquide): link in the comments.

## The full article

[Energy transition: building infrastructure without losing agility]({{ site.baseurl }}/en/2026/10/29/infrastructure-agility.html)

## Sources

- [La tribune dans le Mag des Jéco 2026](https://jeco-numerique.org/Mag2026/tribune.php?id=42)
- [Jéco 2026 — table ronde « Quelle transition pour les infrastructures de l'énergie ? », 3 novembre 2026](https://www.journeeseconomie.org/conference/2026/quelle-transition-pour-les-infrastructures-de-lenergie-17453)
- [I4CE, Panorama des financements climat, édition 2025 — 102 Md€ investis en 2024, + 87 Md€ à trouver d'ici 2030](https://www.i4ce.org/en/publication/landscape-climate-finance-france-edition-2025/)
- [CRE, consultation publique 2025-08 sur le schéma décennal de RTE — de 3 Md€ (2025) à 8 Md€ par an (2040)](https://www.cre.fr/fileadmin/Documents/Consultations_publiques/2025/250918_Consultation_2025-08_SDDR_RTE.pdf)
- [PLF 2027, évaluations préalables, article 24 — double enchère pour les carburants d'aviation de synthèse](https://www.assemblee-nationale.fr/dyn/contenu/visualisation/1128179/file/PLF%202027%20-%20Evaluations%20pr%C3%A9alables.pdf)
- [Air Liquide, Normand'Hy — électrolyseur de 200 MW exploité en parallèle des vaporeformeurs](https://www.airliquide.com/air-liquide-normandhy)

## Code

To reproduce the figure:

```bash
python3 plot_document.py   # le document de deux pages, FR et EN, à partir du billet de blog
```

All files of this post (figures, data, scripts) are in the folder [2026-10-29-jeco-infrastructures](https://git.persee.minesparis.psl.eu/energy-alternatives/linkedinposts/-/tree/main/posts/2026-10-29-jeco-infrastructures) of the public repository.

<small>Code under the MIT licence; texts and figures under CC BY 4.0; data remain under their producer's licence.</small>
