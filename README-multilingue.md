# Version française / version anglaise du blog

Ce fichier documente le fonctionnement bilingue du site. Il n'est pas publié
(il est couvert par la règle `README-*.md` de la clé `exclude` de `_config.yml`).

## Principe

| | Français (langue par défaut) | Anglais |
|---|---|---|
| Accueil | `/` | `/en/` |
| Archives | `/archive.html` | `/en/archive.html` |
| À propos | `/about.html` | `/en/about.html` |
| Conférences | `/Conferences.html` | `/en/Conferences.html` |
| Flux RSS | `/feed.xml` | `/en/feed.xml` |
| Articles | `_posts/` → `/AAAA/MM/JJ/titre.html` | `_posts_en/` → `/en/AAAA/MM/JJ/titre.html` |

Un bouton **FR / EN** (icône globe) apparaît dans le bandeau de navigation de
chaque page. Il pointe vers la traduction de la page courante quand elle existe,
et sinon vers l'accueil de l'autre langue.

Les deux langues restent étanches : l'accueil français ne liste que les articles
de `_posts`, l'accueil anglais que ceux de `_posts_en`, la recherche ne renvoie
que des résultats de la langue de la page consultée, et chaque page d'archives ne
dépouille que ses propres articles.

## Écrire un article en anglais

Créer un fichier dans `_posts_en/`, nommé comme un article normal :

```
_posts_en/2024-11-18-RaccoFlex.md
```

Le front matter est identique à celui d'un article français. Une seule clé
supplémentaire est utile, `ref`, qui relie les deux versions d'un même article :

```yaml
---
title: Techno-economic value of photovoltaic generation flexibility ...
key: photovoltaics
ref: raccoflex        # <- la même valeur que dans la version française
tags: electricity distribution grid, value of flexibility, photovoltaics
article_header:
  type: cover
  image:
    src: /assets/images/Posts/2024-11-18/Scenarios_PV_large.png
---
```

et, dans `_posts/2024-11-18-RaccoFlex.md`, ajouter la même ligne `ref: raccoflex`.

Le bouton EN de l'article français mènera alors directement à l'article anglais
(et inversement). Sans `ref`, le bouton renvoie simplement vers `/en/`.

Il n'est pas nécessaire de déclarer `lang: en` : c'est fait automatiquement pour
tout ce qui se trouve dans `_posts_en/` et dans `en/` (voir `defaults` dans
`_config.yml`). Les images et fichiers de `assets/` sont partagés entre les deux
langues.

## Ajouter une page en anglais

Créer le fichier dans `en/`, par exemple `en/publications.md`. La langue est
appliquée automatiquement. Pour relier la page à son équivalent français,
utiliser `ref:` des deux côtés — ou, si les deux pages n'ont pas de `ref`,
une URL explicite :

```yaml
translations:
  en: /en/publications.html
```

Pour faire apparaître la page dans le menu, ajouter une entrée dans
`_data/navigation.yml` avec une URL par langue :

```yaml
  - titles:
      en: Publications
      fr: Publications
    url: /publications.html      # repli
    urls:
      fr: /publications.html
      en: /en/publications.html
```

## Libellés d'interface

