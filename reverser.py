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

# helper function
def get_digits(n):
  x = n
  if x < 10:  # it was giving 0s because of the start values < 1
    return (1, 1, x)
  else:
    place_value = 0.1 # start below 0, can *= at start of loop, not end
    place_count = 0
    while x > 9:  # single digits
      place_value *= 10
      place_count += 1
      print(place_value)
      x = n//place_value
      print(x)
    return (place_count, int(place_value), int(x))
# triple tuple: # of digits, place value, digit in largest place

# big guy
def reverser(n):
  # create container
  digits = []
  multipliers = []
  
  # find the largest digit; outputs triple tuple
  a = get_digits(n)
  print(a)
  print('')
  
  # deal with each of those 3 outputs
  
  # first one is how many digits there are, total in n
  num_digits = a[0]
  # remember that one digit is already captured
  
  # second and third outputs can be in the loop
  
  for i in range(num_digits):
    
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
  return digits
  
# just a little bit more!  tomorrow.





