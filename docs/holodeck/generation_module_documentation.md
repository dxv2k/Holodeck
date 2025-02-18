# AI2-Holodeck Generation Module Documentation

## Overview

The `generation` module in the AI2-Holodeck project is responsible for generating and managing various components of a virtual scene. It includes classes and functions for creating rooms, walls, doors, windows, and objects, as well as handling constraints and placements.

## Key Components

### `holodeck.py`
- **`Holodeck` Class**: Orchestrates the generation of scene components, including rooms, walls, doors, windows, and objects.
  - **Initialization**: Sets up models and generators for scene components.
  - **Scene Generation Methods**: Includes methods like `generate_rooms`, `generate_walls`, `generate_doors`, `generate_windows`, `select_objects`, and more.
  - **Scene Generation Workflow**: The `generate_scene` method follows a step-by-step process to generate a complete scene.

### `floor_objects.py`
- **`FloorObjectGenerator` Class**: Manages the generation and placement of floor objects.
  - **Object Generation Methods**: Includes `generate_objects` and `generate_objects_per_room`.
  - **Constraint Handling**: Uses constraints to guide object placement.
  - **Placement and Solving**: Utilizes `DFS_Solver_Floor` for optimal placements.

### `object_selector.py`
- **`ObjectSelector` Class**: Selects objects for a scene using a language model and object retriever.
  - **Object Selection Methods**: Includes `select_objects` and `plan_room`.
  - **Utility Methods**: Handles JSON extraction and room size calculations.
  - **Placement and Capacity Handling**: Validates object size and placement, updates capacity.

## Setup and Usage

1. **Dependencies**: Ensure all dependencies are installed as listed in `requirements.txt`.
2. **Environment Setup**: Configure environment variables such as `OPENAI_API_KEY`.
3. **Scene Generation**: Use the `Holodeck` class to generate scenes by calling `generate_scene` with appropriate parameters.

## Development Guidelines

- Follow coding standards and best practices as outlined in the project's documentation.
- Use the provided classes and methods for consistent scene generation and object placement.

## Troubleshooting and FAQs

- Common issues and solutions are documented in the project's README and error logs.

## Contribution Guidelines

- Follow the branching strategy and code review process outlined in the project's CONTRIBUTING.md.