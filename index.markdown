---
layout: default
title: 首頁
---

<!-- ===== Hero ===== -->
<section class="home-hero">
  <div class="wrapper">
    <h1>🌿 草本故事館</h1>
    <p class="home-hero-sub">用故事認識中藥方劑，讓傳統醫學變得生動有趣</p>

    <div class="hero-social">
      <a href="https://www.instagram.com/meet.the.herbs" target="_blank" rel="noopener noreferrer" class="social-button instagram">
        <svg class="social-icon" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>
        <span>追蹤 IG</span>
      </a>
      <a href="https://open.spotify.com/show/6k6qAkTg8nX7k4FMU32hgT" target="_blank" rel="noopener noreferrer" class="social-button spotify">
        <svg class="social-icon" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M12 0C5.4 0 0 5.4 0 12s5.4 12 12 12 12-5.4 12-12S18.66 0 12 0zm5.521 17.34c-.24.359-.66.48-1.021.24-2.82-1.74-6.36-2.101-10.561-1.141-.418.122-.779-.179-.899-.539-.12-.421.18-.78.54-.9 4.56-1.021 8.52-.6 11.64 1.32.42.18.479.659.301 1.02zm1.44-3.3c-.301.42-.841.6-1.262.3-3.239-1.98-8.159-2.58-11.939-1.38-.479.12-1.02-.12-1.14-.6-.12-.48.12-1.021.6-1.141C9.6 9.9 15 10.561 18.72 12.84c.361.181.54.78.241 1.2zm.12-3.36C15.24 8.4 8.82 8.16 5.16 9.301c-.6.179-1.2-.181-1.38-.721-.18-.601.18-1.2.72-1.381 4.26-1.26 11.28-1.02 15.721 1.621.539.3.719 1.02.419 1.56-.299.421-1.02.599-1.559.3z"/></svg>
        <span>收聽 Podcast</span>
      </a>
      <a href="https://www.facebook.com/MeettheHerbs" target="_blank" rel="noopener noreferrer" class="social-button facebook">
        <svg class="social-icon" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/></svg>
        <span>Facebook 粉專</span>
      </a>
    </div>
  </div>
</section>

<!-- ===== 站內搜尋 ===== -->
<section class="section home-search-section">
  <h2 class="section-title">🔍 直接搜尋</h2>
  <p class="section-subtitle">輸入方劑名、藥材或症狀，馬上找到想讀的文章</p>
  {% include search-widget.html %}
</section>

<!-- ===== 兩大系列分流 ===== -->
<section class="section">
  <h2 class="section-title">兩大主題系列</h2>
  <p class="section-subtitle">從「方」到「藥」，兩條路線帶你讀懂中藥</p>

  <div class="series-split">
    <a href="{{ '/formulas/' | relative_url }}" class="series-card formula">
      <span class="series-emoji">💊</span>
      <h3>方劑系列</h3>
      {% assign formula_count = site.stories | where_exp: "s", "s.date <= site.time" | where_exp: "s", "s.series == nil" | size %}
      <span class="series-count">{{ formula_count }} 帖方劑</span>
      <p>一帖方劑就是一支團隊。讓每味藥材化身角色，用故事讀懂君臣佐使如何搭配、為何有效。</p>
      <span class="series-go">進入方劑系列 →</span>
    </a>

    <a href="{{ '/paozhi/' | relative_url }}" class="series-card paozhi">
      <span class="series-emoji">🔥</span>
      <h3>炮製系列</h3>
      {% assign paozhi_count = site.stories | where_exp: "s", "s.date <= site.time" | where_exp: "s", "s.series == '炮製'" | size %}
      <span class="series-count">{{ paozhi_count }} 篇炮製</span>
      <p>同一把火，炒出三種命運。炒、炙、蒸、煆……看懂中藥入方前的「變身術」，就看懂藥性如何被轉化。</p>
      <span class="series-go">進入炮製系列 →</span>
    </a>
  </div>
</section>

<!-- ===== 最新故事 ===== -->
<section class="section">
  <h2 class="section-title">📚 最新故事</h2>
  <p class="section-subtitle">最近上架的草本故事</p>

  <div class="story-grid">
    {% assign published_stories = site.stories | where_exp: "story", "story.date <= site.time" | sort: 'date' | reverse %}
    {% for story in published_stories limit:6 %}
      <article class="story-card{% if story.series %} paozhi{% endif %}">
        {% if story.series %}
          <span class="series-badge paozhi">🔥 炮製</span>
        {% else %}
          <span class="series-badge formula">💊 方劑</span>
        {% endif %}
        <h3><a href="{{ story.url | relative_url }}">{{ story.title }}</a></h3>
        {% if story.formula %}<div class="formula-name">{{ story.formula }}</div>{% endif %}
        {% if story.excerpt %}<p class="story-excerpt">{{ story.excerpt | strip_html | truncate: 88 }}</p>{% endif %}
        {% if story.effects %}
          <div class="story-effects"><span>✨</span><span>{{ story.effects | truncate: 68 }}</span></div>
        {% endif %}
        <div class="card-footer">
          <time class="story-date">{{ story.date | date: "%Y.%m.%d" }}</time>
          <a href="{{ story.url | relative_url }}" class="read-more">閱讀全文 →</a>
        </div>
      </article>
    {% endfor %}
  </div>

  <div style="text-align:center; margin-top:40px;">
    <a href="{{ '/stories/' | relative_url }}" class="btn btn-primary">📖 查看全部故事</a>
  </div>
