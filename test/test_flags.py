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

from cmake.flags import Flags

class TestFlags(unittest2.TestCase):
    """
        This file test Flags class
    """

    def test_gcc_flags(self):
        under_test = Flags()

        under_test.define_gcc_flags('-std=c++11', '-O2', '-w')

        self.assertEqual('-std=c++11', under_test.gcc_flags['general'])
        self.assertEqual('-O2', under_test.gcc_flags['debug'])
        self.assertEqual('-w', under_test.gcc_flags['release'])

    def test_clang_flags(self):
        under_test = Flags()

        under_test.define_clang_flags('-std=c++11 -stdlib=libc++', '-O2', '-w')

        self.assertEqual('-std=c++11 -stdlib=libc++', under_test.clang_flags['general'])
        self.assertEqual('-O2', under_test.clang_flags['debug'])
        self.assertEqual('-w', under_test.clang_flags['release'])

    def test_msvc_flags(self):
        under_test = Flags()

        under_test.define_msvc_flags('/W4', '/MDd', '/GL')

        self.assertEqual('/W4', under_test.msvc_flags['general'])
        self.assertEqual('/MDd', under_test.msvc_flags['debug'])
        self.assertEqual('/GL', under_test.msvc_flags['release'])