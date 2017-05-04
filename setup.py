#!/usr/bin/env python3
"""Setup script for nvidia2graphite.

Installation command (as superuser):
    $ python3 setup.py install

Author: Stefan Kroboth <stefan.kroboth@uniklinik-freiburg.de>
"""

from distutils.core import setup

setup(name='nvidia2graphite',
      version='1.0',
      description='Writes NVIDIA GPU metrics from nvidia-smi to graphite',
      author='Stefan Kroboth',
      author_email='stefan.kroboth@uniklinik-freiburg.de',
      maintainer='Stefan Kroboth',
      url='https://github.com/stefan-k/nvidia2graphite',
      license='MIT License',
      scripts=['nvidia2graphite.py'],
      data_files=[('/etc/', ['nvidia2graphite.conf']),
                  ('/etc/systemd/system/', ['nvidia2graphite.service'])])
