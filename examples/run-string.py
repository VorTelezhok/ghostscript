#!/usr/bin/env python
"""

Simple test program using run_string() and run_file()

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

doc = """%!
/Helvetica findfont
20 scalefont
setfont       
50 50 moveto
(Hallo \(W \)elt!) show
1 0 0 setrgbcolor
<416c6c20646f6e652e> show
0 1 0 setrgbcolor
<48616c6c6f205c2857205c29656c5c7421> show
showpage
"""

import io
import ghostscript

args = """test.py
     -dNOPAUSE -dBATCH -dSAFER -sDEVICE=pdfwrite -sOutputFile=/tmp/out.pdf
    -c .setpdfwrite""".split()

GS = ghostscript.Ghostscript(*args)
try:
    GS.run_string(doc)
    GS.run_file(io.StringIO(doc))
finally:
    GS.exit()
