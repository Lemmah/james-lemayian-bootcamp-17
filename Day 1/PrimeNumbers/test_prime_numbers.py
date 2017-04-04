#!/usr/bin/env python
# encoding: utf-8

import unittest
from prime_numbers import generate_primes

class test_prime_numbers(unittest.TestCase):
    def test_for_number_input(self):
        self.assertEquals(generate_primes('w22'), 'Please input a valid number!')
    def test_for_correct_output(self):
        self.assertEquals(generate_primes(15),[1,2,3,5,7,11,13])
