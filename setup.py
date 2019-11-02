# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in frappe_blog/__init__.py
from frappe_blog import __version__ as version

setup(
	name='frappe_blog',
	version=version,
	description='[H[H[H[H[H[H[H[H[H[H[H[H[H[H[H[H[H',
	author='Samaila Bala',
	author_email='samailabalap@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
