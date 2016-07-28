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


class Version(object):
    """
        ProjectVersion defines versions of project.
    """

    def __init__(self, major=0, minor=0, patch=0, tweak=0):
        """

        :param major: Major digit.
        :param minor: Minor digit.
        :param patch: Patch digit.
        :param tweak: Tweak digit.
        """
        self.major = major
        self.minor = minor
        self.patch = patch
        self.tweak = tweak

    def get_version(self):
        """
        :return: dict of digits.
        """
        return {
            'major': self.major,
            'minor': self.minor,
            'patch': self.patch,
            'tweak': self.tweak,
        }

    def get_string_version(self):
        """
        :return: Return string version 'x.x.x.x'
        """
        return str(self.major) + '.' \
            + str(self.minor) + '.' \
            + str(self.patch) + '.' \
            + str(self.tweak)
