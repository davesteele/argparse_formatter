# Copyright (c) 2019 David Steele <dsteele@gmail.com>
#
# SPDX-License-Identifier: GPL-2.0-or-later
# License-Filename: LICENSE
#

from argparse import HelpFormatter
import re as _re
import textwrap

class ParagraphHelpFormatter(HelpFormatter):
    """Help message formatter which respects paragraphs and bulleted lists.

    Only the name of this class is considered a public API. All the methods
    provided by the class are considered an implementation detail.
    """

    def _split_lines(self, text, width):
        return self._para_reformat(text, width)

    def _fill_text(self, text, width, indent):
        lines = self._para_reformat(text, width - len(indent))
        linearray = [indent + line if line else "" for line in lines]
        return "\n".join(linearray)

    def _indents(self, line):
        """Return line indent level and "sub_indent" for bullet list text."""

        indent = len(_re.match(r"( *)", line).group(1))
        list_match = _re.match(r"( *)(([*\-+>]+|\w+\)|\w+\.) +)", line)
        if list_match:
            sub_indent = indent + len(list_match.group(2))
        else:
            sub_indent = indent

        return (indent, sub_indent)

    def _split_paragraphs(self, text):
        """Split text in to paragraphs of like-indented lines."""

        import textwrap

        text = textwrap.dedent(text).strip()
        text = _re.sub("\n\n[\n]+", "\n\n", text)

        last_sub_indent = None
        paragraphs = list()
        for line in text.splitlines():
            (indent, sub_indent) = self._indents(line)
            is_text = len(line.strip()) > 0

            if is_text and indent == sub_indent == last_sub_indent:
                paragraphs[-1] += " " + line
            else:
                paragraphs.append(line)

            if is_text:
                last_sub_indent = sub_indent
            else:
                last_sub_indent = None

        return paragraphs

    def _para_reformat(self, text, width):
        """Reformat text, by paragraph."""

        import textwrap

        lines = list()
        for paragraph in self._split_paragraphs(text):

            (indent, sub_indent) = self._indents(paragraph)

            paragraph = self._whitespace_matcher.sub(" ", paragraph).strip()
            new_lines = textwrap.wrap(
                text=paragraph,
                width=width,
                initial_indent=" " * indent,
                subsequent_indent=" " * sub_indent,
            )

            # Blank lines get eaten by textwrap, put it back
            lines.extend(new_lines or [""])

        return lines


class FlexiFormatter(ParagraphHelpFormatter):
    pass

class FlexiHelpFormatter(ParagraphHelpFormatter):
    pass

class ParagraphFormatter(ParagraphHelpFormatter):
    pass

class FlexiFormatter(ParagraphHelpFormatter):
    pass

