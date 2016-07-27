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

from cmake.cmake import CMake
from cmake.supported import CCompiler
from cmake.supported import CXXCompiler

class Flags(object):
    """
        Flags keep flags for compilations
    """

    def __init__(self, name, general, debug, release):
        self.name = name
        self.general = general
        self.debug = debug
        self.release = release
        self.use = False

    def add_to_cmake_compilers(self, compiler, cmake: CMake):
        if compiler not in CCompiler.__members__ and compiler not in CXXCompiler.__members__:
            raise ValueError('Compiler [' + compiler + '] does not exists.' )
        else:
            if compiler == CCompiler.GCC or compiler == CXXCompiler.GXX:
                cmake.flags['GNU'] = {
                    'general': self.general,
                    'debug': self.debug,
                    'release': self.release
                }
                self.use = True
            elif compiler == CCompiler.CLANG.value or compiler == CXXCompiler.CLANGXX.value:
                cmake.flags['CLANG'] = {
                    'general': self.general,
                    'debug': self.debug,
                    'release': self.release
                }
                self.use = True
            elif compiler == CCompiler.MSVC.value or compiler == CXXCompiler.MSVC.value:
                cmake.flags['MSVC'] = {
                    'general': self.general,
                    'debug': self.debug,
                    'release': self.release
                }
                self.use = True
            else:
                raise ValueError('Compiler [' + compiler.compiler + '] is not valid !')


