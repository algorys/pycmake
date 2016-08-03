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
from pycmake.supported import CCompiler
from pycmake.supported import CXXCompiler


class CMake(object):
    """
        CMake is root module of **PyCMake**. He manage all to provide CMake project.
    """

    def __init__(self):
        self.project = None
        self.settings = {}
        self.gnu = {}
        self.clang = {}
        self.msvc = {}
        self.cmakelist = CMakeLists()
        self.gnu_flags = {}
        self.clang_flags = {}
        self.msvc_flags = {}

    def add_project(self, name, language):
        """
        Add a CMake project.

        :param name: name of the project
        :type name: str
        :param language: language.
        :type language: str
        """

        if language == 'C' or language == 'CXX' or language == '':
            self.project = Project()
            self.project.create(name, language)
        else:
            raise ValueError('Language ' + language + ' is not currently supported !')

    def add_settings(self, min_required, policy):
        """
        Set **cmake_minimum_required** and **cmake_policy**.

        :param min_required: the cmake version minimum required.
        :type min_required: str
        :param policy: the policies of project.
        :type policy: str
        """

        self.settings['min_required'] = min_required
        self.settings['policy'] = policy

    def clang_compiler(self, compiler):
        """
        Add a Clang Compiler to CMake.

        :param compiler: Clang Compiler to add. Must be created before.
        :type compiler: Compiler
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

    def gnu_compiler(self, compiler):
        """
        Add a GNU Compiler to CMake.

        :param compiler: Gnu Compiler to add. Must be created before.
        :type compiler: Compiler
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

    def msvc_compiler(self, compiler):
        """
        Add a MSVC Compiler to CMake object.

        :param compiler: MSVC Compiler to add. Must be created before.
        :type compiler: Compiler
        """

        if compiler.compiler_id != 'MSVC' and compiler.compiler_id != 'MSVC++':
            raise ValueError('Compiler [' + compiler.name + '] is not a valid MSVC Compiler.')
        else:
            self.msvc[compiler.compiler_id] = {
                'name': compiler.name,
                'language': compiler.language,
                'version': compiler.version,
                'bin': compiler.executable
            }

    def flags_to_compiler(self, compiler_id, flags):
        """
        Add Flags to a specific compiler.

        :param compiler_id: supported compiler_id.

            - [GCC or G++],
            - [CLANG or CLANG++],
            - [MSVC or MSVC++]
        :type compiler_id: str
        :param flags: Flags to add to the compiler.
        :type flags: Flags
        """

        if compiler_id == CCompiler[0]:
            self.gnu_flags['C'] = flags
        elif compiler_id == CXXCompiler[0]:
            self.gnu_flags['C++'] = flags
        elif compiler_id == CCompiler[1]:
            self.clang_flags['C'] = flags
        elif compiler_id == CXXCompiler[1]:
            self.clang_flags['C++'] = flags
        elif compiler_id == CCompiler[2]:
            self.msvc_flags['C'] = flags
        elif compiler_id == CXXCompiler[2]:
            self.msvc_flags['C++'] = flags
        else:
            raise ValueError('Compiler [' + compiler_id + '] is not valid !')
