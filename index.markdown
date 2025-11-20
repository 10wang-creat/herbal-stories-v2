---
layout: home
title: 首頁
---

<div class="hero-section">
  <h1>🌿 歡迎來到草本故事館</h1>
  <p class="hero-subtitle">用故事認識中藥方劑，讓傳統醫學變得生動有趣</p>
</div>

<div class="features">
  <h2>✨ 我們的特色</h2>
  
  <div class="feature-grid">
    <div class="feature-card">
      <div class="feature-icon">📖</div>
      <h3>故事化呈現</h3>
      <p>用生活化的故事，輕鬆理解中藥方劑</p>
    </div>
    
    <div class="feature-card">
      <div class="feature-icon">🎭</div>
      <h3>藥材擬人化</h3>
      <p>每味藥材都是獨特角色，記憶更深刻</p>
    </div>
    
    <div class="feature-card">
      <div class="feature-icon">💡</div>
      <h3>實用建議</h3>
      <p>提供適用症狀與注意事項</p>
    </div>
  </div>
</div>

<div class="stories-section">
  <h2>📚 最新文章</h2>
  
  <div class="story-list">
  {% for story in site.stories %}
    <div class="story-card">
      <div class="story-date">📅 {{ story.date | date: "%Y年%m月%d日" }}</div>
      <h3><a href="{{ story.url | relative_url }}">{{ story.title }}</a></h3>
      <p class="formula-name">💊 {{ story.formula }}</p>
      <p class="story-excerpt">{{ story.excerpt }}</p>
      <a href="{{ story.url | relative_url }}" class="read-more">閱讀全文 →</a>
    </div>
  {% endfor %}
  </div>
</div>

<style>
body {
  background-color: #f5f1e8;
}

.hero-section {
  text-align: center;
  padding: 60px 20px;
  background: linear-gradient(135deg, #2d5016 0%, #4a7c2c 100%);
  color: white;
  border-radius: 12px;
  margin-bottom: 40px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.15);
}

.hero-section h1 {
  font-size: 2.5em;
  margin-bottom: 15px;
  font-weight: bold;
}

.hero-subtitle {
  font-size: 1.2em;
  opacity: 0.95;
}

.features {
  margin: 50px 0;
}

.features h2 {
  text-align: center;
  color: #2d5016;
  font-size: 2em;
  margin-bottom: 40px;
}

.feature-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 25px;
  margin-bottom: 50px;
}

.feature-card {
  background: linear-gradient(135deg, #4a7c2c 0%, #5a8c3c 100%);
  padding: 35px 25px;
  border-radius: 12px;
  text-align: center;
  color: white;
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
  transition: transform 0.3s, box-shadow 0.3s;
}

.feature-card:hover {
  transform: translateY(-8px);
  box-shadow: 0 8px 20px rgba(0,0,0,0.2);
}

.feature-icon {
  font-size: 3em;
  margin-bottom: 15px;
}

.feature-card h3 {
  color: #ffd700;
  margin: 15px 0;
  font-size: 1.4em;
}

.feature-card p {
  opacity: 0.95;
  line-height: 1.6;
}

.stories-section {
  margin-top: 60px;
}

.stories-section h2 {
  text-align: center;
  color: #2d5016;
  font-size: 2em;
  margin-bottom: 40px;
}

.story-list {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 25px;
}

.story-card {
  background: white;
  padding: 30px;
  border-radius: 12px;
  border-left: 5px solid #4a7c2c;
  box-shadow: 0 3px 10px rgba(0,0,0,0.1);
  transition: transform 0.3s, box-shadow 0.3s;
}

.story-card:hover {
  transform: translateY(-8px);
  box-shadow: 0
