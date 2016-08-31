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

"""
    Compiler define every supported compilers.
"""

from pycmake.supported import LANGUAGE
from pycmake.supported import C_COMPILER
from pycmake.supported import CXX_COMPILER


class Compiler(object):
    """
        Class to define a compiler.
    """

    def __init__(self):
        self.name = None
        self.version = None
        self.language = None
        self.compiler_id = None
        self.executable = None

    @staticmethod
    def check_compiler_options(language, compiler_id):  # pragma: no cover
        """
        Check if compiler is valid. Used for each :func:`~create`.

        :param language: language of project. For more details, see
            :func:`LANGUAGE <pycmake.supported.LANGUAGE>`.
        :type language: str
        :param compiler_id: id of compiler. For more details, see
            :func:`C_COMPILER <pycmake.supported.C_COMPILER>` or
            :func:`CXX_COMPILER <pycmake.supported.CXX_COMPILER>`.
        :type compiler_id: str
        """

        if language not in LANGUAGE:
            raise ValueError('Language ' + language + ' is not currently supported !')
        if language is LANGUAGE[0]:
            if compiler_id not in C_COMPILER:
                raise ValueError('C compiler ' + compiler_id + ' is not currently supported !')
        if language is LANGUAGE[1]:
            if compiler_id not in CXX_COMPILER:
                raise ValueError('C++ compiler ' + compiler_id + ' is not currently supported !')

    def create(self, name, language, compiler_id, version, executable):
        # pylint: disable=too-many-arguments
        """
        Create a compiler.

        :param name: name of compiler.
        :type name: str
        :param language: language of project. For more details, see
            :func:`LANGUAGE <pycmake.supported.LANGUAGE>`.
        :type language: str
        :param compiler_id: id of compiler. For more details, see
            :func:`C_COMPILER <pycmake.supported.C_COMPILER>` or
            :func:`CXX_COMPILER <pycmake.supported.CXX_COMPILER>`.
        :type compiler_id: str
        :param version: version of the compiler.
        :type version: int or float
        :param executable: full path to the executable.
        :type executable: str
        """

        if not isinstance(version, int) and not isinstance(version, float):
            raise ValueError('Version must be an integer or a float !')

        Compiler.check_compiler_options(language, compiler_id)
        self.name = name
        self.language = language
        self.version = version
        self.compiler_id = compiler_id
        self.executable = executable
