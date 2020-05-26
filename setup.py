#!/usr/bin/env python
from setuptools import setup, find_packages


setup(
    name='pykss',
    version='0.6.1',
    description='Python implementation of KSS',
    long_description=open('README.rst').read(),
    author='Kundo',
    author_email='dev@kundo.se',
    url='https://github.com/kundo/pykss',
    license='BSD',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    zip_safe=False,
    extras_require={
        'tests': [
            'Django>=1.6',
            'flake8',
            'mock',
            'pytest<=3.3',
            'attrs==19.1.0',
        ],
    },
)
