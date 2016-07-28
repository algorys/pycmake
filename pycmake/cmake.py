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
        self.settings = {}
        self.compilers = {}
        self.cmakelist = CMakeLists()
        self.flags = {}

    def add_project(self, name='project', language=''):
        """
        Add a project to CMake object.

        :param name: name of the project
        :param language: language. Default is ''
        """

        if language == 'C' or language == 'CXX' or language == '':
            self.project = Project()
            self.project.create(name, language)
        else:
            raise ValueError('Language ' + language + ' is not currently supported !')

    def add_settings(self, min_required='VERSION 3.0', policy='VERSION 3.0'):
        self.settings['min_required'] = min_required
        self.settings['policy'] = policy

    def add_compiler(self, compiler: Compiler):
        """
        Add a Compiler to CMake object.

        :param compiler: Compiler to add. Must be created before.
        """
        if not compiler.name or not compiler.compiler:
            raise ValueError('Your compiler must be created before.')
        self.compilers[compiler.name] = compiler




