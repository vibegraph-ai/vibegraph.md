(() => {
  'use strict';
  const root = document.documentElement;
  const reducedMotion = matchMedia('(prefers-reduced-motion: reduce)');
  const collapsedNavigation = matchMedia('(max-width: 1023px)');
  const themeButtons = document.querySelectorAll('.theme-toggle');
  const menuButton = document.querySelector('.menu-toggle');
  const menu = document.querySelector('#mobile-nav');
  const netButton = document.querySelector('.net-toggle');
  const netTarget = document.querySelector('#net-background');
  const hero = document.querySelector('.hero');
  let explicitTheme = null;
  try {
    const saved = localStorage.getItem('vibe-theme');
    if (saved === 'dark' || saved === 'light') explicitTheme = saved;
  } catch {}
  let netRequested = true;
  let net = null;
  let libraries;
  let generation = 0;
  let heroVisible = true;
  let pageActive = true;

  function updateTheme(theme) {
    root.dataset.theme = theme;
    themeButtons.forEach(button => {
      const next = theme === 'dark' ? 'light' : 'dark';
      button.setAttribute('aria-label', 'Switch to ' + next + ' theme');
      button.querySelector('img').src = 'assets/icon-' + (theme === 'dark' ? 'sun' : 'moon') + '.svg';
    });
    updateNet();
  }
  themeButtons.forEach(button => button.addEventListener('click', () => {
    explicitTheme = root.dataset.theme === 'dark' ? 'light' : 'dark';
    try { localStorage.setItem('vibe-theme', explicitTheme); } catch {}
    updateTheme(explicitTheme);
  }));
  addEventListener('storage', event => {
    if (event.key !== 'vibe-theme' && event.key !== null) return;
    explicitTheme = event.newValue === 'dark' || event.newValue === 'light' ? event.newValue : null;
    updateTheme(explicitTheme || 'light');
  });

  function closeMenu(returnFocus = false) {
    menu.hidden = true;
    menuButton.setAttribute('aria-expanded', 'false');
    menuButton.setAttribute('aria-label', 'Open menu');
    menuButton.querySelector('img').src = 'assets/icon-menu.svg';
    if (returnFocus) menuButton.focus();
  }
  menuButton.addEventListener('click', () => {
    const opening = menu.hidden;
    if (!opening) return closeMenu();
    menu.hidden = false;
    menuButton.setAttribute('aria-expanded', 'true');
    menuButton.setAttribute('aria-label', 'Close menu');
    menuButton.querySelector('img').src = 'assets/icon-close.svg';
  });
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape' && !menu.hidden) closeMenu(true);
  });
  menu.addEventListener('click', event => {
    if (event.target.closest('a')) closeMenu();
  });
  document.addEventListener('click', event => {
    if (!menu.hidden && !event.target.closest('.top')) closeMenu();
  });
  collapsedNavigation.addEventListener('change', () => {
    if (!collapsedNavigation.matches) closeMenu(menu.contains(document.activeElement));
  });

  // Exact page 14 NET reference. Runtime overrides follow the handoff.
  const NET_REFERENCE = {
    backgroundAlpha: 1, backgroundColor: 1250072, color: 12427504,
    gyroControls: false, maxDistance: 20, minHeight: 200, minWidth: 200,
    mouseControls: true, points: 10, scale: 1, scaleMobile: 1,
    showDots: true, spacing: 15, touchControls: true
  };
  function loadScript(src) {
    return new Promise((resolve, reject) => {
      const script = document.createElement('script');
      script.src = src;
      script.onload = resolve;
      script.onerror = () => { script.remove(); reject(new Error('Optional NET library unavailable')); };
      document.head.append(script);
    });
  }
  function loadNet() {
    if (!libraries) {
      libraries = (async () => {
        if (!window.THREE) await loadScript('vendor/three.min.js');
        if (!window.VANTA?.NET) await loadScript('vendor/vanta.net.min.js');
      })().catch(error => { libraries = null; throw error; });
    }
    return libraries;
  }
  function destroyNet() {
    if (net) {
      try { net.destroy(); } catch {}
      net = null;
    }
    netTarget.querySelectorAll('canvas').forEach(canvas => canvas.remove());
  }
  async function updateNet() {
    const revision = ++generation;
    destroyNet();
    const paused = !netRequested || reducedMotion.matches;
    const label = reducedMotion.matches ? 'Static view (reduced motion)' : paused ? 'Play motion' : 'Pause motion';
    netButton.setAttribute('aria-pressed', String(paused));
    netButton.setAttribute('aria-label', label);
    netButton.title = label;
    netButton.disabled = reducedMotion.matches;
    netTarget.classList.add('static-net');
    root.dataset.net = 'static';
    if (paused || document.hidden || !heroVisible || !pageActive) return;
    try {
      await loadNet();
      if (revision !== generation) return;
      const light = root.dataset.theme === 'light';
      net = window.VANTA.NET({
        ...NET_REFERENCE, el: netTarget, THREE: window.THREE,
        ...(light ? { backgroundColor: 0xf6f6f6, color: 0x5a4bd1 } : {}),
        touchControls: false
      });
      // Vanta may catch WebGL errors internally and return a partial effect.
      if (!net.renderer || !netTarget.querySelector('canvas')) throw new Error('WebGL unavailable');
      netTarget.classList.remove('static-net');
      root.dataset.net = 'running';
    } catch {
      if (revision !== generation) return;
      destroyNet();
      netTarget.classList.add('static-net');
      root.dataset.net = 'fallback';
      netButton.disabled = true;
      netButton.setAttribute('aria-label', 'Static background');
      netButton.title = 'Static background';
    }
  }
  netButton.addEventListener('click', () => { netRequested = !netRequested; updateNet(); });
  reducedMotion.addEventListener('change', updateNet);
  document.addEventListener('visibilitychange', updateNet);
  const observer = new IntersectionObserver(entries => {
    heroVisible = entries[0].isIntersecting;
    updateNet();
  });
  observer.observe(hero);
  addEventListener('pagehide', () => { pageActive = false; ++generation; destroyNet(); });
  addEventListener('pageshow', () => { pageActive = true; updateNet(); });
  updateTheme(explicitTheme || 'light');
})();
