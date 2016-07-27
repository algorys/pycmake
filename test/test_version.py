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

import unittest2

from pycmake.version import ProjectVersion

class TestVersion(unittest2.TestCase):
    """
        This file test Flags class.
    """

    def test_project_version(self):
        under_test = ProjectVersion(0, 1, 1, 387)

        self.assertEqual(0, under_test.major)
        self.assertEqual(1, under_test.minor)
        self.assertEqual(1, under_test.patch)
        self.assertEqual(387, under_test.tweak)

    def test_get_version(self):
        under_test = ProjectVersion(1, 2, 0, 485)

        self.assertEqual({'major':1, 'minor':2, 'patch':0, 'tweak':485}, under_test.get_version())

    def test_string_version(self):
        under_test = ProjectVersion(2, 0, 0, 12)

        self.assertEqual('2.0.0.12', under_test.get_string_version())