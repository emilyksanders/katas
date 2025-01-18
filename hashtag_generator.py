# Python Practice
# January 17, 2025

# The Hashtag Generator - 5 kyu
# https://www.codewars.com/kata/52449b062fb80683ec000024

# INSTRUCTIONS

# Description:
# 
# The marketing team is spending way too much 
# time typing in hashtags.
# 
# Let's help them with our own Hashtag Generator!
# 
# Here's the deal:
# 
#     It must start with a hashtag (#).
#     All words must have their first letter capitalized.
#     If the final result is longer than 140 
#     chars it must return false.
#     If the input or the result is an empty 
#     string it must return false.

# EXAMPLES

# s = " Hello there thanks for trying my Kata"  
# =>  "#HelloThereThanksForTryingMyKata"
# s = "    Hello     World   "                  
# =>  "#HelloWorld"
# s = ""                                        
# =>  false

# MY STUFF

def generate_hashtag(s):
  # Arg.
    # s: the string to be hashtagified
  # Return
    # A string in Pascal(?) case with no spaces, 
    # and starting with a hashtag (#)
  # Raise
    # Type errors, potentially
  
  # imports
  import re

  words = re.findall(r'[a-z]+', s.lower())
  h = '#'
  for i in words:
    h = h + i[0].upper() + i[1:]
    
  if ((h=='#') or (len(h)>140)):
    return False
  else:
    return h

# test the length thing
s = "qwertyuiopasdfghjklzxcvbnm qwertyuiopasdfghjklzxcvbnm qwertyuiopasdfghjklzxcvbnm qwertyuiopasdfghjklzxcvbnm qwertyuiopasdfghjklzxcvbnm qwertyuiopasdfghjklzxcvbnm qwertyuiopasdfghjklzxcvbnm"
# nice!

s = "WhAt aBoUt ThIs"
# nice!



# here's the top voted answer from codewars, and 
# yeah
# it's legitimately better.  (dang!)
# Well, I am still proud of myself for what I did
# remember, and for persevering with what I 
# remembered rather than casting around for a 
# spoonfed solution.

def generate_hashtag(s):
    output = "#"
    
    for word in s.split():
        output += word.capitalize()
    
    return False if (len(s) == 0 or len(output) > 140) else output
        
# actually, I think they missed one thing
s = '     ' # bunch of spaces
len(s)  # 5
generate_hashtag(s) #  the output is "#"
# this doesn't technically break the rules, but it's 
# stupid.  no company would actually want that.
# furthermore, len(output) will NEVER > len(s)
# if s = '', output = '#'
# if s = '      ', output = '#'
# therefore, I propose:

def generate_hashtag(s):
    output = "#"
    
    for word in s.split():
        output += word.capitalize()
    
    return False if ((output == '#') or (len(output) > 140)) else output

# try this again
s = '     ' # bunch of spaces
len(s)  # 5
generate_hashtag(s) #  the output is False

# another user pointed out that if the first character
# was already a hashtag, this would spit out a double
# so now I propose
# ... tests failed the first time because it didn't
# control for the input case, adding .lower()

def generate_hashtag(s):
  output = "#"
    
  for word in s.lower().split():
    word = re.sub(r'[^a-z]+', '', word)
    output += word.capitalize()

  return False if ((output == '#') or (len(output) > 140)) else output

tests = [
  "my mother's mother is my grandmother",
  "you're cute, but I think you should go",
  "#brooklyn99",
  "     ",
  "      Hello World   ",
  "qwertyuiopasdfghjklzxcvbnm qwertyuiopasdfghjklzxcvbnm qwertyuiopasdfghjklzxcvbnm qwertyuiopasdfghjklzxcvbnm qwertyuiopasdfghjklzxcvbnm qwertyuiopasdfghjklzxcvbnm qwertyuiopasdfghjklzxcvbnm",
  "WhAt aBoUt ThIs",
  " Hello there thanks for trying my Kata",
  "WellHiThere"
]

for i in tests:
  print(i)
  print(generate_hashtag(i))
  
# hmm.

s = "      Hello World   "
s.lower().split()
for word in s.lower().split(): 
  print(word)
  print(re.sub(r'[^a-z]+', '', word))
  print(re.sub(r'[^a-z]+', '', word).capitalize())
# oh whoops
# it works fine; I was looking at the wrong output line

# scraps
matches = re.search(r' ', 's')
while matches != None:
  matches = re.search(r' ', 's')






