.PHONY: run install uninstall upload

run:
	pipx uninstall brick-interface && cd src && pipx install -e .
	pipx inject brick-interface gpiod
	cd src && brick-interface

install:
	cd src && pipx install -e .

uninstall:
	pipx uninstall brick-interface
