#!/usr/bin/env python
# encoding: utf-8

import unittest
from prime_numbers import generate_primes

class test_prime_numbers(unittest.TestCase):
    def test_for_number_input(self):
        self.assertEquals(generate_primes('w22'), 'Please input a valid number!')
    def test_for_correct_output(self):
        self.assertEquals(generate_primes(15),[2,3,5,7,11,13])
    def test_for_negative_input(self):
    	self.assertEquals(generate_primes(-2), 'Please input a positive number.')
    def test_for_not_zero(self):
    	self.assertEquals(generate_primes(0), 'Please input a positive number.')
    def test_for_not_one(self):
    	self.assertEquals(generate_primes(1), 'Please input a number greater than 1.')
