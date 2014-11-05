#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Andy Sayler
# Summer 2014
# CSCI 3308
# Univerity of Colorado
# Text Processing Module

import unittest
import textproc

class TextprocTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_init(self):
        text = "tesing123"
        p = textproc.Processor(text)
        self.assertEqual(p.text, text, "'text' does not match input")

    def test_notString(self):
        A = []
        self.assertRaises(textproc.TextProcError, lambda:textproc.Processor([]))

    def test_count(self):
        text = "testCountMethod"
        p = textproc.Processor(text)
        self.assertEqual(p.count(), 15, "'test' count is not correct")

    def test_countAlpha(self):
        text = "thereshouldbe23characters"
        p = textproc.Processor(text)
        self.assertEqual(p.count_alpha(), 23, "'test' doesn't count only the characters")

    def test_countNumeric(self):
        text = "somethingtestlikewithnumbers12345678910!"
        p = textproc.Processor(text)
        self.assertEqual(p.count_numeric(), 10, "'test' doesn't count only the numbers")

    def test_countvowerls(self):
        text = "thereare6vowels"
        p = textproc.Processor(text)
        self.assertEqual(p.count_vowels(), 6, "'test' doesn't count vowels properly")

    def test_isPhonenumber(self):
        text = "123-4567890"
        p = textproc.Processor(text)
        self.assertEqual(p.is_phonenumber(), False, "'test' doesn't count phone numbers")

# Main: Run Test Cases
if __name__ == '__main__':
    unittest.main()
