#!/usr/bin/env python3
import os

os.makedirs("screenshots", exist_ok=True)
os.makedirs("assets", exist_ok=True)

# -------------------------------------------------------------
# 1. SCREENSHOT 01: Hero Desktop Preview (1440 x 920)
# -------------------------------------------------------------
s1 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 920" width="1440" height="920">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#070A0B"/>
      <stop offset="50%" stop-color="#0D1316"/>
      <stop offset="100%" stop-color="#050708"/>
    </linearGradient>
    <linearGradient id="glowG" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#10B981" stop-opacity="0.35"/>
      <stop offset="100%" stop-color="#06B6D4" stop-opacity="0.0"/>
    </linearGradient>
    <linearGradient id="amberG" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#F59E0B" stop-opacity="0.25"/>
      <stop offset="100%" stop-color="#EF4444" stop-opacity="0.0"/>
    </linearGradient>
    <linearGradient id="btnGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#10B981"/>
      <stop offset="100%" stop-color="#059669"/>
    </linearGradient>
    <linearGradient id="glassGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFFFFF" stop-opacity="0.08"/>
      <stop offset="100%" stop-color="#FFFFFF" stop-opacity="0.02"/>
    </linearGradient>
    <filter id="shadowLg" x="-10%" y="-10%" width="120%" height="130%">
      <feDropShadow dx="0" dy="24" stdDeviation="32" flood-color="#000000" flood-opacity="0.6"/>
    </filter>
    <filter id="pillGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="0" stdDeviation="8" flood-color="#10B981" flood-opacity="0.4"/>
    </filter>
  </defs>

  <style>
    .font-sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Inter', sans-serif; }
    .mono { font-family: 'SF Mono', Consolas, 'Fira Code', monospace; }
  </style>

  <!-- Browser Chrome Window Header -->
  <rect width="1440" height="920" fill="url(#bgGrad)"/>
  <rect width="1440" height="42" fill="#0A0E10" stroke="rgba(255,255,255,0.06)" stroke-width="1"/>
  <!-- Window Controls -->
  <circle cx="24" cy="21" r="6" fill="#EF4444"/>
  <circle cx="44" cy="21" r="6" fill="#F59E0B"/>
  <circle cx="64" cy="21" r="6" fill="#10B981"/>
  <rect x="420" y="8" width="600" height="26" rx="6" fill="rgba(255,255,255,0.04)" stroke="rgba(255,255,255,0.06)" stroke-width="1"/>
  <text x="720" y="25" text-anchor="middle" class="font-sans mono" font-size="12" fill="#64748B">https://aerobiome.design • Figma Desktop Frame (1440 x 900 Auto Layout)</text>

  <!-- Ambient Light Orbs -->
  <ellipse cx="1100" cy="380" rx="420" ry="320" fill="url(#glowG)"/>
  <ellipse cx="280" cy="240" rx="300" ry="240" fill="url(#amberG)"/>

  <!-- TOP ANNOUNCEMENT BANNER -->
  <rect y="42" width="1440" height="36" fill="rgba(16,185,129,0.08)" stroke="rgba(16,185,129,0.2)" stroke-width="1"/>
  <text x="720" y="65" text-anchor="middle" class="font-sans" font-size="13" font-weight="500" fill="#34D399">
    🌿 Introducing AeroBiome Genesis: The World's First Bio-Responsive Desktop Ecosystem. <tspan font-weight="700" text-decoration="underline" fill="#FFFFFF">Read Whitepaper →</tspan>
  </text>

  <!-- STICKY HEADER / NAVIGATION BAR (Auto Layout: Horizontal, Space-Between) -->
  <g transform="translate(80, 102)">
    <rect width="1280" height="68" rx="20" fill="url(#glassGrad)" stroke="rgba(255,255,255,0.1)" stroke-width="1" filter="url(#shadowLg)"/>
    
    <!-- Logo Lockup -->
    <g transform="translate(24, 16)">
      <circle cx="18" cy="18" r="16" fill="none" stroke="#10B981" stroke-width="2"/>
      <circle cx="18" cy="18" r="8" fill="#34D399" fill-opacity="0.3"/>
      <circle cx="18" cy="18" r="3" fill="#FFFFFF"/>
      <text x="44" y="24" class="font-sans" font-size="18" font-weight="800" letter-spacing="-0.5" fill="#F8FAFC">AERO<tspan fill="#34D399">BIOME</tspan></text>
    </g>

    <!-- Nav Links (Auto Layout: Horizontal, Gap 36px) -->
    <g transform="translate(420, 26)" class="font-sans" font-size="14" font-weight="500">
      <text x="0" y="14" fill="#FFFFFF" font-weight="600">Product</text>
      <circle cx="26" cy="22" r="2" fill="#34D399"/>
      <text x="60" y="14" fill="#94A3B8">Biophilic Tech</text>
      <text x="175" y="14" fill="#94A3B8">Circadian Science</text>
      <text x="315" y="14" fill="#94A3B8">SensorIQ™</text>
      <text x="415" y="14" fill="#94A3B8">Reviews</text>
    </g>

    <!-- Header Actions (CTA) -->
    <g transform="translate(1030, 14)">
      <text x="40" y="26" class="font-sans" font-size="14" font-weight="600" fill="#E2E8F0">Sign In</text>
      <g transform="translate(110, 0)">
        <rect width="116" height="40" rx="10" fill="url(#btnGrad)" filter="url(#pillGlow)"/>
        <text x="58" y="25" text-anchor="middle" class="font-sans" font-size="13" font-weight="700" fill="#FFFFFF">Pre-Order</text>
      </g>
    </g>
  </g>

  <!-- HERO SECTION CONTAINER (Auto Layout Dual-Column) -->
  <g transform="translate(80, 230)">
    
    <!-- LEFT COLUMN: Content & Typography (Width 640px) -->
    <g transform="translate(0, 30)">
      <!-- Status Badge Pill (Component Variant) -->
      <g>
        <rect width="250" height="32" rx="16" fill="rgba(16,185,129,0.12)" stroke="rgba(52,211,153,0.3)" stroke-width="1"/>
        <circle cx="16" cy="16" r="4" fill="#34D399" filter="url(#pillGlow)"/>
        <text x="28" y="21" class="font-sans" font-size="12" font-weight="600" fill="#34D399" letter-spacing="0.5">BIO-RESPONSIVE HARDWARE</text>
      </g>

      <!-- Main Headline (Display 58px) -->
      <text x="0" y="95" class="font-sans" font-size="54" font-weight="800" fill="#F8FAFC" letter-spacing="-1.8">
        Pure Air. Living Moss.
      </text>
      <text x="0" y="155" class="font-sans" font-size="54" font-weight="800" fill="url(#btnGrad)" letter-spacing="-1.8">
        Circadian Harmony.
      </text>

      <!-- Body Copy (18px) -->
      <text x="0" y="210" class="font-sans" font-size="18" line-height="28" font-weight="400" fill="#94A3B8">
        AeroBiome merges living botanical micro-filtration with adaptive
      </text>
      <text x="0" y="238" class="font-sans" font-size="18" line-height="28" font-weight="400" fill="#94A3B8">
        solar photonics. Neutralize indoor brain fatigue, balance melatonin,
      </text>
      <text x="0" y="266" class="font-sans" font-size="18" line-height="28" font-weight="400" fill="#94A3B8">
        and purify workspace air by 99.4% in a whisper-silent form factor.
      </text>

      <!-- Primary & Secondary CTA Buttons (Auto Layout: Horizontal, Gap 16px) -->
      <g transform="translate(0, 310)">
        <!-- Primary Button (Master Component) -->
        <g>
          <rect width="200" height="52" rx="14" fill="url(#btnGrad)" filter="url(#pillGlow)"/>
          <text x="90" y="32" text-anchor="middle" class="font-sans" font-size="15" font-weight="700" fill="#FFFFFF">Order Genesis Pod</text>
          <!-- Arrow Icon -->
          <path d="M 165 26 L 175 26 M 171 22 L 175 26 L 171 30" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
        </g>
        
        <!-- Secondary Button (Ghost Glass) -->
        <g transform="translate(216, 0)">
          <rect width="180" height="52" rx="14" fill="rgba(255,255,255,0.05)" stroke="rgba(255,255,255,0.12)" stroke-width="1"/>
          <!-- Play Icon -->
          <circle cx="32" cy="26" r="10" fill="rgba(255,255,255,0.1)"/>
          <polygon points="30,22 36,26 30,30" fill="#F8FAFC"/>
          <text x="98" y="32" text-anchor="middle" class="font-sans" font-size="15" font-weight="600" fill="#F8FAFC">Watch 90s Film</text>
        </g>
      </g>

      <!-- Trust Metrics / Social Proof Ticker (Auto Layout: Horizontal, Gap 32px) -->
      <g transform="translate(0, 410)" class="font-sans">
        <g>
          <text x="0" y="0" font-size="28" font-weight="800" fill="#F8FAFC">99.4%</text>
          <text x="0" y="20" font-size="12" font-weight="500" fill="#64748B">VOC &amp; PM2.5 Removal</text>
        </g>
        <line x1="140" y1="-8" x2="140" y2="28" stroke="rgba(255,255,255,0.1)" stroke-width="1"/>
        <g transform="translate(160, 0)">
          <text x="0" y="0" font-size="28" font-weight="800" fill="#F8FAFC">&lt; 18 dB</text>
          <text x="0" y="20" font-size="12" font-weight="500" fill="#64748B">WhisperQuiet Acoustics</text>
        </g>
        <line x1="320" y1="-8" x2="320" y2="28" stroke="rgba(255,255,255,0.1)" stroke-width="1"/>
        <g transform="translate(340, 0)">
          <text x="0" y="0" font-size="28" font-weight="800" fill="#F8FAFC">4.9/5</text>
          <text x="0" y="20" font-size="12" font-weight="500" fill="#64748B">Rated by 2,400+ Designers</text>
        </g>
      </g>
    </g>

    <!-- RIGHT COLUMN: 3D Product Mockup & Ambient Bio-Pod Visual (Width 580px) -->
    <g transform="translate(680, 0)">
      
      <!-- Elevated Backdrop Pod Card -->
      <rect width="560" height="560" rx="32" fill="url(#glassGrad)" stroke="rgba(255,255,255,0.08)" stroke-width="1" filter="url(#shadowLg)"/>

      <!-- Ambient Lighting Radial Gradient inside pod container -->
      <circle cx="280" cy="280" r="220" fill="#10B981" fill-opacity="0.1" filter="url(#glowG)"/>

      <!-- Stylized AeroBiome Physical Device Illustration -->
      <g transform="translate(180, 60)">
        <!-- Top Halo Ring (Circadian Light) -->
        <ellipse cx="100" cy="50" rx="90" ry="24" fill="#34D399" fill-opacity="0.2" stroke="#34D399" stroke-width="3" filter="url(#pillGlow)"/>
        
        <!-- Matte Titanium Upper Chassis -->
        <path d="M 10 50 L 10 120 C 10 140 190 140 190 120 L 190 50 Z" fill="#1E293B" stroke="rgba(255,255,255,0.15)"/>
        <!-- Titanium texture highlights -->
        <line x1="20" y1="56" x2="20" y2="114" stroke="rgba(255,255,255,0.2)" stroke-width="1.5"/>
        <line x1="180" y1="56" x2="180" y2="114" stroke="rgba(0,0,0,0.5)" stroke-width="2"/>
        
        <!-- Center Glass Terrarium Chamber (Living Moss Ecosystem) -->
        <rect x="15" y="120" width="170" height="180" rx="8" fill="rgba(16,185,129,0.08)" stroke="rgba(52,211,153,0.3)" stroke-width="1.5"/>
        <!-- Glass reflections -->
        <path d="M 25 130 L 60 130 L 35 290 L 25 290 Z" fill="#FFFFFF" fill-opacity="0.05"/>
        
        <!-- Living Botanical Moss Specimen (Sculptural Greenery) -->
        <g transform="translate(45, 170)">
          <path d="M 30 100 C 10 80 15 50 40 40 C 60 30 80 50 85 70 C 95 60 110 75 100 100 Z" fill="#047857"/>
          <path d="M 20 100 C 5 85 20 65 35 60 C 50 55 60 75 55 100 Z" fill="#10B981" opacity="0.9"/>
          <path d="M 60 100 C 50 75 75 50 95 65 C 105 75 100 90 90 100 Z" fill="#34D399" opacity="0.8"/>
          <!-- Dew drops / Bio-mist particles -->
          <circle cx="45" cy="55" r="2.5" fill="#A7F3D0"/>
          <circle cx="75" cy="48" r="3" fill="#6EE7B7"/>
          <circle cx="35" cy="80" r="2" fill="#FFFFFF"/>
          <circle cx="85" cy="85" r="2" fill="#FFFFFF"/>
        </g>

        <!-- Lower Acoustic Turbine & HEPA Base -->
        <path d="M 10 300 L 10 370 C 10 395 190 395 190 370 L 190 300 Z" fill="#0F172A" stroke="rgba(255,255,255,0.12)"/>
        <!-- Acoustic Perforated Mesh Air Grilles -->
        <g fill="rgba(255,255,255,0.2)">
          <circle cx="30" cy="330" r="1.5"/><circle cx="50" cy="330" r="1.5"/><circle cx="70" cy="330" r="1.5"/><circle cx="90" cy="330" r="1.5"/><circle cx="110" cy="330" r="1.5"/><circle cx="130" cy="330" r="1.5"/><circle cx="150" cy="330" r="1.5"/><circle cx="170" cy="330" r="1.5"/>
          <circle cx="40" cy="342" r="1.5"/><circle cx="60" cy="342" r="1.5"/><circle cx="80" cy="342" r="1.5"/><circle cx="100" cy="342" r="1.5"/><circle cx="120" cy="342" r="1.5"/><circle cx="140" cy="342" r="1.5"/><circle cx="160" cy="342" r="1.5"/>
          <circle cx="30" cy="354" r="1.5"/><circle cx="50" cy="354" r="1.5"/><circle cx="70" cy="354" r="1.5"/><circle cx="90" cy="354" r="1.5"/><circle cx="110" cy="354" r="1.5"/><circle cx="130" cy="354" r="1.5"/><circle cx="150" cy="354" r="1.5"/><circle cx="170" cy="354" r="1.5"/>
        </g>

        <!-- Ambient Base Glow -->
        <ellipse cx="100" cy="385" rx="96" ry="18" fill="url(#btnGrad)" opacity="0.35" filter="url(#pillGlow)"/>
      </g>

      <!-- FLOATING HUD CARD 1: Live Bio-Metric Stream (Top Right) -->
      <g transform="translate(330, 40)">
        <rect width="200" height="90" rx="16" fill="rgba(15,23,42,0.85)" stroke="rgba(52,211,153,0.3)" stroke-width="1" filter="url(#shadowLg)"/>
        <circle cx="22" cy="24" r="5" fill="#10B981" filter="url(#pillGlow)"/>
        <text x="36" y="28" class="font-sans" font-size="12" font-weight="700" fill="#34D399">ECO-PURITY INDEX</text>
        <text x="22" y="58" class="font-sans" font-size="24" font-weight="800" fill="#FFFFFF">99.8 <tspan font-size="13" font-weight="500" fill="#94A3B8">AQI Optimal</tspan></text>
        <rect x="22" y="70" width="156" height="5" rx="2.5" fill="rgba(255,255,255,0.1)"/>
        <rect x="22" y="70" width="145" height="5" rx="2.5" fill="#10B981"/>
      </g>

      <!-- FLOATING HUD CARD 2: Circadian Solar Mode (Bottom Left) -->
      <g transform="translate(30, 420)">
        <rect width="210" height="100" rx="16" fill="rgba(15,23,42,0.85)" stroke="rgba(245,158,11,0.3)" stroke-width="1" filter="url(#shadowLg)"/>
        <circle cx="24" cy="24" r="6" fill="#F59E0B" filter="url(#pillGlow)"/>
        <text x="38" y="28" class="font-sans" font-size="12" font-weight="700" fill="#F59E0B">SOLAR SYNC: 1800K</text>
        <text x="22" y="58" class="font-sans" font-size="20" font-weight="700" fill="#FFFFFF">Evening Relax</text>
        <text x="22" y="78" class="font-sans" font-size="12" font-weight="400" fill="#94A3B8">Melatonin induction in 42m</text>
      </g>
    </g>

  </g>

  <!-- Figma Grid & Auto Layout Meta Watermark -->
  <g transform="translate(80, 880)">
    <rect width="450" height="24" rx="4" fill="rgba(0,0,0,0.6)"/>
    <text x="10" y="16" class="font-sans mono" font-size="11" fill="#94A3B8">❖ Figma Auto Layout v2.4 • Frame: Desktop 1440 • Constraints: Center &amp; Scale • System: 8pt Grid</text>
  </g>
