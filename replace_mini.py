import re
with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

replacement = '''<div class="mini-grid">
      <div class="mini-card">
        <img src="assests/images/iot_dashboard.png" alt="IoT Weather Station" class="mini-card-img"/>
        <div class="mini-card-body">
          <div class="mini-card-num">Internet of Things</div>
          <div class="mini-card-title">IoT Weather Station & Alert System</div>
          <p style="font-size:12px;color:#888;line-height:1.65;margin: 8px 0 8px;">Simulated a complete sensor-to-cloud data pipeline using ESP32 and DHT22 in Wokwi. Configured live visualization and threshold-based email alerts via ThingSpeak.</p>
          <div class="mini-card-tools">ESP32 · C++ · ThingSpeak · Wokwi</div>
          <div style="margin-top: 16px; display: flex; gap: 8px;">
            <a href="iot_weather_station.html" class="btn-warm" style="font-size: 12px; padding: 6px 16px;">Project Details</a>
          </div>
        </div>
      </div>
      <div class="mini-card">
        <img src="assests/images/cad_portfolio_thumb.jpg" alt="CAD modelling" class="mini-card-img"/>
        <div class="mini-card-body">
          <div class="mini-card-num">Coursework</div>
          <div class="mini-card-title">CAD Modelling Portfolio</div>
          <p style="font-size:12px;color:#888;line-height:1.65;margin: 8px 0 8px;">Assembly and detail drawings spanning engine sub-assemblies, precision jigs, and mechanical linkages - produced with strict adherence to GD&T standards and design-for-manufacture conventions.</p>
          <div class="mini-card-tools">SolidWorks</div>
          <div style="margin-top: 16px; display: flex; gap: 8px;">
            <a href="cad_portfolio.html" class="btn-warm" style="font-size: 12px; padding: 6px 16px;">Project Details</a>
          </div>
        </div>
      </div>
      <div class="mini-card">
        <img src="assests/images/gripper_ansys.png" alt="Industrial Gripper" class="mini-card-img"/>
        <div class="mini-card-body">
          <div class="mini-card-num">Industrial Design</div>
          <div class="mini-card-title">2-Finger Industrial Gripper</div>
          <p style="font-size:12px;color:#888;line-height:1.65;margin: 8px 0 8px;">Designed a gear-driven parallel jaw gripper for 10 kg payloads. Modelled the dual parallelogram linkage in SolidWorks and validated the design with static structural FEA in ANSYS.</p>
          <div class="mini-card-tools">SolidWorks · ANSYS Workbench</div>
          <div style="margin-top: 16px; display: flex; gap: 8px;">
            <a href="industrial_gripper.html" class="btn-warm" style="font-size: 12px; padding: 6px 16px;">Project Details</a>
          </div>
        </div>
      </div>
      <div class="mini-card">
        <img src="assests/images/booksolver_thumb.jpg" alt="Physics & Maths" class="mini-card-img"/>
        <div class="mini-card-body">
          <div class="mini-card-num">Booksolver</div>
          <div class="mini-card-title">Physics & Maths Expert</div>
          <p style="font-size:12px;color:#888;line-height:1.65;margin: 8px 0 8px;">Produced detailed video solutions for JEE Advanced-level physics and mathematics problems, emphasising conceptual clarity and structured problem-solving methodology.</p>
          <div class="mini-card-tools">Content Creation · EdTech</div>
          <div style="margin-top: 16px; display: flex; gap: 8px;">
            <a href="https://www.youtube.com/playlist?list=PLioTSJheQgGiX10VHZz487jypl0BGnESb" target="_blank" class="btn-warm" style="font-size: 12px; padding: 6px 16px;"><i class="fa-brands fa-youtube"></i> Playlist</a>
          </div>
        </div>
      </div>
    </div>'''

new_c = re.sub(r'<div class="mini-grid">.*?</div>\s*</div>\s*</section>', replacement + '\n  </div>\n</section>', c, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_c)
