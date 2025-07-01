# Chaos Animations

This repository contains visualizations and animations of chaotic systems using numerical methods.

## GitHub Pages Setup

This project is set up to be published as a GitHub Pages site. Here's how the structure works:

### File Structure

- **`index.html`** (in root): Main landing page that contains links to all animations
- **`pages/`**: Directory containing all individual animation pages
  - `animation.html`: Runge-Kutta solution animation
  - (add more pages here as needed)
- **`animations/`**: Directory containing animation files (GIFs, etc.)
- **`functions/`**: Directory containing code/functions used in the project

### How GitHub Pages Works with this Repository

1. GitHub Pages for project sites **requires** an `index.html` file in the root directory.
2. When visitors go to `https://matthematics1137.github.io/chaos/`, they see the content of the root `index.html`.
3. The landing page links to individual content pages in the `pages/` directory.

### Adding New Pages

To add a new animation or visualization:

1. Create a new HTML file in the `pages/` directory (e.g., `pages/new-animation.html`).
2. Add any associated animation files to the `animations/` directory.
3. Add a button or link to the new page from the main landing page (`index.html`).

Example button to add to index.html:
```html
<a href="pages/new-animation.html" class="button">New Animation Title</a>
```

### Maintaining the Site

- Always keep `index.html` in the root directory
- Keep all other content pages in the `pages/` directory
- For organization, store animation files in the `animations/` directory
- Make sure links between pages use relative paths correctly

### Troubleshooting Common Issues

- If the site shows a 404 error, ensure `index.html` exists in the root directory
- If images or animations don't load, check file paths in your HTML
- Remember that GitHub Pages is case-sensitive, ensure filenames match exactly

## Local Development

To test the site locally, simply open the `index.html` file in a web browser.
