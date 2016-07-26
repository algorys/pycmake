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

# from cmake.project import CMakeProject
from cmake.cmakelists import CMakeLists
from cmake.version import ProjectVersion
from cmake.compiler import Compiler
from cmake.flags import Flags
from cmake.externals import Externals
from cmake.variables import Variables

class CMake(object):
    """
        This module is main module of CMake.
    """

    def __init__(self):
        self.project = {}
        self.settings = None
        # self.min_required = None
        self.cmakelist = None

    def add_settings(self, min_required='VERSION 3.0', policy='VERSION 3.0'):
        self.settings = {
            'min_required': min_required,
            'policy': policy
        }

    def add_project(self, name, language):
        if 'C' == language or 'CXX' == language or '' == language:
            self.project['project'] = {
                'name': name,
                'language': language
            }
        else:
            raise ValueError('Language ' + language + ' is not currently supported !')

    def add_version(self, major=0, minor=0, patch=0, tweak=0):
        version = ProjectVersion(major=major, minor=minor, patch=patch, tweak=tweak)
        self.project['version'] = version

    def add_compiler(self, name, language, compiler, version, executable):
        new_compiler = Compiler()
        new_compiler.create_compiler(name, language, compiler, version, executable)
        if 'compilers' in self.project:
            self.project['compilers'][name] = new_compiler
        else:
            self.project['compilers'] = {
                name: new_compiler
            }

    def init_cmakelist(self):
        self.cmakelist = CMakeLists()


