#!/usr/bin/env python
# coding: utf-8
'''Set up package Iydon.
'''
import setuptools


with open("README.md", "r") as f:
	long_description = f.read()

setuptools.setup(
	name="mathlang",
	version="0.0.1",
	author="Iydon Liang",
	author_email="liangiydon@gmail.com",
	license='GPLv3 License',
	description="*Mathlang* is a Python module that will change the world, but as for the approach, it is still a secret.",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/mathlang-org",
	packages=setuptools.find_packages(),
	classifiers=[
		"Programming Language :: Python :: 3",
		"Operating System :: OS Independent",
	],
	python_requires='>=3.7',
	install_requires=[],
	tests_require=[
		'pytest',
	],
)
