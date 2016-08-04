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

from pycmake.variables import Variables


class Project(object):
    """
        CMakeProject contains all data related to project.
    """

    def __init__(self):
        self.name = None
        self.language = None
        self.version = None
        self.definitions = None
        self.variables = Variables()
        self.sources_dirs = {}
        self.sources_files = {}
        self.dependencies = None
        self.targets = {}

    def create(self, name, language):
        """
        Create a project.

        :param name: name of the project.
        :type name: str
        :param language: language of the project.
        :type language: str
        """

        self.name = name
        self.language = language
        self.variables.add('PROJECT_NAME', name, option='set')

    def get_variable(self, name):
        """
        Returns the contents of the specified **variable**.
        Will look into :class:`~pycmake.variables.Variables`

        :param name: the name of the desired variable.
        :type name: str
        :return: a variable of the project.
        :rtype: dict
        """

        try:
            return self.variables.values[name]
        except KeyError as e:
            print('Variable [' + name + '] does not exist: ' + str(e))

    def preprocessor_definitions(self, *definitions):
        """
        Add Preprocessor Definitions.

        :param definitions: add preprocessor definitions to project: FOO BAR
        :type definitions: tuple
        """

        self.definitions = definitions

    def project_dir(self, path):
        """
        Defines the main project directory in a variable named: PROJECT_DIR.

        :param path: relative path from CMakeLists.txt.
        :type path: str
        """

        if not self.name:
            raise KeyError('Project was not been created, you must create it before.')
        else:
            self.variables.add('PROJECT_DIR', path, option='set')

    def add_library_target(self, name, shared=False):
        """
        Add a Library target.

        :param name: the library name.
        :type name: str
        :param shared: shared library or not.
        :type shared: bool
        """

        self.targets[name] = {
            'name': name,
            'shared': shared,
            'target_type': 'library'
        }

    def add_executable_target(self, name):
        """
        Add an executable target.

        :param name: name of the executable.
        :type name: str
        """

        self.targets[name] = {
            'name': name,
            'target_type': 'executable'
        }

    def library_output_path(self, path):
        """
        Output Path for Shared libraries and add LIBRARY_OUTPUT_PATH variable.

        :param path: path where build Shared libraries.
        :type path: str
        """

        if not self.name:
            raise KeyError('Project was not been created, you must create it before.')
        else:
            self.variables.add('LIBRARY_OUTPUT_PATH', path, option='set')

    def archive_output_path(self, path):
        """
        Output Path for Static libraries and add ARCHIVE_OUTPUT_PATH variable.

        :param path: path where build Static libraries.
        :type path: str
        """

        if not self.name:
            raise KeyError('Project was not been created, you must create it before.')
        else:
            self.variables.add('ARCHIVE_OUTPUT_PATH', path, option='set')

    def executable_output_path(self, path):
        """
        Output Path for Executables and add EXECUTABLE_OUTPUT_PATH variable.

        :param path: path where build executable.
        :type path: str
        """

        if not self.name:
            raise KeyError('Project was not been created, you must create it before.')
        else:
            self.variables.add('EXECUTABLE_OUTPUT_PATH', path, option='set')

    def add_version(self, major, minor, patch, tweak=0):
        """

        :param major: number of Major Version
        :type major: int
        :param minor: Number of Minor Version
        :type minor: int
        :param patch: Number of Patch version
        :type patch: int
        :param tweak: Number of Tweak version.
        :type tweak: int
        """
        try:
            isinstance(major, int)
            isinstance(minor, int)
            isinstance(patch, int)
            isinstance(tweak, int)
        except ValueError:
            print('Version digits must be Integer !')

        self.version = {
            'major': major,
            'minor': minor,
            'patch': patch,
            'tweak': tweak
        }

    def add_source_directories(self, dirs_id, target, recursive, from_proj, *sources):
        """
        Add one or many sources directories to project.

        :param dirs_id: id of the directories.
        :type dirs_id: str
        :param target: add directories to a specific target.
        :type target: str
        :param recursive: recursive or not
        :type recursive: bool
        :param from_proj: if True, append to ${PROJECT_DIR} variable, see :func:`~project_dir`
        :type from_proj: bool
        :param sources: source directories to add.
        :type sources: tuple
        """

        if target not in self.targets:
            raise ValueError('Target: ' + target + ' does not exist. Create it before !')
        self.sources_dirs[dirs_id] = {
            'target': target,
            'sources': sources,
            'recursive': recursive,
            'from_proj': from_proj,
        }

    def add_source_files(self, files_id, target, from_proj=False, *files):
        """
        Add one or many sources files to project.

        :param files_id: id of the files.
        :type files_id: str
        :param target: add files to a specific target.
        :type target: str
        :param from_proj: add ${PROJECT_DIR} to source files if True.
        :type from_proj: bool
        :param files: files to add.
        :type files: tuple
        """

        self.sources_files[files_id] = {
            'target': target,
            'files': files,
            'from_proj': from_proj,
        }

    def add_dependencies(self, dependencies):
        """
        Add some dependencies to project.

        :param dependencies: dependencies of the project, like subdirectories or external link.
        :type dependencies: Externals
        """

        self.dependencies = dependencies
