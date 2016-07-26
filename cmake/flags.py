# -*- coding: utf-8 -*-
#
# Copyright (C) 2016-2016: PyCMake team, actually just Estrada Matthieu
#
# This file is part of PyCMake.
#
# PyCMake is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PyCMake is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with PyCMake.  If not, see <http://www.gnu.org/licenses/>.

from cmake.compiler import *

class Flags(object):
    """
        Flags keep flags for compilations
    """

    def __init__(self):
        self.compiler = None
        self.general = None
        self.debug = None
        self.release = None

    def add_flags_to_compiler(self, compiler: Compiler, general, debug, release):
        if not isinstance(compiler, Compiler):
            raise AttributeError("Waiting for <class 'Compiler'> object. Get : " + str(type(compiler)) + ' instead !')
        if compiler.compiler is None or compiler.name is None:
            raise ValueError('Your Compiler seems not to have been created : ' + str(compiler.compiler))

        self.compiler = compiler.compiler
        self.general = general
        self.debug = debug
        self.release = release

