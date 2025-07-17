.PHONY: run install uninstall upload

run:
	pipx uninstall brick-interface && cd src && pipx install -e . && brick-interface

install:
	cd src && pipx install -e .

uninstall:
	pipx uninstall brick-interface

upload:
	git push origin HEAD:brickman