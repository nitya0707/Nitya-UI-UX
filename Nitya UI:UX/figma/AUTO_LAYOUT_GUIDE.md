# 📐 Step-by-Step Figma Auto Layout Guide

This guide walks you through replicating the **AeroBiome Landing Page** in Figma using 100% native **Auto Layout** (Keyboard Shortcut: `Shift + A`).

---

## 1. Frame Hierarchy & Tree Structure

```text
❖ Desktop Frame (1440 x Auto) [Auto Layout Vertical, Gap: 0, Align: Center]
  ├── [Auto Layout Horizontal, Fill W, Hug H] Announcement Banner
  ├── [Auto Layout Horizontal, Max W: 1280, Hug H] Header Container
  │     └── ❖ Component: Navigation / Header
  │           ├── Logo Lockup [Auto Layout Horizontal, Gap: 12, Hug]
  │           ├── Navigation Links [Auto Layout Horizontal, Gap: 32, Hug]
  │           └── Action Container [Auto Layout Horizontal, Gap: 16, Hug]
  ├── [Auto Layout Vertical, Max W: 1280, Gap: 64, Pad: 64 32] Hero Section
  │     └── [Auto Layout Horizontal, Fill W, Gap: 64, Align: Center] Hero Row
  │           ├── Hero Content Left [Auto Layout Vertical, Gap: 24, Fill W]
  │           │     ├── Status Pill [Auto Layout Horizontal, Gap: 8, Hug]
  │           │     ├── Headline Text [Fill W]
  │           │     ├── Paragraph Body [Fill W]
  │           │     ├── CTA Button Row [Auto Layout Horizontal, Gap: 16, Hug]
  │           │     │     ├── ❖ Master Button (Primary)
  │           │     │     └── ❖ Master Button (Secondary Glass)
  │           │     └── Metrics Row [Auto Layout Horizontal, Gap: 24, Fill W]
  │           └── Hero Visual Right [Auto Layout Vertical, Gap: 16, Fill W]
  │                 └── Visual Card with Embedded Image + HUD Widgets
  ├── [Auto Layout Vertical, Max W: 1280, Gap: 48, Pad: 80 32] Feature Section
  │     ├── Section Header Row [Auto Layout Horizontal, Space Between, Fill W]
  │     └── Feature Cards Grid [Auto Layout Horizontal, Gap: 32, Fill W]
  │           ├── ❖ Master Feature Card (Instance 1: Bio-Filter Matrix) [Fill W]
  │           ├── ❖ Master Feature Card (Instance 2: Circadian Halo - Highlighted) [Fill W]
  │           └── ❖ Master Feature Card (Instance 3: SensoriIQ Mesh) [Fill W]
  └── [Auto Layout Vertical, Fill W, Pad: 64 80] Footer
        └── [Auto Layout Horizontal, Space Between, Fill W] Footer Columns
```

---

## 2. Key Auto Layout Rules Cheat Sheet

| Container | Direction | Alignment | Spacing / Gap | Padding | Horizontal Resizing | Vertical Resizing |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Main Page Canvas** | Vertical (↓) | Center | `0px` | `0px` | Fixed (`1440px`) | `Hug contents` |
| **Section Wrapper** | Vertical (↓) | Center | `48px` | `64px Top/Bottom, 80px Left/Right` | `Fill container` | `Hug contents` |
| **Header Pill** | Horizontal (→)| Center | Space-between | `12px Top/Bottom, 24px Left/Right` | `Fill container` (Max: 1280px) | `Hug contents` |
| **Button / Master** | Horizontal (→)| Center | `8px` | `14px Top/Bottom, 28px Left/Right` | `Hug contents` | Fixed (`52px`) |
| **Feature Card** | Vertical (↓) | Top-Left | `20px` | `32px all sides` | `Fill container` | `Hug contents` |
| **Status Pill** | Horizontal (→)| Center | `6px` | `6px Top/Bottom, 14px Left/Right` | `Hug contents` | `Hug contents` |

---

## 3. How to Create the Components in Figma

### A. Creating Component 1: `Button / Master`
1. Press `T` and type your button text: `Order Genesis Pod`. Apply text style `Body/Medium` (15px, Bold).
2. Draw or import a 16x16 arrow icon.
3. Select both text and icon, press `Shift + A` to turn into an Auto Layout frame.
4. Set **Direction** to `Horizontal`, **Gap** to `8px`, **Alignment** to `Center`.
5. Set **Padding**: `Top/Bottom: 14px`, `Left/Right: 28px`.
6. Add **Fill**: Linear Gradient (`#10B981` to `#059669`).
7. Set **Corner Radius** to `14px`.
8. Right click and select **Create Component** (or `Cmd + Option + K`).
9. Add **Variants**:
   - `Type = Primary` (Emerald gradient)
   - `Type = Secondary` (Fill `rgba(255,255,255,0.06)`, Stroke `1px rgba(255,255,255,0.15)`)
   - `Type = Ghost` (No fill, stroke `none`, text color `#34D399`)

### B. Creating Component 2: `Card / FeatureCard`
1. Create a 48x48 icon frame (Auto Layout Center, Corner Radius `14px`).
2. Create an H2 title layer: `Living Bio-Filter Matrix` (Resizing: `Fill container`).
3. Create a body paragraph layer: `Stabilized micro-moss culture...` (Resizing: `Fill container`).
4. Create a checklist stack (Auto Layout Vertical, Gap: 8px).
5. Select all elements and press `Shift + A`.
6. Set **Padding** to `32px` all sides, **Gap** to `20px`.
7. Add **Fill**: `#10161A` (Opacity 80%), **Stroke**: `1px rgba(255,255,255,0.08)`, **Corner Radius**: `20px`.
8. Add an **Effect**: `Drop Shadow` (Y: 20, Blur: 24, Opacity: 50%).
9. Make it a Component and define the **Highlighted Variant** with an emerald border (`#10B981`, 1.5px) and ambient glow.

### C. Creating Component 3: `Navigation / Header`
1. Create the brand logo lockup (Icon + `AEROBIOME` text).
2. Create a row of navigation links with `Shift + A`, Gap: `32px`.
3. Place an instance of `Button / Master` (Small: 36px).
4. Select logo, links, and button, press `Shift + A`.
5. Change spacing mode to `Space between` (or set the middle links frame to `Auto`).
6. Set **Padding**: `12px 24px`, **Corner Radius**: `20px`.
7. Set **Fill**: `rgba(16,22,26,0.75)`, add **Background Blur**: `20px`.
