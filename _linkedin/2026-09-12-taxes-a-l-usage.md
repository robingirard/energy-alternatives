---
title: "Les taxes sur l'énergie, par usage et par vecteur"
date: 2026-09-12
date_affichee: "12 septembre 2026"
lang: fr
ref: linkedin-taxes-a-l-usage
key: linkedin-taxes-a-l-usage
permalink: /linkedin/2026-09-12-taxes-a-l-usage.html
linkedin: https://www.linkedin.com/feed/update/urn:li:activity:7504436929250246656/
cover: /assets/linkedin/2026-09-12-taxes-a-l-usage/figure_taxes_usage_fr_2024_paysage_fr.png
accroche: "Un MWh d'électricité est plus taxé qu'un MWh de gaz, mais les deux ne se comparent pas : entre le MWh livré et le service rendu, il y a le rendement de la machine. Par 100 km, par 100 passagers-km, par MWh de chaleur utile, par casserole, le classement change — et l'avion ne paie rien du tout."
tags: ["fiscalité", "prix de l'énergie", "pompe à chaleur", "voiture électrique", "avion", "train", "cuisson", "rendement", "France"]
---

<!-- Page engendrée par Communication/Linkedin/publier.py — ne pas éditer ici :
     modifier meta.yml / texte_fr.md dans Communication/Linkedin/2026-09-12_taxes-a-l-usage/ -->

<p class="linkedin-meta"><a href="https://www.linkedin.com/feed/update/urn:li:activity:7504436929250246656/" target="_blank" rel="noopener"><i class="fab fa-linkedin"></i> Voir le post et ses commentaires sur LinkedIn</a> · publié le 12 septembre 2026 · <a href="/linkedin.html">tous les posts</a></p>

<figure class="linkedin-figure">
<a href="{{ site.baseurl }}/assets/linkedin/2026-09-12-taxes-a-l-usage/figure_taxes_usage_fr_2024_paysage_fr.png" target="_blank"><img src="{{ site.baseurl }}/assets/linkedin/2026-09-12-taxes-a-l-usage/figure_taxes_usage_fr_2024_paysage_fr.png" alt="Les taxes sur l'énergie, par usage et par vecteur" style="max-width:100%;height:auto;"></a>
<figcaption><small>France, 2024, prix TTC. Quatre unités de service : euros par 100 km de voiture, par 100 passagers-km, par MWh de chaleur utile, par MWh de chaleur dans la casserole. Chaque barre est la barre « par MWh livré » du post précédent divisée par le rendement de la machine, avec les mêmes quatre postes : énergie et fourniture, réseau, accises et taxes, TVA. Le chiffre rouge au-dessus de chaque barre est le total des prélèvements (accises + TVA) par unité de service ; le réseau n'en fait pas partie. Sous chaque barre, la consommation ou le rendement retenu. L'avion est à zéro : le kérosène des soutes internationales n'est soumis ni à l'accise ni à la TVA — un vol intérieur a la même barre, la TVA à 10 % et la taxe de solidarité portent sur le billet, pas sur l'énergie. La recharge rapide publique est posée à 0,50 €/kWh TTC : seules la TVA et l'accise non-ménage y sont identifiables, ses prélèvements sont une borne basse. Le train est tracé au prix de l'électricité des industriels faute de prix ferroviaire publié, TVA comprise : l'opérateur achète moins cher et la déduit, sa barre est un majorant.</small></figcaption>
</figure>

## La même figure, à explorer — et l'année au choix

Les quatre panneaux du post, un usage à la fois, avec **le millésime au choix** : 2024, celui de la figure du post, ou 2025. L'échelle des ordonnées est calculée sur les deux années, pour que changer d'année fasse bouger les barres et non l'axe ; chauffage et cuisson la partagent, comme dans la figure. Survolez une barre pour sa décomposition et la part des prélèvements ; la vue « tableau » donne les nombres. Engendré depuis le CSV des barres tracées, plus bas, par `build_interactif.py`.

<iframe src="{{ site.baseurl }}/assets/linkedin/2026-09-12-taxes-a-l-usage/interactif_taxes_usage.html?lang=fr" title="La même figure, à explorer — et l'année au choix" loading="lazy" style="width:100%;height:660px;border:0;"></iframe>

<small><a href="{{ site.baseurl }}/assets/linkedin/2026-09-12-taxes-a-l-usage/interactif_taxes_usage.html?lang=fr" target="_blank">Ouvrir le graphique dans un onglet</a></small>

