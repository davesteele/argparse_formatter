[![Build Status](https://travis-ci.org/davesteele/argparse_formatter.svg?branch=master)](https://travis-ci.org/davesteele/argparse_formatter)
[![Coverage](https://codecov.io/gh/davesteele/argparse_formatter/branch/master/graph/badge.svg)](https://codecov.io/gh/davesteele/argparse_formatter/branch/master) 


Argparse Paragraph Formatter
============================

This project is a simple Python module that provides
[**argparse**](https://docs.python.org/3/library/argparse.html) formatters
that support more flexibility in the display of description, help, and epilog
text.

Background
----------

By default, **argparse** will collapse and transform all sequences of whitespace
into a single space, and then wrap the text to an appropriate line length.
This causes all text to be transformed into a single paragraph.

There are optional **RawDescriptionHelpFormatter** and
**RawTextHelpFormatter** classes that can be used to preserve paragraphs, but
they do not perform any word wrapping. What is needed are formatters that
support more flexibility while still providing word wrapping.

The ParagraphFormatter
----------------------

This module provides the **ParagraphFormatter** class. If this class is passed
to the **argparse.ArgumentParser** creation call as the *formatter_class*
argument, then help and epilog paragraphs, separated by single blank lines,
will be preserved. Word wrapping will be performed within the paragraphs.

Note that **ParagraphFormatter** is implemented by overriding two private
methods in the default **argparse** formatter, and that the internals of that
class are not considered part of the **argparse** API. There is therefore a
small risk that the code may break with a future standard library release. The
module has been tested across all supported Python 3 versions.


The FlexiFormatter
------------------

As it turns out, **ParagraphFormatter** is a more primitive version of a rich
formatter that has been [long proposed](https://bugs.python.org/issue12806)
for inclusion in Python.

This module provides that **FlexiFormatter** class, with some modifications.
This formatter preserves line feeds and indentation, and understands bullet
lists.

FlexiFormatter has been submitted for inclusion in Python3.9 - 
[PR22129](https://github.com/python/cpython/pull/22129).
It would be good for this formatter to be merged - it eliminates the
API-migration risk.

Demo
----

The script
[*demo.py*](https://github.com/davesteele/argparse_formatter/blob/master/demo.py)
demonstrates the effect of using the ParagraphFormatter:

    # ./demo.py
    *************************
    Using the Default formatter
    *************************
    
    usage: demo.py [-h] [--arg ARG]
    
    optional arguments:
      -h, --help  show this help message and exit
      --arg ARG   This same feature would be useful for arguments that would
                  benefit from more explanation. Wouldn't it?
    
    This is a multi-paragraph epilog. It is presenting data that would benefit by
    being visually broken up into pieces. It sure would be nice if it was
    represented that way.
    
    
    *************************
    Using the Paragraph formatter
    *************************
    
    usage: demo.py [-h] [--arg ARG]
    
    optional arguments:
      -h, --help  show this help message and exit
      --arg ARG   This same feature would be useful for arguments that would
                  benefit from more explanation.
              
                  Wouldn't it?
    
    This is a multi-paragraph epilog. It is presenting data that would benefit by
    being visually broken up into pieces.
    
    It sure would be nice if it was represented that way.

The [*flexidemo.py*](https://github.com/davesteele/argparse_formatter/blob/master/flexidemo.py)
script shows the output for **FlexiFormatter**


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
    Using the Flexi formatter
    *************************
    
    usage: flexidemo.py [-h] [--arg ARG]
    
    optional arguments:
      -h, --help  show this help message and exit
      --arg ARG   This same feature would be useful for arguments that would
                  benefit from more explanation.
                   
                    1. It looks nicer
                    2. It is easier to read, even if some of the bullets get to be
                       a little long.
         
    This is a multi-paragraph epilog. It is presenting data that would benefit by
    being visually broken up into pieces.
     
    It sure would be nice if it was represented that way.
     
      1. This is a pretty long line, in a bullet list - getting longer and longer
         and longer
      2. this isn't


Install
-------

Install from [PyPi](https://pypi.org/project/argparse-formatter/) with:

    pip install argparse-formatter
