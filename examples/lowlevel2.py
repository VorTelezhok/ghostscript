#!/usr/bin/env python
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
__credits__ = "Based on an example from http://www.ghostscript.com/doc/8.63/API.htm"

import sys
from ghostscript import _gsprint as gs

start_string = "systemdict /start get exec\n"


instance = gs.new_instance()

# set_stdio() is not yet implemented
#gs.set_stdio(isntance, gsdll_stdin, gsdll_stdout, gsdll_stderr)

code = gs.init_with_args(instance, sys.argv)
if code == 0:
    code = gs.run_string(instance, start_string)
code1 = gs.exit(instance)
if code == 0 or code == gs.e_Quit:
    code = code1
gs.delete_instance(instance)
if not (code == 0 or code == gs.e_Quit):
    sys.exit(1)
