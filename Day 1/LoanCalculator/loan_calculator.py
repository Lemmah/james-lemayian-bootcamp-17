#!/usr/bin/env python
# encoding: utf-8
# This program calculates the repayable loan on a simple interest format.

def calculate_loan_repayable(borrowed_amount, time_months, percentage_rate):
    if borrowed_amount > 0 and time_months > 0 and percentage_rate > 0:
        if isinstance(borrowed_amount, int) and isinstance(time_months, int) and isinstance(percentage_rate, int):
            borrowed_amount = float(borrowed_amount)
            percentage_rate = float(percentage_rate)
            if borrowed_amount >= 5000 and borrowed_amount <= 10000000:
                if time_months <= 12:
                    repayable_amount = borrowed_amount + borrowed_amount * (time_months/12) * (percentage_rate/100)
                    return repayable_amount
                else:
                    return "Maximum time allowed is 12 months."
            else:
                return "You can only borrow between 5000 and 10000000."
        else:
            return "Input a valid number."
    else:
        return "You cannot have values less than 0."
print calculate_loan_repayable(10000,12,12)

