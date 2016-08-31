.. _sources:
.. highlight:: python

Sources
=======

Sources are the files you want to add to your target project. They must be created before adding them to a :any:`Project` object.

To create sources files, you need to know more about :any:`SRC_TYPE <pycmake.supported.SRC_TYPE>`.

Sources Files
-------------

Simply instantiate a `Sources` object::

    files = Sources()
    # You can create a list before
    src = ['../../src/main.cpp', '../../src/conf.cpp']
    # 'myfiles' will be the ID of your sources.
    files.add('myfiles', SRC_TYPE[1], src)

That's all. You cannot make files recursive, but you can make their path relative from **PROJECT_DIR** variable::

    files.add('files', SRC_TYPE[1], src, from_proj=True)

The **from_proj** variable is **False** by default.

Sources Directory
-----------------

For sources directory, PyCmake will create a variable with **file** cmake command to add them to your target after. The process is the same as *Sources Files*, but you can make them resursive or not. You can specify, in your directory listing, the file extensions you want to include::

    dirs = Sources()
    src_dir = ['../../src/*.cpp', '../../src/include/*.h']
    dirs.add('mydirs', SRC_TYPE[0], src_dir)
    # You can make them recursive
    dirs.make_resursive(True)

Recursive is **False** by default.

Add Sources to a Project
------------------------

Once you have defined your Sources, you add them to a Project. You must specify a **valid target** to get it work. You can add multiple files or directory to the same target::

    project.add_sources_to_target('mytarget', files)
    project.add_sources_to_target('mytarget', dirs)

When PyCMake generate *CMakeLists.txt*, it automatically adds the source to the specified target.


