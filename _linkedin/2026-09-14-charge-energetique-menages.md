---
title: "Inégalité énergétique et transition"
date: 2026-09-14
date_affichee: "14 septembre 2026"
lang: fr
ref: linkedin-charge-energetique-menages
key: linkedin-charge-energetique-menages
permalink: /linkedin/2026-09-14-charge-energetique-menages.html
linkedin: https://www.linkedin.com/feed/update/urn:li:share:7505166973262098432/
cover: /assets/linkedin/2026-09-14-charge-energetique-menages/figure_charge_vingtiemes_et_serie_fr_fr.png
accroche: "La part du revenu que les Français consacrent à l'énergie bouge peu depuis 1960 ; mais en 2020, 12 % des ménages passent le seuil de précarité énergétique sur la seule énergie du logement, et 56 % dans le vingtième le plus modeste."
tags: ["ménages", "revenu", "précarité énergétique", "distribution", "inégalités", "France"]
---

<!-- Page engendrée par Communication/Linkedin/publier.py — ne pas éditer ici :
     modifier meta.yml / texte_fr.md dans Communication/Linkedin/2026-09-14_charge-energetique-menages/ -->

<p class="linkedin-meta"><a href="https://www.linkedin.com/feed/update/urn:li:share:7505166973262098432/" target="_blank" rel="noopener"><i class="fab fa-linkedin"></i> Voir le post et ses commentaires sur LinkedIn</a> · publié le 14 septembre 2026 · <a href="/linkedin.html">tous les posts</a></p>

<figure class="linkedin-figure">
<a href="{{ site.baseurl }}/assets/linkedin/2026-09-14-charge-energetique-menages/figure_charge_vingtiemes_et_serie_fr_fr.png" target="_blank"><img src="{{ site.baseurl }}/assets/linkedin/2026-09-14-charge-energetique-menages/figure_charge_vingtiemes_et_serie_fr_fr.png" alt="Inégalité énergétique et transition" style="max-width:100%;height:auto;"></a>
<figcaption><small>En haut : la moyenne nationale de 1960 à 2025 (Insee, comptes nationaux), part de l'énergie dans le revenu disponible brut des ménages — énergie du logement posée sur la ligne de base, c'est le champ de l'enquête du bas, et carburants empilés au-dessus, absents de cette enquête. En bas : la même part par vingtième de niveau de vie, France 2020 (Insee, Enquête nationale logement, microdonnées) — ratio d'agrégats, écart interquartile, premier et neuvième déciles, seuil conventionnel de précarité énergétique à 8 %.</small></figcaption>
</figure>

## Le texte du post

Inégalité énergétique et transition. Je continue avec le prix de l'énergie, mais du point de vue de la charge sur les consommateurs : son évolution de long terme en moyenne, et sa distribution aujourd'hui — enfin, en 2020.

Le graphique du haut montre la part du revenu que les Français consacrent à leur énergie directe, carburants compris, en marron. Elle monte à partir du premier choc pétrolier, et le principal contributeur est l'électricité : son prix réel n'a presque pas bougé sur la période, c'est donc un effet de volume — le chauffage électrique qui s'installe, rendu possible par le parc nucléaire — plus qu'un effet de coût. Puis la baisse du contre-choc pétrolier vers 1985, amplifiée par la chute du dollar de l'époque. Sinon, le moins qu'on puisse dire, c'est que cette part n'évolue pas beaucoup. Nous consommons ce que nous pouvons consommer, ou peut-être que les taxes s'ajustent à ce que nous pouvons payer. Je reviendrai là-dessus.

Le graphique du bas montre la distribution, en excluant les carburants : on peut alors utiliser l'enquête logement 2020, dont les microdonnées permettent de descendre au vingtième. Sur ces dépenses hors carburant, le seuil de 8 % du revenu sert à qualifier la précarité énergétique, et environ 12 % des ménages sont au-dessus en 2020.

C'est moins qu'avant : la même enquête donnait 22 % à la fin des années 1980 (mais à peu près pareil qu'aujourd'hui en 2006). Je suis curieux de voir les chiffres de 2026.

