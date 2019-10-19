import argparse
from argparse_paragraph import ParagraphFormatter

test_cases = (
    ("Default", argparse.HelpFormatter),
    ("Paragraph", ParagraphFormatter),
)

def argparse_demo(formatter):
    parser = argparse.ArgumentParser(
        epilog="""
            This is a multi-paragraph epilog. It is presenting data that would
            benefit by being visually broken up into pieces.

            It sure would be nice if it was represented that way.
            """,
        formatter_class=formatter,
    )

    parser.add_argument(
        "--arg",
        help="""
            This same feature would be useful for arguments that would benefit
            from more explanation.

            Wouldn't it?
        """,
    )

    return parser.format_help()

for (name, formatter) in test_cases:
    print("*************************")
    print("Using the {} formatter".format(name))
    print("*************************")
    print()
    print(argparse_demo(formatter))
    print()
