# -*- coding: utf-8 -*-
from sys import stdin, stdout
import typing
from tika import parser  # type: ignore


def main(input: typing.BinaryIO) -> str:
    raw = parser.from_file(input)
    return raw['content']


if __name__ == "__main__":
    content = main(stdin.buffer)
    stdout.write(content)
