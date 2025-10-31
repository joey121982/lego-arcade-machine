# BrickBox

### version 1.0.0, last updated 31.10.2025

----

## Attention: This project was written using Python 3.10+, older versions will NOT work.

----

## Prerequisites
* pip & pipx
* python ^3.10
* pygame (installed through pipx: ```pipx install pygame```)
* make (for the automated Makefile)

----

## Script
From the project root:
* ``` make run ``` - install and run
* ``` make install ``` - install only
* ``` make uninstall ``` - uninstall project

----

## Manual Installation
From ```src/``` run:
* editable mode (recommended)
```sh
pipx install -e .
```
* normal mode
```sh
pipx install .
```

----

## Running
After installation, the project will be added to PATH by pipx automatically, no further steps are required.
The project can be run from the terminal:
```sh
brick-interface
```

----

# External Credits:

Brickman Map Generator:
* Niels Lohmann - json.hpp https://github.com/nlohmann/json
* OpenGL3, GLFW - https://www.opengl.org/ & https://www.glfw.org/
* ImGui - https://github.com/ocornut/imgui

----

## [Changelog](./changelog.md)

