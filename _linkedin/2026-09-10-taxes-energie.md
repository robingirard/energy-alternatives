---
title: "Taxes sur l'énergie en France : une vision d'ensemble"
date: 2026-09-10
date_affichee: "10 septembre 2026"
lang: fr
ref: linkedin-taxes-energie
key: linkedin-taxes-energie
permalink: /linkedin/2026-09-10-taxes-energie.html
linkedin: https://www.linkedin.com/feed/update/urn:li:activity:7503706312531410944/
cover: /assets/linkedin/2026-09-10-taxes-energie/figure_facture_fr_mwh_2024_paysage_fr.png
accroche: "Ce qu'un consommateur paie par MWh d'électricité, de gaz, de bois ou de carburant, et ce que l'État en prend : la fiscalité de l'énergie ne suit ni le carbone, ni l'énergie."
tags: ["fiscalité", "prix de l'énergie", "électricité", "gaz", "bois", "carburants", "France"]
---

<!-- Page engendrée par Communication/Linkedin/publier.py — ne pas éditer ici :
     modifier meta.yml / texte_fr.md dans Communication/Linkedin/2026-09-10_taxes-energie/ -->

<p class="linkedin-meta"><a href="https://www.linkedin.com/feed/update/urn:li:activity:7503706312531410944/" target="_blank" rel="noopener"><i class="fab fa-linkedin"></i> Voir le post et ses commentaires sur LinkedIn</a> · publié le 10 septembre 2026 · <a href="/linkedin.html">tous les posts</a></p>

<figure class="linkedin-figure">
<a href="{{ site.baseurl }}/assets/linkedin/2026-09-10-taxes-energie/figure_facture_fr_mwh_2024_paysage_fr.png" target="_blank"><img src="{{ site.baseurl }}/assets/linkedin/2026-09-10-taxes-energie/figure_facture_fr_mwh_2024_paysage_fr.png" alt="Taxes sur l'énergie en France : une vision d'ensemble" style="max-width:100%;height:auto;"></a>
<figcaption><small>France, 2024, euros par MWh livré, TTC. Quatre postes par vecteur et par type de client : énergie et fourniture, réseau, accises et taxes, TVA. Le pourcentage en bout de barre est la part des prélèvements (accises + TVA) dans le prix ; le réseau n'en fait pas partie.</small></figcaption>
</figure>

> Le millésime est 2024, le dernier pour lequel le biométhane injecté et le kérosène des soutes internationales sont publiés. La version 2025 de la figure, sans ces deux barres, se refait avec la même commande en omettant `--annee 2024` : l'électricité des ménages y est à 262 €/MWh dont 77 de prélèvements (l'accise, en cours de rétablissement après le bouclier tarifaire, passe de 25 à 37 €/MWh), le gaz à 136 dont 40.

## Le texte du post

Taxes sur l'énergie en France : une vision d'ensemble qui pointe quelques déséquilibres.

J'ai passé une partie de l'été à préparer un cours d'introduction à l'énergie pour le nouveau I-BE³, le PSL International Bachelor of Environmentally Engaged Engineering, et je vais essayer de partager progressivement ici quelques remarques et figures. Ici le but était de faire comprendre qu'il y avait dans le prix de l'énergie en général des taxes (TVA et autres), un coût réseau et un coût de l'énergie. Il y a des taxes proportionnelles au prix (comme la TVA), d'autres « fixes » (proportionnelles au volume) comme l'accise récemment introduite sur l'électricité.

Ce qui est frappant, ce sont les différences sur les taxes entre vecteurs : la fiscalité de l'énergie en France ne suit ni le contenu carbone, ni le contenu énergétique. Elle suit l'histoire des taxes, vecteur par vecteur, et aussi (surtout ? ce sera le prochain post) elle est liée au poids que peut représenter la facture d'énergie associée dans le budget des ménages.

Le gaz est très peu taxé, surtout par rapport à l'électricité. Évidemment le niveau sur le kérosène est presque révoltant, résultat d'une difficile coordination internationale, mais je trouve aussi assez singulier que le bois soit aussi peu taxé, beaucoup de circuits courts difficiles à suivre sans doute. Mais est-ce logique que le biométhane soit à ce point plus taxé que le bois ?

Pour l'électricité et le gaz ce sont des valeurs « moyennes », car il y a beaucoup de types d'abonnement. Pour le pétrole c'est aussi de la moyenne, dans le temps.

Sources : Eurostat (nrg_pc_204_c et 205_c) pour l'électricité et le gaz, Weekly Oil Bulletin de la Commission pour les carburants, bilan énergétique du SDES pour le bois.

## Sources

- [Eurostat, prix de l'électricité pour les ménages par composante (nrg_pc_204_c)](https://ec.europa.eu/eurostat/databrowser/view/nrg_pc_204_c/default/table)
- [Eurostat, prix du gaz pour les ménages par composante (nrg_pc_205_c) ; séries 202_c et 203_c pour les industriels](https://ec.europa.eu/eurostat/databrowser/view/nrg_pc_205_c/default/table)
- [Commission européenne, Weekly Oil Bulletin (carburants et fioul, prix avec et hors taxes)](https://energy.ec.europa.eu/data-and-analysis/weekly-oil-bulletin_en)
- [SDES, Bilan énergétique de la France (bois de chauffage : dépense et fiscalité des ménages)](https://www.statistiques.developpement-durable.gouv.fr/bilan-energetique-de-la-france-en-2025-donnees-provisoires)
- [Code des impositions sur les biens et services, art. L. 312-9 et suivants (champ de l'accise sur les énergies)](https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000044595989/LEGISCTA000044598327/)

## Données

- [`donnees_facture_fr_mwh_2024_2025.csv`]({{ site.baseurl }}/assets/linkedin/2026-09-10-taxes-energie/donnees_facture_fr_mwh_2024_2025.csv) — Les douze barres de la figure, millésimes 2024 et 2025, en €/MWh : énergie, réseau, accises, TVA, prix TTC, prélèvements et leur part.

## Code

Le code qui produit la figure est dans le dépôt public du cours, [bachelor_intro_to_energy_figures](https://git.persee.minesparis.psl.eu/energy-alternatives/bachelor_intro_to_energy_figures/-/tree/main/python/energy_taxes), dossier `python/energy_taxes`.

Pour refaire la figure :

```bash
cd python/energy_taxes
python3 prepare_eurostat.py      # électricité et gaz, API Eurostat
python3 prepare_carburants.py    # carburants et fioul, Weekly Oil Bulletin
python3 prepare_bilan_sdes.py    # bois de chauffage, bilan SDES
python3 plot_facture.py --unite mwh --paysage --lang fr --annee 2024
python3 plot_facture.py --unite mwh --paysage --annee 2024   # version anglaise
```

Les trois scripts `prepare_*` téléchargent les sources et écrivent les CSV de `data/processed/` ; ceux-ci sont dans le dépôt, donc `plot_facture.py` se lance directement.

<small>Code sous licence MIT ; textes et figures sous CC BY 4.0 ; les données restent sous la licence de leur producteur.</small>
