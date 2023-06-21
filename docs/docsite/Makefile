SPHINXOPTS    = -aE
SPHINXBUILD   = sphinx-build
BUILDDIR      = build

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  html       to build HTML files"
	@echo "  clean      to remove built files"

clean:
	rm -rf $(BUILDDIR)/*

html:
	$(SPHINXBUILD) -b html $(SPHINXOPTS) $(BUILDDIR)/html
	@echo
	@echo "Build finished. The HTML pages are in $(BUILDDIR)/html."