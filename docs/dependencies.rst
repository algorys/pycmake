.. _dependencies:
.. highlight:: python

Dependencies
============

Externals
---------

CMake offers many way to add dependencies to your project. PyCmake use :any:`Externals` object to manage this::

    depends = Externals()

Currently, PyCMake supports `add_subdirectory` for other directory with CMakeLists projects. And you can `link_directories` to link binaries already built::

    depends.add_subdirectory('zlib', '${PROJECT_DIR}/external/zlib/', '${PROJECT_DIR}/build/zlib')
    depends.add_link_directories(('${PROJECT_DIR}/external/g3log')

Links
-----

You can link your project with your dependencies. Simply tell which target you want to link with them. If the target exists in your project, PyCmake will link them::

    depends.target_link_libraries('mylib', 'zlib', 'g3log')
    project.add_dependencies(depends)

