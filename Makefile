test-install:
	virtualenv _test-install-virtualenv
	. _test-install-virtualenv/bin/activate && pip install pytest
	. _test-install-virtualenv/bin/activate && pip install -e .

dev-install:
	virtualenv _dev-install-virtualenv
	. _dev-install-virtualenv/bin/activate && pip install pytest
	. _dev-install-virtualenv/bin/activate && pip install -e .

build-package:
	pipenv run python setup.py sdist

upload-package:
	pipenv run python -m twine upload dist/*

_test-install-virtualenv/bin/activate: setup.py test-install

run-unit_tests: _test-install-virtualenv/bin/activate
	. _test-install-virtualenv/bin/activate && cd tests && time python -m pytest -s

run-cli_tests: _test-install-virtualenv/bin/activate
	. _test-install-virtualenv/bin/activate && cd tests && time cram *.t

run-tests:
	make test-install
	make run-unit_tests
	make run-cli_tests
