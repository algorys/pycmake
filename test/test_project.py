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
from pycmake.externals import Externals
from pycmake.sources import Sources, SRC_TYPE


class TestProject(unittest2.TestCase):
    """
        This file test Project class.
    """

    def test_create(self):
        under_test = Project()

        under_test.create('MyProject', 'CXX')

        self.assertEqual('MyProject', under_test.name)
        self.assertEqual('CXX', under_test.language)
        self.assertTrue(under_test.get_variable('PROJECT_NAME'))

    def test_get_variable(self):
        under_test = Project()

        under_test.create('MyProject', 'CXX')

        self.assertEqual({'name': 'PROJECT_NAME', 'value': 'MyProject', 'option': 'set'},
                         under_test.get_variable('PROJECT_NAME'))


    def test_preprocessor_definition(self):
        under_test = Project()
        under_test.preprocessor_definitions('UNICODE', 'NDEBUG')

        self.assertEqual('UNICODE', under_test.definitions[0])
        self.assertEqual('NDEBUG', under_test.definitions[1])

    def test_add_library_and_executable(self):
        under_test = Project()

        self.assertFalse(under_test.targets)

        under_test.add_library_target('MyLib', shared=True)

        self.assertTrue(under_test.targets)
        self.assertEqual(True, under_test.targets.get('MyLib')['shared'])
        self.assertEqual('library', under_test.targets.get('MyLib')['target_type'])

        under_test.add_executable_target('MyExe')
        self.assertEqual('executable', under_test.targets.get('MyExe')['target_type'])

    def test_add_files(self):
        under_test = Project()
        under_test.create('MyProject', 'CXX')
        under_test.add_executable_target('myexe')

        src_files = Sources()
        src_files.add('files', SRC_TYPE[1], ['src/main.cpp', 'src/stream.cpp'])

        under_test.add_sources_to_target('myexe', src_files)

        self.assertFalse(under_test.sources_files.get('files')['from_proj'])
        self.assertEqual(['src/main.cpp', 'src/stream.cpp'],
                         under_test.sources_files.get('files')['files'])

    def test_add_sources_directory(self):
        under_test = Project()
        under_test.create('MyLib', 'CXX')
        under_test.add_library_target('mylib', shared=True)

        src_dir_cpp = Sources()
        src_dir_cpp.add('cpp', SRC_TYPE[0], ['src/*.cpp', 'src/test/*.cpp'], from_proj=True)
        src_dir_cpp.make_recursive(True)

        src_dir_header = Sources()
        src_dir_header.add('header', SRC_TYPE[0], ['src/*.h', 'src/test/*.h'])

        under_test.add_sources_to_target('mylib', src_dir_cpp)
        under_test.add_sources_to_target('mylib', src_dir_header)

        self.assertEqual(['src/*.cpp', 'src/test/*.cpp'],
                         under_test.sources_dirs.get('cpp')['sources'])
        self.assertTrue(under_test.sources_dirs.get('cpp')['recursive'])
        self.assertTrue(under_test.sources_dirs.get('cpp')['from_proj'])

        self.assertEqual(['src/*.h', 'src/test/*.h'],
                         under_test.sources_dirs.get('header')['sources'])
        self.assertFalse(under_test.sources_dirs.get('header')['recursive'])
        self.assertFalse(under_test.sources_dirs.get('header')['from_proj'])

    def test_add_version(self):
        under_test = Project()
        under_test.add_version(1, 2, 3)

        self.assertEqual(1, under_test.version.get('major'))
        self.assertEqual(2, under_test.version.get('minor'))
        self.assertEqual(3, under_test.version.get('patch'))
        self.assertEqual(0, under_test.version.get('tweak'))

    def test_add_dependencies(self):
        under_test = Project()

        depends = Externals()
        depends.add_subdirectory('zlib', '${PROJECT_DIR}/external/zlib', '${PROJECT_DIR}/build/zlib')
        depends.add_subdirectory('g3log', '${PROJECT_DIR}/external/g3log', '${PROJECT_DIR}/build/g3log')

        under_test.add_dependencies(depends)

        self.assertEqual('${PROJECT_DIR}/external/zlib',
                         under_test.dependencies.sub_directories.get('zlib')['source_dir'])
        self.assertEqual('${PROJECT_DIR}/build/zlib',
                         under_test.dependencies.sub_directories.get('zlib')['binary_dir'])
        self.assertEqual('${PROJECT_DIR}/external/g3log',
                         under_test.dependencies.sub_directories.get('g3log')['source_dir'])
        self.assertEqual('${PROJECT_DIR}/build/g3log',
                         under_test.dependencies.sub_directories.get('g3log')['binary_dir'])
