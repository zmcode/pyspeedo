#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='pyspeedo',
    version='0.1',
    description='A network\'s speed monitoring tool',
    license='GPLv3',
    url='https://github.com/zmcode/pyspeedo',
    install_requires=['cement',
                      'peewee',
                      'pyspeedtest'],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    entry_points={'console_scripts': ['pyspeedo=pyspeedo.cli.app:main']},
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Operating System :: Unix',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: System :: Networking :: Monitoring'
    ]

)
