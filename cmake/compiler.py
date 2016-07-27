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

from cmake.supported import *

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
    def check_compiler_options(language, compiler, version):
        if not isinstance(version, int) and not isinstance(version, float):
            raise ValueError('Version must be an integer or a float !')
        if language not in Language.__members__:
            raise ValueError('Language ' + language + ' is not currently supported !')
        if language is Language.C:
            if compiler not in CCompiler.__members__:
                raise ValueError('C compiler ' + compiler + ' is not currently supported !')
        if language is Language.CXX:
            if compiler not in CXXCompiler.__members__:
                raise ValueError('C++ compiler ' + compiler + ' is not currently supported !')

    def create_compiler(self, name='gcc', language='', compiler='gcc', version=5, executable='/usr/bin/gcc-5'):
        Compiler.check_compiler_options(language, compiler, version)
        self.name = name
        self.language = language
        self.version = version
        self.compiler = compiler
        self.executable = executable







