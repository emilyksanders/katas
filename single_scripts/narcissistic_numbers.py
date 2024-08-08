# Python Practice
# August 1, 2024

# Does my number look big in this? - 6 kyu
# https://www.codewars.com/kata/5287e858c6b5a9678200083c/python

# A Narcissistic Number (or Armstrong Number) is a positive 
# number which is the sum of its own digits, each raised to 
# the power of the number of digits in a given base. In this
# Kata, we will restrict ourselves to decimal (base 10).
# 
# For example, take 153 (3 digits), which is narcissistic:
# 
#     1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
# 
# and 1652 (4 digits), which isn't:
# 
#     1^4 + 6^4 + 5^4 + 2^4 = 1 + 1296 + 625 + 16 = 1938
# 
# The Challenge:
# 
# Your code must return true or false (not 'true' and 
# 'false') depending upon whether the given number is a 
# Narcissistic number in base 10.
# 
# This may be True and False in your language, e.g. PHP.
# 
# Error checking for text strings or other invalid inputs is
# not required, only valid positive non-zero integers will 
# be passed into the function.

# scratch work
def narcissistic(value):
  # s_val = str(value)
  # digits = [i for i in s_val]
  digits = [i for i in str(value)]
  added = sum([(int(i)**len(digits)) for i in digits])
  if value == added:
    return True
  else:
    return False
  # return added
  
# clean and readable
def narcissistic(value):
  digits = [i for i in str(value)]
  added = sum([(int(i)**len(digits)) for i in digits])
  if value == added:
    return True
  else:
    return False
  
# most succinct
def narcissistic(value):
  return True if (value==sum([(int(i)**len([i for i in str(value)])) for i in [i for i in str(value)]])) else False
  
# medium
def narcissistic(value):
  digits = [i for i in str(value)]
  added = sum([(int(i)**len(digits)) for i in digits])
  return True if (value==added) else False

# learning from others
# there is no need to make the digits a list. len() works
# directly on strings.  You also return an eval, rather 
# than specifying true or false directly.
# this is the top answer:

def narcissistic(value):
  return value == sum(int(x)**len(str(value)) for x in str(value))



