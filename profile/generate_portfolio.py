"""
generate_portfolio.py
----------------------
Ye script ek static HTML/CSS/JS portfolio site generate karta hai.
Content (naam, bio, skills, projects, contact) neeche CONFIG dict me hai --
bas usko edit karo aur script dobara run karo:

    python generate_portfolio.py

Output "site/" folder me ban jayega (index.html, style.css, script.js).
"""

import os

# ============================================================
# 1. CONFIG -- apni details yahan badlo
# ============================================================

CONFIG = {
    "name": "Jahir Alom",
    "role": "Python Developer & Creative Coder",
    "tagline": "Turning code into motion, one particle at a time.",
    "about": (
        "I'm a Python developer who enjoys building things that move, glow and "
        "surprise -- from particle-based generative art to small automation "
        "tools. I like exploring what happens when code gets a little "
        "theatrical: animation timing, color, and motion as much as logic."
    ),
    "email": "your.email@example.com",
    "github": "https://github.com/your-username",
    "location": "India",

    "skills": [
        "Python", "Turtle Graphics", "Generative Art", "Automation & Scripting",
        "HTML / CSS", "Problem Solving", "Algorithms", "Creative Coding",
    ],

    "projects": [
        {
            "title": "Galaxy Name Animation",
            "tag": "generative-art",
            "desc": (
                "Particles scatter from every edge of the screen and drift "
                "together to spell out a name in glowing white dots -- like "
                "a galaxy slowly assembling itself."
            ),
            "stack": "Python, turtle",
            "accent": "cyan",
        },
        {
            "title": "The Cursed Name",
            "tag": "horror-fx",
            "desc": (
                "A haunted-house take on text animation: trembling strokes, "
                "flickering backgrounds, blood drips and jump-scare ghost "
                "eyes, all drawn frame by frame."
            ),
            "stack": "Python, turtle",
            "accent": "red",
        },
        {
            "title": "This Portfolio",
            "tag": "web",
            "desc": (
                "A static site generated entirely from a Python script, "
                "with a hero animation that borrows the same "
                "particles-assemble-into-text idea from the projects above."
            ),
            "stack": "Python, HTML, CSS, JS",
            "accent": "violet",
        },
    ],
}

# ============================================================
# 2. TEMPLATES
# ============================================================

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{name} -- {role}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=IBM+Plex+Sans:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css">
</head>
<body>

<nav class="nav">
  <span class="nav-logo">JA<span class="dot">.</span></span>
  <div class="nav-links">
    <a href="#about">about</a>
    <a href="#skills">skills</a>
    <a href="#projects">projects</a>
    <a href="#contact">contact</a>
  </div>
</nav>

<header class="hero">
  <canvas id="nameCanvas"></canvas>
  <p class="eyebrow">&#47;&#47; {role}</p>
  <p class="hero-tagline">{tagline}</p>
  <a href="#projects" class="scroll-cue">scroll to see the work &darr;</a>
</header>

<main>

  <section id="about" class="section">
    <p class="section-label">01 -- about</p>
    <p class="about-text">{about}</p>
    <p class="about-meta">based in {location} &nbsp;&middot;&nbsp; <a href="mailto:{email}">{email}</a></p>
  </section>

  <section id="skills" class="section">
    <p class="section-label">02 -- skills</p>
    <div class="terminal">
      <div class="terminal-bar"><span></span><span></span><span></span></div>
      <div class="terminal-body">
        <p class="term-line"><span class="prompt">$</span> skills --list</p>
        <div class="skills-grid">
{skills_html}
        </div>
      </div>
    </div>
  </section>

  <section id="projects" class="section">
    <p class="section-label">03 -- projects</p>
    <div class="projects-grid">
{projects_html}
    </div>
  </section>

  <section id="contact" class="section contact">
    <p class="section-label">04 -- contact</p>
    <h2 class="contact-headline">Have something worth building?</h2>
    <div class="contact-links">
      <a href="mailto:{email}" class="contact-link">{email}</a>
      <a href="{github}" class="contact-link" target="_blank" rel="noopener">{github_display}</a>
    </div>
  </section>

