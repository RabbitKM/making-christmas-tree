# Copilot Instructions for MakingChristmasTree

This project is a Python-based mini-game for customizing a Christmas tree, inspired by birthday cake decoration games.

## Project Overview
- **Purpose**: Allow users to create a personalized Christmas tree by selecting shape, color, and decorations, then display it in the console.
- **Scope**: Single-file script (`main.py`) with interactive input and ASCII art output.
- **Language**: Python 3.x.

## Architecture
- Main entry point: `main.py`.
- Key functions: `draw_tree()` for rendering the tree, `main()` for user interaction.
- No complex components; uses loops for tree drawing and random for decorations.

## Key Patterns
- User input via `input()` for customization options (height, shape, color, decorations).
- ASCII art drawing with centered strings and ANSI color codes for visual appeal.
- Random placement of decorations (lights, ornaments) using `random` module.
- Shape variations: 'triangle', 'star', 'pine' with different loop structures.
- Color mapping: Dictionary for ANSI escape codes (green, blue, red).

## Workflows
- **Run**: `python main.py` in terminal.
- **Test**: Run script and provide inputs; visually inspect output for correctness.
- **Debug**: Add print statements in loops to check iteration values or decoration placement.

## Conventions
- Follow PEP 8 for code style.
- Use `if __name__ == "__main__":` for script execution.
- Handle invalid inputs with loops and try-except for integers.

## Dependencies
- Standard library only (`random` for decorations).

## Examples
- Tree drawing: For 'triangle', loop `for i in range(1, height + 1): print(' ' * (height - i) + '*' * (2 * i - 1))`
- Decorations: Randomly insert colored dots or 'O' in tree lines.
- Trunk: Print centered '|' characters below the tree.