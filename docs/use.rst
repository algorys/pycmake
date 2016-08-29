.. _use:
.. highlight:: python

How to use PyCMake
==================

CMake
-----

First you need to create a :any:`CMake` instance, which will be used to manage common features::

    cmake = CMake()

Then we can set global settings of CMake::

    min_required = 'VERSION 3.5'
    policy = 'VERSION 3.5'
    cmake.add_settings(min_required, policy)

Compilers
~~~~~~~~~

You must add at least one compiler to get it functional. Then you can add other compilers, flags for each of them and manage global settings of CMake.

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

The advantage with the object Compiler is that you can easily :func:`create` a new one and add it to our object CMake. But take care, it will replace the previous values.

Flags
~~~~~

Your compiler can receive flags to ensure your project compiles as needed. You need object :any:`Flags` to make it::

    gcc_flags = Flags('G++-5 Flags', '-std=c++11', 'Wall', '-GL')
    cmake.flags_to_compiler(compiler_id, gcc_flags)

As you can see, flags name is not important, that's **compiler_id** who make the link between your flags and your compilers.

Now your CMake is ready to receive a Project.

Project
-------

The :any:`Project` is the heart of your script. He will contains all information about sources, dependencies, links, definitions, ...

Initialise object and create your project::

    project = Project()
    language = 'C++'
    project.create('myLib', 'C++')

Currently, only **C** and **C++** are valid language. During :func:`create`, PyCMake create a variable named **PROJECT_NAME** (See below).

Variables
~~~~~~~~~

To facilitate read and management of your project, PyCMake will help you to generate variable you can use after along the process.

There is some default variables who will be created and you can create your own if needed.

Predefined Variables
********************

* **PROJECT_NAME:** when the :func:`create` method is called, name of your project is automatically associated with this variable.
* **PROJECT_DIR:** you can use :func:`project_dir` method to set this variable. **WARNING:** you have to indicate a relative path from your future **CMakeLists.txt** location ! Cause this variable will define absolute path from this.
* **OUTPUTS:** you have 3 methods for each type of target. You have to give the path for each.

  * :func:`library_output_path`
  * :func:`archive_output_path`
  * :func:`executable_output_path`

Here is a way to use it::

    project.variables.library_output_path('${PROJECT_DIR}/build')

Feel free to use existing variables in your paths.

Custom Variables
****************

You can also add custom variables to your project. Simply type the following::

    project.variables.add('TEST_DIR', '${PROJECT_DIR}/${PROJECT_NAME}/src/tests')

You can add as many variables as you want or replace existing ones. The :any:`Project` object provides the :func:`get_variable` method to access any variable created.

Targets and Files
~~~~~~~~~~~~~~~~~

Now that your project is defined, you must add target(s) to build and her files. 

Targets
*******

There is 2 types of targets :

* **Libraries:** You have to precise the **true** name of your library. She can be shared or static. For a shared library called `libmylib.so` (or `mylib.dll` on Windows) or a static library::

    # If shared
    project.add_library_target('mylib', shared=True)
    # Or if static
    project.add_library_target('mylib')

* **Executables:** You have to precise the **true** name of your executable. Fo an executable called `myexe`::

    project.add_executable_target('myexe')

Then you must define the files or folders for each of your targets.

Files and Directories
*********************

**Note:** these methods will be reworked in the future to facilitate the addition of files and folders.

There are two distinct methods in PyCMake to add folders or files to your target. Each must receive a :class:`tuple` of them to get it work. They can be append to your `PROJECT_DIR` variable or not.

For folders, you can set `recursive` mode or not.

Here is a full example for a library and his folders::

    project.add_library_target('mylib', shared=True)
    project.add_source_directories('dir_cpp',
                                   'mylib',
                                   True,
                                   False,
                                   '../../lib/src/*.cpp',
                                   '../../lib/src/test/*.cpp',
                                   )
    project.add_source_directories('dir_header',
                                   'mylib',
                                   True,
                                   False,
                                   '../../lib/src/includes/*.h',
                                   '../../lib/src/test/includes/*.h',
                                   )

You can also add specific files::

    project.add_source_files('cpp_files',
                             'mylib',
                             True,
                             '../../main.cpp',
                             '../../graphics.cpp',
                             )
    project.add_source_files('headers_files',
                             'mylib',
                             True,
                             '../../stdafx.h',
                             '../../main.h',
                             '../../graphics.h',
                             )

PyCMake then associate these files to the target to compile.

Preprocessor Definitions
~~~~~~~~~~~~~~~~~~~~~~~~

If your project need specific definitions for preprocessor, you can set it like that::

    project.preprocessor_definitions('UNICODE', '_UNICODE', 'MYLIB_EXPORTS')

Easy and simple.

Dependencies
------------

CMake offers many way to add dependencies to your project. Currently, PyCMake supports only `add_subdirectory` and `link_directories` with :any:`Externals` object.


You can link after with your dependencies. Here is an example::

    depends = Externals()
    depends.add_subdirectory('zlib', '${PROJECT_DIR}/external/zlib/', '${PROJECT_DIR}/build/zlib')
    depends.add_link_directories(('${PROJECT_DIR}/external/g3log')
    # Now link the target with the wanted libraries
    depends.target_link_libraries('mylib', 'zlib', 'g3log')

Once you have set all your dependencies, you can add it to your project::

    project.add_dependencies(depends)

Now your project can find dependecies and add to your target during compilation.

CMakeLists
----------

Once your project is properly configured, you can create your `CMakeLists.txt`. This file is needed by CMake (and fo course by PyCMake too) to compile your project.

Create a :any:`CMakeLists` object::

    cmakelist = CMakeLists()

Create your file and write it using your :any:`CMake` and :any`Project` objects you have created::

    # PyCmake will try to create folders if not exists.
    cmakelist.create_file('./platform/cmake')
    cmakelist.write_cmakelists(cmake, project)

Normally, you have a **CMakeLists.txt** ready to use, created in the specified folder !
