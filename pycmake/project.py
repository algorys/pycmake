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
        self.sources_dir = {}
        self.sources = {}
        self.dependencies = None
        self.targets = {}

    def create(self, name, language=''):
        """
        Create a project.

        :param name: name of the project.
        :param language: language of the project.
        """

        self.name = name
        self.language = language
        self.variables.add('PROJECT_NAME', name, option='set')

    def get_variable(self, name):
        try:
            return self.variables.values[name]
        except KeyError as e:
            print('Variable [' + name + '] does not exist: ' + str(e))

    def preprocessor_definitions(self, *definitions):
        """
        Add Preprocessor Definitions.

        :param definitions: add preprocessor definitions to project: FOO BAR
        """

        self.definitions = definitions

    def project_dir(self, path):
        """
        Set the main dir of the project.

        :param path: relative or absolute path from CMakeLists.txt.
        """

        if not os.path.exists(path):
            raise ValueError('This path does not exists : ' + path)
        elif not self.name:
            raise KeyError('Project was not been created, you must create it before.')
        else:
            var_name = self.name.upper() + '_DIR'
            self.variables.add(var_name, path, option='set')

    def add_library(self, name, shared=False):
        """
        Add a Library target.

        :param name:
        :param shared:
        """

        self.targets[name] = {
            'name': name,
            'shared': shared,
            'target_type': 'library'
        }

    def add_executable(self, name):
        """
        Add an executable target.

        :param name:
        """

        self.targets[name] = {
            'name': name,
            'target_type': 'executable'
        }

    def library_output_path(self, path):
        """
        Set Output Path for Shared Libraries.

        :param path: relative or absolute path.
        """

        if not self.name:
            raise KeyError('Project was not been created, you must create it before.')
        else:
            self.variables.add('LIBRARY_OUTPUT_PATH', path, option='set')

    def archive_output_path(self, path):
        """
        Set Output Path for Static Libraries.

        :param path: relative or absolute path.
        """

        if not self.name:
            raise KeyError('Project was not been created, you must create it before.')
        else:
            self.variables.add('ARCHIVE_OUTPUT_PATH', path, option='set')

    def executable_output_path(self, path):
        """
        Set Output Path for Executables.

        :param path: relative or absolute path.
        """

        if not self.name:
            raise KeyError('Project was not been created, you must create it before.')
        else:
            self.variables.add('EXECUTABLE_OUTPUT_PATH', path, option='set')

    def add_version(self, major, minor, patch, tweak=0):
        """

        :param major:
        :param minor:
        :param patch:
        :param tweak:
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

    def add_source_directories(self, dirs_id, target, *sources, recursive=False, from_proj=False):
        """
        Add one or many sources directories to Project.

        :param dirs_id: id of the directories.
        :param target: add directories to a specific target.
        :param sources: source directories to add.
        :param recursive: resursive or not
        :param from_proj: append ${PROJECT_DIR} to source directories if True.
        """

        if target not in self.targets:
            raise ValueError('Target: ' + target + ' does not exist. Create it before !')
        self.sources_dir[dirs_id] = {
            'target': target,
            'sources': sources,
            'recursive': recursive,
            'from_proj': from_proj,
        }

    def add_source_files(self, files_id, target, *files, from_proj=False):
        """
        Add one or many sources files to Project.

        :param files_id: id of the files.
        :param target: add files to a specific target.
        :param files: files to add.
        :param from_proj: add ${PROJECT_DIR} to source files if True.
        """

        self.sources[files_id] = {
            'target': target,
            'files': files,
            'from_proj': from_proj,
        }

    def add_dependencies(self, dependencies):
        self.dependencies = dependencies
