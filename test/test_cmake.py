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

from cmake.cmake import CMake

class TestCMake(unittest2.TestCase):
    """
        This file test PyCMake class
    """

    def test_add_project(self):
        under_test = CMake()

        under_test.add_project('project', 'CXX')

        self.assertIsNotNone(under_test.project)
        self.assertEqual('project', under_test.project.settings['name'])
        self.assertEqual('CXX', under_test.project.settings['language'])

    def test_add_compiler(self):
        under_test = CMake()

        under_test.add_compiler('Clang++-Debian', 'CXX', 'clang++', 3.7, '/usr/bin/clang++-3.7')

        self.assertTrue(under_test.compilers.get('Clang++-Debian'))

    def test_add_multiple_compiler(self):
        under_test = CMake()

        under_test.add_compiler('Clang++-Debian', 'CXX', 'clang++', 3.7, '/usr/bin/clang++-3.7')
        under_test.add_compiler('GCC-Debian', 'C', 'gcc', 5, '/usr/bin/gcc-5')

        self.assertTrue(under_test.compilers.get('Clang++-Debian'))
        self.assertTrue(under_test.compilers.get('GCC-Debian'))



