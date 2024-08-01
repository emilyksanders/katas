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
      print(place_value)
      x = n//place_value # floor divide to shed a digit
      # x will be a n without the last digit, e.g., 1234 -> 123
      num += int(place_value)*int(x)
    return (num_digits, int(place_value), int(x))
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
  
  
  # deal with each of th0se 3 outputs
  
  # first one is how many digits ther3 ar3, total, in n
  digits_in_n = a[0]
  # r3member that one digit is alr3ady captur3d
  
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
    # r3run
    a = get_digits(n)
  
  # after the pr3scribed # of runs, i will have a list
  print(digits)
  print(multipliers)
  
  digits = digits[::-1]
  
  # start at 0
  reversed_num = 0
  
  for i in range(len(digits)):
    reversed_num += digits[i]*multipliers[i]
  
  return reversed_num


'''
SO. The problem here is that this code can't handle 0s
in the middle of the number.  Every time it hits a 0,
the {n = n - num*multiplier} step knocks it down by TWO
orders of magnitude.  This means that (a) multipliers 
are missing that may have been needed to symmetrically
reverse the number (e.g., 10987 can't come out to 78901,
with an 8 in the 1000s place, if the multipliers skip
from 10000 directly to 100), and (b) because the number
goes down by more than one order of magnitude at a time,
but my loop is defined by the number of digits, it runs
get_digits() on single digit numbers, especially 0, 
multiple times.  This adds extra 0s to the end of 
[digits], and extra 1s to the end of [multipliers]. When
one list is then inverted, the earliest entries to 
[digits] are matched with 0s in [multipliers], and
obliterated.  Additionally, because there are so many 1s
in [multipliers], many single digit numbers are included
in the reconstructive addition.  This can further warp 
the result, because two multipliers of 1, applied to 
single digits and then added together, will likely sum
to a two digit number.

For example, reverse(10987) results in:
  
  5 digits -> 5 repetitions in the loop
  
  REP 1:
  
    get_digits(10987) = (5, 10000, 1)
    digits = [1]
    multipliers = [10000]
    
    n = n - num*multiplier
    n = 10987 - 1*10000
    n = 987 [SKIPPED 1000!!]
  
  REP 2:
  
    get_digits(987) = (3, 100, 9)
    digits = [1, 9]
    multipliers = [10000, 100]
    
    n = n - num*multiplier
    n = 987 - 9*100
    n = 87 

  REP 3:
  
    get_digits(87) = (2, 10, 8)
    digits = [1, 9, 8]
    multipliers = [10000, 100, 10]
    
    n = n - num*multiplier
    n = 87 - 8*10
    n = 7 

  REP 4:
  
    get_digits(7) = (1, 1, 7)
    digits = [1, 9, 8, 7]
    multipliers = [10000, 100, 10, 1]
    
    n = n - num*multiplier
    n = 7 - 7*1
    n = 0 [THIS IS WHERE IT SHOULD STOP, BUT...] 

  REP 5:
  
    get_digits(0) = (1, 1, 0)
    digits = [1, 9, 8, 7, 0] [ADDED 0]
    multipliers = [10000, 100, 10, 1, 1] [EXTRA 1]
    
    n = n - num*multiplier
    n = 0 - 0*1
    n = 0 
  
  It stops there, but then...
  
  digits = [1, 9, 8, 7, 0]
  multipliers = [10000, 100, 10, 1, 1]
  
  reverse one of the lists (doesn't matter which)...
  
  multipliers = [10000, 100, 10, 1, 1]
  digits = [0, 7, 8, 9, 1]
  
  do the addition...
  
  multipliers[i]*digits[i]
  
  10000*0=0
  100*7=700
  10*8=80
  1*9=9
  1*1=1
  
  0+700+80+9+1=790


My version is robust against ending 0s, but fails to
manage internal 0s.  I learned a lot though, and it felt
good to get back into some python!  

I also had to study up on bytes and bits and binary in 
order to understand why reverse(14) didn't work, but 
reverse(16) did -- it turns out that & is NOT the 
same as 'and'!  It does bitwise comparison, and only 
pops up if BOTH bites are 1s (not even if they're 
both 0s!).  When I wrote {n>-10 & n<10}, I meant
{(n>-10) & (n<10)}, but it was interpreted as
{n > (-10 & n) < 10}.  Now, how a binary number can be
negative is its own thing that I don't really 
understand yet, but it has something to do with how 
python assigns signs to integers, even if you don't
specify one.  The point is, it exists.  So it's 
this intersection term, (-10 & n), and then determining
whether that value is lesser than both n and 10.  This
was only a problem for numbers 10-15.  (At least in my
version, where I specified to return single digit
numbers unchanged.)  

The binary code for -10 is (in python) the same as 
that for ~9, and that is 11110110.  The code for 16,
which is where it started working again, is 
00010000.  Because the if statement included <10, 
most of the matches (intersections) with -10 (~9) 
would trigger a False, which is (somewhat 
coincidentally) the same outcome I wanted from
{(n>-10) & (n<10)}.  All of those leftward 1s represent
numbers >=16.  The digit in the 8s spot is 0, so that 
can't trigger a True either.  The 1s place is another 0,
so the result of the evaluation {(-10 & n)} can only be
even.  The only possible outcomes that are <10, and thus
will trigger a True and result in n being returned as 
is, are 00000110 (6), 00000100 (4), or 00000010 (2).  

All numbers <10 will either match, maximally, to 
themselves (already meeting the <10 requirement), or be
reduced by failures to match (e.g., 8 = 
00001000, no overlap -> 00000000 = 0, <10 and <n)

Starting at 10, and comparing to 11110110:
10 = 00001010, overlaps at 2 -> 00000010 = 2 <10 and <n
11 = 00001011, overlaps at 2 -> 00000010 = 2 <10 and <n
12 = 00001100, overlaps at 4 -> 00000100 = 4 <10 and <n
13 = 00001101, overlaps at 4 -> 00000100 = 4 <10 and <n
14 = 00001110, overlaps at 6 -> 00000110 = 6 <10 and <n
15 = 00001111, overlaps at 6 -> 00000110 = 6 <10 and <n

But then at 16, 
16 = 00010000, which overlaps with 11110110 at 16, which
is NOT <10, so it triggers a False, and the instructions
to return n unchanged are not executed.  Because 
11110110 is all 1s from then on (moving rightward), and
because all numbers >=16 will include at least one 1 in 
the last 5 (reading right to left) spots, no additional 
numbers will be able to match so badly that they drop 
below 10. Therefore, all further numbers will trigger
False, the early return instructions will not execute, 
and the remainder of the code will continue.'''



  
  
