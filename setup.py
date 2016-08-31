import sys

try:
    from setuptools import setup, find_packages
except:
    sys.exit("Error: missing python-setuptools library")

try:
    python_version = sys.version_info
except:
    python_version = (1, 5)
if python_version < (2,7):
    sys.exit("This application requires a minimum Python 3.0.x, sorry!")

# Define paths
paths = {}
if 'linux' in sys.platform or 'sunos5' in sys.platform:
    paths = {
        'bin':     "/usr/bin",
        'var':     "/var/lib/pycmake/",
        'share':   "/var/lib/pycmake/share",
        'etc':     "/etc/pycmake",
        'run':     "/var/run/pycmake",
        'log':     "/var/log/pycmake",
        'libexec': "/var/lib/pycmake/libexec",
    }
else:
    print("Unsupported platform, sorry!")
    exit(1)

from pycmake import __description__, __version__, __license__
from pycmake import __name__ as __pkg_name__



setup(
    name=__pkg_name__,
    version=__version__,

    license=__license__,

    # metadata for upload to PyPI
    author="Estrada Matthieu",
    author_email="ttamalfor@gmail.com",
    keywords="pycmake cmake make",
    url="https://github.com/algorys/pycmake",
    description=__description__,
    long_description=open('README.rst').read(),

    zip_safe=False,

    packages=find_packages(),
    include_package_data=True,

    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Customer Service',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Code Generators',
        'Topic :: Software Development :: Compilers',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]

)
