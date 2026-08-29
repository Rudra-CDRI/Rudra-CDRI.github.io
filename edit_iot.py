import re

with open('iot_weather_station.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = re.sub(r'<title>.*?</title>', '<title>IoT Weather Station | Rudrapriya Rajesh Choudhari</title>', html)

new_content = """
<div class="proj-header-wrap">
  <span class="proj-eyebrow">Internet of Things · Cloud Computing</span>
  <h1 class="proj-title">IoT Weather Station & Alert System</h1>
  <p class="proj-subtitle">A simulated, cloud-connected environmental monitoring system featuring an ESP32, real-time ThingSpeak dashboard, and threshold-based email alerts.</p>
</div>

<div class="proj-body">
  <div class="main-content">
    <div class="content-box">
      <h2>Project Overview</h2>
      <p class="content-text">This project demonstrates a complete sensor-to-cloud data pipeline. Due to hardware limitations, the entire physical layer is simulated using <strong>Wokwi</strong>, running a virtual ESP32 microcontroller and a DHT22 temperature/humidity sensor. The system successfully connects to a virtual Wi-Fi network and publishes environmental data via HTTP to the ThingSpeak cloud for real-time aggregation, visualization, and automated alerting.</p>
      
      <div class="hero-visual">
        <div class="visual-grid">
          <div class="visual-card">
            <div>
              <div class="visual-kicker">Edge Layer</div>
              <div class="visual-title">Wokwi ESP32</div>
            </div>
            <div class="visual-desc">Simulated hardware running C++ firmware to sample DHT22 data on GPIO 15.</div>
          </div>
          <div class="visual-card">
            <div>
              <div class="visual-kicker">Network Layer</div>
              <div class="visual-title">Wi-Fi & HTTP</div>
            </div>
            <div class="visual-desc">Wokwi virtual gateway transmitting JSON payloads to REST APIs.</div>
          </div>
          <div class="visual-card">
            <div>
              <div class="visual-kicker">Cloud Layer</div>
              <div class="visual-title">ThingSpeak</div>
            </div>
            <div class="visual-desc">Dashboard visualization and backend React scripts for email alerts.</div>
          </div>
        </div>
      </div>
    </div>

    <div class="content-box">
      <h2>1. System Architecture</h2>
      <p class="content-text">The architecture follows a standard three-tier IoT topology, engineered to function robustly in a simulated environment before physical deployment.</p>
      <img src="assests/images/iot/architecture.png" style="width:100%; border-radius:12px; margin:20px 0; border:1px solid var(--card-border);" alt="Architecture Diagram">
      <ul class="content-list">
        <li><strong>Sensor Node:</strong> A virtual ESP32 interfaces with a DHT22 sensor via a 1-wire protocol on GPIO 15. The firmware is written in C++ (Arduino Core) and utilizes the <code>DHT sensor library</code> for data extraction.</li>
        <li><strong>Connectivity:</strong> The ESP32 connects to the "Wokwi-GUEST" virtual access point. It utilizes the <code>WiFiClient</code> and <code>HTTPClient</code> libraries to construct POST requests.</li>
        <li><strong>Cloud Ingestion:</strong> ThingSpeak receives the HTTP requests using a specific Write API Key. Temperature is mapped to Field 1, and Humidity is mapped to Field 2. Updates occur at a strict 20-second interval to comply with ThingSpeak's rate limits.</li>
      </ul>
    </div>

    <div class="content-box">
      <h2>2. Hardware Simulation (Wokwi)</h2>
      <p class="content-text">By utilizing Wokwi, the exact C++ firmware that would run on physical silicon is compiled and executed in the browser. This allows for rigorous testing of the logic loop, Wi-Fi reconnection handling, and API integration without the friction of physical wiring or hardware failure.</p>
      <img src="assests/images/iot/circuit.png" style="width:100%; border-radius:12px; margin:20px 0; border:1px solid var(--card-border);" alt="Wokwi Circuit">
    </div>

    <div class="content-box">
      <h2>3. Cloud Visualization & Alerting</h2>
      <p class="content-text">The ThingSpeak platform serves as the central data hub. Two distinct workflows were established:</p>
      <p class="content-text"><strong>Live Dashboard:</strong> Incoming data streams are visualized using native gauges and line charts, providing an immediate overview of environmental trends.</p>
      <img src="assests/images/iot/dashboard.png" style="width:100%; border-radius:12px; margin:20px 0; border:1px solid var(--card-border);" alt="ThingSpeak Dashboard">
      <p class="content-text"><strong>Automated Email Alerts:</strong> A ThingSpeak <em>React</em> is configured to evaluate incoming data points against predefined safety thresholds (Temperature &gt; 35&deg;C, or Humidity &gt; 80%). If a threshold is breached, a <em>ThingHTTP</em> action is triggered to dispatch an urgent email alert to the system administrator.</p>
      <img src="assests/images/iot/email.png" style="width:100%; border-radius:12px; margin:20px 0; border:1px solid var(--card-border);" alt="Email Alert">
    </div>
    
    <div class="content-box">
      <h2>Demo Video</h2>
      <video controls style="width:100%; border-radius:12px; border:1px solid var(--card-border);">
        <source src="assests/images/iot/demo.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
    </div>
  </div>

  <div class="sidebar">
    <div class="sidebar-section">
      <div class="sidebar-label">Tech Stack</div>
      <span class="skill-pill">ESP32</span>
      <span class="skill-pill">C++</span>
      <span class="skill-pill">Wokwi Simulator</span>
      <span class="skill-pill">ThingSpeak</span>
      <span class="skill-pill">HTTP/REST</span>
      <span class="skill-pill">IoT Architecture</span>
    </div>

    <div class="sidebar-section">
      <div class="side-card">
        <h3>Project Focus</h3>
        <p>This project showcases end-to-end IoT system development, focusing on reliable data sampling, network communication protocols, and integrating cloud platforms for real-time monitoring and event-driven architectures.</p>
        <div class="chip-row">
          <span class="mini-chip">Hardware</span>
          <span class="mini-chip">Networking</span>
          <span class="mini-chip">Cloud API</span>
        </div>
      </div>
    </div>

    <div class="sidebar-section">
      <div class="sidebar-label">Project Assets</div>
      <div class="link-row">
        <a href="assests/documents/iot_report.pdf" target="_blank" class="btn-warm"><i class="fa-solid fa-file-pdf"></i> View Project Report</a>
        <a href="https://github.com/Rudra-CDRI/esp32-iot-weather-station" target="_blank" class="btn-ghost"><i class="fa-brands fa-github"></i> View Repository</a>
      </div>
    </div>
  </div>
</div>
"""

pattern = re.compile(r'<div class="proj-header-wrap">.*?</div>\s*</div>\s*</div>\s*</div>', re.DOTALL)
html = pattern.sub(new_content, html)

with open('iot_weather_station.html', 'w', encoding='utf-8') as f:
    f.write(html)
