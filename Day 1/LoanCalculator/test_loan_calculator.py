#!/usr/bin/env python
# encoding: utf-8
"""
This is a test case for the loan calculator, a function that I suppose should:
    0. Calculate the payable amount accurately when the paramaters are passed
    1. Accept number inputs which are: borrowed_amount, time_payable (in months), percentage_rate
    2. Ensure a loan is repayed within 12 months (I don't know why...we just decided to do this in class.)
    3. Set a minimum amount of borrowable loan of 5 thousand. (You cannot just borrow any amount, like 5 bob makes no sense.)
    4. Ensures that all the inputs are positive numbers ie greater than zero. You borrow a loan with a negative interest, it simply means you wont pay.
    5. Prohibits someone from borrowing a loan greater than 10 million. Assumption is it is a microfinancing thing.
This test is supposed to ensure that my function passes all the required tests.

"""
import unittest
from loan_calculator import calculate_loan_repayable

class test_loan_calculator(unittest.TestCase): # Does it calculate the loan correctly?
    def test_input_is_number(self):
        self.assertEquals(calculate_loan_repayable("SELECT * FROM",8,2), "Input a valid number.")
    def test_input_is_positive(self):
        self.assertEquals(calculate_loan_repayable(10000,-1,-1), "You cannot have values less than 0.")
    def test_for_number_of_months(self): # It makes sure that the number of months are less than 12 as agreed
        self.assertEquals(calculate_loan_repayable(100000,13,11), "Maximum time allowed is 12 months.")
    def test_minimum_amount_borrowable(self):
        self.assertEquals(calculate_loan_repayable(4600,3,13), "You can only borrow between 5000 and 10000000.")
    def test_maximum_amount_borrowable(self):
        self.assertEquals(calculate_loan_repayable(1000000000,2,9), "You can only borrow between 5000 and 10000000.")
    def test_repayable_amount_output(self):
        self.assertEquals(calculate_loan_repayable(100000,12,12), 112000)
if __name__ == '__main__':
    unittest.main()
