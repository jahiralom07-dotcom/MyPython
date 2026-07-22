
document.getElementById('year').textContent = new Date().getFullYear();

// ---------- particle name animation (hero) ----------
// Same idea as the Python "galaxy name" project: sample the pixels of a
// rendered text string, then animate particles from random start points
// into those positions.

(function () {
  const canvas = document.getElementById('nameCanvas');
  const ctx = canvas.getContext('2d');
  const NAME = "JAHIR ALOM";

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
