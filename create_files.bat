@echo off
chcp 65001 > nul

REM Create story.html layout
(
echo ---
echo layout: default
echo ---
echo.
echo ^<article class="story"^>
echo   ^<header class="story-header"^>
echo     ^<h1^>{{ page.title }}^</h1^>
echo     ^<p class="formula-name"^>{{ page.formula }}^</p^>
echo     ^<div class="meta"^>
echo       ^<span class="date"^>{{ page.date ^| date: "%%Y年%%m月%%d日" }}^</span^>
echo     ^</div^>
echo   ^</header^>
echo.
echo   ^<div class="story-content"^>
echo     {{ content }}
echo   ^</div^>
echo.
echo   {% if page.ingredients %}
echo   ^<section class="ingredients"^>
echo     ^<h2^>藥材組成^</h2^>
echo     ^<ul^>
echo     {% for ingredient in page.ingredients %}
echo       ^<li^>^<strong^>{{ ingredient.name }}^</strong^> - {{ ingredient.description }}^</li^>
echo     {% endfor %}
echo     ^</ul^>
echo   ^</section^>
echo   {% endif %}
echo.
echo   {% if page.effects %}
echo   ^<section class="effects"^>
echo     ^<h2^>功效^</h2^>
echo     ^<p^>{{ page.effects }}^</p^>
echo   ^</section^>
echo   {% endif %}
echo ^</article^>
) > _layouts\story.html

echo Created _layouts\story.html
pause