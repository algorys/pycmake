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

from pycmake.version import Version
from pycmake.variables import Variables


class Project(object):
    """
        CMakeProject contains all data related to project.
    """

    def __init__(self):
        self.name = None
        self.language = None
        self.version = None
        self.variables = Variables()

    def create(self, name, language=''):
        """
        Create a project.

        :param name: name of the project.
        :param language: language of the project.
        """

        self.name = name
        self.language = language
        self.variables.add('PROJECT_NAME', name, option='filename_component')

    def set_project_dir(self, path):
        """
        Set the main dir of the project.

        :param path: relative or absolute path from CMakeLists directory.
        """

        if not os.path.exists(path):
            raise ValueError('This path does not exists : ' + path)
        elif not self.name:
            raise KeyError('Project has no name, you must create it before.')
        else:
            var_name = self.name.upper() + '_DIR'
            self.variables.add(var_name, path, option='set')

    def add_version(self, version: Version):
        """
        Add a version to project.

        :param version: version to add.
        :type version: Version
        """

        self.version = version

