# Python Practice
# August 2, 2024

# Sum of Digits / Digital Root - 6 kyu
# https://www.codewars.com/kata/541c8630095125aba6000c00/python

# Digital root is the recursive sum of all the digits in a number.
# 
# Given n, take the sum of the digits of n. If that 
# value has more than one digit, continue reducing 
# in this way until a single-digit number is produced. 
# The input will  be a non-negative integer.
# 
# Examples
#     16  -->  1 + 6 = 7
#    942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
# 132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
# 493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  
#                    -->  2 + 9 = 11  -->  1 + 1 = 2


def digital_root(n):
  while n>9:
    n = sum([int(i) for i in str(n)])
  return n
   
  
# n =   493193
# n%9 or n
# n or n%9
# n and 9
# 
# def digital_root_bad(n):
# 	return n%9 or n and 9 
# 






