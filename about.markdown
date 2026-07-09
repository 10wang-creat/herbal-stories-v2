---
layout: default
title: 關於
permalink: /about/
---

<section class="page-hero">
  <div class="page-emoji">🌿</div>
  <h1>關於草本故事館</h1>
  <p class="subtitle">讓傳統中醫，變成你我都能理解的故事</p>
</section>

<div class="inner-page narrow">
  <div class="about-content">
    <section class="mission">
      <div class="section-icon">💡</div>
      <h2>我們的使命</h2>
      <p>中藥方劑有著千年智慧，但對現代人來說卻常常顯得遙遠而難懂。我們相信，每一個方劑背後都藏著一個精彩的故事，每味藥材都有它獨特的個性。</p>
      <p><strong>草本故事館</strong>的使命，就是用生動的故事、貼近生活的比喻，讓中醫知識變得有趣、好懂、好記。</p>
    </section>

    <section class="approach">
      <div class="section-icon">✨</div>
      <h2>我們的做法</h2>
      <div class="approach-grid">
        <div class="approach-card">
          <h3>📖 故事化</h3>
          <p>將枯燥的方劑變成有情節的故事，讓你在閱讀中自然記住</p>
        </div>
        <div class="approach-card">
          <h3>🎭 擬人化</h3>
          <p>每味藥材都是獨特的角色，有自己的性格和專長</p>
        </div>
        <div class="approach-card">
          <h3>🏥 生活化</h3>
          <p>從真實案例出發，讓你知道什麼時候需要這些方劑</p>
        </div>
        <div class="approach-card">
          <h3>🔬 科學化</h3>
          <p>基於中醫理論，提供準確的藥材資訊和使用建議</p>
        </div>
      </div>
    </section>

    <section class="values">
      <div class="section-icon">💚</div>
      <h2>我們的價值觀</h2>
      <ul class="values-list">
        <li><strong>尊重傳統</strong>：忠於中醫經典，不扭曲方劑本意</li>
        <li><strong>貼近現代</strong>：用現代語言和思維重新詮釋</li>
        <li><strong>負責任</strong>：強調個體差異，鼓勵專業諮詢</li>
        <li><strong>有趣味</strong>：學習中醫不該是苦差事</li>
      </ul>
    </section>

    <section class="target">
      <div class="section-icon">👥</div>
      <h2>適合誰閱讀？</h2>
      <div class="target-grid">
        <div class="target-item">
          <div class="target-emoji">🤔</div>
          <p>對中醫好奇，但看不懂古文的你</p>
        </div>
        <div class="target-item">
          <div class="target-emoji">📚</div>
          <p>正在學習中醫，需要輔助記憶的學生</p>
        </div>
        <div class="target-item">
          <div class="target-emoji">💊</div>
          <p>想了解自己吃的中藥的患者</p>
        </div>
        <div class="target-item">
          <div class="target-emoji">🌱</div>
          <p>關心健康，想預防保健的現代人</p>
        </div>
      </div>
    </section>

    <section class="disclaimer">
      <div class="section-icon">⚠️</div>
      <h2>重要聲明</h2>
      <div class="disclaimer-box">
        <p><strong>草本故事館</strong>是一個教育性質的平台，所有內容僅供參考學習，不構成醫療建議。</p>
        <p>中藥方劑的使用需要根據個人體質、症狀、季節等多種因素調整，<strong>請務必在合格中醫師的指導下使用</strong>。</p>
        <p>如有任何健康問題，請及時就醫，切勿自行診斷或用藥。</p>
      </div>
    </section>


  </div>
</div>

<style>
.about-content section {
  background: white;
  padding: 40px;
  border-radius: 12px;
  margin-bottom: 30px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.08);
}

.section-icon {
  font-size: 2.5em;
  text-align: center;
  margin-bottom: 20px;
}

.about-content h2 {
  color: #2d5016;
  font-size: 2em;
  margin-bottom: 25px;
  text-align: center;
}

.about-content p {
  line-height: 1.8;
  color: #333;
  font-size: 1.1em;
  margin-bottom: 1.2em;
}

.approach-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 20px;
  margin-top: 30px;
}

@media (max-width: 1024px) {
  .approach-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 768px) {
  .approach-grid {
    grid-template-columns: 1fr;
  }
}

.approach-card {
  background: linear-gradient(135deg, #e8f5e9 0%, #f1f8f4 100%);
  padding: 30px 20px;
  border-radius: 10px;
  text-align: center;
  border: 2px solid #c8e6c9;
  transition: transform 0.3s;
}

.approach-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 6px 16px rgba(74, 124, 44, 0.15);
}

.approach-card h3 {
  color: #2d5016;
  font-size: 1.3em;
  margin-bottom: 15px;
}

.approach-card p {
  color: #555;
  font-size: 1em;
}

/* LINE 貼圖區塊樣式 */
.sticker-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 20px;
  margin: 30px 0;
}

@media (max-width: 768px) {
  .sticker-grid {
    grid-template-columns: 1fr;
  }
}

.sticker-card {
  background: linear-gradient(135deg, #fff8e1 0%, #fffde7 100%);
  padding: 30px 20px;
  border-radius: 10px;
  text-align: center;
  border: 2px solid #ffe082;
  transition: transform 0.3s;
}

.sticker-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 6px 16px rgba(255, 193, 7, 0.2);
}

.sticker-emoji {
  font-size: 3em;
  margin-bottom: 15px;
}

.sticker-card h3 {
  color: #f57c00;
  font-size: 1.3em;
  margin-bottom: 15px;
}

.sticker-card p {
  color: #555;
  font-size: 1em;
  margin-bottom: 0;
}

.sticker-cta {
  text-align: center;
  margin-top: 20px;
}

.sticker-button {
  display: inline-block;
  background: linear-gradient(135deg, #06c755 0%, #00b341 100%);
  color: white;
  padding: 15px 40px;
  border-radius: 30px;
  text-decoration: none;
  font-size: 1.2em;
  font-weight: bold;
  transition: all 0.3s;
  box-shadow: 0 4px 12px rgba(6, 199, 85, 0.3);
}

.sticker-button:hover {
  transform: translateY(-3px);
  box-shadow: 0 6px 20px rgba(6, 199, 85, 0.4);
  color: white;
}

.values-list {
  list-style: none;
  padding: 0;
  margin-top: 20px;
}

.values-list li {
  padding: 15px 20px;
  margin: 10px 0;
  background: #f8f9fa;
  border-left: 4px solid #4a7c2c;
  border-radius: 5px;
  line-height: 1.6;
  font-size: 1.1em;
}

.values-list strong {
  color: #2d5016;
}

.target-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 20px;
  margin-top: 30px;
}

@media (max-width: 1024px) {
  .target-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 768px) {
  .target-grid {
    grid-template-columns: 1fr;
  }
}

.target-item {
  text-align: center;
  padding: 25px;
  background: #f5f1e8;
  border-radius: 10px;
  transition: transform 0.3s;
}

.target-item:hover {
  transform: scale(1.05);
}

.target-emoji {
  font-size: 3em;
  margin-bottom: 15px;
}

.target-item p {
  color: #2d5016;
  font-weight: 500;
  margin: 0;
}

.disclaimer-box {
  background: #fff3cd;
  border: 2px solid #ffc107;
  border-radius: 10px;
  padding: 25px;
  margin-top: 20px;
}

.disclaimer-box p {
  color: #856404;
  margin-bottom: 15px;
}

.disclaimer-box strong {
  color: #664d03;
}

</style>