</main>

<footer class="footer">
  <span>&copy; <span id="year"></span> {name}</span>
  <span>built with Python</span>
</footer>

<script src="script.js"></script>
</body>
</html>
"""

SKILL_CHIP = '          <span class="skill-chip">{skill}</span>\n'

PROJECT_CARD = """      <article class="project-card accent-{accent}">
        <p class="project-tag">{tag}</p>
        <h3 class="project-title">{title}</h3>
        <p class="project-desc">{desc}</p>
        <p class="project-stack">{stack}</p>
      </article>
"""

CSS_TEMPLATE = """
/* ---------- tokens ---------- */
:root {
  --bg: #0a0c14;
  --bg-soft: #12141f;
  --bg-card: #14172346;
  --text: #eef0f5;
  --muted: #8b8fa3;
  --border: #23273a;
  --accent-cyan: #5eead4;
  --accent-red: #f4405e;
  --accent-violet: #a78bfa;

  --display: 'Space Grotesk', sans-serif;
  --body: 'IBM Plex Sans', sans-serif;
  --mono: 'JetBrains Mono', monospace;
}

* { box-sizing: border-box; }

html { scroll-behavior: smooth; }

body {
  margin: 0;
  background: var(--bg);
  color: var(--text);
  font-family: var(--body);
  line-height: 1.6;
}

a { color: inherit; }

/* ---------- nav ---------- */
.nav {
  position: fixed;
  top: 0; left: 0; right: 0;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 24px 6vw;
  z-index: 10;
  font-family: var(--mono);
  font-size: 0.85rem;
  backdrop-filter: blur(6px);
}

.nav-logo {
  font-family: var(--display);
  font-weight: 700;
  font-size: 1.1rem;
  letter-spacing: 0.02em;
}
.nav-logo .dot { color: var(--accent-cyan); }

.nav-links a {
  text-decoration: none;
  color: var(--muted);
  margin-left: 28px;
  transition: color 0.2s ease;
}
.nav-links a:hover { color: var(--accent-cyan); }

/* ---------- hero ---------- */
.hero {
  position: relative;
  height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  overflow: hidden;
  padding: 0 20px;
}

#nameCanvas {
  width: 100%;
  max-width: 900px;
  height: 220px;
}

.eyebrow {
  font-family: var(--mono);
  color: var(--accent-cyan);
  letter-spacing: 0.08em;
  font-size: 0.9rem;
  margin: 8px 0 4px;
}

.hero-tagline {
  color: var(--muted);
  font-size: 1.05rem;
  max-width: 480px;
}

.scroll-cue {
  position: absolute;
  bottom: 34px;
  font-family: var(--mono);
  font-size: 0.75rem;
  color: var(--muted);
  text-decoration: none;
  animation: floaty 2.4s ease-in-out infinite;
}

@keyframes floaty {
  0%, 100% { transform: translateY(0); opacity: 0.6; }
  50% { transform: translateY(6px); opacity: 1; }
}

/* ---------- sections ---------- */
.section {
  max-width: 900px;
  margin: 0 auto;
  padding: 120px 6vw 40px;
}

.section-label {
  font-family: var(--mono);
  color: var(--accent-cyan);
  font-size: 0.8rem;
  letter-spacing: 0.08em;
  margin-bottom: 18px;
}

.about-text {
  font-size: 1.25rem;
  font-family: var(--display);
  font-weight: 400;
  color: var(--text);
  max-width: 640px;
}

.about-meta {
  color: var(--muted);
  font-family: var(--mono);
  font-size: 0.85rem;
  margin-top: 18px;
}
.about-meta a { color: var(--accent-cyan); text-decoration: none; }

