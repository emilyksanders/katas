# Python Practice
# August 6, 2024

# Sum by Factors - 4 kyu
# URL

# Given an array of positive or negative integers
# 
#  I= [i1,..,in]
# 
# you have to produce a sorted array P of the form
# 
# [ [p, sum of all ij of I for which p is a prime factor (p positive) of ij] ...]
# 
# P will be sorted by increasing order of the prime numbers. 
# The final result has to be given as an array of arrays.
# Example:
# 
# I = [12, 15] # result = [[2, 12], [3, 27], [5, 15]]
# I = [12, 15, 50] # [[2, 62], [3, 27], [5, 65]]
# 2, 3, 5, 7, 11, 13, 17, 19, 23, 29
# 
# [2, 3, 5] is the list of all prime factors of the elements of I, 
# hence the result.
# 
# Notes:
# 
#     It can happen that a sum is 0 if some numbers are negative!
# 
# Example: I = [15, 30, -45] 5 divides 15, 30 and (-45) so 5 appears in 
# the result, the sum of the numbers for which 5 is a factor is 0 so we 
# have [5, 0] in the result amongst others.
# 
# The returned string is not permitted to contain any redundant trailing 
# whitespace: you can use dynamically allocated character strings.

I1 = [12, 15]
I2 = [15, 30, -45]


def sum_for_list(X):
  
  ## FIND PRIME FACTORS
  
  # make them all positive just for now
  pos_list = [i if i>=0 else i*-1 for i in X]
  
  # define potential prime factors
  max_fact = abs( # largest odd number in range, no cap
    max(pos_list)) if (abs(max(pos_list))%2!=0) else (abs(max(pos_list))-1)
  factors = [i for i in list(range(3, (max_fact+1), 2))] # all odds in range
  # print(f'factors is {factors}')
  
  # define a container
  primes = [2] # we know 2 is prime
  # print(f'primes is {primes}')
  
  # for all potential prime factors
  for i in factors:
    # print(f'i is {i}. this is a potential factor OF the numbers in the list')
    mults = [j for j in list(range(2, i)) if i%j==0] # skip 1 and the num itself
    # print(f'mults = {mults}')
    if (len(mults)==0) and (i not in primes):
      primes.append(i)
    # print(f'primes is {primes}')
    
  ## ARE THEY ACTUALLY FACTORS THO?
  
  # get a container
  P = []
  
  # just to be safe
  primes.sort()
  
  # pull them out
  for p in primes:
    a = [i for i in X if i%p==0]
    if len(a)!=0:
      P.append([p, sum(a)])
  
  return P
    
    
    
    
    
    
    
    
# no, not this, just 3. factors OF numbers in the list can be smaller than the min(X)    
  min_fact = max(3, # the smallest odd number in range unless it's less than 3, then 3
    abs(min(pos_list)) if (abs(min(pos_list))%2!=0) else (abs(min(pos_list))+1))    
    
    
    
    
    
#     # set a counter
#     mults = 0
#     print(f'mults is {mults}')
#     # check if they're actually prime
#     sub_factors = list(range(2, i))
#     print(f'sub_factors of {i} are {sub_factors}')
# 
#     # do this as a list comp and then use len(lc)
#     # rather than mults==0
#     for j in sub_factors:  # skip 1 and i
#       print(f'current subfactor is {j}')
#       print(f'mults is {mults}')
#       print(f'{i}%{j}==0 is {i%j==0}')
#       if i%j==0:
#         mults+=1
#       print(f'mults is {mults}')
#       # at the end of that...
#       print(f'mults==0 is {mults==0}')
#       print(f'i not in primes is {i not in primes}')
#       if ((mults==0) and (i not in primes)):
#         primes.append(i)
#       print(f'primes is {primes}')
#     print('')
#   return primes
#     
#     # # get a new list without that one
#     # sub_factors = factors.copy()
#     # sub_factors.remove(i)
#     # 
#     # # from that new list
#     # for j in sub_factors:
#       
#       
# 
# # factors > 5
# # 
# # [(list(range(3, max(I1)+1, 2))).append(2)]
# # 
# # 
# # X = I1.copy()
# # 
# # 
# # 
# # import numpy as np
# # v = np.array([3, -1, 5, 2, -7])
# # 
# # v[v!=-7]
# # 
# 
# 
# 
# 
