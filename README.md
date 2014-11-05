Usage: `run.py EXAMPLE_IN.pdf EXAMPLE_OUT.pdf`

EXAMPLE_OUT.pdf will be a copy of EXAMPLE_IN.pdf with some text replaced.

Configuration:
The script operates by converting EXAMPLE_IN.pdf to a temporary postscript
file, then replacing any text in the postscript file that matches a regular
expression in regexp.txt with the corresponding line in replacewith.txt, then
creating EXAMPLE_OUT.pdf and shredding the temporary postscript file. You
will need to create the files regexp.txt and replacewith.txt to specify how the
script should replace text. See the example files example_regexp.txt and
exmaple_replacewith.txt.

I use this for removing account numbers from financial documents.
