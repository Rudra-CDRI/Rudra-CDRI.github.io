with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Compact vertical density
c = c.replace('.proj-panel .proj-img-wrap { overflow: hidden; border-radius: 0; width: 100%; height: 280px; display: block; flex-shrink: 0; }',
              '.proj-panel .proj-img-wrap { overflow: hidden; border-radius: 0; width: 100%; height: 220px; display: block; flex-shrink: 0; }')

c = c.replace('.proj-panel .proj-img { width: 100%; height: 100%; object-fit: cover; min-height: 280px; transform-origin: center; border-radius: 0; }',
              '.proj-panel .proj-img { width: 100%; height: 100%; object-fit: cover; min-height: 220px; transform-origin: center; border-radius: 0; transition: transform 0.4s ease-out, filter 0.4s ease-out; }')

c = c.replace('.proj-content { padding: 32px; display: flex; flex-direction: column; justify-content: flex-start; background: transparent; flex-grow: 1; }',
              '.proj-content { padding: 24px 28px; display: flex; flex-direction: column; justify-content: flex-start; background: transparent; flex-grow: 1; }')

c = c.replace('.proj-num{font-size:12px;letter-spacing:.2em;text-transform:uppercase;color:#c97d4e;font-weight:700;margin-bottom: 16px;}',
              '.proj-num{font-size:12px;letter-spacing:.2em;text-transform:uppercase;color:#c97d4e;font-weight:700;margin-bottom: 8px;}')

c = c.replace('.proj-title{font-size:24px;font-weight:800;line-height:1.25;margin-bottom: 16px;color:#1c1c1e;}',
              '.proj-title{font-size:22px;font-weight:800;line-height:1.25;margin-bottom: 12px;color:#1c1c1e;}')

c = c.replace('.proj-body{font-size:15px;color:#666;line-height:1.8;margin-bottom: 16px;}',
              '.proj-body{font-size:14.5px;color:#666;line-height:1.65;margin-bottom: 16px;}')

c = c.replace('.proj-tags{display:flex;flex-wrap:wrap;gap: 8px;margin-bottom: 16px;}',
              '.proj-tags{display:flex;flex-wrap:wrap;gap: 6px;margin-bottom: 12px;}')

c = c.replace('.proj-tools{font-size:12px;color:#aaa;margin-bottom: 24px;}',
              '.proj-tools{font-size:12px;color:#aaa;margin-bottom: 0px;}')

# Fix inline padding on buttons wrapper
c = c.replace('padding-top: 24px;', 'padding-top: 16px;')

# 2. Hover Interactions
c = c.replace('.main-proj-wrapper:hover { transform: scale(1.02); box-shadow: 0 20px 40px rgba(0,0,0,0.08); }',
              '.main-proj-wrapper:hover { transform: translateY(-4px); box-shadow: 0 16px 32px rgba(0,0,0,0.06); }')

c = c.replace('.proj-panel:hover .proj-img { filter: brightness(1.05); }',
              '.proj-panel:hover .proj-img { transform: scale(1.03); filter: brightness(1.05); }')

# 3. Fix mobile padding for proj-content
c = c.replace('.proj-content { padding: 32px 24px; }',
              '.proj-content { padding: 24px 20px; }')

c = c.replace('.proj-img { min-height: 240px; border-radius: 0; }',
              '.proj-img { min-height: 200px; border-radius: 0; }')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)
