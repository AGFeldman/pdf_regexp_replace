# Usage: python run.py PDF_IN[optional] PDF_OUT[optional]

from subprocess import call
import re
import sys

# File paths
pdfin = 'testfile.pdf'
outfile = '~/Desktop/testout.pdf'
tempps = 'tempps.ps'

# Linux utilities
pdftops = 'pdftops'
pstopdf = 'ps2pdf'
shred = 'shred -u'

# Get arg for input pdf
if len(sys.argv) > 1:
    pdfin = sys.argv[1]
    if len(sys.argv) > 2:
        outfile = sys.argv[2]

# Convert PDF to a temporary PS
cmd = ' '.join((pdftops, pdfin, tempps))
call(cmd, shell=True)

# Get regexp
with open('regexp.txt', 'rb') as regexpfile:
    regexps = [line.strip() for line in regexpfile]

ps = [re.compile(regexp) for regexp in regexps]

# Get replacement text
with open('replacewith.txt', 'rb') as replacewithfile:
    replacewiths = [line.strip() for line in replacewithfile]

# Replace regexp text
with open(tempps, 'r+') as f:
    text = f.read()
    for p, replacewith in zip(ps, replacewiths):
        text = p.sub(replacewith, text)
    f.seek(0)
    f.write(text)
    f.truncate()

# Output a new PDF
cmd = ' '.join((pstopdf, tempps, outfile))
call(cmd, shell=True)

# Shred temporary PS
cmd = ' '.join((shred, tempps))
call(cmd, shell=True)