</svg>"""

with open("screenshots/01_hero_desktop_preview.svg", "w") as f:
    f.write(s1)

print("Created screenshots/01_hero_desktop_preview.svg")

# -------------------------------------------------------------
# 2. SCREENSHOT 02: Reusable Components Library (1440 x 1000)
# -------------------------------------------------------------
s2 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 1000" width="1440" height="1000">
  <defs>
    <linearGradient id="bgGrad2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#070A0B"/>
      <stop offset="100%" stop-color="#0E1418"/>
    </linearGradient>
    <linearGradient id="btnGlow" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#10B981"/>
      <stop offset="100%" stop-color="#059669"/>
    </linearGradient>
    <linearGradient id="cardG" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1E293B" stop-opacity="0.6"/>
      <stop offset="100%" stop-color="#0F172A" stop-opacity="0.8"/>
    </linearGradient>
    <filter id="cShadow" x="-10%" y="-10%" width="120%" height="130%">
      <feDropShadow dx="0" dy="16" stdDeviation="20" flood-color="#000000" flood-opacity="0.5"/>
    </filter>
  </defs>

  <style>
    .font-sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Inter', sans-serif; }
    .mono { font-family: 'SF Mono', Consolas, 'Fira Code', monospace; }
  </style>

  <rect width="1440" height="1000" fill="url(#bgGrad2)"/>

  <!-- Figma Canvas Frame Title Header -->
  <g transform="translate(60, 40)">
    <rect width="1320" height="70" rx="16" fill="rgba(255,255,255,0.03)" stroke="rgba(255,255,255,0.08)"/>
    <text x="30" y="35" class="font-sans" font-size="20" font-weight="800" fill="#F8FAFC">❖ FIGMA DESIGN SYSTEM • REUSABLE MASTER COMPONENTS</text>
    <text x="30" y="55" class="font-sans mono" font-size="12" fill="#34D399">Auto Layout Enabled • Variants &amp; States • Hug/Fill Container Architecture</text>
    <rect x="1150" y="20" width="140" height="30" rx="8" fill="rgba(16,185,129,0.15)" stroke="#10B981"/>
    <text x="1220" y="40" text-anchor="middle" class="font-sans" font-size="11" font-weight="700" fill="#34D399">WCAG AAA COMPLIANT</text>
  </g>

  <!-- SECTION 1: COMPONENT 1 - MASTER BUTTON (Variants & States) -->
  <g transform="translate(60, 140)">
    <!-- Section Header -->
    <rect width="1320" height="42" rx="8" fill="rgba(16,185,129,0.08)" stroke="rgba(16,185,129,0.2)"/>
    <text x="20" y="26" class="font-sans" font-size="14" font-weight="700" fill="#34D399">COMPONENT 1: Button / Master (Variants: Primary, Secondary Frosted, Ghost | States: Default, Hover, Disabled)</text>
    <text x="1050" y="26" class="font-sans mono" font-size="11" fill="#94A3B8">Auto Layout: Horizontal | Padding: 14px 28px | Gap: 8px</text>

    <!-- Variants Grid -->
    <g transform="translate(0, 60)">
      <!-- Variant 1: Primary Default -->
      <g transform="translate(20, 0)">
        <rect width="190" height="48" rx="12" fill="url(#btnGlow)"/>
        <text x="95" y="30" text-anchor="middle" class="font-sans" font-size="14" font-weight="700" fill="#FFFFFF">Primary Default</text>
        <text x="95" y="70" text-anchor="middle" class="font-sans mono" font-size="10" fill="#64748B">Variant: Primary | State: Default</text>
      </g>

      <!-- Variant 2: Primary Hover (Glow ring) -->
      <g transform="translate(240, 0)">
        <rect width="190" height="48" rx="12" fill="#34D399" stroke="#A7F3D0" stroke-width="2"/>
        <text x="95" y="30" text-anchor="middle" class="font-sans" font-size="14" font-weight="700" fill="#064E3B">Primary Hover ↗</text>
        <text x="95" y="70" text-anchor="middle" class="font-sans mono" font-size="10" fill="#64748B">Variant: Primary | State: Hover</text>
      </g>

      <!-- Variant 3: Secondary Frosted -->
      <g transform="translate(460, 0)">
        <rect width="190" height="48" rx="12" fill="rgba(255,255,255,0.06)" stroke="rgba(255,255,255,0.2)" stroke-width="1"/>
        <text x="95" y="30" text-anchor="middle" class="font-sans" font-size="14" font-weight="600" fill="#F8FAFC">Secondary Glass</text>
        <text x="95" y="70" text-anchor="middle" class="font-sans mono" font-size="10" fill="#64748B">Variant: Secondary | Glass 12%</text>
      </g>

      <!-- Variant 4: Ghost / Link Button -->
      <g transform="translate(680, 0)">
        <rect width="190" height="48" rx="12" fill="none" stroke="rgba(255,255,255,0.1)" stroke-dasharray="4 4"/>
        <text x="95" y="30" text-anchor="middle" class="font-sans" font-size="14" font-weight="600" fill="#34D399">Ghost Text Link →</text>
        <text x="95" y="70" text-anchor="middle" class="font-sans mono" font-size="10" fill="#64748B">Variant: Ghost | State: Default</text>
      </g>

      <!-- Variant 5: Disabled State -->
      <g transform="translate(900, 0)">
        <rect width="190" height="48" rx="12" fill="rgba(255,255,255,0.03)" stroke="rgba(255,255,255,0.05)"/>
        <text x="95" y="30" text-anchor="middle" class="font-sans" font-size="14" font-weight="500" fill="#475569">Disabled Action</text>
        <text x="95" y="70" text-anchor="middle" class="font-sans mono" font-size="10" fill="#64748B">State: Disabled (Opacity 40%)</text>
      </g>

      <!-- Variant 6: Small Size Pill (36px) -->
      <g transform="translate(1120, 6)">
        <rect width="160" height="36" rx="18" fill="url(#btnGlow)"/>
        <text x="80" y="23" text-anchor="middle" class="font-sans" font-size="12" font-weight="700" fill="#FFFFFF">Small Pill (36px)</text>
        <text x="80" y="64" text-anchor="middle" class="font-sans mono" font-size="10" fill="#64748B">Size: SM | Radius: 999px</text>
      </g>
    </g>
  </g>

  <!-- SECTION 2: COMPONENT 2 - FEATURE CARD COMPONENT (At least 3 instances) -->
  <g transform="translate(60, 310)">
    <rect width="1320" height="42" rx="8" fill="rgba(16,185,129,0.08)" stroke="rgba(16,185,129,0.2)"/>
    <text x="20" y="26" class="font-sans" font-size="14" font-weight="700" fill="#34D399">COMPONENT 2: Card / FeatureCard (Auto Layout: Vertical | Padding: 32px | Gap: 20px | Width: Fill Container)</text>
    <text x="1030" y="26" class="font-sans mono" font-size="11" fill="#94A3B8">3 Reusable Instances with Slot Overrides</text>

    <!-- 3 Reusable Cards in Auto Layout Horizontal Grid -->
    <g transform="translate(20, 60)">
      
      <!-- CARD 1: Botanical Bio-Filtration -->
      <g transform="translate(0, 0)">
        <rect width="400" height="310" rx="20" fill="url(#cardG)" stroke="rgba(255,255,255,0.08)" stroke-width="1" filter="url(#cShadow)"/>
        <!-- Icon Container (Auto Layout Center 48x48) -->
        <rect x="32" y="32" width="52" height="52" rx="14" fill="rgba(16,185,129,0.15)" stroke="rgba(16,185,129,0.3)"/>
        <path d="M 58 46 C 66 52 70 60 70 66 C 70 72 65 74 58 74 C 51 74 46 72 46 66 C 46 60 50 52 58 46 Z" fill="#34D399"/>
        <!-- Badge -->
        <rect x="260" y="38" width="108" height="26" rx="13" fill="rgba(52,211,153,0.1)"/>
        <text x="314" y="55" text-anchor="middle" class="font-sans" font-size="11" font-weight="700" fill="#34D399">BIOPHILIC CORE</text>
        <!-- Title -->
        <text x="32" y="125" class="font-sans" font-size="20" font-weight="700" fill="#F8FAFC">Living Bio-Filter Matrix</text>
        <!-- Description -->
        <text x="32" y="156" class="font-sans" font-size="14" line-height="22" font-weight="400" fill="#94A3B8">Stabilized micro-moss culture captures</text>
        <text x="32" y="178" class="font-sans" font-size="14" line-height="22" font-weight="400" fill="#94A3B8">fine dust and metabolized VOCs, generating</text>
        <text x="32" y="200" class="font-sans" font-size="14" line-height="22" font-weight="400" fill="#94A3B8">fresh negative oxygen ions continuous 24/7.</text>
        <!-- Footer Metric / Link -->
        <line x1="32" y1="230" x2="368" y2="230" stroke="rgba(255,255,255,0.06)"/>
        <text x="32" y="265" class="font-sans" font-size="13" font-weight="600" fill="#34D399">Zero Filter Waste • Self-Hydrating →</text>
        <!-- Auto layout indicator -->
        <text x="32" y="295" class="font-sans mono" font-size="10" fill="#64748B">AutoLayout: Vert[Gap=20, Pad=32, HugH]</text>
      </g>

      <!-- CARD 2: Solar Circadian Photonics (Active/Highlighted Variant) -->
      <g transform="translate(440, 0)">
        <rect width="400" height="310" rx="20" fill="url(#cardG)" stroke="#10B981" stroke-width="1.5" filter="url(#cShadow)"/>
        <!-- Glow border line -->
        <rect x="32" y="32" width="52" height="52" rx="14" fill="rgba(245,158,11,0.15)" stroke="rgba(245,158,11,0.3)"/>
        <!-- Sun icon -->
        <circle cx="58" cy="58" r="10" fill="#F59E0B"/>
        <line x1="58" y1="42" x2="58" y2="46" stroke="#F59E0B" stroke-width="2"/>
        <line x1="58" y1="70" x2="58" y2="74" stroke="#F59E0B" stroke-width="2"/>
        <line x1="42" y1="58" x2="46" y2="58" stroke="#F59E0B" stroke-width="2"/>
        <line x1="70" y1="58" x2="74" y2="58" stroke="#F59E0B" stroke-width="2"/>
        <!-- Badge -->
        <rect x="260" y="38" width="108" height="26" rx="13" fill="rgba(245,158,11,0.15)"/>
        <text x="314" y="55" text-anchor="middle" class="font-sans" font-size="11" font-weight="700" fill="#F59E0B">SOLAR SYNC</text>
        <!-- Title -->
        <text x="32" y="125" class="font-sans" font-size="20" font-weight="700" fill="#F8FAFC">Adaptive Circadian Halo</text>
        <!-- Description -->
        <text x="32" y="156" class="font-sans" font-size="14" line-height="22" font-weight="400" fill="#94A3B8">Automated 1800K to 6500K spectral curve</text>
        <text x="32" y="178" class="font-sans" font-size="14" line-height="22" font-weight="400" fill="#94A3B8">mirrors real sunlight phases, boosting focus</text>
        <text x="32" y="200" class="font-sans" font-size="14" line-height="22" font-weight="400" fill="#94A3B8">at 10 AM and naturally promoting melatonin.</text>
        <!-- Footer Metric / Link -->
        <line x1="32" y1="230" x2="368" y2="230" stroke="rgba(255,255,255,0.06)"/>
        <text x="32" y="265" class="font-sans" font-size="13" font-weight="600" fill="#F59E0B">Clinical Harvard Sleep Study Certified →</text>
        <text x="32" y="295" class="font-sans mono" font-size="10" fill="#64748B">Variant: Highlighted [Active Border=Emerald]</text>
      </g>

      <!-- CARD 3: SensoriIQ Air Diagnostics -->
      <g transform="translate(880, 0)">
        <rect width="400" height="310" rx="20" fill="url(#cardG)" stroke="rgba(255,255,255,0.08)" stroke-width="1" filter="url(#cShadow)"/>
        <!-- Icon Container -->
        <rect x="32" y="32" width="52" height="52" rx="14" fill="rgba(6,182,212,0.15)" stroke="rgba(6,182,212,0.3)"/>
        <!-- Radar wave icon -->
        <circle cx="58" cy="58" r="12" fill="none" stroke="#06B6D4" stroke-width="2"/>
        <circle cx="58" cy="58" r="6" fill="none" stroke="#06B6D4" stroke-width="2"/>
        <circle cx="58" cy="58" r="2" fill="#06B6D4"/>
        <!-- Badge -->
        <rect x="260" y="38" width="108" height="26" rx="13" fill="rgba(6,182,212,0.1)"/>
        <text x="314" y="55" text-anchor="middle" class="font-sans" font-size="11" font-weight="700" fill="#06B6D4">ML SENSOR ARRAY</text>
        <!-- Title -->
        <text x="32" y="125" class="font-sans" font-size="20" font-weight="700" fill="#F8FAFC">SensoriIQ™ Real-Time Mesh</text>
        <!-- Description -->
        <text x="32" y="156" class="font-sans" font-size="14" line-height="22" font-weight="400" fill="#94A3B8">Ultra-fine laser sensors evaluate eCO₂,</text>
        <text x="32" y="178" class="font-sans" font-size="14" line-height="22" font-weight="400" fill="#94A3B8">formaldehyde, PM1.0, and desk lux every</text>
        <text x="32" y="200" class="font-sans" font-size="14" line-height="22" font-weight="400" fill="#94A3B8">500ms, dynamically dialing airflow rates.</text>
        <!-- Footer Metric / Link -->
        <line x1="32" y1="230" x2="368" y2="230" stroke="rgba(255,255,255,0.06)"/>
        <text x="32" y="265" class="font-sans" font-size="13" font-weight="600" fill="#06B6D4">Connects with Figma &amp; Slack API →</text>
        <text x="32" y="295" class="font-sans mono" font-size="10" fill="#64748B">AutoLayout: Vert[Gap=20, Pad=32, HugH]</text>
      </g>
    </g>
  </g>

  <!-- SECTION 3: COMPONENT 3 - RESPONSIVE NAVIGATION HEADER & FOOTER -->
  <g transform="translate(60, 710)">
    <rect width="1320" height="42" rx="8" fill="rgba(16,185,129,0.08)" stroke="rgba(16,185,129,0.2)"/>
    <text x="20" y="26" class="font-sans" font-size="14" font-weight="700" fill="#34D399">COMPONENT 3: Navigation / Header &amp; Footer (Variants: Desktop 1440 Space-Between | Mobile 375 Sticky Pill)</text>
    <text x="1060" y="26" class="font-sans mono" font-size="11" fill="#94A3B8">Constraints: Left &amp; Right | Scale</text>

    <!-- Desktop Navigation Instance -->
    <g transform="translate(20, 60)">
      <rect width="820" height="64" rx="16" fill="rgba(255,255,255,0.04)" stroke="rgba(255,255,255,0.08)"/>
      <text x="24" y="38" class="font-sans" font-size="16" font-weight="800" fill="#FFFFFF">🌿 AERO<tspan fill="#34D399">BIOME</tspan></text>
      
      <!-- Nav Items -->
      <g transform="translate(240, 22)" class="font-sans" font-size="13" font-weight="500" fill="#94A3B8">
        <text x="0" y="16" fill="#FFFFFF" font-weight="600">Product</text>
        <text x="70" y="16">Features</text>
        <text x="150" y="16">Science</text>
        <text x="230" y="16">Pricing</text>
      </g>
      
      <rect x="680" y="14" width="120" height="36" rx="10" fill="url(#btnGlow)"/>
      <text x="740" y="37" text-anchor="middle" class="font-sans" font-size="12" font-weight="700" fill="#FFFFFF">Pre-Order</text>
      <text x="24" y="90" class="font-sans mono" font-size="10" fill="#64748B">Desktop Header [1440px] • Auto Layout: Space-Between • Padding: 16px 32px</text>
    </g>

    <!-- Mobile Header Instance (Variant) -->
    <g transform="translate(880, 60)">
      <rect width="400" height="64" rx="16" fill="rgba(255,255,255,0.04)" stroke="rgba(255,255,255,0.08)"/>
      <text x="24" y="38" class="font-sans" font-size="16" font-weight="800" fill="#FFFFFF">🌿 AERO<tspan fill="#34D399">BIOME</tspan></text>
      
      <!-- Mobile Hamburger Button -->
      <g transform="translate(330, 20)">
        <rect width="40" height="24" rx="6" fill="rgba(255,255,255,0.06)"/>
        <line x1="8" y1="6" x2="32" y2="6" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round"/>
        <line x1="8" y1="12" x2="32" y2="12" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round"/>
        <line x1="8" y1="18" x2="32" y2="18" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round"/>
      </g>
      <text x="24" y="90" class="font-sans mono" font-size="10" fill="#64748B">Mobile Header Variant [375px] • Auto Layout: Space-Between • Hamburger Drawer</text>
    </g>
  </g>

  <!-- SECTION 4: COMPONENT 4 (Bonus) - STATUS PILL & METRIC BADGES -->
  <g transform="translate(60, 890)">
    <rect width="1320" height="70" rx="12" fill="rgba(255,255,255,0.02)" stroke="rgba(255,255,255,0.06)"/>
    <text x="20" y="24" class="font-sans" font-size="12" font-weight="700" fill="#94A3B8">BONUS COMPONENT: StatusPill / Master (Variants: Live Pulse, Warning, Circadian Mode, Battery Level)</text>
    
    <g transform="translate(20, 32)">
      <!-- Pill 1 -->
      <rect width="130" height="26" rx="13" fill="rgba(16,185,129,0.12)" stroke="rgba(52,211,153,0.3)"/>
      <circle cx="14" cy="13" r="3.5" fill="#34D399"/>
      <text x="24" y="17" class="font-sans" font-size="11" font-weight="600" fill="#34D399">ACTIVE AIRFLOW</text>

      <!-- Pill 2 -->
      <g transform="translate(150, 0)">
        <rect width="140" height="26" rx="13" fill="rgba(245,158,11,0.12)" stroke="rgba(245,158,11,0.3)"/>
        <circle cx="14" cy="13" r="3.5" fill="#F59E0B"/>
        <text x="24" y="17" class="font-sans" font-size="11" font-weight="600" fill="#F59E0B">SOLAR SYNC 2700K</text>
      </g>

      <!-- Pill 3 -->
      <g transform="translate(310, 0)">
        <rect width="150" height="26" rx="13" fill="rgba(6,182,212,0.12)" stroke="rgba(6,182,212,0.3)"/>
        <circle cx="14" cy="13" r="3.5" fill="#06B6D4"/>
        <text x="24" y="17" class="font-sans" font-size="11" font-weight="600" fill="#06B6D4">VOC FILTER: 99.4%</text>
      </g>

      <!-- Pill 4 -->
      <g transform="translate(480, 0)">
        <rect width="160" height="26" rx="13" fill="rgba(168,85,247,0.12)" stroke="rgba(168,85,247,0.3)"/>
        <circle cx="14" cy="13" r="3.5" fill="#C084FC"/>
        <text x="24" y="17" class="font-sans" font-size="11" font-weight="600" fill="#C084FC">WHISPERQUIET 16dB</text>
      </g>

      <text x="680" y="18" class="font-sans mono" font-size="11" fill="#64748B">Figma Component Set: 4 Variants • Auto Layout: Horizontal • Padding: 6px 14px • Gap: 6px</text>
    </g>
  </g>
</svg>"""