</section>

<!-- ===== 草本夜話 Podcast ===== -->
<section class="podcast-section">
  <div class="podcast-header">
    <span class="podcast-badge">🎙️ 熱播中</span>
    <h2>草本夜話</h2>
    <p class="podcast-tagline">每一味藥草，都有自己的故事</p>
  </div>
  <div class="podcast-content-centered">
    <p class="podcast-intro">夜深了，讓我為你說一段草本的故事。</p>
    <p>跟著二十四節氣的腳步，一起認識那些陪伴人們千年的草本植物——它們的名字由來、民間傳說、歷代名醫如何運用，還有如何在日常生活中與它們相遇。</p>
    <div class="podcast-meta">
      <span class="meta-item">🌙 適合睡前聆聽</span>
      <span class="meta-item">📅 每兩週更新</span>
    </div>
    <div class="podcast-player">
      <iframe style="border-radius:12px" src="https://open.spotify.com/embed/show/6k6qAkTg8nX7k4FMU32hgT?utm_source=generator&theme=0" width="100%" height="352" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
    </div>
    <a href="https://open.spotify.com/show/6k6qAkTg8nX7k4FMU32hgT" target="_blank" rel="noopener noreferrer" class="podcast-cta">
      <svg class="spotify-icon" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M12 0C5.4 0 0 5.4 0 12s5.4 12 12 12 12-5.4 12-12S18.66 0 12 0zm5.521 17.34c-.24.359-.66.48-1.021.24-2.82-1.74-6.36-2.101-10.561-1.141-.418.122-.779-.179-.899-.539-.12-.421.18-.78.54-.9 4.56-1.021 8.52-.6 11.64 1.32.42.18.479.659.301 1.02zm1.44-3.3c-.301.42-.841.6-1.262.3-3.239-1.98-8.159-2.58-11.939-1.38-.479.12-1.02-.12-1.14-.6-.12-.48.12-1.021.6-1.141C9.6 9.9 15 10.561 18.72 12.84c.361.181.54.78.241 1.2zm.12-3.36C15.24 8.4 8.82 8.16 5.16 9.301c-.6.179-1.2-.181-1.38-.721-.18-.601.18-1.2.72-1.381 4.26-1.26 11.28-1.02 15.721 1.621.539.3.719 1.02.419 1.56-.299.421-1.02.599-1.559.3z"/></svg>
      在 Spotify 上收聽
    </a>
  </div>
</section>

<!-- ===== 本草心語抽卡 ===== -->
<section class="oracle-section">
  <div class="oracle-content">
    <div class="oracle-text">
      <span class="oracle-badge">🔮 互動小物</span>
      <h2 class="oracle-title">本草心語</h2>
      <p class="oracle-subtitle">Herbal Heart Language</p>
      <p class="oracle-desc">靜下心，感受此刻的自己。讓一味本草，回應你內心的聲音。</p>
      <p class="oracle-detail">抽一張卡，看看今天的草本想對你說什麼——無論是當歸的思念、薄荷的清涼、還是人參的力量，都是專屬於你的一段心靈對話。</p>
      <a href="https://tcm-oracle-cards-v2.vercel.app/" target="_blank" rel="noopener noreferrer" class="oracle-cta">開始抽牌 →</a>
    </div>
    <div class="oracle-visual">
      <div class="oracle-card-stack">
        <div class="oracle-card card-shadow-1"></div>
        <div class="oracle-card card-shadow-2"></div>
        <div class="oracle-card card-main">
          <img src="{{ '/assets/images/oracle-card-back.png' | relative_url }}" alt="本草心語卡牌">
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ===== 特色 ===== -->
<section class="section features">
  <h2 class="section-title">✨ 我們的特色</h2>
  <div class="feature-grid">
    <div class="feature-card"><span class="feature-icon">📖</span><div><h3>故事化呈現</h3><p>用生活化的故事，輕鬆理解中藥方劑</p></div></div>
    <div class="feature-card"><span class="feature-icon">🎭</span><div><h3>藥材擬人化</h3><p>每味藥材都是獨特角色，記憶更深刻</p></div></div>
    <div class="feature-card"><span class="feature-icon">💡</span><div><h3>實用建議</h3><p>提供適用症狀與注意事項</p></div></div>
  </div>
