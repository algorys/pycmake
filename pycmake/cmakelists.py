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

import os
import sys


class CMakeLists(object):

    """
        CMakeLists create and generate CMakeLists.txt.
    """

    def __init__(self):
        self.cmakelists = None

    def create_file(self, path):
        """
        Create CMakeLists.txt

        :param path: path where to create CMakeLists.txt.
        :type path: str
        """

        if not os.path.exists(path):
            try:
                os.makedirs(path)
            except PermissionError as e:
                sys.exit('Cannot create : ' + path + '. ' + str(e))

        try:
            if path[-1:] == '/' or path[-1:] == '\\':
                self.cmakelists = open(str(path) + 'CMakeLists.txt', 'w')
            else:
                self.cmakelists = open(str(path) + '/CMakeLists.txt', 'w')
        except PermissionError as e:
            sys.exit('Maybe you do not have sufficient rights : ' + str(e))

    def write_cmakelists(self, cmake):  # pragma: no cover
        """
        Write CMakeLists.txt from the CMake data.

        :param cmake: CMake object, who contains a Project, Compilers and Targets.
        :type cmake: CMake
        """

        if self.cmakelists:
            try:
                self.cmakelists.write(
                    '# This file was automatically generated by PyCMake.\n')
                self.cmakelists.write(
                    '# WARNING: Do not edit this file unless you know what you are doing.\n')
            except PermissionError as e:
                print('Maybe you do not have sufficient rights : ' + str(e))

        self.cmakelists.write(
            '# ------------------------- CMakeLists ------------------\n')

        # Write settings
        if cmake.settings:
            self.cmakelists.write('cmake_minimum_required(' + cmake.settings['min_required']
                                  + ')'
                                  )
            self.cmakelists.write('cmake_policy('
                                  + cmake.settings['version']
                                  + ')'
                                  )
        else:
            self.cmakelists.write('# WARNING: minimum_required is not set.\n')
            self.cmakelists.write('# WARNING: policy is not set.\n')

        # Write variables
        if cmake.project.variables:
            for var in cmake.project.variables.values:
                current_var = dict(cmake.project.get_variable(var))
                if current_var.get('option') == 'filename_component':
                    self.cmakelists.write(
                        'get_filename_component('
                        + current_var.get('name')
                        + ' "'
                        + current_var.get('value') +
                        '" ABSOLUTE)\n')
                elif current_var.get('option') == 'set':
                    self.cmakelists.write(
                        'set('
                        + current_var.get('name')
                        + ' "'
                        + current_var.get('value')
                        + '")\n')
                else:
                    raise ValueError(
                        'Variable: [' + current_var.get('name') + '] is incorrect !')

        # Write Project
        self.cmakelists.write(
            'project(${PROJECT_NAME} ' + cmake.project.language + ')\n')

        # GNU Flags
        if cmake.gnu_flags:
            self.cmakelists.write(
                'if ("${CMAKE_CXX_COMPILER_ID}" STREQUAL "GNU")\n')
            if 'C' in cmake.gnu_flags:
                if cmake.gnu_flags['C'].general:
                    self.cmakelists.write('    set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} '
                                          + cmake.gnu_flags['C'].general
                                          + '")\n'
                                          )
                    if cmake.gnu_flags['C'].debug:
                        self.cmakelists.write(
                            '    set(CMAKE_C_FLAGS_DEBUG "${CMAKE_C_FLAGS_DEBUG} '
                            + cmake.gnu_flags['C'].debug + '")\n')
                    if cmake.gnu_flags['C'].release:
                        self.cmakelists.write(
                            '  set(CMAKE_C_FLAGS_RELEASE "${CMAKE_C_FLAGS_RELEASE} '
                            + cmake.gnu_flags['C'].release + '")\n')
            if 'C++' in cmake.gnu_flags:
                if cmake.gnu_flags['C++'].general:
                    self.cmakelists.write(
                        '    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} '
                        + cmake.gnu_flags['C++'].general + '")\n')
                if cmake.gnu_flags['C++'].debug:
                    self.cmakelists.write(
                        '    set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} '
                        + cmake.gnu_flags['C++'].debug + '")\n')
                if cmake.gnu_flags['C++'].release:
                    self.cmakelists.write(
                        '    set(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE} '
                        + cmake.gnu_flags['C++'].release + '")\n')
            self.cmakelists.write('endif()\n')
        # CLANG Flags
        if cmake.clang_flags:
            self.cmakelists.write(
                'if ("${CMAKE_CXX_COMPILER_ID}" STREQUAL "Clang")\n')
            if 'C' in cmake.clang_flags:
                if cmake.clang_flags['C'].general:
                    self.cmakelists.write(
                        '    set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} '
                        + cmake.clang_flags['C'].general + '")\n')
                if cmake.clang_flags['C'].debug:
                    self.cmakelists.write(
                        '    set(CMAKE_C_FLAGS_DEBUG "${CMAKE_C_FLAGS_DEBUG} '
                        + cmake.clang_flags['C'].debug + '")\n')
                if cmake.clang_flags['C'].release:
                    self.cmakelists.write(
                        '    set(CMAKE_C_FLAGS_RELEASE "${CMAKE_C_FLAGS_RELEASE} '
                        + cmake.clang_flags['C'].release + '")\n')
            if 'C++' in cmake.clang_flags:
                if cmake.clang_flags['C++'].general:
                    self.cmakelists.write(
                        '    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} '
                        + cmake.clang_flags['C++'].general + '")\n')
                if cmake.clang_flags['C++'].debug:
                    self.cmakelists.write(
                        '    set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} '
                        + cmake.clang_flags['C++'].debug + '")\n')
                if cmake.clang_flags['C++'].release:
                    self.cmakelists.write(
                        '    set(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE} '
                        + cmake.clang_flags['C++'].release + '")\n')
            self.cmakelists.write('endif()\n')
        # MSVC Flags
        if cmake.msvc_flags:
            self.cmakelists.write(
                'if ("${CMAKE_CXX_COMPILER_ID}" STREQUAL "MSVC")\n')
            if 'C' in cmake.msvc_flags:
                if cmake.msvc_flags['C'].general:
                    self.cmakelists.write(
                        '    set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} '
                        + cmake.msvc_flags['C'].general + '")\n')
                if cmake.msvc_flags['C'].debug:
                    self.cmakelists.write(
                        '    set(CMAKE_C_FLAGS_DEBUG "${CMAKE_C_FLAGS_DEBUG} '
                        + cmake.msvc_flags['C'].debug + '")\n')
                if cmake.msvc_flags['C'].release:
                    self.cmakelists.write(
                        '    set(CMAKE_C_FLAGS_RELEASE "${CMAKE_C_FLAGS_RELEASE} '
                        + cmake.msvc_flags['C'].release + '")\n')
            if 'C++' in cmake.msvc_flags:
                if cmake.msvc_flags['C++'].general:
                    self.cmakelists.write(
                        '    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} '
                        + cmake.msvc_flags['C++'].general + '")\n')
                if cmake.msvc_flags['C++'].debug:
                    self.cmakelists.write(
                        '    set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} '
                        + cmake.msvc_flags['C++'].debug + '")\n')
                if cmake.msvc_flags['C++'].release:
                    self.cmakelists.write(
                        '    set(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE} '
                        + cmake.msvc_flags['C++'].release + '")\n')
            self.cmakelists.write('endif()\n')

        # Definitions
        if cmake.project.definitions:
            self.cmakelists.write('add_definitions(\n')
            for index, definition in enumerate(cmake.project.definitions):
                self.cmakelists.write('    -D' + definition + '\n')
            self.cmakelists.write(')\n')

        # Files: Sources_Dir
        if cmake.project.sources_dirs:
            for source_dir in cmake.project.sources_dirs:
                self.cmakelists.write('file(')
                if cmake.project.sources_dirs.get(source_dir)['recursive']:
                    self.cmakelists.write('GLOB_RECURSE')
                else:
                    self.cmakelists.write('GLOB')
                self.cmakelists.write(' ' + source_dir.upper() + '\n')
                sources_dir = cmake.project.sources_dirs.get(source_dir)['sources']
                for index, source in enumerate(sources_dir):
                    if cmake.project.sources_dirs.get(source_dir)['from_proj']:
                        self.cmakelists.write(
                            '    ${PROJECT_DIR}/' + source + '\n')
                    else:
                        self.cmakelists.write('    ' + source + '\n')
                self.cmakelists.write(')\n')
        # Files: Files
        if cmake.project.sources_files:
            for source_file in cmake.project.sources_files:
                self.cmakelists.write('file(')
                self.cmakelists.write(source_file.upper() + '\n')
                for index, file in enumerate(cmake.project.sources_files.get(source_file)['files']):
                    if cmake.project.sources_files.get(source_file)['from_proj']:
                        self.cmakelists.write(
                            '    ${PROJECT_DIR}/' + file + '\n')
                    else:
                        self.cmakelists.write('    ' + file + '\n')
                self.cmakelists.write(')\n')

        # Dependencies
        if cmake.project.dependencies:
            if cmake.project.dependencies.sub_directories:
                for sub in cmake.project.dependencies.sub_directories:
                    current_sub = cmake.project.dependencies.sub_directories.get(
                        sub)
                    self.cmakelists.write(
                        'add_subdirectory(' + current_sub['source_dir'] + ' '
                        + current_sub['binary_dir'] + ')\n')
            if cmake.project.dependencies.add_link_directories:
                link_directories = cmake.project.dependencies.link_directories
                for index, link in enumerate(link_directories):
                    self.cmakelists.write(
                        'link_directories(' + link + ')\n')

        # Add target
        if cmake.project.targets:
            targets = cmake.project.targets
            for target in targets:
                if targets.get(target)['target_type'] == 'library':
                    self.cmakelists.write('add_library(')
                    if targets.get(target)['name'] == cmake.project.name:
                        self.cmakelists.write('${PROJECT_NAME} ')
                    else:
                        self.cmakelists.write(
                            targets.get(target)['name'] + ' ')
                    if targets.get(target)['shared']:
                        self.cmakelists.write('SHARED\n')
                    else:
                        self.cmakelists.write('STATIC\n')

                if cmake.project.sources_dirs:
                    for source_dir in cmake.project.sources_dirs:
                        target_dir = cmake.project.sources_dirs.get(source_dir)['target']
                        if target_dir == targets.get(target)['name']:
                            self.cmakelists.write(
                                '    ' + source_dir.upper() + '\n')
                if cmake.project.sources_files:
                    for source_file in cmake.project.sources_files:
                        target_files = cmake.project.sources_files.get(source_file)['target']
                        if target_files == targets.get(target)['name']:
                            self.cmakelists.write(
                                '    ' + source_file.upper() + '\n')
                self.cmakelists.write(')\n')

        # Add links
        if cmake.project.dependencies and cmake.project.targets:
            libraries = cmake.project.dependencies.libraries

            for lib in libraries:
                print(libraries.get(lib))
                self.cmakelists.write('target_link_libraries(')
                self.cmakelists.write(libraries.get(lib)['target'])
                for l in libraries.get(lib)['libraries']:
                    self.cmakelists.write(' ' + l)
                self.cmakelists.write(')')
