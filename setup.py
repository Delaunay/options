#!/usr/bin/env python
from setuptools import setup


if __name__ == '__main__':
    setup(
        name='options',
        version='0.0.0',
        description='Options Trading utilities',
        author='Pierre Delaunay',
        packages=[
            'options',
        ],
        setup_requires=['setuptools'],
        install_requires=[
            'pandas',
            'matplotlib'
        ]
    )
