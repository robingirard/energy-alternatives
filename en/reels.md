---
layout: article
title: Short videos, with their sources
key: page-reels-en
ref: reels
permalink: /en/reels.html
comment: false
aside:
  toc: false
---

{%- assign depot = "https://git.persee.minesparis.psl.eu/energy-alternatives/reels" -%}

One diagram, ninety seconds, one industrial process. The videos live on
[YouTube](https://www.youtube.com/@energy_alternatives) and
[Instagram](https://www.instagram.com/energy_alternatives/); this page carries what they
cannot: **where the numbers come from, and through what code**. A video that scrolls past
gives you no time to check a value, and a social media caption is no place for sources.

The animated figures are reused as they are from my own slides: no number can drift
between the slide and the video. If you are looking for my LinkedIn posts, their figures
and their code, that is [the other page]({{ site.baseurl }}/en/linkedin.html).

**The videos are in French for now.** An English series will have its own channel; the
sources below are worth reading in either case.

{% assign _reels = site.data.reels | reverse %}
<div class="reels-list">
{% for r in _reels %}
<div class="reels-item" style="display:flex;flex-wrap:wrap;gap:1.4rem;margin:2.6rem 0;align-items:flex-start;">
  <div style="flex:0 0 220px;max-width:100%;">
  {%- if r.youtube %}
    <div style="position:relative;width:220px;max-width:100%;aspect-ratio:9/16;">
      <iframe src="https://www.youtube-nocookie.com/embed/{{ r.youtube }}" title="{{ r.serie }} {{ r.numero }} — {{ r.titre_en | default: r.titre }}" style="position:absolute;inset:0;width:100%;height:100%;border:1px solid #e1e0d9;" loading="lazy" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>
  {%- else %}
    <img src="{{ r.couverture | relative_url }}" alt="{{ r.serie }} {{ r.numero }} — {{ r.titre_en | default: r.titre }}" style="width:220px;max-width:100%;height:auto;border:1px solid #e1e0d9;">
  {%- endif %}
  </div>
  <div style="flex:1 1 280px;">
    <small>{{ r.serie }} {{ r.numero }} · {{ r.duree }}</small>
    <h3 style="margin:.2rem 0 .5rem;">{{ r.titre_en | default: r.titre }}</h3>
    <p style="margin:0 0 .6rem;">{{ r.accroche_en | default: r.accroche }}</p>
    <p style="margin:0 0 .6rem;"><small>
    {%- if r.youtube -%}
      <a href="https://www.youtube.com/watch?v={{ r.youtube }}" target="_blank" rel="noopener">Watch on YouTube</a> ·
    {%- else -%}
      <em>Coming soon.</em> ·
    {%- endif %}
    <a href="{{ depot }}{% if r.code %}/-/tree/main/{{ r.code }}{% endif %}" target="_blank" rel="noopener">the code that builds it</a>
    </small></p>
    {% if r.sources %}
    <details>
      <summary><small>The numbers, and where they come from</small></summary>
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

<small>The code lives in the public [reels]({{ depot }}) repository: the scripts read the
same data files as the figures, time the animation against the voice track and burn in the
subtitles. Nothing is typed by hand, which is the only way to guarantee that a correction
made on a slide also reaches the video.</small>
