with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('<div class="projects-stack" style="display:grid; grid-template-columns: repeat(2, 1fr); gap:32px;">', 
              '<div class="projects-stack" style="display:grid; grid-template-columns: repeat(3, 1fr); gap:24px;">')

css_addition = '''@media(max-width: 1200px) {
  .projects-stack { grid-template-columns: repeat(2, 1fr) !important; }
}'''

c = c.replace('@media(max-width:900px){', css_addition + '\n\n@media(max-width:900px){')

# The user also says "these tiles are too big make them smaller". 
# The image height was 220px, maybe reduce it to 180px for a 3-column layout?
c = c.replace('height: 220px', 'height: 180px')
c = c.replace('min-height: 220px', 'min-height: 180px')
c = c.replace('.proj-content { padding: 24px 28px;', '.proj-content { padding: 20px 24px;')

# slightly smaller titles/text
c = c.replace('.proj-title{font-size:22px', '.proj-title{font-size:20px')
c = c.replace('.proj-body{font-size:14.5px;color:#666;line-height:1.65;margin-bottom: 16px;}', '.proj-body{font-size:13.5px;color:#666;line-height:1.6;margin-bottom: 16px;}')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)
