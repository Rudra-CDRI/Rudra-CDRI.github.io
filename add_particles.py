with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Add canvas to hero
c = c.replace('<section id="hero" class="hero-geometric">\n  <div class="hero-text reveal"',
              '<section id="hero" class="hero-geometric">\n  <canvas id="hero-canvas" style="position:absolute;top:0;left:0;width:100%;height:100%;z-index:0;pointer-events:none;"></canvas>\n  <div class="hero-text reveal"')

js_logic = '''
// Interactive Particle Background for Hero
(function() {
  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (prefersReducedMotion) return;

  const canvas = document.getElementById('hero-canvas');
  const hero = document.getElementById('hero');
  if (!canvas || !hero) return;
  
  const ctx = canvas.getContext('2d');
  let width, height;
  let particles = [];
  
  let mouse = { x: -9999, y: -9999 };
  
  hero.addEventListener('mousemove', (e) => {
    const rect = hero.getBoundingClientRect();
    mouse.x = e.clientX - rect.left;
    mouse.y = e.clientY - rect.top;
  });
  hero.addEventListener('mouseleave', () => {
    mouse.x = -9999;
    mouse.y = -9999;
  });
  
  function resize() {
    width = canvas.width = hero.offsetWidth;
    height = canvas.height = hero.offsetHeight;
    initParticles();
  }
  window.addEventListener('resize', resize);
  
  class Particle {
    constructor() {
      this.x = Math.random() * width;
      this.y = Math.random() * height;
      this.vx = (Math.random() - 0.5) * 0.8; // Slow drifting speed
      this.vy = (Math.random() - 0.5) * 0.8;
      this.radius = Math.random() * 1.5 + 1; // 1 to 2.5px
    }
    update() {
      this.x += this.vx;
      this.y += this.vy;
      
      // Wrap around edges instead of bouncing for a smoother infinite feel
      if (this.x < -10) this.x = width + 10;
      if (this.x > width + 10) this.x = -10;
      if (this.y < -10) this.y = height + 10;
      if (this.y > height + 10) this.y = -10;
      
      // Repel from mouse
      const dx = mouse.x - this.x;
      const dy = mouse.y - this.y;
      const dist = Math.sqrt(dx * dx + dy * dy);
      const repelRadius = 180;
      
      if (dist < repelRadius) {
        const force = (repelRadius - dist) / repelRadius;
        this.x -= (dx / dist) * force * 3;
        this.y -= (dy / dist) * force * 3;
      }
    }
    draw() {
      ctx.beginPath();
      ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
      ctx.fillStyle = 'rgba(201, 125, 78, 0.6)'; // Accent color
      ctx.fill();
    }
  }
  
  function initParticles() {
    particles = [];
    // Number of particles depends on screen size, capped at 120
    const numParticles = Math.min(Math.floor((width * height) / 12000), 120);
    for (let i = 0; i < numParticles; i++) {
      particles.push(new Particle());
    }
  }
  
  function animate() {
    ctx.clearRect(0, 0, width, height);
    
    // Update and draw particles
    particles.forEach(p => {
      p.update();
      p.draw();
    });
    
    // Draw connecting lines
    ctx.lineWidth = 1;
    for (let i = 0; i < particles.length; i++) {
      for (let j = i + 1; j < particles.length; j++) {
        const dx = particles[i].x - particles[j].x;
        const dy = particles[i].y - particles[j].y;
        const dist = Math.sqrt(dx * dx + dy * dy);
        
        // Connect if close enough
        if (dist < 140) {
          ctx.beginPath();
          const opacity = (1 - (dist / 140)) * 0.35; // Max opacity 0.35
          ctx.strokeStyle = `rgba(201, 125, 78, ${opacity})`;
          ctx.moveTo(particles[i].x, particles[i].y);
          ctx.lineTo(particles[j].x, particles[j].y);
          ctx.stroke();
        }
      }
    }
    
    requestAnimationFrame(animate);
  }
  
  setTimeout(() => {
    resize();
    animate();
  }, 100);
})();
'''

c = c.replace('window.dispatchEvent(new Event(\'scroll\'));\n\n// EXPERIMENTAL: Parallax Hover Effect in Hero', 
              'window.dispatchEvent(new Event(\'scroll\'));\n\n' + js_logic + '\n// EXPERIMENTAL: Parallax Hover Effect in Hero')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)
