---
layout: home
title: Home
---

# Welcome to Herbal Stories

Learn Traditional Chinese Medicine through storytelling.

## Featured Stories

<div class="story-list">
{% for story in site.stories %}
  <div class="story-card">
    <h3><a href="{{ story.url | relative_url }}">{{ story.title }}</a></h3>
    <p class="formula-name">{{ story.formula }}</p>
    <p>{{ story.excerpt }}</p>
  </div>
{% endfor %}
</div>
