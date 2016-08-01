from enum import Enum


class Language(Enum):
    """
    Supported Languages.
    """
    C = 'C'
    CXX = 'CXX'


class CCompiler(Enum):
    """
    Supported C Compilers.
    """
    GCC = 'GCC'
    CLANG = 'CLANG'
    MSVC = 'MSVC'


class CXXCompiler(Enum):
    """
    Supported C++ Compilers.
    """
    GXX = 'G++'
    CLANGXX = 'CLANG++'
    MSVC = 'MSVC'
