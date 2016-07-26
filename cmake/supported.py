from enum import Enum

class Language(Enum):
    C = 'C'
    CXX = 'CXX'

class CCompiler(Enum):
    GCC = 'gcc'
    CLANG = 'Clang'
    MSVC = 'MSVC'

class CXXCompiler(Enum):
    GXX = 'g++'
    CLANGXX = 'Clang++'
    MSVC = 'MSVC'