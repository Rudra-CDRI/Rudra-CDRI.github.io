import re
with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

with open('projects_html.txt', 'r', encoding='utf-8') as f:
    replacement = f.read()

# Replace from <div class="projects-stack" to <!-- MINI PROJECTS -->
new_c = re.sub(r'<div class="projects-stack".*?<!-- MINI PROJECTS -->', replacement + '\n\n    <!-- MINI PROJECTS -->', c, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_c)
