#!/usr/bin/env python3

from setuptools import setup


setup(
    name="vsix",
    description="vsix.us",
    author="Ryan Finnie",
    packages=["vsix"],
    include_package_data=True,
    install_requires=["Django", "django-xff"],
)
