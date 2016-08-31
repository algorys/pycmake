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

"""
    Externals contains all dependencies related to project.
"""


class Externals(object):
    """
        Class to manage dependencies.
    """

    def __init__(self):
        self.sub_directories = {}
        self.link_directories = None
        self.libraries = {}

    def add_subdirectory(self, subdir_id, source_dir, binary_dir):
        """
        Add one subdirectory to the build.

        :param subdir_id: id of the subdir.
        :type subdir_id: str
        :param source_dir: directory in which the source CMakeLists.txt is located
        :type source_dir: str
        :param binary_dir: directory in which to place the output files.
        :type binary_dir: str
        """

        self.sub_directories[subdir_id] = {
            'source_dir': source_dir,
            'binary_dir': binary_dir,
        }

    def add_link_directories(self, *directories):
        """
        Link with the specified directories.

        :param directories: directories in which the linker will look for libraries.
        :type directories: tuple
        """

        self.link_directories = directories

    def target_link_libraries(self, target, *libraries):
        """
        Link the libraries specified to the associated target.

        :param target: relevant target.
        :type target: str
        :param libraries: libraries to link to target.
        :type libraries: tuple
        """

        self.libraries[target] = {
            'target': target,
            'libraries': libraries
        }
