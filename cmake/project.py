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


class Project(object):
    """
        CMakeProject contains all data related to project.
    """

    def __init__(self, name='project', language='CXX'):
        """

        :param name: name of CMake Project. Default: 'project'
        :param language: type of langage.
        """

        self.settings = {
            'name': name,
            'language': language
        }
        self.version = None

    def add_settings(self, min_required='VERSION 3.0', policy='VERSION 3.0'):
        self.settings['min_required'] = min_required
        self.settings['policy'] = policy

    def add_version(self, major=0, minor=0, patch=0, tweak=0):
        version = ProjectVersion(major=major, minor=minor, patch=patch, tweak=tweak)
        self.version = version

