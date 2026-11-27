
from flask import Flask, render_template_string

app = Flask(__name__)

HTML = r"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Pundhir's CCTV Services | Premium Security</title>

<style>
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    scroll-behavior: smooth;
}

body {
    background: #090b10;
    color: #f5f5f5;
    font-family: Arial, sans-serif;
}

:root {
    --gold: #d9b45b;
    --dark: #090b10;
    --card: #151820;
}

header {
    background: #0d1017;
    padding: 20px 7%;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid #29241a;
    position: sticky;
    top: 0;
    z-index: 10;
}

.logo {
    color: var(--gold);
    font-size: 19px;
    font-weight: bold;
}

nav a {
    color: white;
    text-decoration: none;
    margin-left: 15px;
    font-size: 13px;
}

nav a:hover {
    color: var(--gold);
}

.hero {
    min-height: 570px;
    padding: 110px 8% 80px;
    text-align: center;
    background:
      radial-gradient(ellipse at top, #45371c 0%, transparent 60%),
      linear-gradient(135deg, #10131b, #090b10);
}

.tag {
    color: var(--gold);
    letter-spacing: 4px;
    font-size: 12px;
}

.hero h1 {
    font-size: clamp(34px, 7vw, 65px);
    margin: 25px 0;
    line-height: 1.15;
}

.hero h1 span {
    color: var(--gold);
}

.hero p {
    color: #c5c5c5;
    line-height: 1.8;
    max-width: 650px;
    margin: auto;
}

.btn {
    display: inline-block;
    padding: 15px 25px;
    margin: 25px 8px 0;
    border-radius: 5px;
    text-decoration: none;
    font-weight: bold;
    transition: 0.3s;
}

.gold {
    background: var(--gold);
    color: #111;
}

.outline {
    border: 1px solid var(--gold);
    color: var(--gold);
}

.btn:hover {
    transform: translateY(-4px);
}

section {
    padding: 75px 7%;
}

.heading {
    text-align: center;
    margin-bottom: 40px;
}

.heading small {
    color: var(--gold);
    letter-spacing: 3px;
}

.heading h2 {
    font-size: 32px;
    margin-top: 12px;
}

.services {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 20px;
}

.card {
    background: var(--card);
    border: 1px solid #302a20;
    border-radius: 12px;
    padding: 30px 22px;
    transition: 0.3s;
}

.card:hover {
    border-color: var(--gold);
    transform: translateY(-5px);
}

.card .icon {
    font-size: 38px;
}

.card h3 {
    color: var(--gold);
    margin: 18px 0 12px;
}

.card p {
    color: #b8bbc3;
    line-height: 1.7;
    font-size: 14px;
}

.about {
    background: #11151d;
    text-align: center;
}

.about p {
    max-width: 750px;
    margin: 20px auto;
    color: #c3c3c3;
    line-height: 1.9;
}

.features {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
    gap: 15px;
    margin-top: 35px;
}

.feature {
    padding: 22px 10px;
    border: 1px solid #40351f;
    border-radius: 8px;
    color: var(--gold);
}

.projects {
    text-align: center;
    background: #0c0f16;
}

.project-box {
    max-width: 800px;
    margin: auto;
    background: linear-gradient(120deg, #292113, #171a21);
    border: 1px solid #64502a;
    padding: 35px 20px;
    border-radius: 12px;
}

.contact {
    background: #11151d;
    text-align: center;
}

.contact-box {
    max-width: 650px;
    margin: auto;
    padding: 30px;
    background: var(--card);
    border: 1px solid #42351d;
    border-radius: 12px;
    line-height: 2.2;
}

.contact-box strong {
    color: var(--gold);
}

footer {
    text-align: center;
    background: #07090d;
    padding: 30px 15px;
    color: #999;
    line-height: 2;
}

footer span {
    color: var(--gold);
}

@media(max-width: 650px) {
    header {
        flex-direction: column;
        gap: 18px;
    }
    nav a {
        margin: 0 6px;
        font-size: 12px;
    }
    .hero {
        padding: 85px 6%;
    }
    section {
        padding: 60px 6%;
    }
}
</style>
</head>

<body>

<header>
    <div class="logo">♛ PUNDHIR'S CCTV</div>
    <nav>
        <a href="#home">Home</a>
        <a href="#services">Services</a>
        <a href="#about">About</a>
        <a href="#contact">Contact</a>
    </nav>
</header>

<div class="hero" id="home">
    <div class="tag">SMART SECURITY • PROFESSIONAL SOLUTIONS</div>

    <h1>SECURITY YOU <span>CAN TRUST</span></h1>

    <p>
      Advanced CCTV Surveillance, IP Camera Installation
      and Complete Security Solutions for Homes,
      Offices, Shops and Commercial Projects.
    </p>

    <a class="btn gold"
       href="https://wa.me/919870671684">
       GET A QUOTATION
    </a>

    <a class="btn outline" href="#services">
       EXPLORE SERVICES
    </a>
</div>

<section id="services">
    <div class="heading">
        <small>WHAT WE DO</small>
        <h2>Our Professional Services</h2>
    </div>

    <div class="services">

        <div class="card">
            <div class="icon">📹</div>
            <h3>CCTV Installation</h3>
            <p>Professional CCTV camera installation
            for residential and commercial properties.</p>
        </div>

        <div class="card">
            <div class="icon">📷</div>
            <h3>IP Camera Solutions</h3>
            <p>Modern IP camera setup and network
            surveillance solutions.</p>
        </div>

        <div class="card">
            <div class="icon">🛠️</div>
            <h3>Repair & Maintenance</h3>
            <p>Reliable CCTV troubleshooting,
            repair and maintenance services.</p>
        </div>

        <div class="card">
            <div class="icon">🏢</div>
            <h3>Commercial Projects</h3>
            <p>Complete surveillance solutions
            for offices, warehouses and businesses.</p>
        </div>

        <div class="card">
            <div class="icon">🌙</div>
            <h3>Night Vision Cameras</h3>
            <p>Camera solutions with night vision
            capabilities for low-light monitoring.</p>
        </div>

        <div class="card">
            <div class="icon">📱</div>
            <h3>Mobile Live Viewing</h3>
            <p>Remote camera viewing setup
            on supported mobile devices.</p>
        </div>

    </div>
</section>

<section class="about" id="about">
    <div class="heading">
        <small>ABOUT OUR COMPANY</small>
        <h2>Pundhir's CCTV Services</h2>
    </div>

    <p>
      We provide CCTV installation, repair,
      maintenance and modern surveillance solutions.
      Our focus is on professional service,
      reliable systems and customer satisfaction.
      We also undertake commercial CCTV projects.
    </p>

    <div class="features">
        <div class="feature">✓ Professional Service</div>
        <div class="feature">✓ Smart Solutions</div>
        <div class="feature">✓ Reliable Support</div>
        <div class="feature">✓ Commercial Projects</div>
    </div>
</section>

<section class="projects">
    <div class="heading">
        <small>OUR EXPERTISE</small>
        <h2>Commercial Security Solutions</h2>
    </div>

    <div class="project-box">
        <h2 style="color:#d9b45b">
        Secure Your Business
        </h2>
        <p style="margin-top:15px;line-height:1.8">
        Looking for CCTV surveillance solutions
        for your office, shop, warehouse or
        commercial property?
        </p>

        <a class="btn gold"
           href="https://wa.me/919870671684?text=Hello%2C%20I%20need%20a%20commercial%20CCTV%20quotation.">
           DISCUSS YOUR PROJECT
        </a>
    </div>
</section>

<section class="contact" id="contact">
    <div class="heading">
        <small>GET IN TOUCH</small>
        <h2>Contact Our Team</h2>
    </div>

    <div class="contact-box">
        <p>Company: <strong>Pundhir's CCTV Services</strong></p>
        <p>Bharat Pundhir: <strong>9870671684</strong></p>
        <p>Kushal Pundhir: <strong>9259438689</strong></p>
        <p>Location: <strong>Gorai, Aligarh, UP</strong></p>

        <a class="btn gold"
           href="tel:9870671684">CALL NOW</a>

        <a class="btn outline"
           href="https://wa.me/919870671684">
           WHATSAPP
        </a>
    </div>
</section>

<footer>
    <h3><span>PUNDHIR'S CCTV SERVICES</span></h3>
    <p>Security You Can Trust 🔒</p>
    <p>© 2026 Pundhir's CCTV Services. All Rights Reserved.</p>
</footer>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
