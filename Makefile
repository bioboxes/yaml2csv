path    = PATH=$(PWD)/.tox/py3-build/bin:$(shell echo "${PATH}")
version = $(shell $(path) python setup.py --version)
dist    = dist/yaml2csv-$(version)

publish: $(dist) env
	$(path) aws s3 cp \
		$< \
		s3://bioboxes-packages/yaml2csv/yaml2csv-$(version).xz \
		--grants read=uri=http://acs.amazonaws.com/groups/global/AllUsers



test:
	tox -e py3-unit -- $(ARGS)

###########################################
#
# Build project binary and documentation
#
###########################################

build:  $(dist)/bin/yaml2csv


%.xz: %
	xz --keep $<

$(dist)/bin/yaml2csv: \
	$(shell find yaml2csv bin -type f  ! -iname "*.pyc") \
	requirements/default.txt \
	setup.py \
	MANIFEST.in
	tox -e py3-build -- $(dir $@)


#################################################
#
# Bootstrap project requirements
#
#################################################


bootstrap:

.PHONY: test bootstrap build publish
