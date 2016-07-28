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

from pycmake.supported import Language
from pycmake.supported import CCompiler
from pycmake.supported import CXXCompiler

class Compiler(object):
    """
        Compilers define a compiler.
    """

    def __init__(self):
        self.name = None
        self.version = None
        self.language = None
        self.compiler = None
        self.executable = None

    @staticmethod
    def check_compiler_options(language, compiler):
        """
        Check if compiler is valid.

        :param language: language of compiler
        :param compiler: compiler (GCC, GXX, CLANG, CLANGXX, MSVC)
        """

        if language not in Language.__members__:
            raise ValueError('Language ' + language + ' is not currently supported !')
        if language is Language.C:
            if compiler not in CCompiler.__members__:
                raise ValueError('C compiler ' + compiler + ' is not currently supported !')
        if language is Language.CXX:
            if compiler not in CXXCompiler.__members__:
                raise ValueError('C++ compiler ' + compiler + ' is not currently supported !')

    def create(self, name, language, compiler, version, executable):
        """
        Create a compiler.

        :param name: name of compiler.
        :param language: language of compiler
        :param compiler: compiler (GCC, GXX, CLANG, CLANGXX, MSVC)
        :param version: version of the compiler.
        :param executable: full path to the executable.
        """
        if not isinstance(version, int) and not isinstance(version, float):
            raise ValueError('Version must be an integer or a float !')

        Compiler.check_compiler_options(language, compiler)
        self.name = name
        self.language = language
        self.version = version
        self.compiler = compiler
        self.executable = executable







