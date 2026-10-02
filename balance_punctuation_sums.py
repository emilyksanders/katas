# Python Practice
# 2026-10-01

# Exclamation marks series #17: 
# Put the exclamation marks and question marks on the 
# balance - are they balanced? - 6 kyu
# https://www.codewars.com/kata/57fb44a12b53146fe1000136

# INSTRUCTIONS
# Each exclamation mark's weight is 2; each question 
# mark's weight is 3. Putting two strings left and 
# right on the balance - are they balanced?
# 
# If the left side is more heavy, return "Left"; 
# if the right side is more heavy, return "Right"; 
# if they are balanced, return "Balance".
# 
# Examples
# "!!", "??"     -->  "Right"
# "!??", "?!!"   -->  "Left"
# "!?!!", "?!?"  -->  "Left"
# "!!???!????", "??!!?!!!!!!!"  -->  "Balance"

# MY STUFF

def balance(left, right):
  
  import re
  
  left_sum = ((len(re.findall('!', left)))*2) + ((len(re.findall('\\?', left)))*3)
  right_sum = ((len(re.findall('!', right)))*2) + ((len(re.findall('\\?', right)))*3)
  
  if left_sum > right_sum:
    return 'Left'
  elif right_sum > left_sum:
    return 'Right'
  elif left_sum == right_sum:
    return 'Balance'
  else: 
    raise
    return 'BROKEN'
    







