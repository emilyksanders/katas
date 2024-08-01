# Python Practice
# July 31, 2024

# Make negative - 8 kyu
# URL: https://www.codewars.com/kata/58069e4cf3c13ef3a6000168/discuss/python

# In this simple assignment you are given a number and have to make it negative. But maybe the number is already negative?
# Examples
# 
# make_negative(1);  # return -1
# make_negative(-5); # return -5
# make_negative(0);  # return 0
# 
# Notes
# 
#     The number can be negative already, in which case no change is required.
#     Zero (0) is not checked for any specific sign. Negative zeros make no mathematical sense.
# 

def make_negative(number):
  return -1*abs(number)
