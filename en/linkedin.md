---
layout: article
title: LinkedIn posts, with data and code
key: page-linkedin-en
ref: linkedin
permalink: /en/linkedin.html
comment: false
aside:
  toc: false
---

Here you will find all my [LinkedIn](https://www.linkedin.com/in/robin-girard-a88baa4/) posts since September 2026. A figure is a claim, and a claim without its computation cannot be checked. This page therefore gathers, for each post: the text, the figure in English and in French, the primary sources, the prepared data and the code that reproduces the figure. More often than not, the figure also comes in an extended version: interactive, over other years, other countries, other units or other readings than the one in the post.

These pages are not blog articles: subscribers receive no email for them, and comments happen on LinkedIn. The longer articles stay on the [home page]({{ site.baseurl }}/en/).

{% assign _items = site.linkedin_en | sort: 'date' | reverse %}
<div class="linkedin-list">
{% for p in _items %}
<div class="linkedin-item" style="display:flex;flex-wrap:wrap;gap:1.2rem;margin:2rem 0;align-items:flex-start;">
  <a href="{{ p.url | relative_url }}" style="flex:0 0 240px;max-width:100%;"><img src="{{ p.cover | relative_url }}" alt="{{ p.title }}" style="width:240px;max-width:100%;height:auto;border:1px solid #e1e0d9;"></a>
  <div style="flex:1 1 260px;">
    <small>{{ p.date_affichee }}</small>
    <h3 style="margin:.2rem 0 .5rem;"><a href="{{ p.url | relative_url }}">{{ p.title }}</a></h3>
    <p style="margin:0 0 .5rem;">{{ p.accroche }}</p>
    <small><a href="{{ p.url | relative_url }}">Figure, sources, data and code</a> · <a href="{{ p.linkedin }}" target="_blank" rel="noopener"><i class="fab fa-linkedin"></i> the post on LinkedIn</a></small>
  </div>
</div>
{% endfor %}
</div>

<small>The code of the figures is published in the repository [bachelor_intro_to_energy_figures](https://git.persee.minesparis.psl.eu/energy-alternatives/bachelor_intro_to_energy_figures); the courses it comes from are on [my teaching page](https://www.robingirard.eu/Teaching.html).</small>
