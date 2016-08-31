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


from pycmake.supported import SRC_TYPE


class Sources(object):
    """
        Sources contains files and directory for a Project.
    """

    __recursive = False

    def __init__(self):
        self.name = None
        self.src_type = None
        self.from_proj = False
        self.sources = []

    def add(self, name, src_type, sources, from_proj=False):
        """
        Add sources with a specific type.

        :param name: name of the sources.
        :type name: str
        :param src_type: type of the sources: *DIR* or *FILE*
        :type src_type: SRC_TYPE
        :param from_proj: sources relative from project directory.
        :type from_proj: bool
        :param sources: sources to add.
        :type sources: list
        """

        self.name = name
        self.src_type = src_type
        self.from_proj = from_proj
        self.sources = sources

    def make_recursive(self, recursive):
        """
        Make sources directory recursive.

        :param recursive: recursive or not.
        :type recursive: bool
        """

        if self.src_type == SRC_TYPE[0]:
            self.__recursive = recursive
        else:
            raise ValueError('Sources Files can not be recursive.')

    def is_recursive(self):
        """
        Check if sources are recursive are not.

        """
        return self.__recursive
