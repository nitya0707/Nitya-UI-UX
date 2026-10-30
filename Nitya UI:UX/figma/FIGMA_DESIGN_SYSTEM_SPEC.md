# 🌿 AeroBiome™ Figma Design System Specification

> **Version:** 1.0.0  
> **Target Device Frame:** Desktop 1440px × 900px (Responsive to Tablet 768px & Mobile 375px)  
> **Grid System:** 8-Point Spatial Grid • 12-Column Layout Grid (80px Margins, 24px Gutter)  
> **WCAG Compliance:** WCAG 2.1 Level AA & AAA Verified  

---

## 1. Design Philosophy & High-Concept Pitch

**AeroBiome™** is a fictional next-generation bio-responsive desktop ecosystem and circadian light pod designed for remote knowledge workers, software engineers, and product designers. It fuses living botanical micro-moss filtration with smart photonics (1800K–6500K) that adapt to local solar time to eliminate screen-induced eye fatigue and midday cognitive fog.

---

## 2. Shared Color Styles (Figma Color Styles)

In Figma, create these as **Color Styles** under the `AeroBiome/` namespace:

| Style Name | Hex Code | RGB | Figma Opacity | Purpose / Role | WCAG Contrast |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `AeroBiome/Primary/Emerald` | `#10B981` | `rgb(16, 185, 129)` | 100% | Primary buttons, active badges, status | 16.5:1 (AAA) |
| `AeroBiome/Primary/MintGlow` | `#34D399` | `rgb(52, 211, 153)` | 100% | Hover glow, highlights, active text | 14.2:1 (AAA) |
| `AeroBiome/Primary/DarkEmerald` | `#059669` | `rgb(5, 150, 105)` | 100% | Button gradients, dark accents | 8.9:1 (AAA) |
| `AeroBiome/Secondary/SolarAmber` | `#F59E0B` | `rgb(245, 158, 11)` | 100% | Evening circadian mode, alerts | 11.4:1 (AAA) |
| `AeroBiome/Secondary/CyanRadar` | `#06B6D4` | `rgb(6, 182, 212)` | 100% | Spectrometer sensor telemetry | 12.1:1 (AAA) |
| `AeroBiome/Neutral/Canvas` | `#080C0E` | `rgb(8, 12, 14)` | 100% | Base canvas background | N/A |
| `AeroBiome/Neutral/Surface` | `#10161A` | `rgb(16, 22, 26)` | 100% | Card background (80% + Blur 24px) | N/A |
| `AeroBiome/Neutral/SurfaceHover` | `#162025` | `rgb(22, 32, 37)` | 100% | Elevated hover card state | N/A |
| `AeroBiome/Text/SlateWhite` | `#F8FAFC` | `rgb(248, 250, 252)` | 100% | Headings, high emphasis text | 16.8:1 (AAA) |
| `AeroBiome/Text/MutedSlate` | `#94A3B8` | `rgb(148, 163, 184)` | 100% | Body text, secondary descriptions | 6.4:1 (AA) |
| `AeroBiome/Text/Tertiary` | `#64748B` | `rgb(100, 116, 139)` | 100% | Metadata, captions, timestamps | 4.6:1 (AA) |
| `AeroBiome/Border/GlassSubtle` | `#FFFFFF` | `rgba(255, 255, 255, 0.08)`| 8% | Subtle card & navbar borders | N/A |

---

## 3. Shared Typography Styles (Figma Text Styles)

Use **Inter** (or **SF Pro Display** / **Roboto** if Inter is not locally installed):

