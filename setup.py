# Copyright (c) 2019 David Steele <dsteele@gmail.com>
#
# SPDX-License-Identifier: GPL-2.0-or-later
# License-Filename: LICENSE
#

from os import path
from setuptools import setup

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="argparse_formatter",
    version="1.4",
    packages=["argparse_formatter"],
    url="https://github.com/davesteele/argparse_formatter",
    license="GPL 2.0",
    author="David Steele",
    author_email="dsteele@gmail.com",
    description="Paragraph-preserving formatter for argparse",
    long_description=long_description,
    long_description_content_type="text/markdown",
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Environment :: Console",
        "License :: OSI Approved :: "
        "GNU General Public License v2 or later (GPLv2+)",
        "Natural Language :: English",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Software Development :: User Interfaces",
    ]
)
