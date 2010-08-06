.. -*- mode: rst ; ispell-local-dictionary: "american" -*-

==========================
`python-ghostscript`
==========================

---------------------------------------------------------------------
Python-Interface to the Ghostscript C-API
---------------------------------------------------------------------

:Author:  Hartmut Goebel <h.goebel@crazy-compiler.com>
:Version: Version 0.2
:Copyright: GNU Public License v3 (GPLv3)
:Homepage: http://bitbucket.org/htgoebel/python-ghostscript

`Ghostscript`__, is a well known interpreter for the PostScript
language and for PDF. This package implements a interface to the
Ghostscript C-API using `ctypes`__. Both a low-level and a pythonic,
high-level interface are provided.

__ http://www.ghostscript.com/
__ http://docs.python.org/library/ctypes.html


This package is currently tested only under GNU/Linux. Please report
whether it works in your environment, too. Thanks.


Example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Here is an example for how to use the high-level interface of
`python-ghostscript`. This implements a very basic ps2pdf-tool::

  import sys
  import ghostscript

  args = [
      "ps2pdf",	# actual value doesn't matter
      "-dNOPAUSE", "-dBATCH", "-dSAFER",
      "-sDEVICE=pdfwrite",
      "-sOutputFile=" + sys.argv[1],
      "-c", ".setpdfwrite",
      "-f",  sys.argv[2]
      ]

  ghostscript.Ghostscript(*args)


Requirements and Installation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Please note: This package is meant for developers. Even if there are
  some usable examples included, installations instructions are meant
  for developers.

`python-ghostscript` requires

* `Python`__ 2.3 or higher (tested with Python 2.6)
* `ctypes`__ when using Python 2.3 or 2.4 (`ctypes` is already
             included in Python 2.5 and higher)
* `setuptools`__ or `distribute`__ for installation (see below).
* `Ghostscript`__ Version 8.x

__ http://www.python.org/download/
__ http://pypi.python.org/pypi/ctypes
__ http://pypi.python.org/pypi/setuptools
__ http://pypi.python.org/pypi/distribute
__ http://www.ghostscript.com/


Installing python-ghostscript
---------------------------------

Since this package is meant for developers, we assume you have
experience in installing Python packages.

`python-ghostscript` is listed on `PyPI (Python Package Index)`__, so
you can install it using `easy_install` or `pip` as usual. Please
refer to the manuals of `easy_install` resp. `pip` for further
information.

__ http://pypi.python.org/pypi

Alternatively you my download and unpack the source package of
`python-ghostscript` from http://pypi.python.org/pypi/ghostscript and
run::

   python ./setup.py install
