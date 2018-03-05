#using test driven development to solve project euler problems

import unittest
import os

'''If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.'''

#FLOW
#setup tests and functions
#loop to 1000
#get multiples of 3 and 5
#sum them up

def multiplesOf3And5():
    multiplesOf3()
    multiplesOf5()
    sumMultiplesOf3and5

def multiplesOf3():
    return 0

def multiplesOf5():
    return 0

def multiplesOf3And5():
    return 0

print (multiplesOf3())
assert multiplesOf3()  == 0
assert multiplesOf5() == 0
assert multiplesOf3And5() == 0
