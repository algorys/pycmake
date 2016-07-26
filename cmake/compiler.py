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

from enum import Enum

class Compiler(object):
    language_supported = [
        'C',
        'c',
        'C++',
        'c++',
    ]

    c_compiler_supported = [
        'gcc',
        'clang',
        'MSVC'
    ]

    cpp_compiler_supported = [
        'g++',
        'clang++',
        'MSVC'
    ]


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
        if language not in Compiler.language_supported:
            raise ValueError('Language ' + language + ' is not currently supported !')
        if language is 'C' or language is 'c':
            if compiler not in Compiler.c_compiler_supported:
                raise ValueError('C compiler ' + compiler + ' is not currently supported !')
        if language is 'C++' or language is 'c++':
            if compiler not in Compiler.cpp_compiler_supported:
                raise ValueError('C++ compiler ' + compiler + ' is not currently supported !')

    def create_compiler(self, name='gcc', language='C', compiler='gcc', version=5, executable='/usr/bin/gcc-5'):
        Compiler.check_compiler_options(language, compiler, version)
        self.name = name
        self.language = language
        self.version = version
        self.compiler = compiler
        self.executable = executable




