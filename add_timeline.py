with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Replace CSS
c = c.replace('.timeline::before{content:\'\';position:absolute;left: 11px;top: 0;bottom: 0;width:2px;background:linear-gradient(#c97d4e,#e8e4dc);}', 
              '.timeline::before{content:\'\';position:absolute;left: 11px;top: 0;bottom: 0;width:2px;background:#e8e4dc;}\n.timeline-progress { position:absolute;left: 11px;top: 0;width:2px;background:#c97d4e;height:0%;transition:height 0.1s ease-out;z-index: 1; }')
c = c.replace('body.dark .timeline::before { background:linear-gradient(#c97d4e,#222222); }', 
              'body.dark .timeline::before { background:#222222; }')
              
c = c.replace('.tl-dot{position:absolute;left: 4px;top: 0px;width:16px;height:16px;border-radius:50%;background:#c97d4e;border:3px solid #fafaf8;box-shadow:0 0 0 2px #c97d4e;}',
              '.tl-dot{position:absolute;left: 4px;top: 0px;width:16px;height:16px;border-radius:50%;background:#e8e4dc;border:3px solid #fafaf8;box-shadow:0 0 0 2px #e8e4dc;transition: background 0.4s ease, box-shadow 0.4s ease;z-index: 2;}\n.tl-dot.active { background:#c97d4e;box-shadow:0 0 0 2px #c97d4e; }')

c = c.replace('body.dark .tl-dot { border-color: #080808; }',
              'body.dark .tl-dot { background: #222; box-shadow: 0 0 0 2px #333; border-color: #080808; }\nbody.dark .tl-dot.active { background:#c97d4e; box-shadow:0 0 0 2px #c97d4e; border-color: #080808; }')

# Clean up any empty dots css since we made all dots initially empty
c = c.replace('.tl-dot.empty{background:#e8e4dc;box-shadow:0 0 0 2px #e8e4dc;}', '')
c = c.replace('body.dark .tl-dot.empty { background: #222; box-shadow: 0 0 0 2px #333; }', '')

# Change .tl
c = c.replace('.tl{position:relative;padding: 0 0 32px 40px;}',
              '.tl{position:relative;padding: 0 0 32px 40px; opacity:0; transform:translateY(16px); transition:opacity 0.6s ease-out, transform 0.6s ease-out;}\n.tl.active { opacity:1; transform:translateY(0); }')

# Insert timeline progress div
c = c.replace('<div class="timeline reveal">\n      <div class="tl">', 
              '<div class="timeline">\n      <div class="timeline-progress"></div>\n      <div class="tl">')

# Add JS logic
js_logic = '''
// Timeline Scroll Animation
window.addEventListener('scroll', () => {
  const timeline = document.querySelector('.timeline');
  if (!timeline) return;
  const rect = timeline.getBoundingClientRect();
  const timelineHeight = rect.height;
  const triggerPoint = window.innerHeight * 0.7; // 70% down the screen
  
  // Calculate how far the trigger point is past the top of the timeline
  let progress = (triggerPoint - rect.top) / timelineHeight;
  progress = Math.max(0, Math.min(1, progress));
  
  const progressLine = document.querySelector('.timeline-progress');
  if (progressLine) progressLine.style.height = `${progress * 100}%`;
  
  const tls = document.querySelectorAll('.tl');
  tls.forEach(tl => {
    // Offset relative to timeline container (plus a little buffer so it activates exactly when line hits dot)
    const tlPercentage = (tl.offsetTop) / timelineHeight;
    if (progress >= tlPercentage) {
      tl.classList.add('active');
      const dot = tl.querySelector('.tl-dot');
      if (dot) dot.classList.add('active');
    }
  });
});
// Trigger once on load
window.dispatchEvent(new Event('scroll'));
'''
c = c.replace('// EXPERIMENTAL: Parallax Hover Effect in Hero', js_logic + '\n// EXPERIMENTAL: Parallax Hover Effect in Hero')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)
