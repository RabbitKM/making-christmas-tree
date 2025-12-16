# Copilot Instructions for MakingChristmasTree

This project is a web-based mini-game for customizing a Christmas tree, inspired by birthday cake decoration games.

## Project Overview
- **Purpose**: Allow users to create a personalized Christmas tree by selecting shape, color, and decorations, then display it in the browser.
- **Scope**: Static web application with HTML, CSS, and JavaScript.
- **Language**: JavaScript (ES6+), HTML5, CSS3.

## Architecture
- Main entry point: `index.html`.
- Key files: `script.js` for logic, `styles.css` for styling.
- No server-side components; client-side only for GitHub Pages deployment.

## Key Patterns
- DOM manipulation for user input and output display.
- String concatenation for ASCII art tree generation.
- Event listeners for button clicks.
- Random placement of decorations using `Math.random()`.
- Shape variations: 'triangle', 'star', 'pine' with different loop structures.
- Color styling: Inline CSS for tree colors.

## Workflows
- **Run**: Open `index.html` in a web browser or use a local server.
- **Test**: Interact with UI elements; visually inspect tree output.
- **Debug**: Use browser dev tools; console.log for variable checks.
- **Deploy**: Push to GitHub and enable Pages for hosting.

## Conventions
- Use semantic HTML5 elements.
- Follow CSS BEM or similar naming conventions.
- Use `const` and `let` for variables; avoid `var`.
- Handle user input validation in JavaScript.

## Dependencies
- No external libraries; vanilla JavaScript only.

## Examples
- Tree drawing: For 'triangle', loop `for (let i = 1; i <= height; i++) { ... }`
- Decorations: Randomly insert HTML spans with colors in tree strings.
- Trunk: Append brown-colored '|' characters below the tree.