with open("screenshots/02_reusable_components_library.svg", "w") as f:
    f.write(s2)

print("Created screenshots/02_reusable_components_library.svg")


# -------------------------------------------------------------
# 3. SCREENSHOT 03: Color & Typography System (1440 x 900)
# -------------------------------------------------------------
s3 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 900" width="1440" height="900">
  <defs>
    <linearGradient id="bgGrad3" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#080B0D"/>
      <stop offset="100%" stop-color="#0F1418"/>
    </linearGradient>
  </defs>

  <style>
    .font-sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Inter', sans-serif; }
    .mono { font-family: 'SF Mono', Consolas, 'Fira Code', monospace; }
  </style>

  <rect width="1440" height="900" fill="url(#bgGrad3)"/>

  <!-- Canvas Header -->
  <g transform="translate(60, 40)">
    <rect width="1320" height="70" rx="16" fill="rgba(255,255,255,0.03)" stroke="rgba(255,255,255,0.08)"/>
    <text x="30" y="35" class="font-sans" font-size="20" font-weight="800" fill="#F8FAFC">❖ DESIGN TOKENS • COLOR PALETTE &amp; TYPOGRAPHY SCALE</text>
    <text x="30" y="55" class="font-sans mono" font-size="12" fill="#34D399">Shared Figma Styles • 8-Point Spatial Grid • WCAG 2.1 AA/AAA Contrast Verified</text>
    <rect x="1150" y="20" width="140" height="30" rx="8" fill="rgba(16,185,129,0.15)" stroke="#10B981"/>
    <text x="1220" y="40" text-anchor="middle" class="font-sans" font-size="11" font-weight="700" fill="#34D399">TOKENS V1.0</text>
  </g>

  <!-- LEFT COLUMN: Color Swatches & Tokens (Width 640px) -->
  <g transform="translate(60, 140)">
    <rect width="640" height="710" rx="16" fill="rgba(255,255,255,0.02)" stroke="rgba(255,255,255,0.06)"/>
    
    <g transform="translate(24, 24)">
      <text x="0" y="16" class="font-sans" font-size="16" font-weight="700" fill="#F8FAFC">SHARED COLOR TOKENS &amp; PALETTE</text>
      <text x="0" y="34" class="font-sans mono" font-size="11" fill="#64748B">Semantic Design Token Architecture with Hex, RGB &amp; Contrast</text>

      <!-- Swatch 1: Primary Emerald -->
      <g transform="translate(0, 50)">
        <rect width="100" height="70" rx="12" fill="#10B981"/>
        <text x="116" y="24" class="font-sans" font-size="15" font-weight="700" fill="#FFFFFF">Primary / Emerald Glow</text>
        <text x="116" y="44" class="font-sans mono" font-size="12" fill="#34D399">HEX: #10B981 • RGB: rgb(16, 185, 129)</text>
        <text x="116" y="62" class="font-sans" font-size="11" fill="#94A3B8">Usage: Primary CTAs, active status, bio-growth indicators (WCAG AAA)</text>
      </g>

      <!-- Swatch 2: Luminescent Mint -->
      <g transform="translate(0, 134)">
        <rect width="100" height="70" rx="12" fill="#34D399"/>
        <text x="116" y="24" class="font-sans" font-size="15" font-weight="700" fill="#FFFFFF">Accent / Luminescent Mint</text>
        <text x="116" y="44" class="font-sans mono" font-size="12" fill="#34D399">HEX: #34D399 • RGB: rgb(52, 211, 153)</text>
        <text x="116" y="62" class="font-sans" font-size="11" fill="#94A3B8">Usage: Interactive hover states, glow filters, highlight text</text>
      </g>

      <!-- Swatch 3: Solar Amber -->
      <g transform="translate(0, 218)">
        <rect width="100" height="70" rx="12" fill="#F59E0B"/>
        <text x="116" y="24" class="font-sans" font-size="15" font-weight="700" fill="#FFFFFF">Secondary / Solar Amber</text>
        <text x="116" y="44" class="font-sans mono" font-size="12" fill="#F59E0B">HEX: #F59E0B • RGB: rgb(245, 158, 11)</text>
        <text x="116" y="62" class="font-sans" font-size="11" fill="#94A3B8">Usage: Circadian evening photon mode, sunset alert warnings</text>
      </g>

      <!-- Swatch 4: Deep Obsidian Canvas -->
      <g transform="translate(0, 302)">
        <rect width="100" height="70" rx="12" fill="#090D0E" stroke="rgba(255,255,255,0.15)" stroke-width="1"/>
        <text x="116" y="24" class="font-sans" font-size="15" font-weight="700" fill="#FFFFFF">Background / Deep Obsidian</text>
        <text x="116" y="44" class="font-sans mono" font-size="12" fill="#94A3B8">HEX: #090D0E • Base Canvas</text>
        <text x="116" y="62" class="font-sans" font-size="11" fill="#94A3B8">Usage: Primary dark mode background, eliminates blue light strain</text>
      </g>

      <!-- Swatch 5: Elevated Card Surface -->
      <g transform="translate(0, 386)">
        <rect width="100" height="70" rx="12" fill="#11181C" stroke="rgba(255,255,255,0.1)" stroke-width="1"/>
        <text x="116" y="24" class="font-sans" font-size="15" font-weight="700" fill="#FFFFFF">Surface / Glass Card Elevated</text>
        <text x="116" y="44" class="font-sans mono" font-size="12" fill="#94A3B8">HEX: #11181C • Surface 80% with Blur</text>
        <text x="116" y="62" class="font-sans" font-size="11" fill="#94A3B8">Usage: Feature card containers, header glass backdrop, dialogs</text>
      </g>

      <!-- Swatch 6: Typography Text Slate White -->
      <g transform="translate(0, 470)">
        <rect width="100" height="70" rx="12" fill="#F8FAFC"/>
        <text x="116" y="24" class="font-sans" font-size="15" font-weight="700" fill="#FFFFFF">Text / Slate White (Primary)</text>
        <text x="116" y="44" class="font-sans mono" font-size="12" fill="#94A3B8">HEX: #F8FAFC • Contrast 16.8:1 (AAA)</text>
        <text x="116" y="62" class="font-sans" font-size="11" fill="#94A3B8">Usage: Main headlines, button text, high-emphasis copy</text>
      </g>

      <!-- Swatch 7: Muted Secondary Text -->
      <g transform="translate(0, 554)">
        <rect width="100" height="70" rx="12" fill="#94A3B8"/>
        <text x="116" y="24" class="font-sans" font-size="15" font-weight="700" fill="#FFFFFF">Text / Muted Slate (Secondary)</text>
        <text x="116" y="44" class="font-sans mono" font-size="12" fill="#94A3B8">HEX: #94A3B8 • Contrast 6.4:1 (AA)</text>
        <text x="116" y="62" class="font-sans" font-size="11" fill="#94A3B8">Usage: Body descriptions, timestamps, subtext, nav links</text>
      </g>
    </g>
  </g>

  <!-- RIGHT COLUMN: Typography Hierarchy & Spatial Grid (Width 640px) -->
  <g transform="translate(740, 140)">
    <rect width="640" height="710" rx="16" fill="rgba(255,255,255,0.02)" stroke="rgba(255,255,255,0.06)"/>

    <g transform="translate(24, 24)">
      <text x="0" y="16" class="font-sans" font-size="16" font-weight="700" fill="#F8FAFC">TYPOGRAPHY HIERARCHY SCALE</text>
      <text x="0" y="34" class="font-sans mono" font-size="11" fill="#64748B">Primary Font Family: Inter / Apple SF Pro Display</text>

      <!-- Display Hero -->
      <g transform="translate(0, 60)">
        <text x="0" y="40" class="font-sans" font-size="44" font-weight="800" fill="#F8FAFC" letter-spacing="-1.5">Hero Display (56px)</text>
        <text x="0" y="60" class="font-sans mono" font-size="11" fill="#34D399">Font: Inter ExtraBold • Size: 56px • Line-Height: 64px • Tracking: -0.03em</text>
      </g>

      <line x1="0" y1="140" x2="590" y2="140" stroke="rgba(255,255,255,0.06)"/>

      <!-- Heading 1 -->
      <g transform="translate(0, 155)">
        <text x="0" y="30" class="font-sans" font-size="32" font-weight="700" fill="#F8FAFC" letter-spacing="-1">Heading 1 / Section Titles (36px)</text>
        <text x="0" y="50" class="font-sans mono" font-size="11" fill="#34D399">Font: Inter Bold • Size: 36px • Line-Height: 44px • Tracking: -0.02em</text>
      </g>

      <line x1="0" y1="220" x2="590" y2="220" stroke="rgba(255,255,255,0.06)"/>

      <!-- Heading 2 -->
      <g transform="translate(0, 235)">
        <text x="0" y="24" class="font-sans" font-size="24" font-weight="700" fill="#F8FAFC">Heading 2 / Card Titles (24px)</text>
        <text x="0" y="44" class="font-sans mono" font-size="11" fill="#34D399">Font: Inter SemiBold • Size: 24px • Line-Height: 32px • Tracking: -0.01em</text>
      </g>

      <line x1="0" y1="295" x2="590" y2="295" stroke="rgba(255,255,255,0.06)"/>

      <!-- Body Large -->
      <g transform="translate(0, 310)">
        <text x="0" y="20" class="font-sans" font-size="18" font-weight="400" fill="#F8FAFC">Body Large / Lead In Paragraphs (18px)</text>
        <text x="0" y="42" class="font-sans mono" font-size="11" fill="#34D399">Font: Inter Regular • Size: 18px • Line-Height: 28px • Paragraph Gap: 16px</text>
      </g>

      <line x1="0" y1="370" x2="590" y2="370" stroke="rgba(255,255,255,0.06)"/>

      <!-- Body Regular -->
      <g transform="translate(0, 385)">
        <text x="0" y="18" class="font-sans" font-size="15" font-weight="400" fill="#94A3B8">Body Regular / Card &amp; Feature Descriptions (15px)</text>
        <text x="0" y="38" class="font-sans mono" font-size="11" fill="#34D399">Font: Inter Regular/Medium • Size: 15px • Line-Height: 24px</text>
      </g>

      <line x1="0" y1="440" x2="590" y2="440" stroke="rgba(255,255,255,0.06)"/>

      <!-- Caption & Badge -->
      <g transform="translate(0, 455)">
        <text x="0" y="16" class="font-sans" font-size="12" font-weight="700" fill="#34D399" letter-spacing="1">STATUS PILL &amp; CAPTION (12PX UPPERCASE)</text>
        <text x="0" y="36" class="font-sans mono" font-size="11" fill="#34D399">Font: Inter SemiBold • Size: 12px • Line-Height: 16px • Tracking: +0.06em</text>
      </g>

      <line x1="0" y1="510" x2="590" y2="510" stroke="rgba(255,255,255,0.06)"/>

      <!-- SPATIAL 8-POINT GRID SYSTEM -->
      <g transform="translate(0, 525)">
        <text x="0" y="18" class="font-sans" font-size="15" font-weight="700" fill="#F8FAFC">8-POINT SPATIAL GRID SYSTEM</text>
        <g transform="translate(0, 35)">
          <rect x="0" y="0" width="8" height="30" fill="#10B981"/>
          <text x="0" y="46" class="font-sans mono" font-size="9" fill="#94A3B8">8px</text>
          
          <rect x="24" y="0" width="16" height="30" fill="#10B981" opacity="0.9"/>
          <text x="24" y="46" class="font-sans mono" font-size="9" fill="#94A3B8">16px</text>
          
          <rect x="56" y="0" width="24" height="30" fill="#10B981" opacity="0.8"/>
          <text x="56" y="46" class="font-sans mono" font-size="9" fill="#94A3B8">24px</text>
          
          <rect x="96" y="0" width="32" height="30" fill="#10B981" opacity="0.7"/>
          <text x="96" y="46" class="font-sans mono" font-size="9" fill="#94A3B8">32px</text>
          
          <rect x="144" y="0" width="48" height="30" fill="#10B981" opacity="0.6"/>
          <text x="144" y="46" class="font-sans mono" font-size="9" fill="#94A3B8">48px</text>
          
          <rect x="208" y="0" width="64" height="30" fill="#10B981" opacity="0.5"/>
          <text x="208" y="46" class="font-sans mono" font-size="9" fill="#94A3B8">64px</text>

          <rect x="288" y="0" width="80" height="30" fill="#10B981" opacity="0.4"/>
          <text x="288" y="46" class="font-sans mono" font-size="9" fill="#94A3B8">80px (Margins)</text>
        </g>
      </g>
    </g>
  </g>
