#!/bin/sh

python $(dirname $0)/gs.py \
    -dNOPAUSE -dBATCH -dSAFER -sDEVICE=pdfwrite -sOutputFile=/tmp/out.pdf \
    -c .setpdfwrite -f $(dirname $0)/test.ps

