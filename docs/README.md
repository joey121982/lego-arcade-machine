# BrickBox

### versiune 0.0.5

----

## atentie: proiectul este scris in python 3.10+, versiuni mai vechi nu o sa mearga

----

## pre-rechizite
* pip & pipx
* python ^3.10
* pygame (instalat prin pipx astfel: ```pipx install pygame``` in folderul ```src/```)
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

## [Changelog](./changelog.md)

