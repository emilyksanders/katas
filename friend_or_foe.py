# Python Practice
# July 18, 2024

# Friend or Foe? - 7 kyu
# https://www.codewars.com/kata/55b42574ff091733d900002f/python

# Make a program that filters a list of strings and returns a 
# list with only your friends name in it.
# 
# If a name has exactly 4 letters in it, you can be sure 
# that it has to be a friend of yours! Otherwise, you can
# be sure he's not...
# 
# Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], 
# Output = ["Ryan", "Yous"]

# does this work for strings?  it do!!!
len('ryan')

def friend(people):
  return [x for x in people if len(x)==4]

friend(["Ryan", "Kieran", "Jason", "Yous"])
