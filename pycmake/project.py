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


from pycmake.variables import Variables
from pycmake.sources import Sources
from pycmake.sources import SRC_TYPE


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

    def add_sources_to_target(self, target, src):
        """
        Add sources directory or files to a specific target.

        :param target: existing target.
        :type target: str
        :param src: the sources to add.
        :type src: Sources
        """

        if target not in self.targets:
            raise ValueError('Target: [' + target + '] does not exist !')
        if src.src_type == SRC_TYPE[0]:
            self.sources_dirs[src.name] = {
                'target': target,
                'sources': src.sources,
                'from_proj': src.from_proj,
                'recursive': src.is_recursive(),
            }
        if src.src_type == SRC_TYPE[1]:
            self.sources_files[src.name] = {
                'target': target,
                'files': src.sources,
                'from_proj': src.from_proj,
            }

    def add_dependencies(self, dependencies):
        """
        Add some dependencies to project.

        :param dependencies: dependencies of the project, like subdirectories or external link.
        :type dependencies: Externals
        """

        self.dependencies = dependencies
