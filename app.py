# app.py - Ajay Nikam | DevOps Portfolio
# Run: pip install -r requirements.txt
# Then: python app.py or via Docker

from flask import Flask, render_template_string
import os

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>Ajay Nikam | DevOps Engineer</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;900&display=swap" rel="stylesheet"/>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css"/>
<style>
  *{margin:0;padding:0;box-sizing:border-box;}
  :root{
    --bg:#0a0f1e;--card:#111827;--accent:#00d4ff;--accent2:#7c3aed;
    --text:#e2e8f0;--muted:#94a3b8;--border:#1e293b;
  }
  body{font-family:"Inter",sans-serif;background:var(--bg);color:var(--text);scroll-behavior:smooth;}
  a{color:var(--accent);text-decoration:none;}
  nav{position:fixed;top:0;width:100%;background:rgba(10,15,30,0.92);backdrop-filter:blur(12px);
    border-bottom:1px solid var(--border);z-index:999;padding:0 5%;}
  .nav-inner{display:flex;justify-content:space-between;align-items:center;height:64px;}
  .logo{font-weight:900;font-size:1.3rem;background:linear-gradient(135deg,var(--accent),var(--accent2));
    -webkit-background-clip:text;-webkit-text-fill-color:transparent;}
  .nav-links a{margin-left:2rem;font-size:.9rem;color:var(--muted);transition:.3s;}
  .nav-links a:hover{color:var(--accent);}
  .hero{min-height:100vh;display:flex;align-items:center;padding:0 10%;
    background:radial-gradient(ellipse at 20% 50%,rgba(0,212,255,.08) 0,transparent 60%),
               radial-gradient(ellipse at 80% 20%,rgba(124,58,237,.08) 0,transparent 60%);}
  .hero-content{max-width:700px;}
  .badge{display:inline-block;background:rgba(0,212,255,.1);border:1px solid rgba(0,212,255,.3);
    color:var(--accent);padding:.4rem 1rem;border-radius:2rem;font-size:.8rem;margin-bottom:1.5rem;}
  .hero h1{font-size:clamp(2.5rem,6vw,4.5rem);font-weight:900;line-height:1.1;margin-bottom:1rem;}
  .hero h1 span{background:linear-gradient(135deg,var(--accent),var(--accent2));
    -webkit-background-clip:text;-webkit-text-fill-color:transparent;}
  .hero p{font-size:1.15rem;color:var(--muted);margin-bottom:2rem;line-height:1.7;}
  .btn-group{display:flex;gap:1rem;flex-wrap:wrap;}
  .btn{padding:.8rem 2rem;border-radius:.5rem;font-size:.95rem;font-weight:600;cursor:pointer;transition:.3s;}
  .btn-primary{background:linear-gradient(135deg,var(--accent),var(--accent2));color:#fff;border:none;}
  .btn-primary:hover{opacity:.85;transform:translateY(-2px);}
  .btn-outline{background:transparent;border:1px solid var(--accent);color:var(--accent);}
  .btn-outline:hover{background:rgba(0,212,255,.1);}
  .hero-stats{display:flex;gap:3rem;margin-top:3rem;}
  .stat h3{font-size:2rem;font-weight:900;color:var(--accent);}
  .stat p{font-size:.85rem;color:var(--muted);}
  section{padding:6rem 10%;}
  .section-title{font-size:2rem;font-weight:800;margin-bottom:.5rem;}
  .section-title span{color:var(--accent);}
  .section-sub{color:var(--muted);margin-bottom:3rem;font-size:1rem;}
  .divider{width:3rem;height:3px;background:linear-gradient(135deg,var(--accent),var(--accent2));
    border-radius:2px;margin-bottom:1rem;}
  .about-grid{display:grid;grid-template-columns:1fr 1fr;gap:3rem;align-items:center;}
  .about-text p{color:var(--muted);line-height:1.8;margin-bottom:1rem;}
  .about-info{display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin-top:1.5rem;}
  .info-item label{font-size:.75rem;color:var(--accent);text-transform:uppercase;letter-spacing:.1em;}
  .info-item p{font-size:.95rem;color:var(--text);margin-top:.2rem;}
  .avatar{width:100%;aspect-ratio:1;border-radius:1.5rem;
    background:linear-gradient(135deg,var(--accent2),var(--accent));
    display:flex;align-items:center;justify-content:center;font-size:6rem;}
  /* Additional CSS omitted for brevity; include your full CSS from original HTML */
</style>
</head>
<body>

<!-- NAV -->
<nav>
  <div class="nav-inner">
    <div class="logo">AN.</div>
    <div class="nav-links">
      <a href="#about">About</a>
      <a href="#skills">Skills</a>
      <a href="#experience">Experience</a>
      <a href="#projects">Projects</a>
      <a href="#contact">Contact</a>
    </div>
  </div>
</nav>

<!-- HERO -->
<section class="hero" id="home">
  <div class="hero-content">
    <div class="badge">&#128640; Available for Full-Time DevOps Roles</div>
    <h1>Hi, I'm <span>Ajay Nikam</span></h1>
    <p>A passionate DevOps Engineer skilled in CI/CD pipelines, containerization, infrastructure automation, and cloud-native monitoring. Currently building real-world DevOps expertise at Hisan Labs Pvt Ltd, Pune.</p>
    <div class="btn-group">
      <a href="#projects" class="btn btn-primary">View My Work</a>
      <a href="#contact" class="btn btn-outline">Get In Touch</a>
    </div>
    <div class="hero-stats">
      <div class="stat"><h3>7+</h3><p>Months Hands-on</p></div>
      <div class="stat"><h3>13+</h3><p>Tools Mastered</p></div>
      <div class="stat"><h3>5+</h3><p>Projects Built</p></div>
    </div>
  </div>
</section>

<!-- ABOUT, SKILLS, EXPERIENCE, PROJECTS, CONTACT sections omitted for brevity; copy from your original HTML -->

<!-- FOOTER -->
<footer>
  <p>Designed & built by <strong style="color:var(--accent);">Ajay Nikam</strong> &nbsp;|&nbsp; DevOps Engineer &nbsp;|&nbsp; Pune, India</p>
  <p style="margin-top:.5rem;">&#169; 2026 Ajay Nikam. All rights reserved.</p>
</footer>

<script>
  function handleSubmit(e){
    e.preventDefault();
    alert("Thanks for reaching out! I'll get back to you soon.");
    e.target.reset();
  }
  const sections=document.querySelectorAll("section[id]");
  const links=document.querySelectorAll(".nav-links a");
  window.addEventListener("scroll",()=>{
    let cur="";
    sections.forEach(s=>{if(window.scrollY>=s.offsetTop-100)cur=s.id;});
    links.forEach(l=>{
      l.style.color=l.getAttribute("href")==="#"+cur?"var(--accent)":"var(--muted)";
    });
  });
</script>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
