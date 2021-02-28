# -*- coding: utf-8 -*-
import unittest

from pdf2txt.main import parse_pdf


class ToolTestCase(unittest.TestCase):
    def test_parse_pdf_extracts_text(self):
        with open('test/testdata/Switzerland Payslip.pdf', 'rb') as input:
            output = parse_pdf(input)

        with open('test/testdata/Switzerland Payslip.txt',
                  'r') as expected_output_file:
            expected_output = expected_output_file.read()

        self.assertEqual(output, expected_output)