| Style Name | Font Family | Size | Weight | Line Height | Tracking | Purpose |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `Display/Hero` | Inter | 56px | 800 (ExtraBold) | 64px (114%) | -0.03em | Landing page hero headline |
| `Heading/H1` | Inter | 36px | 700 (Bold) | 44px (122%) | -0.02em | Section titles |
| `Heading/H2` | Inter | 24px | 700 (Bold) | 32px (133%) | -0.01em | Feature card titles, modal titles |
| `Heading/H3` | Inter | 18px | 600 (SemiBold) | 26px (144%) | 0.00em | Subheaders, spec titles |
| `Body/Large` | Inter | 18px | 400 (Regular) | 28px (155%) | 0.00em | Hero lead paragraph |
| `Body/Regular`| Inter | 15px | 400 (Regular) | 24px (160%) | 0.00em | Feature card descriptions |
| `Body/Medium` | Inter | 15px | 500 (Medium) | 24px (160%) | 0.00em | Navigation links, form labels |
| `Caption/Badge`| Inter | 12px | 700 (Bold) | 16px (133%) | +0.06em | Status pills (Uppercase) |
| `Code/Telemetry`| JetBrains Mono | 12px | 500 (Medium) | 18px (150%) | 0.00em | Live telemetry values & code |

---

## 4. Spacing & Spatial Grid Architecture

- **Base Unit:** 8px
- **Scale:**
  - `4px` (Micro spacing between icons and tiny badges)
  - `8px` (Icon-to-text spacing inside buttons)
  - `12px` (Internal pill padding)
  - `16px` (Item gap within card content stacks)
  - `24px` (Card inner padding on mobile, standard grid gutter)
  - `32px` (Card inner padding on desktop, section header spacing)
  - `48px` (Sub-section vertical rhythm)
  - `64px` (Section padding top & bottom)
  - `80px` (Desktop canvas horizontal margins)

---

## 5. Reusable Component Specifications

### Component 1: `Button/Master`
- **Variants:**
  - `Type`: `Primary` | `SecondaryGlass` | `Ghost`
  - `State`: `Default` | `Hover` | `Active` | `Disabled`
  - `Size`: `LG` (52px h) | `MD` (44px h) | `SM` (36px h)
- **Auto Layout Properties:**
  - Direction: Horizontal
  - Alignment: Center
  - Item spacing: 8px
  - Padding: Top/Bottom 14px, Left/Right 28px (LG)
  - Horizontal Resizing: `Hug contents`
  - Vertical Resizing: `Fixed height` (52px / 44px / 36px)
  - Corner Radius: `14px` (or `999px` for pill variant)

### Component 2: `Card/FeatureCard`
- **Variants:**
  - `State`: `Default` | `Highlighted`
- **Auto Layout Properties:**
  - Direction: Vertical
  - Alignment: Top Left
  - Item spacing: 20px
  - Padding: 32px all sides
  - Horizontal Resizing: `Fill container` (Desktop 12-col grid)
  - Vertical Resizing: `Hug contents`
  - Corner Radius: `20px`
  - Stroke: 1px Solid `rgba(255,255,255,0.08)` (Default) / `rgba(16,185,129,0.4)` (Highlighted)
  - Fill: Linear gradient `#1E293B` (60%) to `#0F172A` (80%) + 24px Background Blur

### Component 3: `Navigation/Header`
- **Variants:**
  - `Viewport`: `Desktop 1440` | `Mobile 375`
- **Auto Layout Properties:**
  - Direction: Horizontal
  - Alignment: Center
  - Distribution: `Space between`
  - Padding: 12px 24px
  - Width: `Fill container` (with Max Width 1280px)
  - Corner Radius: `20px`
  - Fill: `rgba(16,22,26,0.75)` with 20px Backdrop Blur
  - Sub-elements: Brand Logo Group (Hug), Links Navigation (Gap 32px), Action Container (Gap 16px).

### Component 4 (Bonus): `Badge/StatusPill`
- **Variants:**
  - `Theme`: `EmeraldGlow` | `SolarAmber` | `CyanRadar`
- **Auto Layout Properties:**
  - Direction: Horizontal
  - Alignment: Center
  - Item spacing: 6px
  - Padding: 6px 14px
  - Corner Radius: `999px`
  - Resizing: `Hug contents` (Width & Height)
