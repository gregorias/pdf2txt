# -*- coding: utf-8 -*-
import unittest

from app.main import main


class ToolTestCase(unittest.TestCase):
    def test_main_extracts_text(self):
        with open('test/testdata/Switzerland Payslip.pdf', 'rb') as input:
            output = main(input)

        with open('test/testdata/Switzerland Payslip.txt',
                  'r') as expected_output_file:
            expected_output = expected_output_file.read()

        self.assertEqual(output, expected_output)
