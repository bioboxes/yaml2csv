path    = PATH=$(PWD)/.tox/py27-build/bin:$(shell echo "${PATH}")
version = $(shell $(path) python setup.py --version)
name    = $(shell $(path) python setup.py --name)
dist    = dist/$(name)-$(version).tar.gz

publish: $(dist) env
	$(path) aws s3 cp \
		$< \
		s3://bioboxes-packages/yaml2csv/$(version).tar.gz \
		--grants read=uri=http://acs.amazonaws.com/groups/global/AllUsers



test:
	tox -e py27-unit -e py3-unit -- $(ARGS)

#################################################
#
# Build and test the pip package
#
#################################################

build: test-build $(dist)

test-build:
	tox -e py27-build,py3-build

$(dist): $(shell find yaml2csv -type f) requirements/default.txt setup.py MANIFEST.in
	@$(path) python setup.py sdist --formats=gztar
	touch $@

#################################################
#
# Bootstrap project requirements
#
#################################################


bootstrap:

.PHONY: test bootstrap build publish
