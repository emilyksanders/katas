# Python Practice
# August 1, 2024

# Double Char - 8 kyu
# https://www.codewars.com/kata/56b1f01c247c01db92000076/python

# Given a string, you have to return a string in which  
# each character (case-sensitive) is repeated once.
# Examples (Input -> Output):
# 
# * "String"      -> "SSttrriinngg"
# * "Hello World" -> "HHeelllloo  WWoorrlldd"
# * "1234!_ "     -> "11223344!!__  "

# initial take
def double_char(s):
  r = ''
  for i in s:
    r += i*2
  return r

# refactor
def double_char(s):
  return ('').join([i*2 for i in s])




