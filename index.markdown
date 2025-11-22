---
layout: default
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

<section class="stories-section">
  <h2>📚 最新故事</h2>
  
  <div class="story-list">
    {% for story in site.stories limit:6 %}
      <article class="story-card">
        <h3>
          <a href="{{ story.url | relative_url }}">{{ story.title }}</a>
        </h3>
        
        {% if story.formula %}
          <div class="formula-name">💊 {{ story.formula }}</div>
        {% endif %}
        
        {% if story.excerpt %}
          <p class="story-excerpt">{{ story.excerpt }}</p>
        {% endif %}
        
        {% if story.effects %}
          <div class="story-effects">
            <span class="effect-icon">✨</span>
            <span>{{ story.effects }}</span>
          </div>
        {% endif %}
        
        <div class="card-footer">
          <time class="story-date">📅 {{ story.date | date: "%Y年%m月%d日" }}</time>
          <a href="{{ story.url | relative_url }}" class="read-more">閱讀全文 →</a>
        </div>
      </article>
    {% endfor %}
  </div>
</section>

<!-- RSS 訂閱區塊 -->
<div class="rss-subscribe-box">
  <div class="rss-icon">📡</div>
  <div class="rss-content">
    <h3>📬 訂閱草本故事館</h3>
    <p>透過 RSS 訂閱，第一時間收到新文章通知，不錯過任何精彩內容！</p>
    <div class="rss-buttons">
      <a href="{{ '/feed.xml' | relative_url }}" class="rss-button primary">
        📡 訂閱 RSS
      </a>
      <a href="https://feedly.com/i/subscription/feed/{{ site.url }}{{ site.baseurl }}/feed.xml" 
         class="rss-button secondary" target="_blank" rel="noopener">
        🔖 用 Feedly 訂閱
      </a>
    </div>
    <p class="rss-help">
      <small>💡 不知道如何使用 RSS？
        <a href="https://feedly.com" target="_blank" rel="noopener">Feedly</a> 是最簡單的入門工具
      </small>
    </p>
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
  grid-template-columns: repeat(3, 1fr);
  gap: 30px;
}

/* 響應式設計 - 手機螢幕 */
@media (max-width: 900px) {
  .feature-grid {
    grid-template-columns: 1fr;
  }
}

/* 平板螢幕 - 顯示兩欄 */
@media (min-width: 901px) and (max-width: 1200px) {
  .feature-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

.feature-card {
  background: linear-gradient(135deg, #2d5016 0%, #4a7c2c 100%);
  padding: 40px 30px;
  border-radius: 12px;
  text-align: center;
  color: white;
  transition: all 0.3s ease;
  box-shadow: 0 4px 15px rgba(0,0,0,0.1);
}

.feature-card:hover {
  transform: translateY(-8px);
  box-shadow: 0 12px 30px rgba(45, 80, 22, 0.3);
}

.feature-card .icon {
  font-size: 3.5em;
  margin-bottom: 20px;
  display: block;
}

.feature-card h3 {
  color: #c9a961;
  margin-bottom: 15px;
  font-size: 1.6em;
}

.feature-card p {
  color: #f5f1e8;
  line-height: 1.8;
  font-size: 1.05em;
}

.stories-section {
  margin: 50px 0;
}

.stories-section h2 {
  text-align: center;
  color: #2d5016;
  font-size: 2em;
  margin-bottom: 40px;
}

.story-list {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 25px;
  margin-top: 30px;
}

.story-card {
  background: white;
  padding: 25px;
  border-radius: 12px;
  border-left: 4px solid #4a7c2c;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  transition: all 0.3s;
  display: flex;
  flex-direction: column;
}

.story-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 6px 20px rgba(0,0,0,0.15);
}

.story-card h3 {
  margin: 0 0 15px 0;
  color: #2d5016;
  font-size: 1.4em;
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
  font-size: 1.1em;
  margin-bottom: 15px;
}

.story-excerpt {
  color: #555;
  line-height: 1.7;
  margin: 15px 0;
  flex-grow: 1;
}

.story-effects {
  background: #f9f6f0;
  padding: 12px 15px;
  border-radius: 8px;
  margin: 15px 0;
  color: #4a7c2c;
  font-size: 0.95em;
  display: flex;
  align-items: center;
  gap: 8px;
}

.effect-icon {
  font-size: 1.2em;
}

.card-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 20px;
  padding-top: 15px;
  border-top: 1px solid #e8dcc8;
}

.story-date {
  color: #8b7355;
  font-size: 0.9em;
}

.read-more {
  color: #4a7c2c;
  text-decoration: none;
  font-weight: bold;
  transition: color 0.3s;
}

.read-more:hover {
  color: #6b9a3e;
}

  /* RSS 訂閱區塊 */
.rss-subscribe-box {
  display: flex;
  gap: 30px;
  align-items: center;
  background: linear-gradient(135deg, #f9f6f0 0%, #ffffff 100%);
  padding: 40px;
  margin: 50px 0;
  border-radius: 15px;
  border: 2px solid #e8f5e9;
  box-shadow: 0 4px 12px rgba(74, 124, 44, 0.1);
  transition: all 0.3s ease;
}

.rss-subscribe-box:hover {
  box-shadow: 0 6px 20px rgba(74, 124, 44, 0.15);
  transform: translateY(-2px);
}

.rss-icon {
  font-size: 4em;
  line-height: 1;
  flex-shrink: 0;
}

.rss-content {
  flex: 1;
}

.rss-content h3 {
  color: #2d5016;
  margin: 0 0 15px 0;
  font-size: 1.8em;
}

.rss-content > p {
  color: #555;
  margin: 0 0 20px 0;
  line-height: 1.6;
  font-size: 1.05em;
}

.rss-buttons {
  display: flex;
  gap: 15px;
  flex-wrap: wrap;
  margin-bottom: 15px;
}

.rss-button {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 12px 24px;
  border-radius: 25px;
  text-decoration: none;
  font-weight: 600;
  transition: all 0.3s;
  border: 2px solid transparent;
  font-size: 1em;
}

.rss-button.primary {
  background: #4a7c2c;
  color: white;
}

.rss-button.primary:hover {
  background: #6b9a3e;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(74, 124, 44, 0.3);
}

.rss-button.secondary {
  background: white;
  color: #4a7c2c;
  border-color: #4a7c2c;
}

.rss-button.secondary:hover {
  background: #f0f7ed;
  transform: translateY(-2px);
}

.rss-help {
  margin: 0;
}

.rss-help small {
  color: #888;
  font-size: 0.9em;
}

.rss-help a {
  color: #4a7c2c;
  text-decoration: underline;
}

.rss-help a:hover {
  color: #2d5016;
}

/* 響應式設計 - 手機 */
@media (max-width: 768px) {
  .rss-subscribe-box {
    flex-direction: column;
    padding: 30px 20px;
    gap: 20px;
    text-align: center;
  }
  
  .rss-icon {
    font-size: 3em;
  }
  
  .rss-buttons {
    flex-direction: column;
    width: 100%;
  }
  
  .rss-button {
    justify-content: center;
    width: 100%;
  }
}
</style>
