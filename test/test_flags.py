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

    def test_add_flags_to_compiler(self):
        under_test = Flags('clang++3.7', 'std=c++11', 'Wall', '-GL')
        cmake = CMake()
        compiler = Compiler()
        compiler.create('Clang++-Debian', 'CXX', 'clang++', 3.7, '/usr/bin/clang++-3.7')

        cmake.add_compiler(compiler)

        self.assertEqual(False, under_test.use)

        under_test.add_to_cmake_compilers('CLANG', cmake)

        self.assertEqual(True, under_test.use)
