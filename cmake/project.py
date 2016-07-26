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

from cmake.version import ProjectVersion
from cmake.compiler import Compiler
from cmake.flags import Flags
from cmake.externals import Externals
from cmake.variables import Variables

class Project(object):
    """
        CMakeProject contains all data related to project.
    """

    def __init__(self, name, langage):
        """

        :param name: name of CMake Project. Default: 'project'
        :param langage: type of langage.
        """
        self.name = name
        self.langage = ''
        self.version = None
        self.compiler = None
        self.flags = None
        self.externals = None
        self.variables = None

    def init_project(self):
        self.version = ProjectVersion(0,0,0,0)
        self.compiler = Compiler()
        self.flags = Flags()
        self.externals = Externals()
        self.variables = Variables()

