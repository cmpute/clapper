#!/usr/bin/env python

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
    packages=['zzz_driver_datasets_d3d'],
    package_dir={'': 'src'},
    install_requires=['d3d']
)

setup(**d)