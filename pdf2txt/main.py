# -*- coding: utf-8 -*-
import argparse
from sys import stdin, stdout
import typing
from tika import parser  # type: ignore


def parse_pdf(input: typing.BinaryIO) -> str:
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
    stdout.write(content)


if __name__ == "__main__":
    main()
