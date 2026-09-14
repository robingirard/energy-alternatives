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

{% assign _reels = site.data.reels | reverse %}
<div class="reels-list">
{% for r in _reels %}
<div class="reels-item" style="display:flex;flex-wrap:wrap;gap:1.4rem;margin:2.6rem 0;align-items:flex-start;">
  <div style="flex:0 0 220px;max-width:100%;">
  {%- if r.youtube %}
    <div style="position:relative;width:220px;max-width:100%;aspect-ratio:9/16;">
      <iframe src="https://www.youtube-nocookie.com/embed/{{ r.youtube }}" title="{{ r.serie }} {{ r.numero }} — {{ r.titre }}" style="position:absolute;inset:0;width:100%;height:100%;border:1px solid #e1e0d9;" loading="lazy" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>
  {%- else %}
    <img src="{{ r.couverture | relative_url }}" alt="{{ r.serie }} {{ r.numero }} — {{ r.titre }}" style="width:220px;max-width:100%;height:auto;border:1px solid #e1e0d9;">
  {%- endif %}
  </div>
  <div style="flex:1 1 280px;">
    <small>{{ r.serie }} {{ r.numero }} · {{ r.duree }}</small>
    <h3 style="margin:.2rem 0 .5rem;">{{ r.titre }}</h3>
    <p style="margin:0 0 .6rem;">{{ r.accroche }}</p>
    <p style="margin:0 0 .6rem;"><small>
    {%- if r.youtube -%}
      <a href="https://www.youtube.com/watch?v={{ r.youtube }}" target="_blank" rel="noopener">Voir sur YouTube</a> ·
    {%- else -%}
      <em>Bientôt en ligne.</em> ·
    {%- endif %}
    <a href="{{ depot }}{% if r.code %}/-/tree/main/{{ r.code }}{% endif %}" target="_blank" rel="noopener">le code qui la fabrique</a>
    </small></p>
    {% if r.sources %}
    <details>
      <summary><small>Les chiffres, et d'où ils viennent</small></summary>
      <ul style="margin:.6rem 0 0;">
      {% for s in r.sources %}<li><small>{{ s }}</small></li>{% endfor %}
      </ul>
      {% if r.licence %}<p style="margin:.6rem 0 0;"><small>{{ r.licence }}</small></p>{% endif %}
    </details>
    {% endif %}
  </div>
</div>
{% endfor %}
</div>

<small>Le code est dans le dépôt public [reels]({{ depot }}) : les scripts lisent les mêmes
fichiers de données que les figures, calent l'animation sur la voix et incrustent les
sous-titres. Rien n'y est saisi à la main, ce qui est la seule façon de garantir qu'une
correction faite sur une planche arrive aussi dans la vidéo.</small>
