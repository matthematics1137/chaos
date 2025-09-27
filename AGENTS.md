# Agent Notes for Chaos Simulations

This repo hosts a lightweight, dependency‑free GitHub Pages site that visualizes nonlinear dynamics and chaos. When contributing or extending simulations, follow the conventions below.

## Aesthetic & Format
- Layout
  - Use a centered, responsive column with `max-width: 1200px;` and `padding: 2rem;` on a neutral background.
  - Each page uses a grid layout with optional note bubbles at the top, left, right, and bottom.
  - For multi‑view pages, use tabs (rounded pill buttons) and keep the content in `.panel` sections.
- Panels
  - White background, subtle border, light shadow: `border: 1px solid #e0e0e0; border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.04);`
  - Controls are grouped in a flex row with small gaps. Use semantic labels and compact inputs.
- Canvases
  - Prefer sizes around 1000×700 for clarity (`width`/`height` attributes on `<canvas>`).
  - Subtle background gradients are OK; include a 20px margin frame (`strokeRect`) when helpful.
  - Prefer progressive rendering (chunked drawing via `requestAnimationFrame`) for heavy plots.
- Notes
  - Use “note bubbles” for author annotations: `.note-bubble.note-top|left|right|bottom`.
  - For tabbed pages, provide per‑tab note bubbles with `data-tab="panel-<id>"` and a default fallback set.
  - Keep note text in HTML (non‑editable by visitors) so the author can curate explanations.
- Interactions
  - Provide Pause/Reset/Clear on interactive canvases.
  - Reset should restore default parameters, clear the canvas/trails, and resume.
  - Clear should only clear the canvas (keep parameters/state unless otherwise documented).
  - Prefer simple, performant vanilla JS; avoid external dependencies.

## Structure & Files
- `index.html` — landing page linking all simulations.
- `pages/` — individual simulation pages (consistent styles/controls/notes).
- `animations/` — static media (legacy GIFs, etc.).
- `functions/` — offline scripts used to generate assets.
- `ROADMAP.md` — authoritative checklist aligned to Strogatz’s topics.

## Roadmap
- Maintain the checklist in `ROADMAP.md`; check off items as pages are added.
- Group new simulations under the closest section (e.g., One‑Dimensional Maps, Strange Attractors).
- When adding multi‑view content to an existing page (e.g., Logistic: Cobweb/Bifurcation/Lyapunov), implement tabs and per‑tab notes.

## Code Style
- Vanilla ES6+, no build steps.
- Keep functions small and focused; prefer pure math helpers.
- Use progressive rendering and input `input/change` handlers for responsiveness.
- Keep colors consistent: primary `#0366d6`, complementary reds `#ef4444`, muted grays for axes.