> Le millésime est 2024, celui du post précédent, pour que les deux figures se lisent ensemble — et c'est aussi la dernière année où le kérosène des soutes internationales est publié, donc la dernière où la barre « avion » existe. L'accise sur l'électricité y était encore réduite par le bouclier tarifaire (25,0 €/MWh en 2024 contre 37,1 en 2025) : c'est le millésime le plus favorable à l'électricité. Avec les prix 2025 — le bouton « 2025 » du graphique ci-dessus, ou la même commande avec `--annee 2025` — on obtient 26 € de prélèvements par MWh de chaleur utile pour la pompe à chaleur contre 45 pour la chaudière gaz, 77 pour le radiateur électrique, l'égalité de la cuisson tient (91 contre 90) et le TGV reste à 0,21 € pour 4,24 € en voiture aux 100 passagers-km. Le classement ne dépend pas du millésime.

## Le texte du post

Les taxes sur l'énergie, par usage et par vecteur

Beaucoup me l'ont fait remarquer, à juste titre, dans mes derniers posts : un MWh d'électricité coûte plus cher et est plus taxé qu'un MWh de gaz, mais les deux ne se comparent pas. C'est très juste. L'électricité a plus de valeur que le gaz, au MWh. Mais cela dépend évidemment de l'usage. Une pompe à chaleur est trois fois plus efficace qu'une chaudière gaz, un moteur électrique trois fois plus qu'un moteur thermique. Si on met cette électricité dans un radiateur à effet Joule ou dans une plaque à induction, la comparaison change encore.

Je propose donc ici une description du prix de l'énergie et des taxes associées, en fonction de l'usage. France, 2024, prix TTC.

Par ailleurs, je mets sur mon blog tous mes posts LinkedIn, avec les données et le code (merci Claude) qui produisent ces graphiques. Les figures y sont un peu plus complètes et interactives. Ici, par exemple, vous pouvez changer d'année : avec les prix 2025, les écarts se resserrent mais le classement ne change pas.

https://www.energy-alternatives.eu/linkedin.html

Sources : Eurostat, Weekly Oil Bulletin et bilan du SDES pour les prix ; ADEME, Flamme Verte, DGAC et SNCF pour les rendements et consommations. Tout y est, hypothèse par hypothèse.

EDIT, suite à une question en commentaire : la hauteur d'une barre n'est pas un prix au litre, c'est le prix TTC de l'énergie pour une unité de service — 100 km pour les voitures, 100 passagers-km pour l'avion et le train, un MWh de chaleur utile pour le chauffage. Le chiffre rouge au-dessus est le total des taxes dans cette même unité. Une voiture essence à 6,5 l/100 km : 11,84 € aux 100 km, dont 6,5 € de taxes.

## Quatre précisions sur la figure

