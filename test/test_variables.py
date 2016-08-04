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

from pycmake.variables import Variables


class TestVariables(unittest2.TestCase):
    """
        This file test Variables class.
    """

    def test_add_variable(self):
        under_test = Variables()

        self.assertFalse(under_test.values)

        under_test.add('MyVariable', 'my value')

        self.assertTrue(under_test.values)
        self.assertEqual('MyVariable', under_test.values.get('MyVariable')['name'])
        self.assertEqual('my value', under_test.values.get('MyVariable')['value'])
        self.assertNotEqual('my other value', under_test.values.get('MyVariable')['value'])
        self.assertEqual('set', under_test.values.get('MyVariable')['option'])

    def test_project_dir(self):
        under_test = Variables()

        under_test.project_dir('../../..')

        self.assertTrue(under_test.values.get('PROJECT_DIR'))
        self.assertEqual('../../..', under_test.values.get('PROJECT_DIR')['value'])
        self.assertEqual('get_filename_component', under_test.values.get('PROJECT_DIR')['option'])


    def test_outputs(self):
        under_test = Variables()

        under_test.executable_output_path('../../build/bin')
        under_test.library_output_path('../../build/lib')
        under_test.archive_output_path('../../build/lib')

        self.assertTrue(under_test.values.get('EXECUTABLE_OUTPUT_PATH'))
        self.assertEqual('../../build/bin',
                         under_test.values.get('EXECUTABLE_OUTPUT_PATH')['value'])
        self.assertTrue(under_test.values.get('LIBRARY_OUTPUT_PATH'))
        self.assertEqual('../../build/lib',
                         under_test.values.get('LIBRARY_OUTPUT_PATH')['value'])
        self.assertTrue(under_test.values.get('ARCHIVE_OUTPUT_PATH'))
        self.assertEqual('../../build/lib',
                         under_test.values.get('ARCHIVE_OUTPUT_PATH')['value'])
