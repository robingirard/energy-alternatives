---
layout: article
title: Case studies, with the model and its data
key: page-cas-en
ref: cas
permalink: /en/cas.html
comment: false
aside:
  toc: false
---

Each case starts from a concrete question about the energy system, answers it with a model you can run again, and comes with a page where you watch the answer change as you move a slider. For each case: the interactive page, the executed notebook, the figures, the data and the code. These are textbook cases, not forecasts.

They are built with [POMMES](https://git.persee.minesparis.psl.eu/energy-alternatives/pommes), the open-source energy-system planning tool of the PERSEE centre (MINES Paris – PSL), and accompany the training course ["Evolution of the power system in the context of the energy transition"](https://executive-education.minesparis.psl.eu/formations/evolution-du-systeme-electrique-dans-un-contexte-de-transition-energetique/) (MINES Paris – PSL Executive Education, in French).

{% assign _items = site.cas_en | sort: 'date' | reverse %}
<div class="linkedin-list">
{% for p in _items %}
<div class="linkedin-item" style="display:flex;flex-wrap:wrap;gap:1.2rem;margin:2rem 0;align-items:flex-start;">
  <a href="{{ p.url | relative_url }}" style="flex:0 0 240px;max-width:100%;"><img src="{{ p.cover | relative_url }}" alt="{{ p.title }}" style="width:240px;max-width:100%;height:auto;border:1px solid #e1e0d9;"></a>
  <div style="flex:1 1 260px;">
    <small>{{ p.date_affichee }}</small>
    <h3 style="margin:.2rem 0 .5rem;"><a href="{{ p.url | relative_url }}">{{ p.title }}</a></h3>
    <p style="margin:0 0 .5rem;">{{ p.accroche }}</p>
    <small><a href="{{ p.url | relative_url }}">Interactive page, notebook, data and code</a></small>
  </div>
</div>
{% endfor %}
</div>

<small>The code and data of every case are in the public repository [pommes-case-studies](https://git.persee.minesparis.psl.eu/energy-alternatives/pommes_studies/pommes-case-studies).</small>
