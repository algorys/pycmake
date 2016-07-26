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

    def __init__(self):
        self.gcc_flags = None
        self.clang_flags = None
        self.msvc_flags = None

    def define_gcc_flags(self, general, debug, release):
        self.gcc_flags = {
            'general': general,
            'debug': debug,
            'release': release
        }

    def define_clang_flags(self, general, debug, release):
        self.clang_flags = {
            'general': general,
            'debug': debug,
            'release': release
        }

    def define_msvc_flags(self, general, debug, release):
        self.msvc_flags = {
            'general': general,
            'debug': debug,
            'release': release
        }