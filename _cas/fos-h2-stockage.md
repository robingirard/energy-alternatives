---
title: "Fos-sur-Mer : que vaut un stockage d'hydrogène, et que coûte de se passer du gaz ?"
date: 2026-10-05
date_affichee: "5 octobre 2026"
lang: fr
ref: cas-fos-h2-stockage
key: cas-fos-h2-stockage
permalink: /cas/fos-h2-stockage.html
cover: /assets/cas/fos-h2-stockage/figure_valeur_stockage_fr.png
accroche: "Si Fos-sur-Mer produisait ses 83,5 kt d'hydrogène par an entièrement par électrolyse, la cavité saline de Manosque vaudrait 0,48 €/kg à 1 350 €/kW, 1,34 €/kg à 417 €/kW. Sans obligation, elle ne vaut rien : le reformeur au gaz sert déjà de flexibilité. Une page pour jouer avec le CAPEX, le gaz et l'année météo."
tags: ["hydrogène", "électrolyse", "stockage", "cavité saline", "Fos-sur-Mer", "POMMES", "prix de l'électricité"]
---

<!-- Page engendrée par Communication/Cas/publier.py — ne pas éditer ici :
     modifier Communication/Cas/fos-h2-stockage/meta.yml, ou le cas lui-même dans https://git.persee.minesparis.psl.eu/energy-alternatives/pommes_studies/pommes-case-studies/-/tree/main/cas_fos_h2_stockage -->

<p class="linkedin-meta">mis en ligne le 5 octobre 2026 · <a href="{{ site.baseurl }}/cas.html">tous les cas</a></p>

La zone industrielle de Fos-sur-Mer consomme **83,5 kt d'hydrogène par an** (raffinage, méthanol), produit aujourd'hui par un reformeur au gaz naturel, plus un peu d'hydrogène fatal de l'usine de chlore. Un électrolyseur pourrait le produire à la place, en achetant l'électricité au prix horaire. Deux questions :

1. **Que vaut un stockage d'hydrogène**, la cavité saline de Manosque à 110 km, pour cet électrolyseur, et comment cette valeur dépend-elle de son coût d'investissement (CAPEX) ?
2. **Que coûte de se passer du reformeur au gaz** en secours, c'est-à-dire d'imposer 100 % d'hydrogène électrolytique ?

Les prix horaires de l'électricité française viennent d'un modèle POMMES du système électrique européen de 2030 (11 années climatiques, trois prix du gaz ; thèse de Thibaut Knibiehly, PERSEE). Le hub lui-même est un programme linéaire horaire à un nœud, le *modèle réduit*, qui choisit la taille de l'électrolyseur et de la cavité et leur fonctionnement heure par heure au moindre coût annuel. Il redonne la modélisation POMMES complète de Fos à tous les points qu'elle a résolus.

## La page interactive

Choisissez le CAPEX de l'électrolyseur, le prix du gaz (il fixe l'écart entre heures chères et heures creuses), le volume d'hydrogène et le plafond de la cavité : la valeur du stockage se lit en €/kg, en moyenne et pour chacune des 11 années climatiques. La seconde partie impose une part croissante d'électrolyse et montre le surcoût par rapport au hub libre. Les curseurs lisent des grilles précalculées par le modèle réduit ; rien n'est recalculé dans le navigateur.

<p><a class="button button--primary button--rounded" href="{{ site.baseurl }}/assets/cas/fos-h2-stockage/page.html?lang=fr" target="_blank" rel="noopener">Ouvrir la page interactive dans un onglet</a></p>

<iframe src="{{ site.baseurl }}/assets/cas/fos-h2-stockage/page.html?lang=fr" title="La page interactive" loading="lazy" scrolling="no" style="width:100%;height:1100px;border:1px solid #e1e0d9;" onload="var f=this;function h(){try{f.style.height=f.contentDocument.documentElement.scrollHeight+'px'}catch(e){f.scrolling='auto'}}h();new ResizeObserver(h).observe(f.contentDocument.body)"></iframe>

## Le notebook

Le récit complet, exécuté avec ses sorties (en anglais) : les prix horaires, un calcul du modèle réduit pas à pas, le contrôle contre la modélisation POMMES, les deux questions, une règle simplifiée qui se passe de solveur, et ce que le cas ne dit pas.

<p><a class="button button--outline-primary button--rounded" href="{{ site.baseurl }}/assets/cas/fos-h2-stockage/notebook.html" target="_blank" rel="noopener">Lire le notebook exécuté</a></p>

<small><a href="{{ site.baseurl }}/assets/cas/fos-h2-stockage/notebook.ipynb">télécharger le .ipynb</a> · <a href="https://git.persee.minesparis.psl.eu/energy-alternatives/pommes_studies/pommes-case-studies/-/blob/main/cas_fos_h2_stockage/notebook.ipynb" target="_blank" rel="noopener">le voir sur GitLab</a></small>

## Les figures

