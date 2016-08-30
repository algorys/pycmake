.. _cmake:
.. highlight:: python

CMake
=====

Before beginning to create a project and try to compile it with PyCmake, you must create a :any:`CMake` object. He will used to manage common features and can receive your compilers::

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
    # And for MSVC
    # cmake.msvc_compiler(compiler)

The advantage with the object Compiler is that you can easily use :func:`create` to create a new one and add it to our object CMake. But take care, it will replace the previous values.

**For Windows:**

You have to precise full path of ``.bat`` you want to execute before compiling, if you want to use ``NMake Makefiles``. 

Example: "C:\\Program Files (x86)\\Microsoft Visual Studio 14.0\\VC\\bin\\amd64\\vcvars64.bat".

Flags
-----

Your compiler can receive flags to ensure your project compiles as needed. You need object :any:`Flags` to make it::

    gcc_flags = Flags('G++-5 Flags', '-std=c++11', 'Wall', '-GL')
    cmake.flags_to_compiler(compiler_id, gcc_flags)

As you can see, flags name is not important, that's **compiler_id** who make the link between your flags and your compilers.

Now your CMake is ready to receive a Project.

Before Continuing
-----------------

When you use PyCmake, you must pay attention to the way that you will give your projects. 

Paths should be **relative** depending on the folder in which your *CMakeLists.txt* will be located. No matter where you run your python script, your paths must first consider this location.

For example, you will run your script in ``/home/user/scripts`` or other, no matter.

Let's say your project sources are located in ``/home/user/workspace/project/src`` and your **CMakeLists.txt** will be write in folder ``/home/user/workspace/project/platform/cmake``.

If you want to add sources, your paths will be something like ``../../src``. Example::

    project.add_source_files('files',
                             'mylib',
                             True,
                             '../../src/file.cpp'
                            )

See :ref:`Files and Directories <files>` for more information.

Other case is when you want define **PROJECT_DIR** variable and use it throughout your script. You have to give the following path::

    project.variables.project_dir('../../')

Because CMake must go up two folders to define the root of your project (see :ref:`CMake Variables <variables>`).
