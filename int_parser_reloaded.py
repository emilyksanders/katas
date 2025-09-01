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

hard_code_numbers = {
  'zero': 0,
  'one': 1,
  'two': 2,
  'three': 3,
  'four': 4,
  'five': 5,
  'six': 6,
  'seven': 7,
  'eight': 8,
  'nine': 9,
  'ten': 10,
  'eleven': 11,
  'twelve': 12
}



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

# minimum_place_values = {
#   '2': ['ten', 'eleven', 'twelve', 'teen', 'ty'],
#   '3': ['hundred'],
#   '4': ['thousand'] # OR a 2 and a 3 (e.g., fourTEEN HUNDRED)
#   # '5': a 2 and a 4 in that order
#   # '6': a 3 and a 4 in that order
#   '7': ['million']
#   # it's stipulated that 1mil is the max
# }

# 1 000 000
# A BCD EFG

# the only overlap in number words is "O" and "One"

import re

# testing
if re.search('hundred', 'one hundred ninety-six'): 
  print('yes') 
else: 
  print('no')

a = re.search('hundred', 'one hundred ninety-six')
b = re.search('thousand', 'one hundred ninety-six')
c = re.search('million', 'one hundred ninety-six')
d = (a or b or c)




num = # whatever the written number is
num = 'Negative Four Hundred and Twenty-Six Thousand Five Hundred and Eightyone'
num = 'negative twelve'

def parse_int(num):
  
  import re
  
  # drop extraneous words and formatting right away, part 1  
  num = num.lower()
  
  # i'm pretty sure integers CAN be negative
  # identify negative integers, flip the switch, cut the word
  if re.match('negative', num):
    s = -1 # s for sign_multiplier
    num = re.sub('negative ', '', num)
  elif re.match('minus', num):
    s = -1 # s for sign_multiplier
    num = re.sub('minus ', '', num)
  else:
    s = 1
  
  # short circuit if it's the easy-to-spot stipulated max
  if re.search('million', num): 
    return s*1000000 # stipulated max
  
  # no?  ok, keep going (i don't think an else is necessary, 
  # because triggering "return" skips all below it)
  
  # drop extraneous words and formatting right away, part 2
  num = re.sub(' and ', ' ', num)
  num = re.sub('-', ' ', num)
  num = re.sub(r'(ty)([a-z])', r'\1 \2', num)
  
  # easy to spot, hard to isolate programmatically
  # if the whole input is one of these, just spit it back out
  hard_code_numbers = {'zero': 0, 'one': 1, 
    'two': 2, 'three': 3, 'four': 4, 'five': 5, 
    'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 
    'ten': 10, 'eleven': 11, 'twelve': 12}
  
  # moving this if statement up to save steps
  if num in hard_code_numbers.keys():
    return s*hard_code_numbers[num]
  
  # still no?  ok, keep going
  
  # define some search objects for later recall
  search_thou = re.search('thousand', num)
  search_hund = re.search('hundred', num)
  search_ten = re.search('ten', num)
  search_eleven = re.search('eleven', num)
  search_twelve = re.search('twelve', num)
  search_teen = re.search('teen', num)
  search_ty = re.search('ty', num)
  search_two_digits = (search_ten or search_eleven or search_twelve or search_teen or search_ty)
  
  # use the search objects to determine how many digits num should have, 
  # and use letters as placeholders
  if (search_hund and search_thou and (search_hund.span()[1] < search_thou.span()[0])):
    digits = 'ABCDEF'
    min = s*100_000
    max = s*999_999
  elif (search_two_digits and search_thou and (search_two_digits.span()[1] < search_thou.span()[0])):
    digits = 'ABCDE'
    min = s*10_000
    max = s*99_999
  elif search_thou:
    digits = 'ABCD'
    min = s*1_000
    max = s*9_999
  elif search_hund:
    digits = 'ABC'
    min = s*100
    max = s*999
  elif search_two_digits:
    digits = 'AB' # no need for a single digit, those are hard coded
    min = s*13 # 0-12 hard coded
    max = s*99
  else:
    return -999_999_999 # something is broken. # i need to review "Raise"
  
  if len(digits)==6:
    
    # DIGIT A
    
    # this can be done in one line of code, and I know how
    # but it's unreadable, and I'm not vain
    digit_a_stop_loc = search_hund.span()[0] # where the WORD "hundred" starts
    digit_a_name = num[:digit_a_stop_loc].strip()
    digit_a = hard_code_numbers[digit_a_name]
    A = f'{digit_a}'  # this will allow string addition later
    
    # drop the first bit to get the next digit
    first_match_stop_loc = search_hund.span()[1]
    num = num[first_match_stop_loc:].strip()
    
    # NEXT
    
    # this should probably go above, but i can make sense of it here
    # split at the thousand
    
    # check
    if len(re.findall('thousand', num))!=1:
      return "Invalid input (len(re.findall('thousand', num))!=1)"
    
    # assuming all good
    first_part = num[:search_thou.span()[0]].strip()
    second_part = num[search_thou.span()[1]:].strip()
    
    # DIGITS B and C
    
    if first_part in hard_code_numbers.keys():
      AB = f'{hard_code_numbers[first_part]}'
      if len(AB)==1:
        AB = '0'+AB
    elif search_teen:
      
    
  
  
  
  return s, digits






  
    


re.search('hundred', 'one hundred ninety-six').span()[1]
re.search('ty', 'one hundred ninety-six').span()[0]

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

