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

from pycmake.project import Project
from pycmake.cmakelists import CMakeLists
from pycmake.compiler import Compiler


class CMake(object):
    """
        This module is main module of CMake.
    """

    def __init__(self):
        self.project = None
        self.compilers = {}
        self.cmakelist = None
        self.flags = {}

    def add_project(self, name='project', language=''):
        if language == 'C' or language == 'CXX' or language == '':
            self.project = Project()
            self.project.create(name, language)
        else:
            raise ValueError('Language ' + language + ' is not currently supported !')

    def add_compiler(self, name, language, compiler, version, executable):
        new_compiler = Compiler()
        new_compiler.create_compiler(name, language, compiler, version, executable)
        self.compilers[name] = new_compiler

    def init_cmakelist(self):
        self.cmakelist = CMakeLists()



