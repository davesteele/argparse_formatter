# Copyright (c) 2019 David Steele <dsteele@gmail.com>
#
# SPDX-License-Identifier: GPL-2.0-or-later
# License-Filename: LICENSE
#

from argparse import HelpFormatter
import re
import textwrap


class ParagraphFormatter(HelpFormatter):
    """
    An argparse formatter that preserves paragraphs
    (text separated by a blank line)
    """

    def __init__(self, *args, **kwargs):
        self.psep = "\n\n"
        self.psep_re = re.compile(r"\n\s*\n", flags=re.ASCII)
        super().__init__(*args, **kwargs)

    def _fill_text(self, text, width, indent):
        formatted = []
        for paragraph in self.psep_re.split(text):
            paragraph = self._whitespace_matcher.sub(" ", paragraph).strip()
            formatted.append(
                textwrap.fill(
                    paragraph, width, initial_indent=indent, subsequent_indent=indent
                )
            )

        return self.psep.join(formatted)

    def _split_lines(self, text, width):
        formatted = []
        for paragraph in self.psep_re.split(text):
            paragraph = self._whitespace_matcher.sub(" ", paragraph).strip()
            if formatted:
                formatted.append("")
            formatted += textwrap.wrap(paragraph, width)

        return formatted
