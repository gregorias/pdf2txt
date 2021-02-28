# -*- coding: utf-8 -*-
from sys import stdin, stdout
import typing
from tika import parser  # type: ignore


def parse_pdf(input: typing.BinaryIO) -> str:
    raw = parser.from_file(input)
    return raw['content']


def main() -> None:
    content = parse_pdf(stdin.buffer)
    stdout.write(content)


if __name__ == "__main__":
    main()