<figure class="linkedin-figure">
<a href="{{ site.baseurl }}/assets/cas/fos-h2-stockage/figure_valeur_stockage_fr.png" target="_blank"><img src="{{ site.baseurl }}/assets/cas/fos-h2-stockage/figure_valeur_stockage_fr.png" alt="La valeur de la cavité de Manosque selon le CAPEX de l'électrolyseur" style="max-width:100%;height:auto;"></a>
<figcaption><small>À gauche, la valeur de la cavité en €/kg d'hydrogène, sous obligation de 100 % d'électrolyse, selon le CAPEX de l'électrolyseur, pour trois prix du gaz (15, 30 et 65 €/MWh) : courbes du modèle réduit, points de la modélisation POMMES. À droite, aux trois CAPEX résolus par POMMES, la même valeur sans obligation et sous obligation. Fos sans aciérie, 83,5 kt/an, parc électrique européen 2030, moyenne de 11 années climatiques.</small></figcaption>
</figure>

## Ce que le cas ne dit pas

- Les prix de l'électricité sont **exogènes** : l'électrolyseur ne les fait pas bouger.
- La cavité est plafonnée à **200 GWh**, un plafond déclaré et non géologique : la valeur est une borne basse.
- Fos est un **nœud isolé** : un réseau d'hydrogène (vers Lyon, l'Espagne) changerait la valeur d'un stockage local.
- La règle européenne de corrélation horaire de l'hydrogène renouvelable (RFNBO) n'est pas modélisée.
- Un seul parc électrique (2030) : les années météo changent, pas le parc. Rejouer le cas avec les scénarios TYNDP 2026 est la suite naturelle.

## Les posts qui en parlent

- [Infrastructures d'hydrogène : que vaut un stockage ? (LinkedIn, 5 octobre 2026)](/linkedin/2026-10-05-pommes-fos-1-valeur-stockage.html)

## Données

- [donnees_valeur_stockage_pommes.csv]({{ site.baseurl }}/assets/cas/fos-h2-stockage/donnees_valeur_stockage_pommes.csv) — valeur de la cavité dans la modélisation POMMES, par CAPEX, prix du gaz et obligation : moyenne, minimum et maximum sur les 11 années.
- [donnees_valeur_stockage_modele_reduit.csv]({{ site.baseurl }}/assets/cas/fos-h2-stockage/donnees_valeur_stockage_modele_reduit.csv) — la même valeur dans le modèle réduit, par CAPEX (200 à 2 000 €/kW), prix du gaz, volume d'hydrogène et plafond de la cavité.
- [hypotheses.yaml]({{ site.baseurl }}/assets/cas/fos-h2-stockage/hypotheses.yaml) — chaque hypothèse du cas : valeur, unité, source, statut.

## Code

Le code, les données gelées et les hypothèses sont dans le dépôt public [pommes-case-studies](https://git.persee.minesparis.psl.eu/energy-alternatives/pommes_studies/pommes-case-studies/-/tree/main/cas_fos_h2_stockage).

Pour tout refaire :

```bash
git clone https://git.persee.minesparis.psl.eu/energy-alternatives/pommes_studies/pommes-case-studies.git
git clone --branch regles-gelees-v2-2026-10-03 https://git.persee.minesparis.psl.eu/energy-alternatives/regles_parametriques.git
export REGLES_PARAMETRIQUES=$PWD/regles_parametriques OMP_NUM_THREADS=1
cd pommes-case-studies/cas_fos_h2_stockage
python grille.py stockage && python grille.py hybride   # le modèle réduit (HiGHS ; --solveur gurobi plus rapide)
python analyse.py && python figures.py && python build_page.py
jupyter nbconvert --to notebook --execute --inplace notebook.ipynb
```

Les équations et les coûts du modèle réduit sont dans le module public [regles_parametriques](https://git.persee.minesparis.psl.eu/energy-alternatives/regles_parametriques) ; le cas les appelle sans les recopier.

## Sources

- [POMMES, code source (GitLab PERSEE)](https://git.persee.minesparis.psl.eu/energy-alternatives/pommes)
- [Le cas : code, données gelées, hypothèses (pommes-case-studies)](https://git.persee.minesparis.psl.eu/energy-alternatives/pommes_studies/pommes-case-studies/-/tree/main/cas_fos_h2_stockage)
- [Règles paramétriques : le modèle réduit et ses coûts (étiquette regles-gelees-v2-2026-10-03)](https://git.persee.minesparis.psl.eu/energy-alternatives/regles_parametriques)
- [MINES Paris – PSL Executive Education, Évolution du système électrique dans un contexte de transition énergétique (30/11–04/12/2026)](https://executive-education.minesparis.psl.eu/formations/evolution-du-systeme-electrique-dans-un-contexte-de-transition-energetique/)

<small>Code et données du cas sous licence MIT ; textes et figures sous CC BY 4.0 ; les données d'entrée restent sous la licence de leur producteur.</small>