/* ---------- terminal (skills) ---------- */
.terminal {
  border: 1px solid var(--border);
  border-radius: 10px;
  overflow: hidden;
  background: var(--bg-soft);
}

.terminal-bar {
  display: flex;
  gap: 7px;
  padding: 12px 16px;
  background: #181b28;
  border-bottom: 1px solid var(--border);
}
.terminal-bar span {
  width: 10px; height: 10px;
  border-radius: 50%;
  background: #333748;
}
.terminal-bar span:nth-child(1) { background: #f4405e88; }
.terminal-bar span:nth-child(2) { background: #f4c14588; }
.terminal-bar span:nth-child(3) { background: #5eead488; }

.terminal-body { padding: 22px 24px 26px; }

.term-line {
  font-family: var(--mono);
  color: var(--muted);
  margin: 0 0 18px;
  font-size: 0.9rem;
}
.prompt { color: var(--accent-cyan); }

.skills-grid {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.skill-chip {
  font-family: var(--mono);
  font-size: 0.82rem;
  padding: 7px 14px;
  border: 1px solid var(--border);
  border-radius: 20px;
  color: var(--text);
  background: #ffffff06;
}

/* ---------- projects ---------- */
.projects-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 18px;
}

.project-card {
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 24px;
  background: var(--bg-soft);
  transition: transform 0.25s ease, border-color 0.25s ease;
}
.project-card:hover {
  transform: translateY(-4px);
}

.accent-cyan:hover { border-color: var(--accent-cyan); }
.accent-red:hover { border-color: var(--accent-red); }
.accent-violet:hover { border-color: var(--accent-violet); }

.project-tag {
  font-family: var(--mono);
  font-size: 0.72rem;
  letter-spacing: 0.06em;
  color: var(--muted);
  text-transform: uppercase;
  margin: 0 0 10px;
}

.project-title {
  font-family: var(--display);
  font-size: 1.2rem;
  margin: 0 0 10px;
}

.project-desc {
  color: var(--muted);
  font-size: 0.92rem;
  margin: 0 0 16px;
}

.project-stack {
  font-family: var(--mono);
  font-size: 0.78rem;
  color: var(--text);
  opacity: 0.7;
  margin: 0;
}

/* ---------- contact ---------- */
.contact { text-align: center; }

.contact-headline {
  font-family: var(--display);
  font-size: clamp(1.6rem, 4vw, 2.4rem);
  font-weight: 600;
  margin: 0 0 30px;
}

.contact-links {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 12px;
}

.contact-link {
  font-family: var(--mono);
  text-decoration: none;
  color: var(--accent-cyan);
  font-size: 1rem;
  border-bottom: 1px solid transparent;
  transition: border-color 0.2s ease;
}
.contact-link:hover { border-color: var(--accent-cyan); }

/* ---------- footer ---------- */
.footer {
  display: flex;
  justify-content: space-between;
  padding: 30px 6vw 50px;
  font-family: var(--mono);
  font-size: 0.75rem;
  color: var(--muted);
  max-width: 900px;
  margin: 0 auto;
}

/* ---------- accessibility ---------- */
a:focus-visible, button:focus-visible {
  outline: 2px solid var(--accent-cyan);
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .scroll-cue { animation: none; }
  html { scroll-behavior: auto; }
}

@media (max-width: 640px) {
  .nav-links a { margin-left: 16px; }
  #nameCanvas { height: 140px; }
}
"""

JS_TEMPLATE = """
document.getElementById('year').textContent = new Date().getFullYear();

// ---------- particle name animation (hero) ----------
// Same idea as the Python "galaxy name" project: sample the pixels of a
// rendered text string, then animate particles from random start points
// into those positions.

(function () {
  const canvas = document.getElementById('nameCanvas');
  const ctx = canvas.getContext('2d');
  const NAME = "%(NAME_UPPER)s";

  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function setup() {
    const rect = canvas.getBoundingClientRect();
    const dpr = window.devicePixelRatio || 1;
    canvas.width = rect.width * dpr;
    canvas.height = rect.height * dpr;
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    return { w: rect.width, h: rect.height };
  }

  function samplePoints(w, h) {
    const off = document.createElement('canvas');
    off.width = w; off.height = h;
    const octx = off.getContext('2d');
    octx.fillStyle = '#fff';
    let fontSize = Math.min(w / (NAME.length * 0.62), h * 0.7);
    octx.font = `700 ${fontSize}px 'Space Grotesk', sans-serif`;
    octx.textAlign = 'center';
    octx.textBaseline = 'middle';
    octx.fillText(NAME, w / 2, h / 2);

    const data = octx.getImageData(0, 0, w, h).data;
    const pts = [];
    const step = 4; // sampling density
    for (let y = 0; y < h; y += step) {
      for (let x = 0; x < w; x += step) {
        const alpha = data[(y * w + x) * 4 + 3];
        if (alpha > 120) pts.push({ x, y });
      }
    }
    return pts;
  }

  function init() {
    const { w, h } = setup();
    const targets = samplePoints(w, h);

    const particles = targets.map((t) => {
      const edge = Math.floor(Math.random() * 4);
      let sx, sy;
      if (edge === 0) { sx = -20; sy = Math.random() * h; }
      else if (edge === 1) { sx = w + 20; sy = Math.random() * h; }
      else if (edge === 2) { sx = Math.random() * w; sy = -20; }
      else { sx = Math.random() * w; sy = h + 20; }
      return { x: sx, y: sy, tx: t.x, ty: t.y };
    });

    let frame = 0;
    const totalFrames = reduceMotion ? 1 : 70;

    function animate() {
      ctx.clearRect(0, 0, w, h);
      const p = Math.min(frame / totalFrames, 1);
      const ease = 1 - Math.pow(1 - p, 3);

      for (const particle of particles) {
        const x = particle.x + (particle.tx - particle.x) * ease;
        const y = particle.y + (particle.ty - particle.y) * ease;
        ctx.fillStyle = '#eef0f5';
        ctx.fillRect(x, y, 2, 2);
      }

      if (frame < totalFrames) {
        frame++;
        requestAnimationFrame(animate);
      }
    }
    animate();
  }

  init();
  let resizeTimer;
  window.addEventListener('resize', () => {
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(init, 200);
  });
})();
"""

# ============================================================
# 3. BUILD
# ============================================================


def build():
    out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "site")
    os.makedirs(out_dir, exist_ok=True)

    skills_html = "".join(
        SKILL_CHIP.format(skill=s) for s in CONFIG["skills"]
    )

    projects_html = "".join(
        PROJECT_CARD.format(
            accent=p["accent"],
            tag=p["tag"],
            title=p["title"],
            desc=p["desc"],
            stack=p["stack"],
        )
        for p in CONFIG["projects"]
    )

    github_display = CONFIG["github"].replace("https://", "")

    html = HTML_TEMPLATE.format(
        name=CONFIG["name"],
        role=CONFIG["role"],
        tagline=CONFIG["tagline"],
        about=CONFIG["about"],
        email=CONFIG["email"],
        location=CONFIG["location"],
        github=CONFIG["github"],
        github_display=github_display,
        skills_html=skills_html,
        projects_html=projects_html,
    )

    js = JS_TEMPLATE % {"NAME_UPPER": CONFIG["name"].upper()}

    with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)

    with open(os.path.join(out_dir, "style.css"), "w", encoding="utf-8") as f:
        f.write(CSS_TEMPLATE)

    with open(os.path.join(out_dir, "script.js"), "w", encoding="utf-8") as f:
        f.write(js)

    print(f"Portfolio generated in: {out_dir}")
    print("Open site/index.html in your browser to view it.")


if __name__ == "__main__":
    build()
