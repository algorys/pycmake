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

from pycmake.compiler import Compiler

class TestCompiler(unittest2.TestCase):
    """
    This file test Compiler class.
    """

    def test_add_c_compiler(self):
        under_test = Compiler()

        under_test.create_compiler('GCC-Debian', 'C', 'GCC', 5, '/usr/bin/gcc-5')

        self.assertEqual('GCC-Debian', under_test.name)
        self.assertEqual('C', under_test.language)
        self.assertEqual('GCC', under_test.compiler)
        self.assertEqual(5, under_test.version)
        self.assertEqual('/usr/bin/gcc-5', under_test.executable)

    def test_add_cpp_compiler(self):
        under_test = Compiler()

        under_test.create_compiler('Clang++-Debian', 'CXX', 'CLANGXX', 3.7, '/usr/bin/clang++-3.7')

        self.assertEqual('Clang++-Debian', under_test.name)
        self.assertEqual('CXX', under_test.language)
        self.assertEqual('CLANGXX', under_test.compiler)
        self.assertEqual(3.7, under_test.version)
        self.assertEqual('/usr/bin/clang++-3.7', under_test.executable)
