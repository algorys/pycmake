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

from enum import Enum


class DependsType(Enum):
    CMAKEPROJECT = 1
    PACKAGE = 2
    BINARYFILE = 3


class Externals(object):
    """
        Externals contains all dependencies related to project.
    """

    def __init__(self):
        self.dependencies = {}

    def add_dependency(self, depends_type: DependsType, name, path='', ):
        """

        :param depends_type: indicate type of external. CMAKEPROJECT, PACKAGE or BINARYFILE
        :type depends_type: Enum.
        :param name: name of library.
        :param path: path of the library
        """

        self.dependencies[name] = {
            'type': depends_type,
            'name': name,
            'path': path,
        }