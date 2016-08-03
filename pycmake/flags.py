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
        Flags for general, debug and release compilations
    """

    def __init__(self, flags_id, general, debug='', release=''):
        """
        Compilation Flags.
        """

        self.flags_id = flags_id
        """
        :param flags_id: id of flags
        :type flags_id: str
        """
        self.general = general
        """
        :param general: flags for all targets.
        :type general: str
        """
        self.debug = debug
        """
        :param debug: flags for debug target
        :type debug: str
        """
        self.release = release
        """
        :param release: flags for release target.
        :type release: str
        """
