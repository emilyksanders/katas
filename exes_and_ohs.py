# Python Practice
# July 18, 2024

# Exes and Ohs - 7 kyu
# https://www.codewars.com/kata/55908aad6620c066bc00002a/python

# Check to see if a string has the same amount of 'x's 
# and 'o's. The method must return a boolean and be 
# case insensitive. The string can contain any char.
# 
# Examples input/output:
# 
# XO("ooxx") => true
# XO("xooxx") => false
# XO("ooxXm") => true
# XO("zpzpzpp") => true // when not present should return true
# XO("zzoo") => false

z = 'xooxx'
len(re.findall('x', z))

def xo(s):
  import re
  xs = len(re.findall('x', s.lower()))
  os = len(re.findall('o', s.lower()))
  if xs==os:
    return True
  else:
    return False
  
# can I do that without embedding an import?
def xo(s):
  xs = [i for i in s.lower() if i=='x']
  os = [i for i in s.lower() if i=='o']
  if len(xs)==len(os):
    return True
  else:
    return False

tests = ["ooxx", "xooxx", "ooxXm", "zpzpzpp", "zzoo"]

for i in tests:
  xo(i)