Tous les textes du thème (« Plus », « Rechercher », « Tout afficher », formulaire
d'abonnement, titre et description du site, etc.) viennent de `_data/locale.yml`,
dans les blocs `en:` et `fr:`. Les clés ajoutées pour ce site sont
`SITE_TITLE`, `SITE_DESCRIPTION`, `SHOW_ALL`, `SEARCH_GROUP_POSTS`,
`SUBSCRIBE_PROMPT` et `SUBSCRIBE_BUTTON`.

Le titre du site est donc « Alternatives énergétiques » côté français et
« Energy alternatives » côté anglais.

## Déclarer une langue supplémentaire

Dans `_config.yml`, clé `languages`. Chaque entrée déclare le code de langue,
le nom, le libellé du bouton, et les chemins d'accueil / archives / RSS :

```yaml
languages:
  - code   : fr
    name   : Français
    label  : FR
    home   : /
    archive: /archive.html
    rss    : /feed.xml
```

Ajouter une langue suppose aussi de créer le dossier correspondant, une
collection `posts_xx` dans `collections`, les `defaults` associés, et un bloc de
traduction dans `_data/locale.yml`.

## Points à connaître

- **Pagination** : `jekyll-paginate` ne sait paginer qu'une seule page d'accueil.
  Seul l'accueil français est donc paginé (8 articles par page). L'accueil
  anglais liste tous les articles anglais sur une seule page ; à revoir quand ils
  seront nombreux.
- **Flux RSS** : `feed.xml` et `en/feed.xml` ne publient que le dernier article
  (comportement d'origine du site, conservé tel quel).
- **`page.html`** à la racine du dépôt est un ancien doublon de
  `_layouts/page.html` : il est publié tel quel sur `/page.html` et produit une
  page incohérente. Il était déjà là avant le passage au bilingue ; il peut être
  supprimé sans risque.

## État des traductions

Tout est traduit : les pages À propos, Conférences, Archives, l'accueil, les
libellés d'interface, et **les 17 articles**. Chaque article français et sa
version anglaise partagent une clé `ref:`, si bien que le bouton FR/EN mène
directement d'une version à l'autre.

Correspondance des fichiers :

| `_posts/` (FR) | `_posts_en/` (EN) | `ref` |
|---|---|---|
| 2019-05-24-variabilite-…-thermo-sensibilite | 2019-05-24-electricity-demand-variability-and-thermosensitivity | thermosensibilite |
| 2020-03-22-une-contribution-…-2050 | 2020-03-22-low-carbon-strategy-buildings-heating-2050 | snbc-chauffage-2050 |
| 2020-05-07-mix-de-production-… | 2020-05-07-electricity-generation-mix-energy-and-capacity | mix-energie-puissance |
| 2020-08-20-decomposition-lcoe | 2020-08-20-cost-of-electricity-generation | decomposition-lcoe |
| 2021-04-10-france-allemagne | 2021-04-10-france-germany | france-allemagne |
| 2021-10-01-32-ou-40 | 2021-10-01-32-or-40 | 32-ou-40 |
| 2021-10-25-rapport-RTE | 2021-10-25-rte-report | rapport-rte |
| 2021-11-10-DPE-passoires | 2021-11-10-energy-sieves | dpe-passoires |
| 2022-03-16-DPE-open-data | 2022-03-16-epc-open-data | dpe-open-data |
| 2022-05-18-GazRusse | 2022-05-18-russian-gas | gaz-russe |
| 2022-10-29-Sobriete | 2022-10-29-sufficiency-and-solidarity | sobriete-solidarite |
| 2023-05-31-Building-Model | 2023-05-31-building-model | building-model |
| 2023-08-28-Systeme-elec-contraint | 2023-08-28-power-system-under-strain | systeme-elec-contraint |
| 2024-01-28-vehicule-elec | 2024-01-28-electric-vehicles | vehicule-elec |
| 2024-02-08-sobriete-technologie | 2024-02-08-sufficiency-technology-transition | sobriete-technologie |
| 2024-10-06- Rupture de stock ? | 2024-10-06-out-of-stock | rupture-de-stock |
| 2024-11-18-RaccoFlex | 2024-11-18-RaccoFlex | raccoflex |

Les liens internes entre articles ont été réécrits vers les versions anglaises
(`https://www.energy-alternatives.eu/en/...`), ancres comprises. Les pages non
traduites sont `404.html`, `consommation.html` (page de test) et le doublon
`page.html` ; le bouton EN y renvoie vers `/en/`.

## Prévisualiser en local

```bash
bundle exec jekyll serve
```
