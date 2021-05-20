# -*- coding: utf-8 -*-
import argparse
import sys
from sys import stdin, stdout, stderr
import typing
from typing import Optional
from tika import parser  # type: ignore


def parse_pdf(input: typing.BinaryIO) -> Optional[str]:
    raw = parser.from_file(input)
    return raw['content']


def main() -> None:
    parser = argparse.ArgumentParser(
        description='Extract text from PDF files.')
    parser.add_argument('pdf',
                        metavar='PDF',
                        type=argparse.FileType('rb'),
                        help='the PDF file to parse')
    args = parser.parse_args()
    content = parse_pdf(args.pdf)
    if content is None:
        stderr.write("Could not parse the provided PDF.")
        sys.exit(1)
        return
    stdout.write(content)


if __name__ == "__main__":
    main()
