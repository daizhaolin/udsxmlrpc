# -*- coding: UTF-8 -*-
'''
Created on 2020-01-13

@author: daizhaolin
'''

from setuptools import setup, find_packages

setup(
    name='udsxmlrpc',
    version='0.1.3',
    url='https://github.com/daizhaolin/udsxmlrpc',
    license='BSD',
    author='daizhaolin',
    author_email='',
    description='Unix domain socket XML-RPC',
    long_description=__doc__,
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    platforms='',
    install_requires=[],
)
