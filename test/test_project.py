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

from pycmake.project import Project


class TestProject(unittest2.TestCase):
    """
        This file test Project class.
    """

    def test_create_project(self):
        under_test = Project()

        under_test.create('MyProject', 'CXX')

        self.assertEqual('MyProject', under_test.name)
        self.assertEqual('CXX', under_test.language)
        self.assertTrue(under_test.get_variable('PROJECT_NAME'))

    def test_set_project_dir(self):
        under_test = Project()
        under_test.create('My2Lib', '')

        under_test.project_dir('./cmake')

        self.assertTrue(under_test.get_variable('MY2LIB_DIR'))
        self.assertEqual('./cmake', under_test.get_variable('MY2LIB_DIR')['value'])

    def test_outputs(self):
        under_test = Project()
        under_test.create('MyProject', 'CXX')

        under_test.executable_output_path('../../build/bin')
        under_test.library_output_path('../../build/lib')
        under_test.archive_output_path('../../build/lib')

        self.assertTrue(under_test.get_variable('EXECUTABLE_OUTPUT_PATH'))
        self.assertEqual('../../build/bin',
                         under_test.get_variable('EXECUTABLE_OUTPUT_PATH')['value'])
        self.assertTrue(under_test.get_variable('LIBRARY_OUTPUT_PATH'))
        self.assertEqual('../../build/lib',
                         under_test.get_variable('LIBRARY_OUTPUT_PATH')['value'])
        self.assertTrue(under_test.get_variable('ARCHIVE_OUTPUT_PATH'))
        self.assertEqual('../../build/lib',
                         under_test.get_variable('ARCHIVE_OUTPUT_PATH')['value'])

    def test_add_sources(self):
        under_test = Project()
        under_test.create('MyProject', 'CXX')

        under_test.add_sources('cpp', '../../main.cpp ../../graphics.cpp')
        under_test.add_sources('headers', '../../graphics.h ../../stdafx.h')
        under_test.add_sources('config', '/home/user/config/config.cpp', from_proj=False)

        self.assertTrue(under_test.sources.get('cpp')['from_proj'])
        self.assertEqual('../../main.cpp ../../graphics.cpp',
                         under_test.sources.get('cpp')['sources'])
        self.assertTrue(under_test.sources.get('headers')['from_proj'])
        self.assertEqual('../../graphics.h ../../stdafx.h',
                         under_test.sources.get('headers')['sources'])
        self.assertFalse(under_test.sources.get('config')['from_proj'])

    def test_add_sources_directory(self):
        under_test = Project()
        under_test.create('MyLib', 'CXX')

        under_test.add_sources_directory('dir_cpp',
                                         '../../lib/src',
                                         '.cpp',
                                         recursive=False)
        under_test.add_sources_directory('dir_header',
                                         '../../lib/src/includes',
                                         '.h',
                                         recursive=False)

        self.assertEqual('../../lib/src', under_test.sources_dir.get('dir_cpp')['path'])
        self.assertFalse(under_test.sources_dir.get('dir_cpp')['recursive'])
        self.assertTrue(under_test.sources_dir.get('dir_cpp')['from_proj'])
        self.assertEqual('../../lib/src/includes', under_test.sources_dir.get('dir_header')['path'])
        self.assertFalse(under_test.sources_dir.get('dir_header')['recursive'])
        self.assertEqual('.h', under_test.sources_dir.get('dir_header')['ext'])
