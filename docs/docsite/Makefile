SHELL=/bin/bash
DOCS = administration quickstart controllerapi userguide release-notes upgrade-migration-guide
HTMLDIRS = $(DOCS:%=html-%)
SINGLEHTMLDIRS = $(DOCS:%=singlehtml-%)
POTDIRS = $(DOCS:%=pot-%)
PDFDIRS = $(DOCS:%=latexpdf-%)
CLEANDIRS = $(DOCS:%=clean-%)
DOCTESTDIRS = $(DOCS:%=doctest-%)
LINKCHECKDIRS = $(DOCS:%=linkcheck-%)
PYTHON ?= python
VERSION = $(shell $(PYTHON) -c 'import common.source.conf as cfg ; print(cfg.version);')
DEST ?= docsite
LANGUAGE ?= en
PIP ?= pip
SINGLEHTMLARCHIVES = $(shell find . -name "singlehtml")

.PHONY: docs $(DOCS)
.PHONY: docs $(HTMLDIRS)
.PHONY: docs $(POTDIRS)
.PHONY: docs $(PDFDIRS)
.PHONY: docs $(CLEANDIRS)
.PHONY: docs $(LINKCHECKDIRS)
.PHONY: all html latexpdf doctest linkcheck requirements gettext

requirements:
	$(PIP) install -r requirements.txt

docs: $(DOCS)
$(DOCS):
	$(MAKE) -C $@

# URI = "http://jenkins.testing.ansible.com/view/Tower/job/Build_Tower_Docs/"
# URI = "http://docs.ansible.com/tower/"
html: $(HTMLDIRS)
$(HTMLDIRS):
ifeq ($(LANGUAGE),en)
	SPHINXOPTS="-aE" $(MAKE) -C $(@:html-%=%) html
	mkdir -p $(DEST)/$(VERSION)/html/$(@:html-%=%) && rsync -az $(@:html-%=%)/build/html/ $(DEST)/$(VERSION)/html/$(@:html-%=%)
	[ ! -L $(DEST)/$(VERSION)/html/towerapi -a -d $(DEST)/$(VERSION)/html/controllerapi ] && ln -sf controllerapi $(DEST)/$(VERSION)/html/towerapi || :
else
	SPHINXOPTS="-aE -D language='${LANGUAGE}'" $(MAKE) -C $(@:html-%=%) html
	mkdir -p $(DEST)/$(VERSION)/html_${LANGUAGE}/$(@:html-%=%) && rsync -az $(@:html-%=%)/build/html/ $(DEST)/$(VERSION)/html_${LANGUAGE}/$(@:html-%=%)
	[ ! -L $(DEST)/$(VERSION)/html_${LANGUAGE}/towerapi -a -d $(DEST)/$(VERSION)/html_${LANGUAGE}/controllerapi ] && ln -s controllerapi $(DEST)/$(VERSION)/html_${LANGUAGE}/towerapi || :
endif
	[ -h $(DEST)/latest ] || ln -s $(VERSION) $(DEST)/latest

singlehtml: $(SINGLEHTMLDIRS)
$(SINGLEHTMLDIRS):
	SPHINXOPTS="-aE" $(MAKE) -b singlehtml -C $(@:singlehtml-%=%) singlehtml

singlehtmlarchive: clean singlehtml
	tar czvf automation-controller-singlehtml.tar.gz $(SINGLEHTMLARCHIVES)

latexpdf: $(PDFDIRS)
$(PDFDIRS):
	$(MAKE) -C $(@:latexpdf-%=%) latexpdf
	mkdir -p $(DEST)/$(VERSION)/pdf && rsync -az $(@:latexpdf-%=%)/build/latex/*.pdf $(DEST)/$(VERSION)/pdf/
	[ -h $(DEST)/latest ] || ln -s $(VERSION) $(DEST)/latest

linkcheck: $(LINKCHECKDIRS)
$(LINKCHECKDIRS):
	$(MAKE) -C $(@:linkcheck-%=%) linkcheck

gettext: $(POTDIRS)
$(POTDIRS):
	$(MAKE) -C $(@:pot-%=%) gettext

clean: $(CLEANDIRS)
	rm -rf $(DEST)
	rm -rf automation-controller-singlehtml.tar.gz

$(CLEANDIRS):
	$(MAKE) -C $(@:clean-%=%) clean

doctest: $(DOCTESTDIRS)
$(DOCTESTDIRS):
	$(MAKE) -C $(@:doctest-%=%) doctest

version:
	@echo $(VERSION)
