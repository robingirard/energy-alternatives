---
layout: article
title: Cas d'étude, avec le modèle et ses données
key: page-cas
ref: cas
permalink: /cas.html
comment: false
aside:
  toc: false
---

Chaque cas part d'une question concrète sur le système énergétique, y répond avec un modèle qu'on peut relancer, et donne une page où l'on voit la réponse changer quand on bouge un curseur. Pour chaque cas : la page interactive, le notebook exécuté, les figures, les données et le code. Ce sont des cas d'école, pas des prévisions.

Ils sont construits avec [POMMES](https://git.persee.minesparis.psl.eu/energy-alternatives/pommes), l'outil open source de planification des systèmes énergétiques du centre PERSEE (MINES Paris – PSL), et accompagnent la formation [« Évolution du système électrique dans un contexte de transition énergétique »](https://executive-education.minesparis.psl.eu/formations/evolution-du-systeme-electrique-dans-un-contexte-de-transition-energetique/) (MINES Paris – PSL Executive Education).

{% assign _items = site.cas | sort: 'date' | reverse %}
<div class="linkedin-list">
{% for p in _items %}
<div class="linkedin-item" style="display:flex;flex-wrap:wrap;gap:1.2rem;margin:2rem 0;align-items:flex-start;">
  <a href="{{ p.url | relative_url }}" style="flex:0 0 240px;max-width:100%;"><img src="{{ p.cover | relative_url }}" alt="{{ p.title }}" style="width:240px;max-width:100%;height:auto;border:1px solid #e1e0d9;"></a>
  <div style="flex:1 1 260px;">
    <small>{{ p.date_affichee }}</small>
    <h3 style="margin:.2rem 0 .5rem;"><a href="{{ p.url | relative_url }}">{{ p.title }}</a></h3>
    <p style="margin:0 0 .5rem;">{{ p.accroche }}</p>
    <small><a href="{{ p.url | relative_url }}">Page interactive, notebook, données et code</a></small>
  </div>
</div>
{% endfor %}
</div>

<small>Le code et les données de tous les cas sont dans le dépôt public [pommes-case-studies](https://git.persee.minesparis.psl.eu/energy-alternatives/pommes_studies/pommes-case-studies).</small>
