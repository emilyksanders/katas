# Python Practice
# January 17, 2025

# parseInt() reloaded - 4 kyu
# https://www.codewars.com/kata/525c7c5ab6aecef16e0001a5/python

# INSTRUCTIONS

# Description:
# 
# In this kata we want to convert a 
# string into an integer. The strings 
# simply represent the numbers in words.
# 
# Examples:
# 
# "one" => 1
# "twenty" => 20
# "two hundred forty-six" => 246
# "seven hundred eighty-three thousand nine hundred and nineteen" => 783919
# 
# Additional Notes:
# 
# The minimum number is "zero" (inclusively)
# The maximum number, which must be supported 
#     is 1 million (inclusively)
# The "and" in e.g. "one hundred and twenty-four" 
#     is optional, in some cases it's present and in others it's not
# All tested numbers are valid, you don't need to validate them

# MY STUFF

# there is surely a faster way to do this, but I'm going to try to 
# create a dictionary of number words

digit_words: ['one', 'two', 'three', 'four', 
  'five', 'six', 'seven', 'eight', 'nine']

number_words = {
  '0': ['zero', 'o', 'oh', 'ty'],
  '1': ['one', 'teen'],
  '2': ['two', 'twen'],
  '3': ['three', 'thir'],
  '4': ['four', 'for'],
  '5': ['five', 'fif'],
  '6': ['six'],
  '7': ['seven'],
  '8': ['eight', 'eigh'],
  '9': ['nine'],
  '10': ['ten'],
  '11': ['eleven'],
  '12': ['twelve']
}

number_words_list = [
  'zero', 'o', 'oh', 'ty',
  'one', 'teen',
  'two', 'twen',
  'three', 'thir',
  'four', 'for',
  'five', 'fif',
  'six',
  'seven',
  'eight', 'eigh',
  'nine',
  'ten',
  'eleven',
  'twelve'
]

minimum_place_values = {
  '2': ['ten', 'eleven', 'twelve', 'teen', 'ty'],
  '3': ['hundred'],
  '4': ['thousand'] # OR a 2 and a 3 (e.g., fourTEEN HUNDRED)
  # '5': a 2 and a 4 in that order
  # '6': a 3 and a 4 in that order
  '7': ['million']
  # it's stipulated that 1mil is the max
}

# the only overlap in number words is "O" and "One"

import re

s = "two hundred forty-six"
s = s.lower()
s = re.sub(r'[^a-z]', '', s)

if s[:3]=='one':
  t = '1'
  s = s[3:]
else:
  t = ''
  i = 1
  while i <= len(s):
    w = s[:i]
    if w not in number_words_list:
      i += 1
    else: # if it IS in there
      implied_digit = ''.join([i for i in number_words.keys() if w in number_words[i]])
      if s[(i+1):(i+3)] == 'ty':
        implied_digit += '0'
      elif s[(i+1):(i+5)] == 'teen':
        implied_digit = '1' + implied_digit

