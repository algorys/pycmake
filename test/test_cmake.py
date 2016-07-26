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

class TestPyCMake(unittest2.TestCase):
    """
        This file test PyCMake class
    """

    def test_setttings(self):
        under_test = CMake()

        self.assertFalse(under_test.project)
        under_test.add_settings('VERSION 3.5', 'VERSION 3.5')

        self.assertEqual('VERSION 3.5', under_test.settings['min_required'])
        self.assertEqual('VERSION 3.5', under_test.settings['policy'])

    def test_add_project(self):
        under_test = CMake()

        under_test.add_project('project', 'CXX')

        self.assertIsNotNone(under_test.project)
        self.assertEqual('project', under_test.project.get('project')['name'])
        self.assertEqual('CXX', under_test.project.get('project')['language'])

    def test_add_version(self):
        under_test = CMake()

        under_test.add_version(1, 2, 0, 580)

        self.assertEqual(1, under_test.project.get('version').major)
        self.assertEqual(2, under_test.project.get('version').minor)
        self.assertEqual(0, under_test.project.get('version').patch)
        self.assertEqual(580, under_test.project.get('version').tweak)

    def test_add_compiler(self):
        under_test = CMake()

        under_test.add_compiler('Clang++-Debian', 'c++', 'clang++', 3.7, '/usr/bin/clang++-3.7')

        self.assertTrue(under_test.project.get('compilers')['Clang++-Debian'])

    def test_add_multiple_compiler(self):
        under_test = CMake()

        under_test.add_compiler('Clang++-Debian', 'c++', 'clang++', 3.7, '/usr/bin/clang++-3.7')
        under_test.add_compiler('GCC-Debian', 'C', 'gcc', 5, '/usr/bin/gcc-5')

        self.assertTrue(under_test.project.get('compilers')['Clang++-Debian'])
        self.assertTrue(under_test.project.get('compilers')['GCC-Debian'])


