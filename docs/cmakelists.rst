.. _cmakelists:
.. highlight:: python

CMakeLists
==========

What you need to do before
--------------------------

You must have an instance of :any:`CMake` and :any:`Project` create and configured with your requirements to use :any:`CMakeLists`.

Create CMakeLists
-----------------

Once your project is properly configured, you can create your `CMakeLists.txt`. This file is needed by CMake (and of course by PyCMake too) to compile your project.

Create a :any:`CMakeLists` object::
 
    cmakelist = CMakeLists()

Initialize file and write it::

    cmakelist.create_file('./platform/cmake')
    # PyCmake will try to create folders if not exists.
    cmakelist.write_cmakelists(cmake, project)

Normally, you have a **CMakeLists.txt** ready to use, created in the specified folder !

