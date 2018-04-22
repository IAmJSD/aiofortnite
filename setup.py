'''
==========================================
setup.py - Copyright (C) Jake Gealer 2018.
Licensed under the MPL-2.0 license.
https://www.mozilla.org/en-US/MPL/2.0/
==========================================
This file allows you to install pyfortnite.
'''
from setuptools import setup, find_packages

setup(
    name="aiofortnite",
    version="0.12",
    description="A asyncio wrapper for Fortnite.",
    author="Jake Gealer",
    author_email="jake@gealer.email",
    python_requires=">=3.5.3",
    url="https://github.com/JakeMakesStuff/aiofortnite",
    packages=find_packages(exclude=('tests',)),
    install_requires=[
        "aiohttp",
        "requests"
    ],
    include_package_data=True,
    license="GPLv3",
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy"
    ]
)
