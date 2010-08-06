#!/usr/bin/env python
"""
This is a rough Python implementation of the shellscript ps2pdfwr
which comes with Ghostscript.
"""
# -*- coding: utf-8 -*-
#
# Copyright 2010 by Hartmut Goebel <h.goebel@goebel-consult.de>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#

__author__ = "Hartmut Goebel <h.goebel@goebel-consult.de>"
__copyright__ = "Copyright 2010 by Hartmut Goebel <h.goebel@goebel-consult.de>"
__licence__ = "GNU General Public License version 3 (GPL v3)"

import sys
import os

import ghostscript

options = ["-dSAFER"]
args = sys.argv[1:]
while args:
    arg = args[0]
    if arg.startswith('-') and len(arg) > 1:
        options.append(arg)
        arg = args.pop(0)
    else:
        break

def usage():
    print >> sys.stderr, "Usage:", os.path.basename(sys.argv[0]), \
          "[options...] (input.[e]ps|-) [output.pdf|-]"
    sys.exit(1)
    
if len(args) not in (1,2):
    usage()

infile = args[0]
if len(args) == 1:
    if infile == '-':
        outfile = '-'
    else:
        base, ext = os.path.splitext(os.path.basename(infile))
        if ext in ('.ps', '.eps'):
            outfile = base + '.pdf'
        else:
            outfile = base + ext + '.pdf'
else:
    outfile = args[1]

# We have to include the options twice because -I only takes effect if
# it appears before other options.
args = [os.path.basename(sys.argv[0])] # actual value doesn't matter
args.extend(options)
args.extend(["-q", "-dNOPAUSE","-dBATCH", "-sDEVICE=pdfwrite",
             "-sstdout=%stderr",
             "-sOutputFile=" + outfile])
args.extend(options)
args.extend(["-c", ".setpdfwrite", "-f", infile])

# After all these preperations, calling Ghostscript is a piece of cake:
ghostscript.Ghostscript(*args)
