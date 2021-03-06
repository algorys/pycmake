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

    def init_file(self, path):
        """
        Create folders and CMakeLists.txt.

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

    def write_cmakelists(self, cmake, project):  # pragma: no cover
        """
        Write CMakeLists.txt from the CMake data.

        :param cmake: CMake object,
         with :class:`~pycmake.compiler.Compiler` and :class:`~pycmake.flags.Flags`.
        :type cmake: CMake
        :param project: Project object with his target,
         sources and :class:`~pycmake.externals.Externals`.
        :type project: Project
        """

        self.write_info()

        if cmake.settings:
            self.write_global_settings(cmake.settings)

        if project.name and project.targets:
            # Write data for project.
            self.write_variables(project)
            self.write_project_data(project.language, project.definitions)

            # Write Flags for all compilers.
            if cmake.gnu_flags:
                self.write_gnu_flags(cmake.gnu_flags)
            if cmake.clang_flags:
                self.write_clang_flags(cmake.clang_flags)
            if cmake.msvc_flags:
                self.write_msvc_flags(cmake.msvc_flags)

            # Write Variables for sources directories.
            if project.sources_dirs:
                self.write_directory_files(project.sources_dirs)

            # Write dependecies
            if project.dependencies:
                self.write_dependencies(project.dependencies)

            # Write Targets.
            self.write_targets(project)

            # Add links to targets.
            if project.dependencies:
                self.write_links(project.dependencies)

    def write_title(self, title):  # pragma: no cover
        self.cmakelists.write(
            '\n#####################################################################\n'
        )
        self.cmakelists.write('# ' + title + ' #\n')
        self.cmakelists.write(
            '#####################################################################\n\n'
        )

    def write_info(self):  # pragma: no cover
        """
        Write global informations.

        """

        if self.cmakelists:
            try:
                self.cmakelists.write(
                    '# ------------- Generated automatically by PyCMake. ---------------\n'
                    '# -> Do not edit this file unless you know what you are doing.\n')
            except PermissionError as e:
                print('Maybe you do not have sufficient rights : ' + str(e))

    def write_global_settings(self, settings):  # pragma: no cover
        """
        Write settings of CMake.

        :param settings: global settings of CMake
        :type settings: dict
        """

        self.write_title('GLOBAL SETTINGS')
        self.cmakelists.write(
            'cmake_minimum_required(' + settings['min_required'] + ')'
        )
        self.cmakelists.write(
            'cmake_policy(' + settings['version'] + ')'
        )

    def write_variables(self, project):  # pragma: no cover
        """
        Write Project variables and data.

        :param project: project to build.
        :type project: Project
        """

        self.write_title('VARIABLES')
        for var in project.variables.values:
            current_var = dict(project.get_variable(var))
            if current_var.get('option') == 'get_filename_component':
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

    def write_project_data(self, language, definitions):  # pragma: no cover
        """
        Write project and definitions.

        :param language: language of project.
        :type language: str
        :param definitions: definitions of project.
        :type definitions: tuple
        """

        self.write_title('PROJECT')
        # Add Project
        if language == 'C++':
            current_language = 'CXX'
        elif language == 'C':
            current_language = language
        else:
            current_language = ''
        self.cmakelists.write(
            'project(${PROJECT_NAME} ' + current_language + ')\n')

        self.write_title('DEFINITIONS')
        # Preprocessor Definitions
        if definitions:
            self.cmakelists.write('add_definitions(\n')
            for index, definition in enumerate(definitions):
                self.cmakelists.write('    -D' + definition + '\n')
            self.cmakelists.write(')\n')

    def write_gnu_flags(self, gnu_flags):  # pragma: no cover
        """
        Write Flags for compilers.

        :param gnu_flags: Flags for GNU compiler.
        :type gnu_flags: dict
        """

        self.write_title('GNU FLAGS')
        self.cmakelists.write(
            'if ("${CMAKE_CXX_COMPILER_ID}" STREQUAL "GNU")\n')
        if 'C' in gnu_flags:
            if gnu_flags['C'].general:
                self.cmakelists.write('    set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} '
                                      + gnu_flags['C'].general
                                      + '")\n'
                                      )
                if gnu_flags['C'].debug:
                    self.cmakelists.write(
                        '    set(CMAKE_C_FLAGS_DEBUG "${CMAKE_C_FLAGS_DEBUG} '
                        + gnu_flags['C'].debug + '")\n')
                if gnu_flags['C'].release:
                    self.cmakelists.write(
                        '  set(CMAKE_C_FLAGS_RELEASE "${CMAKE_C_FLAGS_RELEASE} '
                        + gnu_flags['C'].release + '")\n')
        if 'C++' in gnu_flags:
            if gnu_flags['C++'].general:
                self.cmakelists.write(
                    '    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} '
                    + gnu_flags['C++'].general + '")\n')
            if gnu_flags['C++'].debug:
                self.cmakelists.write(
                    '    set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} '
                    + gnu_flags['C++'].debug + '")\n')
            if gnu_flags['C++'].release:
                self.cmakelists.write(
                    '    set(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE} '
                    + gnu_flags['C++'].release + '")\n')
        self.cmakelists.write('endif()\n')

    def write_clang_flags(self, clang_flags):  # pragma: no cover
        """
        Write Flags for compilers.

        :param clang_flags: Flags for Clang compiler.
        :type clang_flags: dict
        """

        self.write_title('CLANG FLAGS')
        self.cmakelists.write(
            'if ("${CMAKE_CXX_COMPILER_ID}" STREQUAL "Clang")\n')
        if 'C' in clang_flags:
            if clang_flags['C'].general:
                self.cmakelists.write(
                    '    set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} '
                    + clang_flags['C'].general + '")\n')
            if clang_flags['C'].debug:
                self.cmakelists.write(
                    '    set(CMAKE_C_FLAGS_DEBUG "${CMAKE_C_FLAGS_DEBUG} '
                    + clang_flags['C'].debug + '")\n')
            if clang_flags['C'].release:
                self.cmakelists.write(
                    '    set(CMAKE_C_FLAGS_RELEASE "${CMAKE_C_FLAGS_RELEASE} '
                    + clang_flags['C'].release + '")\n')
        if 'C++' in clang_flags:
            if clang_flags['C++'].general:
                self.cmakelists.write(
                    '    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} '
                    + clang_flags['C++'].general + '")\n')
            if clang_flags['C++'].debug:
                self.cmakelists.write(
                    '    set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} '
                    + clang_flags['C++'].debug + '")\n')
            if clang_flags['C++'].release:
                self.cmakelists.write(
                    '    set(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE} '
                    + clang_flags['C++'].release + '")\n')
        self.cmakelists.write('endif()\n')

    def write_msvc_flags(self, msvc_flags):  # pragma: no cover
        """
        Write Flags for compilers.

        :param msvc_flags: Flags for MSVC compiler.
        :type msvc_flags: dict
        """

        self.write_title('MSVC FLAGS')
        self.cmakelists.write(
            'if ("${CMAKE_CXX_COMPILER_ID}" STREQUAL "MSVC")\n')
        if 'C' in msvc_flags:
            if msvc_flags['C'].general:
                self.cmakelists.write(
                    '    set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} '
                    + msvc_flags['C'].general + '")\n')
            if msvc_flags['C'].debug:
                self.cmakelists.write(
                    '    set(CMAKE_C_FLAGS_DEBUG "${CMAKE_C_FLAGS_DEBUG} '
                    + msvc_flags['C'].debug + '")\n')
            if msvc_flags['C'].release:
                self.cmakelists.write(
                    '    set(CMAKE_C_FLAGS_RELEASE "${CMAKE_C_FLAGS_RELEASE} '
                    + msvc_flags['C'].release + '")\n')
        if 'C++' in msvc_flags:
            if msvc_flags['C++'].general:
                self.cmakelists.write(
                    '    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} '
                    + msvc_flags['C++'].general + '")\n')
            if msvc_flags['C++'].debug:
                self.cmakelists.write(
                    '    set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} '
                    + msvc_flags['C++'].debug + '")\n')
            if msvc_flags['C++'].release:
                self.cmakelists.write(
                    '    set(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE} '
                    + msvc_flags['C++'].release + '")\n')
        self.cmakelists.write('endif()\n')

    def write_directory_files(self, sources_dirs):  # pragma: no cover
        """
        Write different variables for directories of project.

        :param sources_dirs: Sources Directories.
        :type sources_dirs: dict
        """

        self.write_title('DIRECTORY FILES')
        for source_dir in sources_dirs:
            self.cmakelists.write('file(')
            if sources_dirs.get(source_dir)['recursive']:
                self.cmakelists.write('GLOB_RECURSE')
            else:
                self.cmakelists.write('GLOB')
            self.cmakelists.write(' ' + source_dir.upper() + '\n')
            sources_dir = sources_dirs.get(source_dir)['sources']
            for index, source in enumerate(sources_dir):
                if sources_dirs.get(source_dir)['from_proj']:
                    self.cmakelists.write(
                        '    ${PROJECT_DIR}/' + source + '\n')
                else:
                    self.cmakelists.write('    ' + source + '\n')
            self.cmakelists.write(')\n')

    def write_dependencies(self, dependencies):  # pragma: no cover
        """
        Write dependencies of project.

        :param dependencies: Dependencies of the project.
        :type dependencies: Externals
        """

        self.write_title('DEPENDENCIES')
        if dependencies.sub_directories:
            for sub in dependencies.sub_directories:
                current_sub = dependencies.sub_directories.get(
                    sub)
                self.cmakelists.write(
                    'add_subdirectory(' + current_sub['source_dir'] + ' '
                    + current_sub['binary_dir'] + ')\n')
        if dependencies.link_directories:
            link_directories = dependencies.link_directories
            for index, link in enumerate(link_directories):
                self.cmakelists.write(
                    'link_directories(' + link + ')\n')

    def write_targets(self, project):  # pragma: no cover
        """
        Write Targets and add sources Variables.

        :param project: CMake Project.
        :type project: Project
        """

        self.write_title('TARGETS')
        targets = project.targets
        for target in targets:
            # Create Targets
            if targets.get(target)['target_type'] == 'library':
                self.cmakelists.write('add_library(')
            if targets.get(target)['target_type'] == 'executable':
                self.cmakelists.write('add_executable(')
            if targets.get(target)['name'] == project.name:
                self.cmakelists.write('${PROJECT_NAME} ')
            else:
                self.cmakelists.write(
                    targets.get(target)['name'] + ' ')
            if targets.get(target)['shared']:
                self.cmakelists.write('SHARED\n')
            else:
                self.cmakelists.write('STATIC\n')

            # Add sources
            if project.sources_dirs:
                for source_dir in project.sources_dirs:
                    target_dir = project.sources_dirs.get(source_dir)['target']
                    if target_dir == targets.get(target)['name']:
                        self.cmakelists.write(
                            '    ${' + source_dir.upper() + '}\n')
            if project.sources_files:
                for source_file in project.sources_files:
                    files = project.sources_files.get(source_file)['files']
                    for index, file in enumerate(files):
                        if project.sources_files.get(source_file)['from_proj']:
                            self.cmakelists.write(
                                '    ${PROJECT_DIR}/' + file + '\n')
                        else:
                            self.cmakelists.write('    ' + file + '\n')
            self.cmakelists.write(')\n')

    def write_links(self, dependencies):  # pragma: no cover
        """
        Write Links for dependencies of project.

        :param dependencies: Dependencies of the project.
        :type dependencies: Externals
        """

        self.write_title('EXTERNAL LINKS')
        libraries = dependencies.libraries
        for lib in libraries:
            self.cmakelists.write('target_link_libraries(')
            self.cmakelists.write(libraries.get(lib)['target'])
            for l in libraries.get(lib)['libraries']:
                self.cmakelists.write(' ' + l)
            self.cmakelists.write(')')
