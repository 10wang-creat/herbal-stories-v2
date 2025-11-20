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

<style>
.story-list {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 20px;
  margin-top: 30px;
}

.story-card {
  background: white;
  padding: 20px;
  border-radius: 8px;
  border-left: 4px solid #4a7c2c;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  transition: transform 0.2s;
}

.story-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 4px 8px rgba(0,0,0,0.15);
}

.story-card h3 {
  margin-top: 0;
  color: #2d5016;
}

.story-card h3 a {
  text-decoration: none;
  color: #2d5016;
}

.story-card h3 a:hover {
  color: #4a7c2c;
}

.formula-name {
  color: #c9a961;
  font-weight: bold;
  margin: 5px 0;
}
</style>
