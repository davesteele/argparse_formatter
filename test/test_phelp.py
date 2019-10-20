# Copyright (c) 2019 David Steele <dsteele@gmail.com>
#
# SPDX-License-Identifier: GPL-2.0-or-later
# License-Filename: LICENSE
#

import argparse
from collections import namedtuple
from pathlib import Path
import pytest

from argparse_formatter import ParagraphFormatter

NamedString = namedtuple("NamedString", ["name", "string"])
Case = namedtuple("Case", ["name", "result", "ref"])
Formatter = namedtuple("Formatter", ["name", "obj"])

data_path = Path(__file__).resolve().parent / "data"

wordy_text = "this is wordy text. " * 5
liney_text = "this is wordy text. \n" * 5

help_dict = {
    # detect two normal paragraphs
    "w": "{0}\n\n{0}".format(wordy_text),
    # ignore single lfs in the text
    "l": "{0}\n\n{0}".format(liney_text),
    # tolerate blank lines includeing white space
    "s": "{0}\n  \n{0}".format(wordy_text),
}


formatter_dict = {
    "default": argparse.HelpFormatter,
    "paragraph": ParagraphFormatter,
}


@pytest.fixture(params=[NamedString(x, y) for (x, y) in help_dict.items()])
def helpstr(request):
    return request.param


def test_namedstring(helpstr):
    assert help_dict[helpstr.name] == helpstr.string


@pytest.fixture(params=[Formatter(x, y) for (x, y) in formatter_dict.items()])
def formatter(request):
    return request.param


@pytest.fixture()
def testcase(helpstr, formatter):
    case_name = formatter.name
    case_file = case_name + ".ref"

    data_file_path = data_path / case_file

    parser = argparse.ArgumentParser(
        prog="foo", epilog=helpstr.string, formatter_class=formatter.obj
    )
    parser.add_argument("-foo", help=helpstr.string)

    test_text = parser.format_help()

    # The lazy man's way to create reference data
    # data_file_path.write_text(test_text)

    return Case(case_name, test_text, data_file_path.read_text())


def test_case(testcase):
    print(testcase.result)
    assert testcase.result == testcase.ref
