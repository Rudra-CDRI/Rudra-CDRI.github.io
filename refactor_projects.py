import re
with open('index.html', 'r', encoding='utf-8') as f: c = f.read()
c = re.sub(r'<div class=\
projects-stack\.*?<!-- MINI PROJECTS -->', open('projects_html.txt', 'r', encoding='utf-8').read() + '\n\n    <!-- MINI PROJECTS -->', c, flags=re.DOTALL)
with open('index.html', 'w', encoding='utf-8') as f: f.write(c)
