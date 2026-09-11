---
title: "Oil, gas, electricity: what each costs the country, how much we use, what it brings in taxes"
date: 2026-09-11
date_affichee: "11 September 2026"
lang: en
ref: linkedin-facture-et-taxes-par-vecteur
key: linkedin-facture-et-taxes-par-vecteur
permalink: /en/linkedin/2026-09-11-facture-et-taxes-par-vecteur.html
linkedin: https://www.linkedin.com/feed/update/urn:li:activity:7504058324271734784/
cover: /assets/linkedin/2026-09-11-facture-et-taxes-par-vecteur/figure_facture_taxes_vecteur_fr_2012-2024.png
accroche: "Trade balance, final consumption and tax revenue by energy carrier, France 2012-2024. In 2022 the energy bill doubles while taxes fall; the only carrier in surplus is the one taxed most relative to its trade contribution."
tags: ["taxation", "trade balance", "gas", "electricity", "oil", "tariff shield", "France"]
---

<!-- Page engendrée par Communication/Linkedin/publier.py — ne pas éditer ici :
     modifier meta.yml / texte_en.md dans Communication/Linkedin/2026-09-11_facture-et-taxes-par-vecteur/ -->

<p class="linkedin-meta"><a href="https://www.linkedin.com/feed/update/urn:li:activity:7504058324271734784/" target="_blank" rel="noopener"><i class="fab fa-linkedin"></i> See the post and its comments on LinkedIn</a> · published on 11 September 2026 · <a href="/en/linkedin.html">all posts</a></p>

<figure class="linkedin-figure">
<a href="{{ site.baseurl }}/assets/linkedin/2026-09-11-facture-et-taxes-par-vecteur/figure_facture_taxes_vecteur_fr_2012-2024.png" target="_blank"><img src="{{ site.baseurl }}/assets/linkedin/2026-09-11-facture-et-taxes-par-vecteur/figure_facture_taxes_vecteur_fr_2012-2024.png" alt="Oil, gas, electricity: what each costs the country, how much we use, what it brings in taxes" style="max-width:100%;height:auto;"></a>
<figcaption><small>France, 2012 to 2024 (every two years until 2020, yearly afterwards). For each year, three bars: the contribution to the trade balance (billion current euros, the black tick marks the net balance), final energy consumption (TWh, dotted bar, right axis) and gross taxes including VAT (billion euros, hatched bar). Same colour per carrier in all three bars.</small></figcaption>
</figure>

## The text of the post

Asymmetry between energy carriers (2/2). Oil, gas, electricity: how each weighs on the trade balance, what each brings the State in taxes, and what each contributes in final energy.

Here, side by side, for France and for nine years between 2012 and 2024, by energy carrier, are three things: what each energy costs the trade balance (left bar, roughly 60 to 120 billion), how much of it we consume (dotted bar, right axis, about 1,500 TWh), and what it brings the State in taxes (hatched bar, about 60 billion). The colours are the same in all three bars.

Always this gas, which brings the State little (third bar), weighs on the trade balance (first bar), but not too much on French households' budgets, until 2022.

In 2022, France's energy bill doubles at a stroke, from 46 to 118 billion euros. And tax revenue on energy falls, from 59 to 56 billion. On electricity alone, it drops from 16 to 9 billion, then to 7 in 2023. The year energy cost the country the most is the year the State took the least from it: the year of the tariff shield, which we are still paying for today.

In other words: the only energy carrier that contributes positively to the trade balance is also the one taxed most heavily relative to that contribution. It is the one that gives us energy independence, and the one whose uses we must develop for decarbonisation.

Our gas consumption must be divided by three. Yet it is the cheapest grid energy, the one that brings in the least tax revenue, and the one whose weight on the trade balance has grown the most in recent years.

For oil, things are better in place, and the electric car is taking off. For electric heat, residential and industrial, which must replace gas to a large extent, we are not there yet, and one may wonder whether our taxation is the right one.

Source: SDES energy balance of France, long series 2011-2024.

## Three clarifications with respect to the post

- "The most heavily taxed" holds relative to the trade contribution, not per MWh: in 2024 the implicit rate is 57 €/MWh on oil, 34 on electricity, 21 on gas. Relative to the trade balance, taxes amount to 0.92 times the oil deficit, 0.32 times the gas deficit, and electricity is the only carrier that is taxed (€13 bn) while being in surplus (€5 bn).
- Gas is the cheapest and least-taxed grid energy; firewood is cheaper still (52 €/MWh against 136 for household gas in 2025) and almost untaxed (€0.2 bn, the green segment of the figure).
- Oil weighs more than gas on the trade balance every year (€44 bn against 17 in 2024). What is true of gas is that its weight increased the most: ×3.3 between 2021 and 2022, from €14.6 bn to 47.5 bn.

## Sources

- [SDES, Bilan énergétique de la France, séries longues 2011-2024 (balance commerciale par produit, consommation finale, fiscalité par vecteur)](https://www.statistiques.developpement-durable.gouv.fr/media/9283/download?inline)
- [SDES, la fiscalité environnementale en France, état des connaissances en 2025](https://www.statistiques.developpement-durable.gouv.fr/la-fiscalite-environnementale-en-france-etat-des-connaissances-en-2025)

## Data

- [`donnees_facture_et_taxes_fr_2011-2024.csv`]({{ site.baseurl }}/assets/linkedin/2026-09-11-facture-et-taxes-par-vecteur/donnees_facture_et_taxes_fr_2011-2024.csv) — By year: energy bill, gross and net taxes, final consumption, and for each carrier (coal, oil, biofuels, gas, electricity, biomass-heat) the trade balance, taxes and volume.

## Code

The code that produces the figure is in the course's public repository, [bachelor_intro_to_energy_figures](https://git.persee.minesparis.psl.eu/energy-alternatives/bachelor_intro_to_energy_figures/-/tree/main/python/energy_taxes), folder `python/energy_taxes`.

To reproduce the figure:

```bash
cd python/energy_taxes
python3 prepare_bilan_sdes.py                  # lit le classeur SDES des séries longues
python3 plot_facture_taxes_vecteur.py --lang fr
python3 plot_facture_taxes_vecteur.py          # version anglaise ; --toutes : 2011-2024 année par année
```

The prepared CSV is in the repository, so the plotting script runs without the `prepare` step. The SDES workbook (media 9283) must be placed by hand in `bibliographie/xlsx/` to redo it.

<small>Code under the MIT licence; texts and figures under CC BY 4.0; data remain under their producer's licence.</small>
