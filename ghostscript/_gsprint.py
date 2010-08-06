#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
ghostscript._gsprint - A low-lewel interface to the Ghostscript C-API using ctypes
"""
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

__author__ = "Hartmut Goebel <h.goebel@crazy-compilers.com>"
__copyright__ = "Copyright 2010 by Hartmut Goebel <h.goebel@crazy-compilers.com>"
__licence__ = "GNU General Public License version 3 (GPL v3)"
__version__ = "0.2"

from ctypes import *

from . _errors import *

MAX_STRING_LENGTH = 65535

class Revision(Structure):
    _fields_ = [
        ("product", c_char_p),
        ("copyright", c_char_p),
        ("revision", c_long),
        ("revisiondate", c_long)
        ]

gs_main_instance = c_void_p
display_callback = c_void_p

class GhostscriptError(RuntimeError):
    def __init__(self, ecode):
         # :todo:
         RuntimeError.__init__(self, error2name(ecode))

def revision():
    """
    Get version numbers and strings.

    This is safe to call at any time.
    You should call this first to make sure that the correct version
    of the Ghostscript is being used.

    Returns a Revision instance
    """
    revision = Revision()
    rc = libgs.gsapi_revision(pointer(revision), sizeof(revision))
    if rc:
        raise ArgumentError("Revision structure size is incorrect, "
                            "requires %s bytes" % rc)
    return revision

def new_instance(): # display_callback=None):
    """
    Create a new instance of Ghostscript
    
    This instance is passed to most other API functions.
    """
    # :todo: The caller_handle will be provided to callback functions.
    display_callback=None
    instance = gs_main_instance()
    rc = libgs.gsapi_new_instance(pointer(instance), display_callback)
    if rc != 0:
        raise GhostscriptError(rc)
    return instance

def delete_instance(instance):
    """
    Destroy an instance of Ghostscript
    
    Before you call this, Ghostscript must have finished.
    If Ghostscript has been initialised, you must call exit()
    before delete_instance()
    """
    return libgs.gsapi_delete_instance(instance)


GSDLLCALL = CFUNCTYPE(gs_main_instance, POINTER(c_char), c_int)

# :todo:  set_stdio(instance, stdin, stdout, stderr):
# :todo:  set_poll (instance, int(*poll_fn)(void *caller_handle));
# :todo:  set_display_callback(instance, callback):

def init_with_args(instance, argv):
    """
    Initialise the interpreter.

    1. If quit or EOF occur during init_with_args(), the return value
       will be e_Quit. This is not an error. You must call exit() and
       must not call any other functions.
       
    2. If usage info should be displayed, the return value will be
       e_Info which is not an error. Do not call exit().
       
    3. Under normal conditions this returns 0. You would then call one
       or more run_*() functions and then finish with exit()
    """
    ArgArray = c_char_p * len(argv)
    c_argv = ArgArray(*argv) 
    rc = libgs.gsapi_init_with_args(instance, len(argv), c_argv)
    if rc not in (0, e_Quit, e_Info):
        raise GhostscriptError(rc)
    return rc

def exit(instance):
    """
    Exit the interpreter
    
    This must be called on shutdown if init_with_args() has been
    called, and just before delete_instance()
    """
    rc = libgs.gsapi_exit(instance)
    if rc != 0:
        raise GhostscriptError(rc)
    return rc


def run_string_begin(instance, user_errors=False):
    exit_code = c_int()
    rc = libgs.gsapi_run_string_begin(instance, c_int(user_errors),
                                      pointer(exit_code))
    if rc != 0:
        raise GhostscriptError(rc)
    return exit_code.value

def run_string_continue(instance, str, user_errors=False):
    exit_code = c_int()
    rc = libgs.gsapi_run_string_continue(
        instance, c_char_p(str), c_int(len(str)),
        c_int(user_errors), pointer(exit_code))
    if rc != e_NeedInput and rc != 0:
        raise GhostscriptError(rc)
    return exit_code.value

def run_string_end(instance, user_errors=False):
    exit_code = c_int()
    rc = libgs.gsapi_run_string_end(instance, c_int(user_errors),
                                    pointer(exit_code))
    if rc != 0:
        raise GhostscriptError(rc)
    return exit_code.value

def run_string_with_length(*args, **kw):
    raise NotImpelmentedError('Use run_string() instead')


def run_string(instance, str, user_errors=False):
    exit_code = c_int()
    rc = libgs.gsapi_run_string_with_length(
        instance, c_char_p(str), c_int(len(str)),
        c_int(user_errors), pointer(exit_code))
    if rc != 0:
        raise GhostscriptError(rc)
    return exit_code.value


def run_file(instance, filename, user_errors=False):
    exit_code = c_int()
    rc = libgs.gsapi_run_file(instance, c_char_p(filename), 
                              c_int(user_errors), pointer(exit_code))
    if rc != 0:
        raise GhostscriptError(rc)
    return exit_code.value


def set_visual_tracer(I):
    raise NotImplementedError


libgs = cdll.LoadLibrary("libgs.so.8")
