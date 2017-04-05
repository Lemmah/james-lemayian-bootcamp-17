#!/usr/bin/env python
# encoding: utf-8

def generate_primes(n):
    if isinstance(n, int):
        primes_list = list()
        for number in range(2,n+1):
            prime = True
            for i in range(2, number):
                if (number % i == 0):
                    prime = False
            if prime:
                primes_list.append(number)
        return primes_list
    else:
        return "Please input a valid number!"
