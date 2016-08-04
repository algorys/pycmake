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


class Variables(object):
    """
        Variables hold all project variables
    """

    def __init__(self):
        self.values = {}

    def add(self, name, value, option=''):
        """
        Add a variable.

        :param name: Name of the variable.
        :type name: str
        :param value: Value of variable.
        :type value: str
        :param option: option for variable: 'set' or 'filename_component'
        :type option: str
        """

        self.values[name] = {
            'name': name,
            'value': value,
            'option': option
        }

    def project_dir(self, path):
        """
        Defines the main project directory in a variable named: PROJECT_DIR.

        :param path: relative path from CMakeLists.txt.
        :type path: str
        """

        self.add('PROJECT_DIR', path, option='set')

    def library_output_path(self, path):
        """
        Add LIBRARY_OUTPUT_PATH variable for Shared libraries.

        :param path: path where build Shared libraries.
        :type path: str
        """

        self.add('LIBRARY_OUTPUT_PATH', path, option='set')

    def archive_output_path(self, path):
        """
        Add ARCHIVE_OUTPUT_PATH variable for Static libraries.

        :param path: path where build Static libraries.
        :type path: str
        """

        self.add('ARCHIVE_OUTPUT_PATH', path, option='set')

    def executable_output_path(self, path):
        """
        Add EXECUTABLE_OUTPUT_PATH variable for executables.

        :param path: path where build executables.
        :type path: str
        """

        self.add('EXECUTABLE_OUTPUT_PATH', path, option='set')
