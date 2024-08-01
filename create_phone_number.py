# Python Practice
# August 1, 2024

# Create Phone Number - 6 kyu
# https://www.codewars.com/kata/56b1f01c247c01db92000076/python

# Write a function that accepts an array of 10 integers 
# (between 0 and 9), that returns a string of those numbers 
# in the form of a phone number.
#
# Example
# create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) 
# => returns "(123) 456-7890"
# 
# The returned format must be correct in order to complete 
# this challenge.
# 
# Don't forget the space after the closing parentheses!

n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

def create_phone_number(n):
  #n = [str(i) for i in n] # no need to add a line!
  return f'({str(n[0])}{str(n[1])}{str(n[2])}) {str(n[3])}{str(n[4])}{str(n[5])}-{str(n[6])}{str(n[7])}{str(n[8])}{str(n[9])}'

# sleek and succinct
def create_phone_number(n):
  return f'({str(n[0])}{str(n[1])}{str(n[2])}) {str(n[3])}{str(n[4])}{str(n[5])}-{str(n[6])}{str(n[7])}{str(n[8])}{str(n[9])}'

# hardened
def create_phone_number(n):
  
  # no multidigits, floats, or other nonsense
  if (sum([type(i)!=(int or str) for i in n])!=0):
    return "Bad number. Please enter 10 digits."
  
  # no non-number strings
  if len(n[type(n)!=int])==0:
    pass
  else:
    # test if they can be converted to integers
    # I think np.where could help with this one
    # but I'm too tired to remember how.
    # onward to tomorrow!
  # for i in n[type(n)!=int][i]  <- that's the language to isolate what I need
  
  return f'({str(n[0])}{str(n[1])}{str(n[2])}) {str(n[3])}{str(n[4])}{str(n[5])}-{str(n[6])}{str(n[7])}{str(n[8])}{str(n[9])}'