</svg>"""

with open("screenshots/03_color_and_typography_system.svg", "w") as f:
    f.write(s3)

print("Created screenshots/03_color_and_typography_system.svg")


# -------------------------------------------------------------
# 4. SCREENSHOT 04: Target Audience & Personas (1440 x 900)
# -------------------------------------------------------------
s4 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 900" width="1440" height="900">
  <defs>
    <linearGradient id="bgGrad4" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#080C0D"/>
      <stop offset="100%" stop-color="#0E151A"/>
    </linearGradient>
    <linearGradient id="pGrad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#10B981" stop-opacity="0.2"/>
      <stop offset="100%" stop-color="#059669" stop-opacity="0.05"/>
    </linearGradient>
    <linearGradient id="pGrad2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#06B6D4" stop-opacity="0.2"/>
      <stop offset="100%" stop-color="#3B82F6" stop-opacity="0.05"/>
    </linearGradient>
  </defs>

  <style>
    .font-sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Inter', sans-serif; }
    .mono { font-family: 'SF Mono', Consolas, 'Fira Code', monospace; }
  </style>

  <rect width="1440" height="900" fill="url(#bgGrad4)"/>

  <!-- Canvas Header -->
  <g transform="translate(60, 40)">
    <rect width="1320" height="70" rx="16" fill="rgba(255,255,255,0.03)" stroke="rgba(255,255,255,0.08)"/>
    <text x="30" y="35" class="font-sans" font-size="20" font-weight="800" fill="#F8FAFC">USER RESEARCH • TARGET AUDIENCE &amp; DETAILED PERSONAS</text>
    <text x="30" y="55" class="font-sans mono" font-size="12" fill="#34D399">Empathy Mapping • Core User Needs • Design Choices Alignment</text>
    <rect x="1150" y="20" width="140" height="30" rx="8" fill="rgba(16,185,129,0.15)" stroke="#10B981"/>
    <text x="1220" y="40" text-anchor="middle" class="font-sans" font-size="11" font-weight="700" fill="#34D399">USER INSIGHTS</text>
  </g>

  <!-- PERSONA 1: Maya Lin (Senior Product Designer) -->
  <g transform="translate(60, 140)">
    <rect width="640" height="710" rx="20" fill="url(#pGrad1)" stroke="rgba(16,185,129,0.3)" stroke-width="1.5"/>
    
    <g transform="translate(32, 32)">
      <!-- Avatar & Bio Header -->
      <circle cx="40" cy="40" r="40" fill="#047857" stroke="#34D399" stroke-width="2"/>
      <!-- Stylized face illustration -->
      <circle cx="40" cy="32" r="14" fill="#FDE68A"/>
      <path d="M 22 66 C 22 52 32 48 40 48 C 48 48 58 52 58 66 Z" fill="#10B981"/>
      <path d="M 26 28 C 26 16 38 12 48 16 C 54 20 54 28 54 28 Z" fill="#451A03"/>

      <!-- Name & Title -->
      <text x="100" y="30" class="font-sans" font-size="22" font-weight="800" fill="#F8FAFC">Maya Lin, 29</text>
      <text x="100" y="52" class="font-sans" font-size="14" font-weight="600" fill="#34D399">Senior Product Designer &amp; Design Lead</text>
      <text x="100" y="70" class="font-sans mono" font-size="11" fill="#94A3B8">Location: San Francisco, CA • Remote Workspace (10h/day)</text>

      <!-- Key Quote -->
      <g transform="translate(0, 100)">
        <rect width="576" height="54" rx="10" fill="rgba(0,0,0,0.3)" stroke="rgba(255,255,255,0.06)"/>
        <text x="16" y="32" class="font-sans" font-style="italic" font-size="13" fill="#E2E8F0">
          "I stare at Figma and dual 4K monitors all day. By 4 PM my eyes throb and indoor air feels stale."
        </text>
      </g>

      <!-- Goals & Motivations -->
      <g transform="translate(0, 175)">
        <text x="0" y="16" class="font-sans" font-size="14" font-weight="700" fill="#34D399">🎯 CORE GOALS &amp; WORKFLOW</text>
        <text x="0" y="40" class="font-sans" font-size="13" fill="#F8FAFC">• Eliminate evening blue-light eye strain without disturbing creative flow</text>
        <text x="0" y="64" class="font-sans" font-size="13" fill="#F8FAFC">• Maintain a minimalist, biophilic aesthetic that looks inspiring on camera</text>
        <text x="0" y="88" class="font-sans" font-size="13" fill="#F8FAFC">• Avoid hospital-like noisy air filters that vibrate or ruin podcast audio</text>
      </g>

      <!-- Pain Points -->
      <g transform="translate(0, 290)">
        <text x="0" y="16" class="font-sans" font-size="14" font-weight="700" fill="#EF4444">⚠️ USER PAIN POINTS</text>
        <text x="0" y="40" class="font-sans" font-size="13" fill="#CBD5E1">• High CO2 build-up causes mental fog around 3:30 PM</text>
        <text x="0" y="64" class="font-sans" font-size="13" fill="#CBD5E1">• Artificial overhead LED lighting destroys circadian sleep schedule</text>
        <text x="0" y="88" class="font-sans" font-size="13" fill="#CBD5E1">• Hates bulky plastic gadgets with annoying bright blue LEDs</text>
      </g>

      <!-- Design Choices Response -->
      <g transform="translate(0, 405)">
        <text x="0" y="16" class="font-sans" font-size="14" font-weight="700" fill="#F59E0B">💡 FIGMA DESIGN CHOICES FOR MAYA</text>
        <rect y="26" width="576" height="180" rx="12" fill="rgba(0,0,0,0.4)" stroke="rgba(245,158,11,0.2)"/>
        <text x="16" y="52" class="font-sans" font-size="12" font-weight="600" fill="#F59E0B">1. Dark Obsidian Canvas (#090D0E):</text>
        <text x="16" y="70" class="font-sans" font-size="12" fill="#94A3B8">Mimics her dark-themed design software, providing instant visual relief.</text>
        
        <text x="16" y="98" class="font-sans" font-size="12" font-weight="600" fill="#F59E0B">2. Hero Biophilic 3D Focus:</text>
        <text x="16" y="116" class="font-sans" font-size="12" fill="#94A3B8">Positions the living moss chamber front-and-center, appealing to her design taste.</text>

        <text x="16" y="144" class="font-sans" font-size="12" font-weight="600" fill="#F59E0B">3. Single-Click Pre-Order Auto Layout CTAs:</text>
        <text x="16" y="162" class="font-sans" font-size="12" fill="#94A3B8">High-contrast emerald buttons with clear hierarchy save cognitive effort.</text>
      </g>
    </g>
  </g>

  <!-- PERSONA 2: David Chen (Lead Infrastructure Engineer) -->
  <g transform="translate(740, 140)">
    <rect width="640" height="710" rx="20" fill="url(#pGrad2)" stroke="rgba(6,182,212,0.3)" stroke-width="1.5"/>
    
    <g transform="translate(32, 32)">
      <!-- Avatar & Bio Header -->
      <circle cx="40" cy="40" r="40" fill="#0E7490" stroke="#06B6D4" stroke-width="2"/>
      <circle cx="40" cy="32" r="14" fill="#FBCFE8"/>
      <path d="M 22 66 C 22 52 32 48 40 48 C 48 48 58 52 58 66 Z" fill="#0284C7"/>
      <!-- Glasses -->
      <rect x="29" y="28" width="10" height="8" rx="2" fill="none" stroke="#FFFFFF" stroke-width="1.5"/>
      <rect x="41" y="28" width="10" height="8" rx="2" fill="none" stroke="#FFFFFF" stroke-width="1.5"/>
      <line x1="39" y1="32" x2="41" y2="32" stroke="#FFFFFF" stroke-width="1.5"/>

      <!-- Name & Title -->
      <text x="100" y="30" class="font-sans" font-size="22" font-weight="800" fill="#F8FAFC">David Chen, 34</text>
      <text x="100" y="52" class="font-sans" font-size="14" font-weight="600" fill="#06B6D4">Lead Cloud Architect &amp; Bio-Hacker</text>
      <text x="100" y="70" class="font-sans mono" font-size="11" fill="#94A3B8">Location: Austin, TX • Smart Home Office • Metrics Obsessed</text>

      <!-- Key Quote -->
      <g transform="translate(0, 100)">
        <rect width="576" height="54" rx="10" fill="rgba(0,0,0,0.3)" stroke="rgba(255,255,255,0.06)"/>
        <text x="16" y="32" class="font-sans" font-style="italic" font-size="13" fill="#E2E8F0">
          "If I can't measure it via API or telemetry, it's snake oil. Show me the parts per million and decibels."
        </text>
      </g>

      <!-- Goals & Motivations -->
      <g transform="translate(0, 175)">
        <text x="0" y="16" class="font-sans" font-size="14" font-weight="700" fill="#06B6D4">🎯 CORE GOALS &amp; WORKFLOW</text>
        <text x="0" y="40" class="font-sans" font-size="13" fill="#F8FAFC">• Measure home office air quality (VOCs, CO2, PM2.5) with real telemetry</text>
        <text x="0" y="64" class="font-sans" font-size="13" fill="#F8FAFC">• Maximize deep coding sessions without cognitive slump</text>
        <text x="0" y="88" class="font-sans" font-size="13" fill="#F8FAFC">• Integrate workspace devices with Home Assistant / Apple HomeKit</text>
      </g>

      <!-- Pain Points -->
      <g transform="translate(0, 290)">
        <text x="0" y="16" class="font-sans" font-size="14" font-weight="700" fill="#EF4444">⚠️ USER PAIN POINTS</text>
        <text x="0" y="40" class="font-sans" font-size="13" fill="#CBD5E1">• High carbon dioxide concentration spikes past 1400 ppm unnoticed</text>
        <text x="0" y="64" class="font-sans" font-size="13" fill="#CBD5E1">• Purifier fan whine irritates his noise-canceling headphones</text>
        <text x="0" y="88" class="font-sans" font-size="13" fill="#CBD5E1">• Frustrated by marketing jargon that hides technical specifications</text>
      </g>

      <!-- Design Choices Response -->
      <g transform="translate(0, 405)">
        <text x="0" y="16" class="font-sans" font-size="14" font-weight="700" fill="#06B6D4">💡 FIGMA DESIGN CHOICES FOR DAVID</text>
        <rect y="26" width="576" height="180" rx="12" fill="rgba(0,0,0,0.4)" stroke="rgba(6,182,212,0.2)"/>
        <text x="16" y="52" class="font-sans" font-size="12" font-weight="600" fill="#06B6D4">1. Floating Live Telemetry HUD Widget:</text>
        <text x="16" y="70" class="font-sans" font-size="12" fill="#94A3B8">Presents instant real-time data (99.8 AQI, &lt;18dB, 1800K) right in hero.</text>
        
        <text x="16" y="98" class="font-sans" font-size="12" font-weight="600" fill="#06B6D4">2. SensorIQ™ Dedicated Feature Card:</text>
        <text x="16" y="116" class="font-sans" font-size="12" fill="#94A3B8">Highlights 500ms multi-gas spectrometry and open API integration.</text>

        <text x="16" y="144" class="font-sans" font-size="12" font-weight="600" fill="#06B6D4">3. Quantitative Metrics Ticker in Hero:</text>
        <text x="16" y="162" class="font-sans" font-size="12" fill="#94A3B8">Delivers verifiable proof points immediately above the fold.</text>
      </g>
    </g>
  </g>
</svg>"""

