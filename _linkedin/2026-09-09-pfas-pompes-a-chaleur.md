---
title: "PFAS, pompes à chaleur et climatisation : un titre exact qui induit en erreur"
date: 2026-09-09
date_affichee: "9 septembre 2026"
lang: fr
ref: linkedin-pfas-pompes-a-chaleur
key: linkedin-pfas-pompes-a-chaleur
permalink: /linkedin/2026-09-09-pfas-pompes-a-chaleur.html
linkedin: https://www.linkedin.com/feed/update/urn:li:activity:7503181960106647552/
cover: /assets/linkedin/2026-09-09-pfas-pompes-a-chaleur/figure_pfas_emissions_europe_fr.png
accroche: "Sur 68 000 tonnes de PFAS émises chaque année en Europe, près de 39 000 viennent des gaz fluorés du froid. Mais ce total agrège des usages qui n'ont presque rien en commun. Le post qui annonce le billet de blog."
tags: ["PFAS", "pompes à chaleur", "climatisation", "fluides frigorigènes", "TFA", "réglementation européenne"]
---

<!-- Page engendrée par Communication/Linkedin/publier.py — ne pas éditer ici :
     modifier meta.yml / texte_fr.md dans Communication/Linkedin/2026-09-09_pfas-pompes-a-chaleur/ -->

<p class="linkedin-meta"><a href="https://www.linkedin.com/feed/update/urn:li:activity:7503181960106647552/" target="_blank" rel="noopener"><i class="fab fa-linkedin"></i> Voir le post et ses commentaires sur LinkedIn</a> · publié le 9 septembre 2026 · <a href="/linkedin.html">tous les posts</a></p>

<figure class="linkedin-figure">
<a href="{{ site.baseurl }}/assets/linkedin/2026-09-09-pfas-pompes-a-chaleur/figure_pfas_emissions_europe_fr.png" target="_blank"><img src="{{ site.baseurl }}/assets/linkedin/2026-09-09-pfas-pompes-a-chaleur/figure_pfas_emissions_europe_fr.png" alt="PFAS, pompes à chaleur et climatisation : un titre exact qui induit en erreur" style="max-width:100%;height:auto;"></a>
<figcaption><small>Émissions annuelles de PFAS en Europe par usage, en tonnes par an, d'après les avis du comité d'évaluation des risques (RAC) de l'ECHA, 2025-2026. En bleu, les usages où le PFAS est un fluide frigorigène.</small></figcaption>
</figure>

## Le texte du post

« Pompes à chaleur et climatisation sont la première source d'émissions de PFAS en Europe. » C'était le titre d'une chronique du Monde en juin dernier. Le titre est exact. Et pourtant il induit en erreur. C'est ce que j'explique dans ce nouveau post sur mon blog.

Deux réglementations se superposent aujourd'hui sur les mêmes fluides. La « F-gas » vise le climat : elle raisonne en pouvoir de réchauffement, et laisse donc passer les HFO, dans lesquels les industriels ont investi et qui se dégradent en TFA. La restriction PFAS vise la persistance et remet ce choix en cause. Les deux sont nécessaires. Mais appliquées sans étagement, elles prennent la transition énergétique en étau, au moment précis où il faut déployer massivement les pompes à chaleur pour sortir du gaz et du fioul, et la climatisation pour tenir les canicules.

Sur 68 000 tonnes de PFAS émises chaque année en Europe, près de 39 000 viennent des gaz fluorés du froid. Sauf que ce total agrège des usages qui n'ont presque rien en commun. Trois choses changent quand on regarde le détail :

Compter des tonnes de gaz ou compter le TFA réellement formé (la molécule qui pose problème) ne donne pas le même classement, et le retournement est vraiment très important.

Le R32, qui équipe la plupart des climatiseurs et pompes à chaleur récents, n'est pas un PFAS et ne produit pas de TFA.

Le premier levier n'est pas le fluide des machines neuves.

Le comité d'évaluation des risques de l'ECHA écrit lui-même que l'interdiction sans dérogation « n'est probablement pas applicable ». Le vrai débat des deux prochaines années porte donc sur le calibrage des dérogations, usage par usage. C'est ce que je discute dans le billet. Je prépare par ailleurs un travail plus « quantitatif ».

## Le billet complet

[PFAS, pompes à chaleur et climatisation : un titre exact qui induit en erreur]({{ site.baseurl }}/2026/09/04/PFAS-pompes-a-chaleur.html)

## Sources

- [ECHA, restriction des PFAS : dossier, avis du RAC et évaluations sectorielles](https://echa.europa.eu/fr/registry-of-restriction-intentions/-/dislist/details/0b0236e18663449b)
- [ECHA, page thématique PFAS](https://echa.europa.eu/fr/hot-topics/perfluoroalkyl-chemicals-pfas)
- [J.-B. Fressoz, « Pompes à chaleur et climatisation sont la première source d'émissions de PFAS en Europe », Le Monde, 6 juin 2026](https://www.lemonde.fr/idees/article/2026/06/06/pompes-a-chaleur-et-climatisation-sont-la-premiere-source-d-emissions-de-pfas-en-europe_6696594_3233.html)

## Code

Le script [fig_emissions_pfas_europe.py]({{ site.baseurl }}/assets/linkedin/2026-09-09-pfas-pompes-a-chaleur/fig_emissions_pfas_europe.py) produit la figure à lui seul.

Pour refaire la figure :

```bash
python3 fig_emissions_pfas_europe.py fr   # ou `en`
```

Les tonnages sont saisis dans le script lui-même, avec la source de chacun ; il n'y a pas d'autre donnée à télécharger. Toutes les figures du billet sont détaillées dans le billet lui-même.

Tous les fichiers de ce post (figures, données, scripts) sont dans le dossier [2026-09-09-pfas-pompes-a-chaleur](https://git.persee.minesparis.psl.eu/energy-alternatives/linkedinposts/-/tree/main/posts/2026-09-09-pfas-pompes-a-chaleur) du dépôt public.

<small>Code sous licence MIT ; textes et figures sous CC BY 4.0 ; les données restent sous la licence de leur producteur.</small>
