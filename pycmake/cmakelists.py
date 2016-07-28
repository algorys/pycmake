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


class CMakeLists(object):
    """
        CMakeLists create, write CMakeLists.txt
    """

    def __init__(self):
        self.cmakelists = None

    def create_file(self, path):
        """
        Create CMakeLists.txt

        :param path: path where to create CMakeLists
        """

        if not os.path.exists(path):
            raise ValueError('This path does not exists : ' + path)
        else:
            if path[-1:] == '/' or path[-1:] == '\\':
                self.cmakelists = open(str(path) + 'CMakeLists.txt', 'w')
            else:
                self.cmakelists = open(str(path) + '/CMakeLists.txt', 'w')
        if self.cmakelists:
            try:
                self.cmakelists.write(
                    '# This file was automatically generated by PyCMake.\n')
                self.cmakelists.write(
                    '# WARNING: Do not edit this file unless you know what you are doing.\n')
            except PermissionError as e:
                print('Maybe you do not have sufficient rights : ' + str(e))
