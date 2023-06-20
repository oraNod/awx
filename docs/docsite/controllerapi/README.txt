Regarding warnings of files not included ("WARNING: document isn't included in any toctree")

I moved all of the prior chapters into an intro.rst file using the
following markup:

.. include:: tools.rst
.. include:: browseable.rst
.. include:: conventions.rst
.. include:: sorting.rst
.. include:: searching.rst
.. include:: filtering.rst
.. include:: pagination.rst
.. include:: read_only_fields.rst
.. include:: tower_cli.rst

You may see warnings that these are not included when building the docs, but they are.
They are not included in the TOC (Table of Contents), but are included as shown
above in the intro.rst file. These warnings can be ignored.

To work on the API guide, I copied the JSON from the browseable API, 
then converted it to a CSV table using:
http://marianoguerra.github.io/json.human.js/

Using the HTML that http://marianoguerra.github.io/json.human.js/ created,
I added borders and width declarations for all table start points:
<table style="width:100%" border="1" class="jh-type-object jh-root">

Once I could confirm that the table built cleanly with the borders, I 
prettified the HTML using:
http://codebeautify.org/htmlviewer/

Additional CSS work for making the tables suck less:
TBD


