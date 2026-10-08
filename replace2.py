import re
with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

with open('projects_html.txt', 'r', encoding='utf-8') as f:
    replacement = f.read()

new_projects_section = f'''<section class="section" id="projects">
  <div class="sec-inner reveal">
    <div class="sec-eyebrow">Research & Engineering</div>
    <h2 class="sec-title">Projects</h2>
    <p class="sec-sub">Curated selection of my engineering, robotics, and AI work.</p>

    {replacement}
  </div>
</section>'''

# Replace from <section class="section" id="projects"> to its closing </section>
new_c = re.sub(r'<section class="section" id="projects">.*?</section>', new_projects_section, c, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_c)
