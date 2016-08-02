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


class Flags(object):
    """
        Flags keep flags for compilations
    """

    def __init__(self, name, general, debug='', release=''):
        """
        Compilation Flags.

        :param name: name of flags
        :param general: flags for all targets.
        :param debug: flags for debug target
        :param release: flags for release target.
        """
        self.name = name
        self.general = general
        self.debug = debug
        self.release = release
