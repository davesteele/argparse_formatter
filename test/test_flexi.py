# Copyright (c) 2022 David Steele <dsteele@gmail.com>
#
# SPDX-License-Identifier: GPL-2.0-or-later
# License-Filename: LICENSE
#

import re
from typing import NamedTuple

import pytest

from argparse_formatter.flexi_formatter import INDENT_MATCH, LIST_MATCH

class Case(NamedTuple):
    string: str
    result: int

@pytest.mark.parametrize(
    "case",
    [
        Case("", 0),
        Case("x", 0),
        Case(" ", 1),
        Case(" x", 1),
    ]
)
def test_indent_match_re(case):
    assert len(re.match(INDENT_MATCH, case.string).group(1)) == case.result

@pytest.mark.parametrize(
    "case",
    [
        Case("text", 0),
        Case(" A word", 0),
        Case("* ", 1),
        Case(" * ", 1),
        Case(" + ", 1),
        Case(" > ", 1),
        Case(" A ", 0),
        Case(" A. ", 1),
        Case(" 1. ", 1),
        Case(" tag: ", 1),
        Case(" period. ", 0),
    ]
)
def test_list_match_re(case):
    match = re.match(LIST_MATCH, case.string)
    
    islist = True if match else False

    assert islist == bool(case.result)


