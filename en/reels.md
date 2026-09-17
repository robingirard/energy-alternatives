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

{% include reels-liste.html lang="en" depot=depot %}

<small>The code lives in the public [reels]({{ depot }}) repository: the scripts read the
same data files as the figures, time the animation against the voice track and burn in the
subtitles. Nothing is typed by hand, which is the only way to guarantee that a correction
made on a slide also reaches the video.</small>
