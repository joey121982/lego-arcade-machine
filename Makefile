.PHONY: run install uninstall

run:
	pipx uninstall brick-interface && cd src && pipx install -e . && brick-interface

install:
	cd src && pipx install -e .

uninstall:
	pipx uninstall brick-interface