</section>

<style>
/* ===== 首頁專屬樣式 ===== */
.home-hero {
  text-align: center;
  padding: 72px 20px 60px;
  background: linear-gradient(135deg, var(--green-900) 0%, var(--green-500) 100%);
  color: #fff;
}
.home-hero h1 { font-size: clamp(2.2rem, 6vw, 3rem); margin-bottom: 14px; }
.home-hero-sub { font-size: 1.15rem; opacity: 0.95; }

.hero-social { margin-top: 30px; display: flex; justify-content: center; gap: 14px; flex-wrap: wrap; }
.social-button {
  display: inline-flex; align-items: center; gap: 9px; padding: 13px 26px;
  text-decoration: none; border-radius: 30px; font-weight: 600; font-size: 1rem;
  transition: transform 0.3s, box-shadow 0.3s; box-shadow: 0 4px 12px rgba(0,0,0,0.15); color: #fff;
}
.social-button:hover { transform: translateY(-3px); box-shadow: 0 6px 20px rgba(0,0,0,0.25); }
.social-button.instagram { background: linear-gradient(45deg, #f09433 0%, #e6683c 25%, #dc2743 50%, #cc2366 75%, #bc1888 100%); }
.social-button.spotify { background: #1DB954; }
.social-button.facebook { background: #1877f2; }
.social-icon { width: 21px; height: 21px; fill: currentColor; }
@media (max-width: 640px) {
  .hero-social { flex-direction: column; padding: 0 16px; }
  .social-button { width: 100%; justify-content: center; }
}

/* Podcast */
.podcast-section {
  background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
  border-radius: var(--radius-lg); padding: 50px 40px; margin: 56px auto; max-width: 1080px;
  color: #fff; box-shadow: 0 10px 40px rgba(0,0,0,0.3); position: relative; overflow: hidden;
}
.podcast-header { text-align: center; margin-bottom: 36px; }
.podcast-badge {
  display: inline-block; background: linear-gradient(135deg, var(--gold) 0%, var(--gold-soft) 100%);
  color: #1a1a2e; padding: 7px 18px; border-radius: 20px; font-size: 0.88rem; font-weight: 700; letter-spacing: 1px;
}
.podcast-header h2 {
  font-size: 2.6rem; margin: 14px 0;
  background: linear-gradient(135deg, #fff 0%, var(--gold-soft) 100%);
  -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
}
.podcast-tagline { font-size: 1.2rem; color: #a8b2d1; font-style: italic; }
.podcast-content-centered { max-width: 780px; margin: 0 auto; text-align: center; position: relative; z-index: 1; }
.podcast-content-centered p { color: #ccd6f6; line-height: 1.8; margin-bottom: 14px; }
.podcast-intro { font-size: 1.2rem; color: var(--gold); font-weight: 500; }
.podcast-meta { display: flex; flex-wrap: wrap; gap: 14px; margin: 24px 0; justify-content: center; }
.meta-item { background: rgba(255,255,255,0.1); padding: 9px 16px; border-radius: 25px; font-size: 0.88rem; color: #a8b2d1; }
.podcast-player { margin: 28px auto; max-width: 600px; }
.podcast-player iframe { box-shadow: 0 8px 30px rgba(0,0,0,0.4); border-radius: 12px; }
.podcast-cta {
  display: inline-flex; align-items: center; gap: 11px; background: #1DB954; color: #fff;
  padding: 15px 30px; border-radius: 30px; text-decoration: none; font-weight: 600; margin-top: 18px;
  transition: all 0.3s; box-shadow: 0 4px 15px rgba(29,185,84,0.3);
}
.podcast-cta:hover { background: #1ed760; transform: translateY(-3px); }
.spotify-icon { width: 23px; height: 23px; fill: currentColor; }
@media (max-width: 900px) { .podcast-section { padding: 40px 24px; margin: 40px 20px; } .podcast-header h2 { font-size: 2.1rem; } }

/* Oracle */
.oracle-section {
  background: linear-gradient(135deg, #FAF6F0 0%, #F5EDE0 50%, #EDE4D3 100%);
  border-radius: var(--radius-lg); padding: 50px 40px; margin: 56px auto; max-width: 1080px;
  box-shadow: 0 6px 30px rgba(139,94,60,0.1); border: 1px solid rgba(193,163,120,0.2);
}
.oracle-content { max-width: 900px; margin: 0 auto; display: grid; grid-template-columns: 1fr 260px; gap: 46px; align-items: center; }
.oracle-badge { display: inline-block; background: linear-gradient(135deg, #8B5E9B 0%, #A67BB5 100%); color: #fff; padding: 6px 16px; border-radius: 20px; font-size: 0.82rem; font-weight: 700; letter-spacing: 1px; }
.oracle-title { font-size: 2.4rem; font-weight: 900; color: #8B6B3D; margin: 12px 0 4px; letter-spacing: 5px; }
.oracle-subtitle { font-size: 0.95rem; color: #B8976A; letter-spacing: 3px; margin-bottom: 18px; font-weight: 500; }
.oracle-desc { font-size: 1.1rem; color: #6B5B4B; line-height: 1.8; margin-bottom: 6px; }
.oracle-detail { font-size: 0.95rem; color: #8B7B6B; line-height: 1.8; margin: 14px 0 24px; }
.oracle-cta { display: inline-block; background: linear-gradient(135deg, #8B6B3D 0%, #B8976A 100%); color: #fff; padding: 13px 32px; border-radius: 30px; text-decoration: none; font-weight: 600; transition: all 0.3s; box-shadow: 0 4px 15px rgba(139,107,61,0.25); }
.oracle-cta:hover { transform: translateY(-3px); box-shadow: 0 8px 25px rgba(139,107,61,0.35); }
.oracle-visual { display: flex; justify-content: center; }
.oracle-card-stack { position: relative; width: 180px; height: 240px; }
.oracle-card { position: absolute; width: 160px; height: 220px; border-radius: 16px; box-shadow: 0 4px 20px rgba(0,0,0,0.12); }
.card-shadow-1 { background: linear-gradient(135deg, #D4C4A8 0%, #C9B896 100%); top: 0; left: 0; transform: rotate(-8deg); }
.card-shadow-2 { background: linear-gradient(135deg, #C9B896 0%, #BBA97E 100%); top: 0; left: 10px; transform: rotate(-3deg); }
.card-main { top: 0; left: 20px; transform: rotate(2deg); overflow: hidden; transition: transform 0.3s; }
.card-main:hover { transform: rotate(0deg) translateY(-8px); }
.card-main img { width: 100%; height: 100%; object-fit: cover; border-radius: 16px; }
@media (max-width: 768px) {
  .oracle-content { grid-template-columns: 1fr; gap: 28px; text-align: center; }
  .oracle-section { padding: 40px 24px; margin: 40px 20px; }
  .oracle-title { font-size: 2rem; }
  .oracle-visual { order: -1; }
  .oracle-card-stack { margin: 0 auto; }
}

/* Features — 精簡白底卡 */
.feature-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 18px; }
.feature-card {
  background: #fff; border: 1px solid var(--line); border-top: 3px solid var(--green-500);
  padding: 20px 22px; border-radius: var(--radius); display: flex; align-items: flex-start; gap: 14px;
  transition: transform 0.25s, box-shadow 0.25s; box-shadow: var(--shadow-sm);
}
.feature-card:hover { transform: translateY(-3px); box-shadow: var(--shadow-md); }
.feature-icon { font-size: 1.9rem; line-height: 1.1; flex-shrink: 0; }
.feature-card h3 { color: var(--green-700); margin-bottom: 4px; font-size: 1.12rem; }
.feature-card p { color: var(--ink-soft); line-height: 1.6; font-size: 0.94rem; }
@media (max-width: 860px) { .feature-grid { grid-template-columns: 1fr; } }

/* RSS */
.rss-subscribe-box {
  display: flex; gap: 28px; align-items: center;
  background: linear-gradient(135deg, #f9f6f0 0%, #fff 100%);
  padding: 36px; border-radius: var(--radius); border: 2px solid #e8f5e9; box-shadow: var(--shadow-sm);
}
.rss-icon { font-size: 3.6rem; line-height: 1; flex-shrink: 0; }
.rss-content h3 { color: var(--green-700); margin-bottom: 12px; font-size: 1.6rem; }
.rss-content > p { color: #555; margin-bottom: 18px; line-height: 1.6; }
.rss-buttons { display: flex; gap: 13px; flex-wrap: wrap; }
.rss-button { display: inline-flex; align-items: center; gap: 8px; padding: 11px 22px; border-radius: 25px; text-decoration: none; font-weight: 600; transition: all 0.3s; border: 2px solid transparent; }
.rss-button.primary { background: var(--green-500); color: #fff; }
.rss-button.primary:hover { background: var(--green-400); transform: translateY(-2px); }
.rss-button.secondary { background: #fff; color: var(--green-500); border-color: var(--green-500); }
.rss-button.secondary:hover { background: var(--green-050); transform: translateY(-2px); }
@media (max-width: 640px) {
  .rss-subscribe-box { flex-direction: column; text-align: center; padding: 28px 20px; }
  .rss-buttons { flex-direction: column; width: 100%; }
  .rss-button { justify-content: center; width: 100%; }
}
</style>