- Le facteur six entre la voiture électrique et la voiture essence compare des prélèvements par 100 km, pas des taux : une voiture essence paie 55 % de taxes dans son prix à la pompe, une voiture électrique rechargée à domicile 23 % dans sa facture d'électricité. Le facteur six vient d'abord du rendement du moteur (17 contre 56 kWh aux 100 km), ensuite du barème.
- La pompe à chaleur est prise à COP 3, moyenne saisonnière. Par grand froid une PAC air/air descend vers 2, et les prélèvements par MWh de chaleur utile montent alors à 33 € — toujours sous les 41 € de la chaudière gaz.
- L'avion et le train ne sont pas dans la même unité que les voitures du premier panneau : 100 passagers-km, et non 100 km de véhicule. La barre « avion » est le carburant seul, exonéré d'accise et de TVA sur les vols internationaux ; un vol intérieur a la même barre, et ce qu'il paie en plus — TVA à 10 % et taxe de solidarité (2,63 € par passager en classe économique France/UE en 2024) — porte sur le billet, pas sur l'énergie. Le TGV est tracé au prix de l'électricité des industriels faute de prix ferroviaire publié : l'opérateur achète moins cher et déduit la TVA, ses 0,21 € de prélèvements sont un majorant (0,07 € d'accise seule).
- La recharge rapide publique est une hypothèse (0,50 €/kWh TTC) : seules la TVA et l'accise payée par l'opérateur y sont identifiables, le tarif d'acheminement de la borne et la marge sont comptés avec l'énergie. Les prélèvements de cette barre, 1,7 € aux 100 km, sont donc une borne basse.

## Sources

- [Eurostat, prix de l'électricité pour les ménages par composante (nrg_pc_204_c)](https://ec.europa.eu/eurostat/databrowser/view/nrg_pc_204_c/default/table)
- [Eurostat, prix du gaz pour les ménages par composante (nrg_pc_205_c)](https://ec.europa.eu/eurostat/databrowser/view/nrg_pc_205_c/default/table)
- [Commission européenne, Weekly Oil Bulletin (essence, gazole et fioul, prix avec et hors taxes)](https://energy.ec.europa.eu/data-and-analysis/weekly-oil-bulletin_en)
- [SDES, Bilan énergétique de la France (bois de chauffage : dépense et fiscalité des ménages)](https://www.statistiques.developpement-durable.gouv.fr/bilan-energetique-de-la-france-en-2025-donnees-provisoires)
- [ADEME, Base Carbone / Base Empreinte (pouvoirs calorifiques des carburants, rendements des équipements de chauffage)](https://base-empreinte.ademe.fr/)
- [Label Flamme Verte, critères de rendement des appareils de chauffage au bois](https://www.flammeverte.org/)
- [Règlement (UE) n° 66/2014 (écoconception des appareils de cuisson) et norme EN 60350-2, rendement des plaques](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX%3A32014R0066)
- [Norme EN 14825 (SCOP des pompes à chaleur)](https://www.boutique.afnor.org/fr-fr/norme/nf-en-14825/)
- [Code des impositions sur les biens et services, art. L. 312-58 (exonération d'accise du carburant de l'aviation commerciale)](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000044598519)
- [DGAC, chiffres et statistiques du transport aérien (consommation de carburant par passager-kilomètre)](https://www.ecologie.gouv.fr/politiques-publiques/aviation-environnement)
- [SNCF, empreinte environnementale des mobilités (consommation et émissions du TGV par voyageur-kilomètre)](https://www.sncf.com/fr/engagements/transition-ecologique)
- [SDES, Enquête mobilité des personnes 2019 (taux d'occupation moyen des voitures)](https://www.statistiques.developpement-durable.gouv.fr/resultats-detailles-de-lenquete-mobilite-des-personnes-de-2019)

## Données

- [`donnees_taxes_usage_fr_2024_2025.csv`]({{ site.baseurl }}/assets/linkedin/2026-09-12-taxes-a-l-usage/donnees_taxes_usage_fr_2024_2025.csv) — Les barres **telles que tracées**, millésimes 2024 et 2025 : pour chaque machine, les quatre postes en euros par unité de service, le prix TTC, les prélèvements, l'hypothèse retenue et l'unité. C'est ce que lit le graphique interactif ci-dessus. Quatre unités cohabitent dans le fichier — c'est la colonne `unite_fr` qui dit laquelle, et deux lignes d'unités différentes ne s'additionnent pas.
- [`donnees_facture_fr_mwh_2024_2025.csv`]({{ site.baseurl }}/assets/linkedin/2026-09-12-taxes-a-l-usage/donnees_facture_fr_mwh_2024_2025.csv) — Les douze barres « par MWh livré » du post précédent, millésimes 2024 et 2025, en €/MWh : énergie, réseau, accises, TVA, prix TTC, prélèvements et leur part. C'est le point de départ des trois panneaux.
- [`hypotheses_usages.csv`]({{ site.baseurl }}/assets/linkedin/2026-09-12-taxes-a-l-usage/hypotheses_usages.csv) — Toutes les hypothèses d'usage lues par le script : consommations (kWh ou litres aux 100 km, aux 100 passagers-km), taux d'occupation, pouvoirs calorifiques, rendements et COP, avec pour chacune sa source et son degré de confiance. Aucune n'est codée en dur dans le script, et l'unité de chaque consommation y est écrite — c'est elle qui commande la conversion.

## Code

Le code qui produit la figure est dans le dépôt public [linkedinposts](https://git.persee.minesparis.psl.eu/energy-alternatives/linkedinposts/-/tree/main/energy_taxes), dossier `energy_taxes`.

Pour refaire la figure :

```bash
cd energy_taxes
# la figure du post : sans le bloc de notes, illisible sur un fil LinkedIn
python3 plot_taxes_usage.py --paysage --lang fr --sans-note
python3 plot_taxes_usage.py --paysage --sans-note   # version anglaise
python3 plot_taxes_usage.py --paysage --lang fr     # avec les notes (PDF, diapo)
python3 plot_taxes_usage.py                         # portrait, anglais
python3 plot_taxes_usage.py --annee 2025            # le millésime suivant
# les barres des deux millésimes, ce que lit le graphique interactif
python3 plot_taxes_usage.py --export-csv output/taxes_usage_fr_2024_2025.csv \
    --annees 2024 2025
```

`plot_taxes_usage.py` réutilise les chargeurs de `plot_facture.py` (Eurostat, Weekly Oil Bulletin, bilan SDES) : les deux figures reposent sur les mêmes nombres, et le script imprime l'écart avec le CSV publié du post précédent. `--source csv` refait la figure à partir de ce seul CSV, sans les sources primaires.

Tous les fichiers de ce post (figures, données, scripts) sont dans le dossier [2026-09-12-taxes-a-l-usage](https://git.persee.minesparis.psl.eu/energy-alternatives/linkedinposts/-/tree/main/posts/2026-09-12-taxes-a-l-usage) du dépôt public.

<small>Code sous licence MIT ; textes et figures sous CC BY 4.0 ; les données restent sous la licence de leur producteur.</small>
