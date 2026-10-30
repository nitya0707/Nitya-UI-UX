/**
 * AeroBiome™ Interactive Landing Page Scripts
 * Handles Circadian Ambient Switcher, Live Telemetry, & Responsive Navigation
 */

document.addEventListener('DOMContentLoaded', () => {
  // 1. Mobile Menu Toggle
  const mobileMenuBtn = document.getElementById('mobileMenuBtn');
  const navMenu = document.getElementById('navMenu');

  if (mobileMenuBtn && navMenu) {
    mobileMenuBtn.addEventListener('click', () => {
      navMenu.classList.toggle('open');
      const isOpen = navMenu.classList.contains('open');
      mobileMenuBtn.setAttribute('aria-expanded', isOpen);
    });

    // Close menu when clicking any nav link
    navMenu.querySelectorAll('.nav-link').forEach(link => {
      link.addEventListener('click', () => {
        navMenu.classList.remove('open');
      });
    });
  }

  // 2. Circadian Ambient Mode Switcher
  const modeButtons = document.querySelectorAll('[data-set-mode]');
  const body = document.body;
  const solarTag = document.getElementById('currentSolarTag');
  const solarVal = document.getElementById('currentSolarVal');
  const indicator = document.getElementById('spectrumIndicator');

  const modeData = {
    focus: {
      tag: 'CIRCADIAN SPECTRUM: FOCUS',
      val: '4500K • Deep Daylight Flow',
      indicatorPos: '48%'
    },
    evening: {
      tag: 'CIRCADIAN SPECTRUM: DUSK',
      val: '2700K • Sunset Relaxation',
      indicatorPos: '75%'
    },
    night: {
      tag: 'CIRCADIAN SPECTRUM: NIGHT',
      val: '1800K • Melatonin Induction',
      indicatorPos: '95%'
    }
  };

  modeButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      const mode = btn.getAttribute('data-set-mode');
      
      // Update active button state
      modeButtons.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      // Update body dataset
      body.setAttribute('data-mode', mode);

      // Update HUD elements
      if (modeData[mode]) {
        if (solarTag) solarTag.textContent = modeData[mode].tag;
        if (solarVal) solarVal.textContent = modeData[mode].val;
        if (indicator) indicator.style.left = modeData[mode].indicatorPos;
      }
    });
  });

  // 3. Circadian Timeline Nodes Click
  const specNodes = document.querySelectorAll('.spec-node');
  const nodeMap = {
    dawn: { mode: 'focus', pos: '15%' },
    noon: { mode: 'focus', pos: '48%' },
    dusk: { mode: 'evening', pos: '75%' },
    night: { mode: 'night', pos: '95%' }
  };

  specNodes.forEach(node => {
    node.addEventListener('click', () => {
      specNodes.forEach(n => n.classList.remove('active'));
      node.classList.add('active');

      const key = node.getAttribute('data-node');
      if (nodeMap[key]) {
        const { mode, pos } = nodeMap[key];
        body.setAttribute('data-mode', mode);
        if (indicator) indicator.style.left = pos;

        // Sync header mode button
        modeButtons.forEach(b => {
          if (b.getAttribute('data-set-mode') === mode) {
            b.classList.add('active');
          } else {
            b.classList.remove('active');
          }
        });
      }
    });
  });

  // 4. Video Experience Modal
  const openDemoBtn = document.getElementById('openDemoBtn');
  const demoModal = document.getElementById('demoModal');
  const closeModalBtn = document.getElementById('closeModalBtn');

  if (openDemoBtn && demoModal) {
    openDemoBtn.addEventListener('click', (e) => {
      e.preventDefault();
      demoModal.classList.add('open');
    });
  }

  if (closeModalBtn && demoModal) {
    closeModalBtn.addEventListener('click', () => {
      demoModal.classList.remove('open');
    });

    demoModal.addEventListener('click', (e) => {
      if (e.target === demoModal) {
        demoModal.classList.remove('open');
      }
    });
  }

  // 5. Pre-order Form Handling
  const preorderForm = document.getElementById('preorderForm');
  if (preorderForm) {
    preorderForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const input = preorderForm.querySelector('input[type="email"]');
      const email = input.value;
      if (email) {
        alert(`🎉 Thank you! Genesis Pod reservation confirmation sent to: ${email}`);
        input.value = '';
      }
    });
  }

  // 6. Realistic Sensor Stream Telemetry Jitter
  const aqiVal = document.querySelector('.hud-air-quality .hud-val');
  if (aqiVal) {
    setInterval(() => {
      const randomJitter = (99.7 + Math.random() * 0.2).toFixed(1);
      aqiVal.innerHTML = `${randomJitter} <small>AQI (Optimal)</small>`;
    }, 4000);
  }
});
