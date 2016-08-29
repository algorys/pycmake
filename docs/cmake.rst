.. _cmake:
.. highlight:: python

CMake
=====

Before beginning to create a project and try to compile it with PyCmake, you must create a :any:`CMake` object. He will used to manage common features and can receive your compilers.

    cmake = CMake()

Now you can add set global settings of CMake::

    min_required = 'VERSION 3.5'
    policy = 'VERSION 3.5'
    cmake.add_settings(min_required, policy)

Compilers
---------

You must add at least one compiler to get PyCmake functional. Then you can add other compilers, flags for each of them and manage global settings of CMake.

Valid **compiler_id** are currently:

    * GCC or G++
    * CLANG or CLANG++
    * MSVC or MSVC++

Let's create a :any:`Compiler` for GNU::

    compiler = Compiler()
    compiler_id = 'G++'
    compiler.create('G++-5', 'C++', compiler_id, 5, '/usr/bin/g++-5')

Now that the compiler was created, we can add it to our cmake object. CMake object has method and members for each supported compiler::

    cmake.gnu_compiler(compiler)
    # Or for Clang:
    # cmake.clang_compiler(compiler)

The advantage with the object Compiler is that you can easily use :func:`create` to create a new one and add it to our object CMake. But take care, it will replace the previous values.

Flags
-----

Your compiler can receive flags to ensure your project compiles as needed. You need object :any:`Flags` to make it::

    gcc_flags = Flags('G++-5 Flags', '-std=c++11', 'Wall', '-GL')
    cmake.flags_to_compiler(compiler_id, gcc_flags)

As you can see, flags name is not important, that's **compiler_id** who make the link between your flags and your compilers.

Now your CMake is ready to receive a Project.

