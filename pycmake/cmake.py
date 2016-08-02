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
from pycmake.flags import Flags
from pycmake.supported import *


class CMake(object):
    """
        This module is main module of CMake.
    """

    def __init__(self):
        self.project = None
        self.settings = {}
        self.clang = {}
        self.gnu = {}
        self.msvc = {}
        self.cmakelist = CMakeLists()
        self.gnu_flags = {}
        self.clang_flags = {}
        self.msvc_flags = {}

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

    def clang_compiler(self, compiler: Compiler):
        """
        Add a Clang Compiler to CMake object.

        :param compiler: Compiler to add. Must be created before.
        """
        if compiler.compiler_id != 'CLANG' and compiler.compiler_id != 'CLANG++':
            raise ValueError('Compiler [' + compiler.name + '] is not a valid Clang Compiler.')
        else:
            self.clang[compiler.compiler_id] = {
                'name': compiler.name,
                'language': compiler.language,
                'version': compiler.version,
                'bin': compiler.executable
            }

    def gnu_compiler(self, compiler: Compiler):
        """
        Add a GNU Compiler to CMake object.

        :param compiler: Compiler to add. Must be created before.
        """
        if compiler.compiler_id != 'GCC' and compiler.compiler_id != 'G++':
            raise ValueError('Compiler [' + compiler.compiler_id + '] is not a valid GNU Compiler.')
        else:
            self.gnu[compiler.compiler_id] = {
                'name': compiler.name,
                'language': compiler.language,
                'version': compiler.version,
                'bin': compiler.executable
            }

    def msvc_compiler(self, compiler: Compiler):
        """
        Add a MSVC Compiler to CMake object.

        :param compiler: Compiler to add. Must be created before.
        """
        if compiler.compiler_id != 'MSVC' and compiler.compiler_id != 'MSVC':
            raise ValueError('Compiler [' + compiler.name + '] is not a valid MSVC Compiler.')
        else:
            self.gnu[compiler.compiler_id] = {
                'name': compiler.name,
                'language': compiler.language,
                'version': compiler.version,
                'bin': compiler.executable
            }

    def flags_to_compiler(self, compiler_id, flags: Flags):
        """
        Add Flags to a compiler : [GCC,G++], [CLANG,CLANG++], [MSVC,MSVC++]

        :param compiler_id: valid compiler id.
        :param flags: Flags to add.
        """
        if compiler_id == CCompiler.GCC.value:
            self.gnu_flags['C'] = flags
        elif compiler_id == CXXCompiler.GXX.value:
            self.gnu_flags['C++'] = flags
        elif compiler_id == CCompiler.CLANG.value:
            self.clang_flags['C'] = flags
        elif compiler_id == CXXCompiler.CLANGXX.value:
            self.clang_flags['C++'] = flags
        elif compiler_id == CCompiler.MSVC.value:
            self.msvc_flags['C'] = flags
        elif compiler_id == CXXCompiler.MSVC.value:
            self.msvc_flags['C++'] = flags
        else:
            raise ValueError('Compiler [' + compiler_id + '] is not valid !')
