SHELL = /bin/bash

.PHONY: release
release:
	bumpversion --verbose $${PART:-patch}
	git push
	git push --tags

.PHONY: upload
upload:
	./setup.py sdist upload

.PHONY: restview
restview:
	restview README.rst -w README.rst

.PHONY: test
test:
	./tests/test.sh
