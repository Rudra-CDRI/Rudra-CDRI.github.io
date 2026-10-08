with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Change image source
c = c.replace('src="assests/images/hero_profile.png"', 'src="assests/images/new_hero_profile.jpg"')

# Enlarge image sizes
c = c.replace('width: 360px;\n    height: 440px;', 'width: 420px;\n    height: 520px;')
c = c.replace('.hero-photo-geo { width: 300px; height: 380px; }', '.hero-photo-geo { width: 360px; height: 460px; }')

# Fix ID for geometry
c = c.replace('<div class="geo-solid-shape"></div>', '<div class="geo-solid-shape" id="parallaxShape"></div>')

# Modify Parallax Script
c = c.replace("const pBlob = document.getElementById('parallaxBlob');", "const pBlob = document.getElementById('parallaxBlob');\nconst pShape = document.getElementById('parallaxShape');")
c = c.replace("if(pImg) pImg.style.transform = `translate(${x * 1}px, ${y * 1}px)`;", "if(pImg) pImg.style.transform = `translate(${x * 0.1}px, ${y * 0.1}px)`;\n  if(pShape) pShape.style.transform = `translate(${x * 2.5}px, ${y * 2.5}px)`;")
c = c.replace("const elements = [pBlob, pImg, pB1, pB2];", "const elements = [pBlob, pImg, pShape, pB1, pB2];")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)