with open("screenshots/04_user_personas_and_target_audience.svg", "w") as f:
    f.write(s4)

print("Created screenshots/04_user_personas_and_target_audience.svg")


# -------------------------------------------------------------
# 5. SCREENSHOT 05: Responsive Viewports Mockup (1440 x 900)
# -------------------------------------------------------------
s5 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 900" width="1440" height="900">
  <defs>
    <linearGradient id="bgGrad5" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#070A0B"/>
      <stop offset="100%" stop-color="#0E1418"/>
    </linearGradient>
    <linearGradient id="btnGlow5" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#10B981"/>
      <stop offset="100%" stop-color="#059669"/>
    </linearGradient>
    <filter id="mShadow" x="-10%" y="-10%" width="120%" height="130%">
      <feDropShadow dx="0" dy="20" stdDeviation="24" flood-color="#000000" flood-opacity="0.6"/>
    </filter>
  </defs>

  <style>
    .font-sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Inter', sans-serif; }
    .mono { font-family: 'SF Mono', Consolas, 'Fira Code', monospace; }
  </style>

  <rect width="1440" height="900" fill="url(#bgGrad5)"/>

  <!-- Canvas Header -->
  <g transform="translate(60, 40)">
    <rect width="1320" height="70" rx="16" fill="rgba(255,255,255,0.03)" stroke="rgba(255,255,255,0.08)"/>
    <text x="30" y="35" class="font-sans" font-size="20" font-weight="800" fill="#F8FAFC">RESPONSIVE DESIGN BREAKDOWN • DESKTOP / TABLET / MOBILE</text>
    <text x="30" y="55" class="font-sans mono" font-size="12" fill="#34D399">Figma Auto Layout Flex Reflow • 1440px / 768px / 375px Constraints</text>
    <rect x="1150" y="20" width="140" height="30" rx="8" fill="rgba(16,185,129,0.15)" stroke="#10B981"/>
    <text x="1220" y="40" text-anchor="middle" class="font-sans" font-size="11" font-weight="700" fill="#34D399">RESPONSIVE V1</text>
  </g>

  <!-- VIEWPORT 1: Desktop Frame (1440px Scaled) -->
  <g transform="translate(60, 140)">
    <rect width="520" height="700" rx="16" fill="#0D1316" stroke="rgba(255,255,255,0.1)" stroke-width="1.5" filter="url(#mShadow)"/>
    
    <!-- Header bar -->
    <rect width="520" height="36" rx="16" fill="#151E22"/>
    <circle cx="20" cy="18" r="4.5" fill="#EF4444"/>
    <circle cx="34" cy="18" r="4.5" fill="#F59E0B"/>
    <circle cx="48" cy="18" r="4.5" fill="#10B981"/>
    <text x="260" y="23" text-anchor="middle" class="font-sans mono" font-size="11" fill="#94A3B8">Desktop Frame (1440px Viewport)</text>

    <!-- Content Preview inside Desktop Mockup -->
    <g transform="translate(24, 56)">
      <!-- Navbar -->
      <rect width="472" height="40" rx="10" fill="rgba(255,255,255,0.05)"/>
      <text x="16" y="25" class="font-sans" font-size="12" font-weight="800" fill="#FFFFFF">🌿 AERO<tspan fill="#34D399">BIOME</tspan></text>
      <rect x="380" y="8" width="76" height="24" rx="6" fill="url(#btnGlow5)"/>
      <text x="418" y="24" text-anchor="middle" class="font-sans" font-size="10" font-weight="700" fill="#FFFFFF">Pre-Order</text>

      <!-- Hero 2-Column Layout -->
      <g transform="translate(0, 60)">
        <!-- Left Text -->
        <rect width="110" height="18" rx="9" fill="rgba(16,185,129,0.15)"/>
        <text x="10" y="13" class="font-sans" font-size="8" font-weight="700" fill="#34D399">BIO-RESPONSIVE</text>
        <text x="0" y="44" class="font-sans" font-size="20" font-weight="800" fill="#FFFFFF">Pure Air. Moss.</text>
        <text x="0" y="68" class="font-sans" font-size="20" font-weight="800" fill="#34D399">Circadian Sync.</text>
        <rect y="82" width="220" height="6" rx="3" fill="#64748B"/>
        <rect y="94" width="180" height="6" rx="3" fill="#64748B"/>
        <rect y="112" width="110" height="28" rx="8" fill="url(#btnGlow5)"/>

        <!-- Right Visual Mockup -->
        <rect x="250" y="0" width="220" height="160" rx="14" fill="rgba(16,185,129,0.08)" stroke="rgba(52,211,153,0.3)"/>
        <circle cx="360" cy="80" r="45" fill="#047857"/>
        <ellipse cx="360" cy="40" rx="35" ry="10" fill="#34D399" opacity="0.6"/>
      </g>

      <!-- 3 Feature Cards Horizontal Row -->
      <g transform="translate(0, 240)">
        <text x="0" y="20" class="font-sans" font-size="13" font-weight="700" fill="#F8FAFC">Engineered for Peak Cognitive Flow</text>
        <g transform="translate(0, 36)">
          <rect width="148" height="140" rx="12" fill="rgba(255,255,255,0.03)" stroke="rgba(255,255,255,0.08)"/>
          <circle cx="24" cy="24" r="10" fill="#10B981"/>
          <text x="14" y="54" class="font-sans" font-size="10" font-weight="700" fill="#FFFFFF">Bio-Filter Matrix</text>
          <rect x="14" y="66" width="120" height="4" rx="2" fill="#64748B"/>
          <rect x="14" y="76" width="90" height="4" rx="2" fill="#64748B"/>

          <rect x="162" y="0" width="148" height="140" rx="12" fill="rgba(255,255,255,0.03)" stroke="#10B981"/>
          <circle cx="186" cy="24" r="10" fill="#F59E0B"/>
          <text x="176" y="54" class="font-sans" font-size="10" font-weight="700" fill="#FFFFFF">Circadian Halo</text>
          <rect x="176" y="66" width="120" height="4" rx="2" fill="#64748B"/>
          <rect x="176" y="76" width="90" height="4" rx="2" fill="#64748B"/>

          <rect x="324" y="0" width="148" height="140" rx="12" fill="rgba(255,255,255,0.03)" stroke="rgba(255,255,255,0.08)"/>
          <circle cx="348" cy="24" r="10" fill="#06B6D4"/>
          <text x="338" y="54" class="font-sans" font-size="10" font-weight="700" fill="#FFFFFF">SensoriIQ Mesh</text>
          <rect x="338" y="66" width="120" height="4" rx="2" fill="#64748B"/>
          <rect x="338" y="76" width="90" height="4" rx="2" fill="#64748B"/>
        </g>
      </g>

      <!-- Footer preview -->
      <g transform="translate(0, 440)">
        <rect width="472" height="70" rx="10" fill="rgba(0,0,0,0.3)"/>
        <text x="16" y="28" class="font-sans" font-size="10" font-weight="700" fill="#FFFFFF">🌿 AeroBiome Inc.</text>
        <text x="16" y="48" class="font-sans" font-size="9" fill="#64748B">© 2026 Biome Tech. 12-Col Desktop Auto Layout Grid.</text>
      </g>
    </g>

    <!-- Auto layout tag -->
    <rect x="24" y="650" width="472" height="30" rx="6" fill="rgba(16,185,129,0.1)"/>
    <text x="260" y="670" text-anchor="middle" class="font-sans mono" font-size="11" font-weight="600" fill="#34D399">Auto Layout: Horizontal Dual-Column + 3-Card Row</text>
  </g>

  <!-- VIEWPORT 2: Tablet Frame (768px Scaled) -->
  <g transform="translate(620, 140)">
    <rect width="400" height="700" rx="16" fill="#0D1316" stroke="rgba(255,255,255,0.1)" stroke-width="1.5" filter="url(#mShadow)"/>
    <rect width="400" height="36" rx="16" fill="#151E22"/>
    <circle cx="20" cy="18" r="4.5" fill="#EF4444"/>
    <circle cx="34" cy="18" r="4.5" fill="#F59E0B"/>
    <circle cx="48" cy="18" r="4.5" fill="#10B981"/>
    <text x="200" y="23" text-anchor="middle" class="font-sans mono" font-size="11" fill="#94A3B8">Tablet Frame (768px Viewport)</text>

    <!-- Tablet Content (Stacked Auto Layout) -->
    <g transform="translate(20, 56)">
      <rect width="360" height="40" rx="10" fill="rgba(255,255,255,0.05)"/>
      <text x="16" y="25" class="font-sans" font-size="12" font-weight="800" fill="#FFFFFF">🌿 AERO<tspan fill="#34D399">BIOME</tspan></text>
      <rect x="270" y="8" width="76" height="24" rx="6" fill="url(#btnGlow5)"/>
      <text x="308" y="24" text-anchor="middle" class="font-sans" font-size="10" font-weight="700" fill="#FFFFFF">Pre-Order</text>

      <!-- Center Aligned Hero -->
      <g transform="translate(0, 55)">
        <rect x="125" y="0" width="110" height="18" rx="9" fill="rgba(16,185,129,0.15)"/>
        <text x="180" y="13" text-anchor="middle" class="font-sans" font-size="8" font-weight="700" fill="#34D399">BIO-RESPONSIVE</text>
        <text x="180" y="42" text-anchor="middle" class="font-sans" font-size="18" font-weight="800" fill="#FFFFFF">Pure Air. Living Moss.</text>
        <text x="180" y="64" text-anchor="middle" class="font-sans" font-size="18" font-weight="800" fill="#34D399">Circadian Harmony.</text>
        <rect x="40" y="78" width="280" height="5" rx="2.5" fill="#64748B"/>
        <rect x="70" y="88" width="220" height="5" rx="2.5" fill="#64748B"/>

        <!-- Centered Pod Mockup -->
        <rect x="80" y="105" width="200" height="130" rx="12" fill="rgba(16,185,129,0.08)" stroke="rgba(52,211,153,0.3)"/>
        <circle cx="180" cy="170" r="35" fill="#047857"/>
      </g>

      <!-- 2-Column Wrapped Feature Cards -->
      <g transform="translate(0, 310)">
        <rect width="172" height="110" rx="10" fill="rgba(255,255,255,0.03)" stroke="rgba(255,255,255,0.08)"/>
        <text x="12" y="32" class="font-sans" font-size="10" font-weight="700" fill="#FFFFFF">Bio-Filter Matrix</text>
        <rect x="12" y="44" width="140" height="4" rx="2" fill="#64748B"/>

        <rect x="188" y="0" width="172" height="110" rx="10" fill="rgba(255,255,255,0.03)" stroke="#10B981"/>
        <text x="200" y="32" class="font-sans" font-size="10" font-weight="700" fill="#FFFFFF">Circadian Halo</text>
        <rect x="200" y="44" width="140" height="4" rx="2" fill="#64748B"/>

        <!-- 3rd Card Spanning Width -->
        <rect x="0" y="122" width="360" height="80" rx="10" fill="rgba(255,255,255,0.03)" stroke="rgba(255,255,255,0.08)"/>
        <text x="16" y="30" class="font-sans" font-size="10" font-weight="700" fill="#FFFFFF">SensoriIQ™ Real-Time Mesh</text>
        <rect x="16" y="42" width="280" height="4" rx="2" fill="#64748B"/>
      </g>
    </g>

    <rect x="20" y="650" width="360" height="30" rx="6" fill="rgba(16,185,129,0.1)"/>
    <text x="200" y="670" text-anchor="middle" class="font-sans mono" font-size="11" font-weight="600" fill="#34D399">Auto Layout: Wrap Flow • 8-Col Grid</text>
  </g>

  <!-- VIEWPORT 3: Mobile Phone Frame (375px Scaled) -->
  <g transform="translate(1060, 140)">
    <rect width="320" height="700" rx="36" fill="#0D1316" stroke="rgba(255,255,255,0.18)" stroke-width="2" filter="url(#mShadow)"/>
    
    <!-- Phone Notch / Dynamic Island -->
    <rect x="110" y="12" width="100" height="20" rx="10" fill="#000000"/>
    <circle cx="190" cy="22" r="3" fill="#1E293B"/>

    <!-- Mobile Screen Contents -->
    <g transform="translate(16, 48)">
      <!-- Mobile Sticky Header with Hamburger -->
      <rect width="288" height="38" rx="10" fill="rgba(255,255,255,0.05)"/>
      <text x="12" y="24" class="font-sans" font-size="12" font-weight="800" fill="#FFFFFF">🌿 AERO<tspan fill="#34D399">BIOME</tspan></text>
      <!-- Hamburger Icon -->
      <line x1="255" y1="14" x2="273" y2="14" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round"/>
      <line x1="255" y1="19" x2="273" y2="19" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round"/>
      <line x1="255" y1="24" x2="273" y2="24" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round"/>

      <!-- Mobile Hero Stack (Vertical Direction) -->
      <g transform="translate(0, 48)">
        <rect width="120" height="16" rx="8" fill="rgba(16,185,129,0.15)"/>
        <text x="10" y="12" class="font-sans" font-size="7.5" font-weight="700" fill="#34D399">BIO-RESPONSIVE</text>
        <text x="0" y="38" class="font-sans" font-size="17" font-weight="800" fill="#FFFFFF">Pure Air. Moss.</text>
        <text x="0" y="58" class="font-sans" font-size="17" font-weight="800" fill="#34D399">Circadian Sync.</text>
        <rect y="70" width="280" height="4" rx="2" fill="#64748B"/>
        <rect y="78" width="220" height="4" rx="2" fill="#64748B"/>

        <!-- Mobile CTA Full Width (Auto Layout Fill Container) -->
        <rect y="92" width="288" height="36" rx="10" fill="url(#btnGlow5)"/>
        <text x="144" y="115" text-anchor="middle" class="font-sans" font-size="11" font-weight="700" fill="#FFFFFF">Order Genesis Pod →</text>

        <!-- Product Image Preview -->
        <rect y="140" width="288" height="120" rx="12" fill="rgba(16,185,129,0.08)" stroke="rgba(52,211,153,0.3)"/>
        <circle cx="144" cy="200" r="32" fill="#047857"/>
      </g>

      <!-- Stacked Mobile Feature Cards (Auto Layout Vertical, 1-Col) -->
      <g transform="translate(0, 330)">
        <rect width="288" height="74" rx="10" fill="rgba(255,255,255,0.03)" stroke="rgba(255,255,255,0.08)"/>
        <text x="12" y="24" class="font-sans" font-size="11" font-weight="700" fill="#FFFFFF">🌿 Bio-Filter Matrix</text>
        <text x="12" y="42" class="font-sans" font-size="9" fill="#94A3B8">Living moss captures PM2.5</text>
        <text x="12" y="58" class="font-sans" font-size="9" font-weight="600" fill="#34D399">Zero filter replacement →</text>

        <rect y="84" width="288" height="74" rx="10" fill="rgba(255,255,255,0.03)" stroke="#10B981"/>
        <text x="12" y="108" class="font-sans" font-size="11" font-weight="700" fill="#FFFFFF">☀️ Circadian Halo</text>
        <text x="12" y="126" class="font-sans" font-size="9" fill="#94A3B8">1800K - 6500K spectral light</text>
        <text x="12" y="142" class="font-sans" font-size="9" font-weight="600" fill="#F59E0B">Melatonin sync active →</text>

        <rect y="168" width="288" height="74" rx="10" fill="rgba(255,255,255,0.03)" stroke="rgba(255,255,255,0.08)"/>
        <text x="12" y="192" class="font-sans" font-size="11" font-weight="700" fill="#FFFFFF">📡 SensoriIQ™ Mesh</text>
        <text x="12" y="210" class="font-sans" font-size="9" fill="#94A3B8">Real-time eCO2 and VOC radar</text>
        <text x="12" y="226" class="font-sans" font-size="9" font-weight="600" fill="#06B6D4">500ms sensor telemetry →</text>
      </g>
    </g>

    <!-- Home indicator line -->
    <rect x="110" y="682" width="100" height="4" rx="2" fill="#FFFFFF" opacity="0.4"/>

    <rect x="16" y="630" width="288" height="26" rx="6" fill="rgba(16,185,129,0.1)"/>
    <text x="160" y="647" text-anchor="middle" class="font-sans mono" font-size="9.5" font-weight="600" fill="#34D399">Vertical Stack • Fill Container (375px)</text>
  </g>
</svg>"""

with open("screenshots/05_responsive_viewports_mockup.svg", "w") as f:
    f.write(s5)

print("Created screenshots/05_responsive_viewports_mockup.svg")
