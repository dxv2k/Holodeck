# Onboarding Documentation for AI2-Holodeck and AI2-THOR

## Project Overview

The AI2-Holodeck and AI2-THOR projects are designed to facilitate the generation and manipulation of virtual environments. They provide tools for creating scenes, managing objects, and running simulations.

### Directory Structure

- **ai2holodeck/**: Contains modules for scene generation and experimentation.
  - **main.py**: Central script for generating scenes using the Holodeck model.
  - **exp_runner.py**: Manages scene generation and experimentation.
  - **generation/**: Contains modules for generating various components of a scene.

- **ai2thor/**: Manages building, deploying, and testing the AI2-THOR environment.
  - **tasks.py**: Comprehensive script for managing tasks related to building, deploying, and testing.
  - **controller/**: Contains the main controller logic for interacting with the environment.

## Key Modules and Functions

### AI2-Holodeck

- **`main.py`**:
  - `str2bool(v: str)`: Converts a string to a boolean.
  - `generate_single_scene(args)`: Generates a single scene.
  - `generate_multi_scenes(args)`: Generates multiple scenes from a list of queries.
  - `generate_variants(args)`: Generates variants of a given scene.

- **`exp_runner.py`**:
  - `generate_all_experiments(args)`: Loads experiments from a JSON file and generates scenes for each experiment.

### AI2-THOR

- **`tasks.py`**:
  - `push_build(build_archive_name, zip_data, include_private_scenes)`: Pushes a build to AWS S3.
  - `local_build(context, prefix, arch, scenes, scripts_only)`: Creates a local build.
  - `webgl_build(context, scenes, directory, prefix, verbose, content_addressable)`: Creates a WebGL build.
  - `ci_pytest(branch, commit_id)`: Runs pytest for continuous integration.
  - `create_robothor_dataset(context)`: Creates a dataset for the RoboTHOR challenge.

## Setup and Installation

1. **Dependencies**: Ensure all dependencies are installed as listed in `requirements.txt`.
2. **Environment Setup**: Configure environment variables such as `OPENAI_API_KEY` and `OPENAI_ORG`.
3. **Build and Deployment**: Use the `tasks.py` script to manage builds and deployments.

## Usage Instructions

- **Generating Scenes**: Use `main.py` or `exp_runner.py` to generate scenes. Specify the mode and options via command-line arguments.
- **Running Tests**: Use `tasks.py` to run tests and validate the environment.

## Development Guidelines

- Follow coding standards and best practices as outlined in the project's documentation.
- Use the provided scripts for building and testing to ensure consistency.

## Troubleshooting and FAQs

- Common issues and solutions are documented in the project's README and error logs.

## Contribution Guidelines

- Follow the branching strategy and code review process outlined in the project's CONTRIBUTING.md.