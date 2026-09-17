---
layout: article
title: Les vidéos courtes, avec leurs sources
key: page-reels
ref: reels
permalink: /reels.html
comment: false
aside:
  toc: false
---

{%- assign depot = "https://git.persee.minesparis.psl.eu/energy-alternatives/reels" -%}

Une planche, quatre-vingt-dix secondes, un procédé. Les vidéos vivent sur
[YouTube](https://www.youtube.com/@energy_alternatives) et sur
[Instagram](https://www.instagram.com/energy_alternatives/) ; cette page-ci est là pour
ce qu'elles ne peuvent pas porter : **d'où viennent les chiffres, et par quel code**. Une
vidéo qui défile ne laisse pas le temps de vérifier une valeur, et une légende de réseau
social n'est pas un endroit où poser des sources.

Les figures animées sont reprises telles quelles de mes planches : aucun chiffre ne peut
diverger entre la planche et la vidéo. Si vous cherchez mes posts LinkedIn, leurs figures
et leur code, c'est [l'autre page]({{ site.baseurl }}/linkedin.html).

{% include reels-liste.html lang="fr" depot=depot %}

<small>Le code est dans le dépôt public [reels]({{ depot }}) : les scripts lisent les mêmes
fichiers de données que les figures, calent l'animation sur la voix et incrustent les
sous-titres. Rien n'y est saisi à la main, ce qui est la seule façon de garantir qu'une
correction faite sur une planche arrive aussi dans la vidéo.</small>
