VERSION=$(shell python3 -c "import meterplot; print(meterplot.__version__)")

default:
	@echo "\"make publish\"?"

README.rst: README.md
	pandoc README.md -o README.rst
	python3 setup.py check -r -s || exit 1

upload: setup.py README.rst
	# Make sure we're on the master branch
	@if [ "$(shell git rev-parse --abbrev-ref HEAD)" != "master" ]; then exit 1; fi
	rm -f dist/*
	python3 setup.py sdist
	python3 setup.py bdist_wheel --universal
	twine upload dist/*

tag:
	@if [ "$(shell git rev-parse --abbrev-ref HEAD)" != "master" ]; then exit 1; fi
	@echo "Tagging v$(VERSION)..."
	git tag v$(VERSION)
	git push --tags

clean:
	@find . | grep -E "(__pycache__|\.pyc|\.pyo$\)" | xargs rm -rf
	@rm -rf *.egg-info/ build/ dist/ MANIFEST

lint:
	black --check setup.py quadpy/ test/*.py
	flake8 setup.py quadpy/ test/*.py
