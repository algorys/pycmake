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

"""
    This file is only to tell what's compatible or not with **PyCMake**.
"""

LANGUAGE = ('C', 'C++')
"""
:var LANGUAGE: supported languages.
"""

C_COMPILER = ('GCC', 'CLANG', 'MSVC')
"""
:var C_COMPILER: supported C Compilers.
"""

CXX_COMPILER = ('G++', 'CLANG++', 'MSVC++')
"""
:var CXX_COMPILER: supported C++ Compiler.
"""

SRC_TYPE = ('DIR', 'FILE')
"""
:var SRC_TYPE: supported Sources.
"""
