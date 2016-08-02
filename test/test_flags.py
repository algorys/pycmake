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

from pycmake.flags import Flags
from pycmake.cmake import CMake
from pycmake.compiler import Compiler


class TestFlags(unittest2.TestCase):
    """
        This file test Flags class
    """

    cmake_test = CMake()
    gcc = Compiler()
    gcc.create('GCC-Debian', 'C', 'GCC', 5, '/usr/bin/gcc-5')

    cmake_test.gnu_compiler(gcc)

    def test_flags(self):
        under_test = Flags('clang++3.7', 'std=c++11', 'Wall', '-GL')

        self.assertEqual('std=c++11', under_test.general)
        self.assertEqual('Wall', under_test.debug)
        self.assertEqual('-GL', under_test.release)

    def test_add_flags_to_compiler(self):
        under_test = Flags('G++-5', 'std=c++11', 'Wall', '-GL')

        TestFlags.cmake_test.flags_to_compiler('G++', under_test)

        self.assertTrue(TestFlags.cmake_test.gnu_flags)
        self.assertTrue(TestFlags.cmake_test.gnu_flags['C++'])
        self.assertEqual('std=c++11', TestFlags.cmake_test.gnu_flags.get('C++').general)
        self.assertEqual('Wall', TestFlags.cmake_test.gnu_flags.get('C++').debug)
        self.assertEqual('-GL', TestFlags.cmake_test.gnu_flags.get('C++').release)
