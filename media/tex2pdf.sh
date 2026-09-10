#!/bin/bash
# generate pdf and png from the TeX file
BASE=$(basename -s .tex ${1})
latex2png -d 900 ${1}
mogrify -resize 25% -bordercolor white -border 30 ${BASE}.png
