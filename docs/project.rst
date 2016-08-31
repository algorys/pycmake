.. _project:
.. highlight:: python

Project
=======

Create a project
----------------

The :any:`Project` is the heart of your script. He will contains all information about your project sources, dependencies, links, definitions, ...

Initialise object and create your project::

    project = Project()
    language = 'C++'
    project.create('myLib', language)

Currently, only **C** and **C++** are valid language. During :func:`create`, PyCMake create a variable named **PROJECT_NAME** (See below).

.. _variables:

CMake Variables
---------------

To facilitate read and management of your project, PyCMake will help you to generate variable you can use after along the process.

There is some default variables who will be created and you can create your own if needed. 

Predefined Variables
~~~~~~~~~~~~~~~~~~~~

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
~~~~~~~~~~~~~~~~

You can also add custom variables to your project. Simply type the following::

    project.variables.add('TEST_DIR', '${PROJECT_DIR}/src/tests')

You can add as many variables as you want or replace existing ones. The :any:`Project` object provides the :func:`get_variable` method to access any variable created.

Targets
-------

Now that your project is defined, you must add target(s) to build. There is 2 types of targets : libraries and executables.

Libraries
~~~~~~~~~

You have to precise the **true** name of your library. She can be shared or static.

For a shared library called `libmylib.so` (or `mylib.dll` on Windows)::

    project.add_library_target('mylib', shared=True)

For a static library called `libmylib.a` (or `mylib.lib` on Windows)::

    project.add_library_target('mylib')

The **shared** option is false by default.

Executables
~~~~~~~~~~~

You have to give the **true** name of your executable. For an executable called `myexe` (or `myexe.exe` on Windows)::

    project.add_executable_target('myexe')

That's all.

.. _files:

Preprocessor Definitions
------------------------

If your project need specific definitions for preprocessor, you can set it like that::

    project.preprocessor_definitions('UNICODE', '_UNICODE', 'MYLIB_EXPORTS')

Easy and simple.

Sources
-------

Your target will obviously need files to be built. They are added by :any:`Sources` object. Once done, simply add them to a target that you created::

    project.add_sources_to_target('myexe', src)

See the **Next Section** for more details.



