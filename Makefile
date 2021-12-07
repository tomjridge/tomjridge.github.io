SHELL:=bash

# the following ppath allows to accessed shared.py
ppath:=PYTHONPATH=.
# expander:=$(ppath) expander.py -a --eval 'salutation="Mr";surname="Smith"'

all: index.html

#test.html: FORCE
#	-chmod u+w $@
#	$(expander) -f $@.pye
#	$(expander) -f $@.pye > $@
#	chmod u-w $@

index.html: FORCE
	$(ppath) python3 create_index_html.py > index.html

run_server: FORCE
	python3 -m http.server

# parsing.md: parsing.py
# 	$(ppath) python3 $< > $@
# 
# XXXcheck:
# 	linkchecker -v --check-extern -r 3 http://localhost:8000 # except this just retrieves the template, it doesn't wait for the content
# 

extract_links:
	for f in *.md; do echo; echo File is: $$f; python -m markdown_link_extractor $$f; done # pip install markdown-link-extractor

resources:
	FIXME need to copy resources from old site

FORCE:
