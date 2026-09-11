---
layout: article
title: Posts LinkedIn, avec données et code
key: page-linkedin
ref: linkedin
permalink: /linkedin.html
comment: false
aside:
  toc: false
---

Vous trouverez ici l'ensemble de mes posts [LinkedIn](https://www.linkedin.com/in/robin-girard-a88baa4/) depuis septembre 2026. Une figure est une affirmation, et une affirmation sans son calcul ne se vérifie pas. Cette page rassemble donc, pour chaque post : le texte, la figure en français et en anglais, les sources primaires, les données préparées et le code qui refait la figure. Le plus souvent, la figure est aussi fournie dans une version étendue : interactive, sur d'autres années, d'autres pays, d'autres unités ou d'autres lectures que celle du post.

Ces pages ne sont pas des billets : les abonnés du blog ne reçoivent pas de courriel pour elles, et les commentaires se font sur LinkedIn. Les billets, plus longs, restent sur la [page d'accueil]({{ site.baseurl }}/).

{% assign _items = site.linkedin | sort: 'date' | reverse %}
<div class="linkedin-list">
{% for p in _items %}
<div class="linkedin-item" style="display:flex;flex-wrap:wrap;gap:1.2rem;margin:2rem 0;align-items:flex-start;">
  <a href="{{ p.url | relative_url }}" style="flex:0 0 240px;max-width:100%;"><img src="{{ p.cover | relative_url }}" alt="{{ p.title }}" style="width:240px;max-width:100%;height:auto;border:1px solid #e1e0d9;"></a>
  <div style="flex:1 1 260px;">
    <small>{{ p.date_affichee }}</small>
    <h3 style="margin:.2rem 0 .5rem;"><a href="{{ p.url | relative_url }}">{{ p.title }}</a></h3>
    <p style="margin:0 0 .5rem;">{{ p.accroche }}</p>
    <small><a href="{{ p.url | relative_url }}">Figure, sources, données et code</a> · <a href="{{ p.linkedin }}" target="_blank" rel="noopener"><i class="fab fa-linkedin"></i> le post sur LinkedIn</a></small>
  </div>
</div>
{% endfor %}
</div>

<small>Le code des figures, les données préparées et les scripts des graphiques interactifs sont dans le dépôt public [linkedinposts](https://git.persee.minesparis.psl.eu/energy-alternatives/linkedinposts) ; les cours dont viennent ces figures sont sur [ma page d'enseignement](https://www.robingirard.eu/Enseignement.html).</small>
