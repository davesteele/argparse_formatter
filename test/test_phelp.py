# Copyright (c) 2019 David Steele <dsteele@gmail.com>
#
# SPDX-License-Identifier: GPL-2.0-or-later
# License-Filename: LICENSE
#

import argparse
import pytest
import re
import textwrap
from collections import namedtuple
from pathlib import Path

from argparse_formatter import ParagraphFormatter, FlexiFormatter

NamedString = namedtuple("NamedString", ["name", "string"])
Case = namedtuple("Case", ["formatter_name", "text_name", "result", "ref"])
Formatter = namedtuple("Formatter", ["name", "obj"])

data_path = Path(__file__).resolve().parent / "data"

wordy_text = "this is wordy text. " * 5
liney_text = "this is wordy text. \n" * 5

help_dict = {
    # detect two normal paragraphs
    "wordy": "{0}\n\n{0}".format(wordy_text),
    # ignore single lfs in the text
    "liney": "{0}\n\n{0}".format(liney_text),
    # tolerate blank lines including white space
    "spacey": "{0}\n  \n{0}".format(wordy_text),
}


formatter_dict = {
    "default": argparse.HelpFormatter,
    "paragraph": ParagraphFormatter,
    "flexi": FlexiFormatter,
}


@pytest.fixture(params=[NamedString(x, y) for (x, y) in help_dict.items()])
def helpstr(request):
    return request.param


@pytest.fixture(params=[Formatter(x, y) for (x, y) in formatter_dict.items()])
def formatter(request):
    return request.param


@pytest.fixture()
def testcase(helpstr, formatter):
    parser = argparse.ArgumentParser(
        prog="foo", epilog=helpstr.string, formatter_class=formatter.obj
    )
    parser.add_argument("-foo", help=helpstr.string)
    test_text = parser.format_help()

    data_file_path = data_path / (formatter.name + ".ref")
    # The lazy man's way to create reference data
    # data_file_path.write_text(test_text)

    return Case(formatter.name, helpstr.name, test_text, data_file_path.read_text())


def test_case(testcase):
    print(testcase.result)
    assert testcase.result == testcase.ref

SimpleCase = namedtuple("SimpleCase", ["width", "input", "out"])


@pytest.mark.parametrize(
    "case",
    [
        SimpleCase(
            10,
            """
                base text
                  1. text to wrap
            """,
            textwrap.dedent(
            """
                base text
                  1. text
                     to
                     wrap
            """
            ).strip()
        ),
        SimpleCase(
            10,
            """
                base text
                  - text to wrap
            """,
            textwrap.dedent(
            """
                base text
                  - text
                    to
                    wrap
            """
            ).strip()
        ),
        SimpleCase(
            10,
            """
                base text
                  1. text to wrap
            """,
            textwrap.dedent(
            """
                base text
                  1. text
                     to
                     wrap
            """
            ).strip()
        )
    ]
)
def test_flexi_para_reformat(case):
    out = "\n".join(FlexiFormatter("foo")._para_reformat(case.input, case.width))
    print(out)
    assert case.out == out


bullet_template = SimpleCase(
    10,
    """
        base text
          - text to wrap
    """,
    textwrap.dedent(
    """
        base text
          - text
            to
            wrap
    """
    ).strip()
)


@pytest.fixture(params=[x for x in "*-+>"])
def bullet_case(request):
    case = SimpleCase(
        10,
        re.sub("-", request.param, bullet_template.input),
        re.sub("-", request.param, bullet_template.out),
    )

    return case


def test_bullet_chars(bullet_case):
    fmt = FlexiFormatter("foo")
    lines = fmt._para_reformat(bullet_case.input, bullet_case.width)
    out = "\n".join(lines)
    print(out)
    assert bullet_case.out == out
