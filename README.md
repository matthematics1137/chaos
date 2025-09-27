# Chaos Simulations

[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-live-brightgreen?logo=github)](https://matthematics1137.github.io/chaos/)
![Last Commit](https://img.shields.io/github/last-commit/matthematics1137/chaos)
![Made with JavaScript](https://img.shields.io/badge/JS-Vanilla%20ES6%2B-yellow?logo=javascript)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)

Interactive visualizations of nonlinear dynamics and chaos, inspired by Steven Strogatz’s Nonlinear Dynamics and Chaos. The project showcases approachable, high‑quality simulations that invite exploration and learning.

Live site: https://matthematics1137.github.io/chaos/

## Highlights

- Clean, focused landing page with context and links
- Four interactive simulations with consistent UX
- Progressive rendering and rich visuals for clarity
- Built with lightweight, dependency‑free HTML5 Canvas and vanilla JS

## Simulations

- Logistic Map — Cobweb + Bifurcation
  - Cobweb diagram with r/x₀ controls and iteration count
  - Bifurcation diagram with progressive drawing, y‑zoom, and color modes
  - Page: `pages/logistic_map.html`

- Lorenz Attractor — Strange Attractor
  - RK4 integration with rotating 3D projection and parameter controls
  - Play/Pause/Reset/Clear; color varies by depth for visual depth cues
  - Page: `pages/lorenz.html`

- Double Pendulum — Chaotic Motion
  - RK4 animation with gradient rods, shaded bobs, and a fading trail
  - Angle/velocity inputs; Play/Pause/Reset/Clear
  - Page: `pages/double_pendulum.html`

- Runge–Kutta Playground — Phase Plane
  - Systems: SHO, Van der Pol (μ), Lotka–Volterra
  - Methods: RK4, Euler; optional Euler overlay for comparison
  - Vector field, seed presets (ring/grid/random), click to add seeds
  - Page: `pages/animation.html`

## Notes and Annotations

Each simulation page reserves space for author notes in top, bottom, and side “note bubble” areas. These are regular HTML blocks intended for concise explanations, derivations, or teaching commentary. Edit the placeholder text directly in the HTML files to publish your notes.

## Project Structure

- `index.html` — Site landing page
- `pages/` — Individual simulations and animations
  - `animation.html` — Runge–Kutta playground (interactive)
  - `logistic_map.html` — Logistic cobweb + bifurcation
  - `lorenz.html` — Lorenz attractor
  - `double_pendulum.html` — Double pendulum
- `animations/` — Static media assets (e.g., legacy GIFs)
- `functions/` — Supporting scripts and notebooks used to generate assets

## Roadmap

- Presets and snapshots for common parameter regimes
- Export images/animations and shareable links with parameters in the URL
- Additional systems: Duffing oscillator, Henon map, Standard map
- Accessibility and mobile interaction improvements

## Contributing

Contributions are welcome. If you have ideas for clarity, new systems, or UX polish:

- Open an issue describing the change or new visualization
- Keep pages lightweight, dependency‑free, and consistent with the existing style
- Prefer progressive rendering and intuitive controls

## Acknowledgments

- Steven Strogatz, Nonlinear Dynamics and Chaos — ongoing inspiration
