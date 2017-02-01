import pkg_resources, os, pkgutil
from setuptools import setup, find_packages
from yaml2csv.version import __version__

def dependencies():
    file_ = pkg_resources.resource_filename(__name__, os.path.join('requirements', 'default.txt'))
    with open(file_, 'r') as f:
        return f.read().splitlines()

setup(
    name                 = 'yaml2csv',
    version              = __version__,
    description          = 'Convert YAML/JSON to key value comma separated value (CSV) pairs',
    author               = 'Michael Barton',
    author_email         = 'mail@michaelbarton.me.uk',
    install_requires     = dependencies(),

    scripts              = ['bin/yaml2csv'],
    packages             = find_packages(),
    include_package_data = True,

    classifiers = [
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Intended Audience :: Science/Research',
        'Operating System :: POSIX'
    ],
)
