# BrickBox

### versiune 0.1.0, last updated 05.09.2025

----

## atentie: proiectul este scris in python 3.10+, versiuni mai vechi nu o sa mearga

----

## pre-rechizite
* pip & pipx
* python ^3.10
* pygame (instalat prin pipx astfel: ```pipx install pygame```)
* make (doar pentru script-ul automat)

----

## script automat
Din folderul principal ruleaza:
* ``` make run ``` - instaleaza si ruleaza proiectul
* ``` make install ``` - doar instaleaza
* ``` make uninstall ``` - dezinstaleaza

----

## install
Din folderul ```src/``` ruleaza:
* mod editabil (recomandat)
```sh
pipx install -e .
```
* mod normal
```sh
pipx install .
```

----

## rulare
Dupa instalare, programul o sa fie instalat in PATH direct de ```pipx```, fara sa fie nevoie de etape in plus.
Asadar, poate fi rulat din ```src/``` astfel:
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

