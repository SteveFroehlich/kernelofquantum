#!/usr/bin/env python

from distutils.core import setup
setup(name='koq_invertible_matrix',
      version='1.0.0',
      install_requires=[
        'koq_matrix_arithmetic>=1.0.0',
        'koq_identity_matrix>=1.0.0'
        ],
      py_modules=['koq_invertible_matrix'],
      )
