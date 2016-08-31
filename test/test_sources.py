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

from pycmake.sources import *



class TestSources(unittest2.TestCase):
    """
        This file test Sources class.
    """

    src = ['../../src/*.cpp', '../../src/*.h']

    def test_add_sources(self):
        under_test = Sources()

        under_test.add('src_dir', SRC_TYPE[0], TestSources.src, from_proj=True)

        self.assertEqual('src_dir', under_test.name)
        self.assertTrue(under_test.from_proj)
        self.assertFalse(under_test.is_recursive())
        self.assertEqual(
            ['../../src/*.cpp', '../../src/*.h'],
            under_test.sources
        )

    def test_sources_recursive(self):
        under_test = Sources()

        under_test.add('src_dir', SRC_TYPE[0], TestSources.src, from_proj=False)
        under_test.make_recursive(True)

        self.assertTrue(under_test.is_recursive())