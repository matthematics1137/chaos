# Overlaps, Collisions, and Integration Guidelines

This document captures where simulations overlap conceptually or visually, and whether to integrate features into an existing page or create a new one.

## 1D Maps
- Logistic vs Tent
  - Overlap: Same diagnostics (Cobweb, Bifurcation, Lyapunov), same domain [0,1].
  - Integration: Keep Tent as a selectable map under the Logistic page (done). Adjust parameter range (Logistic r∈[2.5,4], Tent s∈[0,2]) and use correct derivatives; add Tent’s analytic λ(s)=ln s overlay.
  - Distinctive content for Tent (if expanded): uniform invariant density at s=2; conjugacy notes to doubling map; otherwise avoid a separate page.

## Phase‑Plane ODEs (2D)
- RK Playground vs Hopf (Brusselator)
  - Overlap: Both integrate 2D systems and draw trajectories/fields.
  - Integration guidance: Keep Hopf as a focused demo (nullclines, Hopf threshold B=1+A²). Optionally add Brusselator as a system in the Playground later; do not duplicate detailed Hopf explanations there.

## 3D Attractors
- Lorenz vs Rössler
  - Overlap: Both are 3D chaotic flows with rotating projection.
  - Integration guidance: Keep separate pages. Add a shared “Poincaré Section” tab to each (same UI pattern) rather than a single combined page.

## Dissipative Maps (2D)
- Hénon vs Logistic/Tent
  - Overlap: Iterated maps showing chaos.
  - Integration guidance: Keep Hénon separate (2D state, different geometry). If adding return maps, mirror Lyapunov/bifurcation ideas without grafting them onto Logistic.

## Synchronization / Locking
- Circle Map vs Kuramoto
  - Overlap: Locking/entrainment phenomena.
  - Integration guidance: Keep separate (single driven phase vs many coupled oscillators). Cross‑link but avoid combining pages.

## General Rules
- Prefer integration when:
  - The UI and diagnostics are identical and the systems are in the same family (e.g., 1D maps).
  - A quick toggle or tab keeps comparisons honest and avoids duplication.
- Prefer new pages when:
  - The state space dimension or core teaching narrative differs (e.g., 2D ODEs vs 3D attractors vs 2D maps).
  - A simulation focuses on a single flagship phenomenon (e.g., Hopf bifurcation) with specific annotations.

