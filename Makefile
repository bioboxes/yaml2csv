path    = PATH=$(abspath env/bin):${PATH}
version = $(shell $(path) python setup.py --version)
name    = $(shell $(path) python setup.py --name)
dist    = dist/$(name)-$(version).tar.gz

publish: $(dist) env
	$(path) aws s3 cp \
		$< \
		s3://bioboxes-packages/yaml2csv/$(version).tar.gz \
		--grants read=uri=http://acs.amazonaws.com/groups/global/AllUsers

build: $(dist)

$(dist): $(shell find yaml2csv -type f) requirements/default.txt setup.py MANIFEST.in
	$(path) python setup.py sdist


test:
	$(path) python -m pytest test

bootstrap: env

env: requirements/default.txt requirements/development.txt
	virtualenv $@
	$(path) pip install -rrequirements/default.txt -rrequirements/development.txt
	touch $@

.PHONY: test bootstrap build publish
