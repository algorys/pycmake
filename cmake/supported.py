from enum import Enum

class Language(Enum):
    C = 'C'
    CXX = 'CXX'

class CCompiler(Enum):
    GCC = 'GCC'
    CLANG = 'CLANG'
    MSVC = 'MSVC'

class CXXCompiler(Enum):
    GXX = 'GXX'
    CLANGXX = 'CLANGXX'
    MSVC = 'MSVC'
