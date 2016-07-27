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

from pycmake.externals import Externals, DependsType

class TestExternals(unittest2.TestCase):
    """
        This file test Externals class.
    """

    def test_externals(self):
        under_test = Externals()

        under_test.add_dependency(DependsType.PACKAGE, 'zlib', 'dependencies/zlib')

        self.assertEqual(DependsType.PACKAGE, under_test.dependencies.get('zlib')['type'])
        self.assertEqual('zlib', under_test.dependencies.get('zlib')['name'])
        self.assertEqual('dependencies/zlib', under_test.dependencies.get('zlib')['path'])


    def test_multiple_externals(self):
        under_test = Externals()

        under_test.add_dependency(DependsType.CMAKEPROJECT, 'graphics', '../../graphics')

        self.assertEqual(DependsType.CMAKEPROJECT, under_test.dependencies.get('graphics')['type'])
        self.assertEqual('graphics', under_test.dependencies.get('graphics')['name'])
        self.assertEqual('../../graphics', under_test.dependencies.get('graphics')['path'])

        under_test.add_dependency(DependsType.BINARYFILE, 'core', 'dependencies/core')

        self.assertEqual(DependsType.BINARYFILE, under_test.dependencies.get('core')['type'])
        self.assertEqual('core', under_test.dependencies.get('core')['name'])
        self.assertEqual('dependencies/core', under_test.dependencies.get('core')['path'])