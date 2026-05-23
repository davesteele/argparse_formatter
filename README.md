[![PyPI version](https://badge.fury.io/py/argparse-formatter.svg)](https://badge.fury.io/py/argparse-formatter)
[![Argparse_Formatter Tests](https://github.com/davesteele/argparse_formatter/actions/workflows/test.yml/badge.svg)](https://github.com/davesteele/argparse_formatter/actions/workflows/test.yml)
[![Coverage](https://codecov.io/gh/davesteele/argparse_formatter/branch/master/graph/badge.svg)](https://codecov.io/gh/davesteele/argparse_formatter/branch/master) 


12/20/25 - FlexiHelpFormatter is making
[progress](https://github.com/python/cpython/pull/22129) in the review process.
I'm replacing the formatter code here with that submission, with aliases with
the old names, for use with older Python versions. The name has changed to
ParagraphHelpFormatter. That class has been aliased to all of the old names
that this module used to reference.

5/22/26 - The MR is [declined](https://github.com/python/cpython/pull/22129#issuecomment-4413724429).


Argparse Paragraph Formatter
============================

This project is a simple Python module that provides an improved paragraph lovin formatter for 
[**argparse**](https://docs.python.org/3/library/argparse.html). This formatter respects paragraphs and bullet lists, providing consistent word wrapping.

Background
----------

By default, **argparse** will collapse and transform all sequences of whitespace
into a single space, and then wrap the text to an appropriate line length.
This causes all text to be transformed into a single paragraph.

There are optional **RawDescriptionHelpFormatter** and
**RawTextHelpFormatter** classes that can be used to preserve paragraphs, but
they do not perform any word wrapping. What is needed are formatters that
support more flexibility while still providing word wrapping.

The ParagraphHelpFormatter
--------------------------

This module provides the **ParagraphHelpFormatter** class. If this class is passed
to the **argparse.ArgumentParser** creation call as the *formatter_class*
argument, then help and epilog paragraphs, separated by single blank lines,
will be preserved. Word wrapping will be performed within the paragraphs.

Note that **ParagraphHelpFormatter** is implemented by overriding two private
methods in the default **argparse** formatter, and that the internals of that
class are not considered part of the **argparse** API. There is therefore a
(vanishingly) small risk that the code may break with a future standard library
release. The module has been tested across all supported Python 3 versions.

This module provides that **ParagraphHelpFormatter** class, with some modifications.
This formatter preserves line feeds and indentation, and understands bullet
lists.

Supported list styles are as follows:

```
    * item
    - item
    + item
    > item
    A. item
    1. item
    key: item
```

ParagraphHelpFormatter has been submitted for inclusion in Python3.15 - 
[PR22129](https://github.com/python/cpython/pull/22129).

Demo
----

The [*flexidemo.py*](https://github.com/davesteele/argparse_formatter/blob/master/flexidemo.py)
script shows the output for **ParagraphHelpFormatter**


    *************************
    Using the Default formatter
    *************************
    
    usage: flexidemo.py [-h] [--arg ARG]
    
    optional arguments:
      -h, --help  show this help message and exit
      --arg ARG   This same feature would be useful for arguments that would
                  benefit from more explanation. 1. It looks nicer 2. It is easier
                  to read, even if some of the bullets get to be a little long.
    
    This is a multi-paragraph epilog. It is presenting data that would benefit by
    being visually broken up into pieces. It sure would be nice if it was
    represented that way. 1. This is a pretty long line, in a bullet list -
    getting longer and longer and longer 2. this isn't
    
    
    *************************
    Using the Paragraph formatter
    *************************
    
    usage: flexidemo.py [-h] [--arg ARG]
    
    optional arguments:
      -h, --help  show this help message and exit
      --arg ARG   This same feature would be useful for arguments that would
                  benefit from more explanation.
                   
                    * It looks nicer
                    * It is easier to read, even if some of the bullets get to be
                       a little long.
         
    This is a multi-paragraph epilog. It is presenting data that would benefit by
    being visually broken up into pieces.
     
    It sure would be nice if it was represented that way.
     
      1. This is a pretty long line, in a bullet list - getting longer and longer
         and longer
      2. this isn't


Install
-------

Install from [PyPI](https://pypi.org/project/argparse-formatter/) with:

    pip install argparse-formatter
