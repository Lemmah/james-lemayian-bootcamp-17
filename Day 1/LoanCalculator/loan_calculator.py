#!/usr/bin/env python
# encoding: utf-8
# This program calculates the repayable loan on a simple interest format.

def calculate_loan_repayable(borrowed_amount, time_months, percentage_rate):
    borrowed_amount = float(borrowed_amount)
    percentage_rate = float(percentage_rate)
    if time_months <= 12:
        repayable_amount = borrowed_amount + borrowed_amount * (time_months/12) * (percentage_rate/100)
        return repayable_amount
    else:
        return "Invalid number of months."
print calculate_loan_repayable(10000,12,12)

