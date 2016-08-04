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

from pycmake.cmake import CMake
from pycmake.compiler import Compiler
from pycmake.flags import Flags


class TestCMake(unittest2.TestCase):
    """
        This file test PyCMake class
    """

    clang_cxx = Compiler()
    clang_cxx.create('Clang++-Debian', 'CXX', 'CLANG++', 3.7, '/usr/bin/clang++-3.7')

    gcc = Compiler()
    gcc.create('GCC-Debian', 'C', 'GCC', 5, '/usr/bin/gcc-5')

    msvc = Compiler()
    msvc.create('MSVC', 'CXX', 'MSVC++', 14, 'C:\\Program Files (x86)\\Microsoft Visual Studio 14.0\\VC\\bin\\amd64\\vcvars64.bat')

    def test_add_settings(self):
        under_test = CMake()

        under_test.add_settings('VERSION 2.7', 'VERSION 2.7')
        self.assertEqual('VERSION 2.7', under_test.settings.get('min_required'))
        self.assertEqual('VERSION 2.7', under_test.settings.get('policy'))

    def test_gnu_compiler(self):
        under_test = CMake()

        self.assertFalse(under_test.gnu)

        under_test.gnu_compiler(TestCMake.gcc)

        self.assertTrue(under_test.gnu)

    def test_clang_compiler(self):
        under_test = CMake()

        self.assertFalse(under_test.clang)

        under_test.clang_compiler(TestCMake.clang_cxx)

        self.assertTrue(under_test.clang)

    def test_msvc_compiler(self):
        under_test = CMake()

        self.assertFalse(under_test.msvc)

        under_test.msvc_compiler(TestCMake.msvc)

        self.assertTrue(under_test.msvc)

    def test_add_multiple_compiler(self):
        under_test = CMake()

        self.assertFalse(under_test.clang)
        self.assertFalse(under_test.gnu)

        under_test.clang_compiler(TestCMake.clang_cxx)
        under_test.gnu_compiler(TestCMake.gcc)

        self.assertTrue(under_test.clang)
        self.assertTrue(under_test.gnu)

    def test_add_flags_to_compiler(self):
        under_test = CMake()

        flags_gnu_test = Flags('G++-5', '-std=c++11', 'Wall', '-GL')
        flags_clang_test = Flags('Clang++-3.7', '-std=c++11 -stdlib=libc++', 'Wall', '-GL')
        flags_msvc_test = Flags('MSVC++', '/W4', '/MDd', '/GL')

        self.assertFalse(under_test.gnu_flags)
        self.assertFalse(under_test.clang_flags)
        self.assertFalse(under_test.msvc_flags)

        under_test.flags_to_compiler('G++', flags_gnu_test)
        under_test.flags_to_compiler('CLANG++', flags_clang_test)
        under_test.flags_to_compiler('MSVC++', flags_msvc_test)

        self.assertTrue(under_test.gnu_flags)
        self.assertTrue(under_test.gnu_flags.get('C++'))
        self.assertEqual('G++-5', under_test.gnu_flags.get('C++').flags_id)
        self.assertEqual('-std=c++11', under_test.gnu_flags.get('C++').general)
        self.assertEqual('Wall', under_test.gnu_flags.get('C++').debug)
        self.assertEqual('-GL', under_test.gnu_flags.get('C++').release)

        self.assertTrue(under_test.clang_flags)
        self.assertTrue(under_test.clang_flags.get('C++'))
        self.assertEqual('Clang++-3.7', under_test.clang_flags.get('C++').flags_id)
        self.assertEqual('-std=c++11 -stdlib=libc++', under_test.clang_flags.get('C++').general)
        self.assertEqual('Wall', under_test.clang_flags.get('C++').debug)
        self.assertEqual('-GL', under_test.clang_flags.get('C++').release)

        self.assertTrue(under_test.msvc_flags)
        self.assertTrue(under_test.msvc_flags.get('C++'))
        self.assertEqual('MSVC++', under_test.msvc_flags.get('C++').flags_id)
        self.assertEqual('/W4', under_test.msvc_flags.get('C++').general)
        self.assertEqual('/MDd', under_test.msvc_flags.get('C++').debug)
        self.assertEqual('/GL', under_test.msvc_flags.get('C++').release)