Cela reste beaucoup, et trop. Les personnes touchées par cette précarité ne peuvent souvent même pas vivre décemment. Et c'est cette partie des Français qu'il faut aider quand le prix de l'énergie s'envole, comme lors de la crise ukrainienne. Nous payons encore le bouclier tarifaire, qui a apporté de l'aide uniformément à tous, là où une partie seulement en avait besoin. Je trouve notre réaction à Ormuz plus proportionnée, et nous développons des solutions comme le véhicule électrique. Il faut dire que le budget est serré.

Mais l'austérité budgétaire ne doit pas nous faire passer à côté de la double nécessité de la transition énergétique, pour notre indépendance et pour l'environnement. D'une part, il faut embarquer tout le monde dans un projet commun, et cela implique de faire reculer la précarité énergétique avec des aides ciblées. De l'autre, la transition c'est surtout des investissements — rénovation, renouvelables, nucléaire : du CAPEX pour des économies d'OPEX.

Sources : Insee, comptes nationaux annuels (base 2020) pour la série longue ; Insee, Enquête nationale logement 2020 et millésimes antérieurs (microdonnées, accès Progedo) pour la distribution.

Le code, les données et les contrôles sont sur mon blog, avec tous mes posts LinkedIn (lien en commentaire).

## Sources

- [Insee, comptes nationaux annuels, consommation effective des ménages par produit (base 2020)](https://www.insee.fr/fr/statistiques/fichier/8988813/T_CONSO_EFF_PRODUITS_fr.xlsx)
- [Insee, évolution du revenu disponible brut et du pouvoir d'achat (taux d'épargne)](https://www.insee.fr/fr/statistiques/fichier/2830244/econ-gen-revenu-dispo-pouv-achat-2.xlsx)
- [Insee, Enquête nationale logement 2020 (microdonnées via Progedo-Adisp, DOI 10.13144/lil-1602)](https://data.progedo.fr/studies/doi/10.13144/lil-1602)
- [Insee, Enquêtes nationales logement 1988 à 2006 (microdonnées Progedo-Adisp) — la série à méthode constante](https://data.progedo.fr/)
- [ONPE, tableau de bord de la précarité énergétique (cité en commentaire, pas sur la figure)](https://www.precarite-energie.org/)

## Données

- [`charge_rdb_fr.csv`]({{ site.baseurl }}/assets/linkedin/2026-09-14-charge-energetique-menages/charge_rdb_fr.csv) — Le panneau du haut : la série 1960-2025 — part du logement, des carburants et du total dans le revenu disponible brut.
- [`tee_enl2020_vingtiemes.csv`]({{ site.baseurl }}/assets/linkedin/2026-09-14-charge-energetique-menages/tee_enl2020_vingtiemes.csv) — Le panneau du bas : par vingtième de niveau de vie, le ratio d'agrégats, les quartiles, les déciles extrêmes, la part au-dessus de 8 %, la facture et le revenu moyens (ENL 2020).
- [`tee_enl_serie_deciles.csv`]({{ site.baseurl }}/assets/linkedin/2026-09-14-charge-energetique-menages/tee_enl_serie_deciles.csv) — Les six millésimes exploitables de l'enquête logement, 1988 à 2020, à méthode constante : c'est d'ici que viennent les 22 % de la fin des années 1980 et la comparaison avec 2006. Pas sur la figure.

## Code

Le code qui produit la figure est dans le dépôt public [linkedinposts](https://git.persee.minesparis.psl.eu/energy-alternatives/linkedinposts/-/tree/main/prix_elec), dossier `prix_elec`.

Pour refaire la figure :

```bash
cd prix_elec
python3 prepare_data_fr_rdb.py                      # Insee : la série longue sur le revenu disponible
python3 prepare_data_fr_distrib.py                  # les vingtièmes de l'ENL (accès Progedo)
python3 figure_vingtiemes_et_serie.py --lang fr     # sans --lang : anglais
```

Les CSV préparés sont dans le dépôt ; seule l'étape ENL demande un accès aux microdonnées.

Tous les fichiers de ce post (figures, données, scripts) sont dans le dossier [2026-09-14-charge-energetique-menages](https://git.persee.minesparis.psl.eu/energy-alternatives/linkedinposts/-/tree/main/posts/2026-09-14-charge-energetique-menages) du dépôt public.

<small>Code sous licence MIT ; textes et figures sous CC BY 4.0 ; les données restent sous la licence de leur producteur.</small>
