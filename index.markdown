---
layout: home
title: 首頁
---

# 歡迎來到草本故事館

用故事的方式，認識傳統中藥方劑。每個方劑都是一個精彩的故事，每味藥材都是一個鮮活的角色。

## 精選故事

<div class="story-list">
{% for story in site.stories %}
  <div class="story-card">
    <h3><a href="{{ story.url | relative_url }}">{{ story.title }}</a></h3>
    <p class="formula-name">{{ story.formula }}</p>
    <p>{{ story.excerpt }}</p>
  </div>
{% endfor %}
</div>
