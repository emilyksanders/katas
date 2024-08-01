# Python Practice
# July 18, 2024

# Reverser - 7 kyu
# https://www.codewars.com/kata/58069e4cf3c13ef3a6000168/python

# Impliment the reverse function, which takes in 
# input n and reverses it. For instance, reverse(123) 
# should return 321. You should do this without 
# converting the inputted number into a string.
#
# Please do not use anything from the following list:
# ['encode','decode','join','zfill','codecs','chr','bytes',
# 'ascii', 'substitute','template','bin', 'os','sys','re', 
# '"', "'", 'str','repr', '%s', 'format', 'type', '__', '.keys',
# 'eval','exec','subprocess']

# I am assuming that the input will always be an integer.
# My solution will not work for floats.

# helper function
def get_digits(n):
  x = n
  if x < 10:  # it was giving 0s because of the start values < 1
    return (1, 1, x)
  else:
    # start with the assumption that this number has 0 digits
    num_digits = 0
    # the first loop will set this to the 1s place (then 10s, 100s, etc.)
    place_value = 0.1 # start below 0, so can *= at start of loop, not end
    num = 0
    while x > 9:  # until it gets into single digits...
      place_value *= 10 # up the max place value of the number
      num_digits += 1 # add a counter to the # of digits
      # print(place_value)
      x = n//place_value # floor divide to shed a digit
      # x will be a n without the last digit, e.g., 1234 -> 123
      print(f'''
      num_digits: {num_digits}
      place_value: {place_value}
      digit: {x}
      ({num_digits}, {int(place_value)}, {int(x)})''')
      num += int(place_value)*int(x)
    return num # (num_digits, int(place_value), int(x))
# triple tuple: # of digits, place value, digit in largest place

# big guy
def reverse(n):
  # create containers
  digits = [] # each digit, as a list
  multipliers = [] # the power of 10 associated with each digit
  # sum(digits[i]*multipliers[i]) for all i = n
  
  # find the largest digit; outputs triple tuple
  a = get_digits(n)
  print(a)
  print('')
  
  # deal with each of those 3 outputs
  
  # first one is how many digits there are, total, in n
  digits_in_n = a[0]
  # remember that one digit is already captured
  
  # second and third outputs can be in the loop
  
  for i in range(digits_in_n):
    
    print(n)
    print(a)
    
    # put things away
    
    # second is the place value of the largest place (e.g., 10, 100)
    multiplier = a[1]
    # third is the digit in that place value
    num = a[2]
    # put that digit, as an integer, in the container
    digits.append(num)
    multipliers.append(multiplier)
    print(digits)
    print(multipliers)
  
    # run again to get the next digit
    
    # drop that place value 
    n = n - num*multiplier
    # rerun
    a = get_digits(n)
  
  # after the prescribed # of runs, i'll have a list
  print(digits)
  print(multipliers)
  
  digits = digits[::-1]
  
  # start at 0
  reversed_num = 0
  
  for i in range(len(digits)):
    reversed_num += digits[i]*multipliers[i]
  
  return reversed_num
  
# just a little bit more!  Xtomorrow.X    done!

# Hmmmm but it's failing the tests.
# OH but there's a comment or something. Read the discussion.



# I'm not sure why it's bugging out, but I think I just realized
# a more efficient way to do this.


def reverse(n):
  # define a toggle
  neg_num = False
  
  # no floats!
  if type(n)!=int:
    return """Tricksy Hobbitses inputting floatses!\
  Smeagol begs for intses, but we must staaaaaaaarve!"""
  
  # return single digits unchanged
  elif n>-10 & n<10:
    return n
  
  # now the real stuff
  else:
    
    # set that toggle to handle later, convert to pos
    if n<0:
      neg_num = True
      n *= -1
    
    # now we have a positive number with at least 2 digits
    
    # create placeholder containers
    digits = []
    # multipliers = []
    
    # iteratively, until // = 0 (because we're down to 1 digit)
    # use modulus to extract the last digit, and put it in jail
    while n!=0:
      digits.append(n%10)
      n = n//10
    
    # use the length of [digits] to get number of place values
    # and create a list of those
    for i in range(len(digits)):
      multipliers.append(10**i)
    
    # reverse order them, to reverse the weight of the digits
    multipliers = multipliers[::-1]
    
    # reconstruct the number
    # remember that n will = 0 bcz of the while loop
    for i in range(len(digits)):
      n += digits[i]*multipliers[i]

    # return it to negative, if need be
    if neg_num==True:
      n*=-1

    return n


# rework to be shorter!

def reverse(n):
  # define a toggle
  neg_num = False
  
  # no floats!
  if type(n)!=int:
    return """Tricksy Hobbitses inputting floatses!\
  Smeagol begs for intses, but we must staaaaaaaarve!"""
  
  # return single digits unchanged
  elif (n>-10) & (n<10): # & needs (); 'and' doesn't
    return n
  
  # now the real stuff
  else:
    
    # set that toggle to handle later, convert to pos
    if n<0:
      neg_num = True
      n*=-1
    
    # now we have a positive number with at least 2 digits
    
    # create placeholder container
    digits = []
    
    # iteratively, until // = 0 (because we're down to 1 digit)
    # use modulus to extract the last digit, and put it in jail
    while n!=0:
      digits.append(n%10)
      n = n//10
    
    # use the length of [digits] to get number of place values
    # and create a list of those, in reverse order
    multipliers = [10**i for i in range(len(digits))][::-1]

    # reconstruct the number
    # remember that n will = 0 bcz of the while loop
    for i in range(len(digits)):
      n += digits[i]*multipliers[i]
    
    # return it to negative, if need be
    if neg_num==True:
      n*=-1
    
    return n

# Most concise answer from codewars (name changed):

def kata_reverse(n):
    m = 0
    while n > 0:
        n, m = n // 10, m * 10 + n % 10
    return m
# this one does work on single digits, and 0, but not neg

# adding my hardening
def revise_reverse(n):

  # no floats!
  if type(n)!=int:
    return """Tricksy Hobbitses inputting floatses!\
  Smeagol begs for intses, but we must staaaaaaaarve!"""  

  # now the real stuff
  else:

    # define a toggle - move, not necessary for floats
    neg_num = False
    
    # set that toggle to handle later, convert to p0s
    if n<0:
      neg_num = True
      n*=-1
    
    # take theirs
    m = 0
    while n > 0:
      n, m = n // 10, m * 10 + n % 10
      
    # restore negative
    if neg_num==True:
      return m*-1
    else: 
      return m
