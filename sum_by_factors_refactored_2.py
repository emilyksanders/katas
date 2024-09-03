I1 = [12, 15]
I2 = [15, 30, -45]
X_2 = [819130, -923140, -517752, -311862, -53501, 781108, -703659, -32265, -530739, -509141, 679211, -716685, -269634]
import time

def sum_for_list(X):
  
  import math
  
  ## FIND PRIME FACTORS
  
  # define potential prime factors based on positive versions of all nums
  # max_fact = max([abs(i) for i in X])
  max_fact = math.ceil(math.sqrt(max([abs(i) for i in X])))
  
  # all odds in range
  t0 = time.perf_counter()
  factors = [
    i for i in list(range(7, (max_fact+1), 2))
    if ((i%3!=0) or (i%5!=0))]
  t1 = time.perf_counter()
  print(t1-t0)
  
  # eliminate easy ones
  # t0 = time.perf_counter()
  # factors = [i for i in factors if i%3!=0]
  # factors = [i for i in factors if i%5!=0]
  # t1 = time.perf_counter()
  # print(t1-t0)
  
  # define a container
  primes = [2, 3, 5] # we know these are prime
  # ]
  # print(f'primes is {primes}')
  
  # # for all potential prime factors
  # [factor, ITS factors]
  t0 = time.perf_counter()
  p = [
    [i, 
    # [j for j in list(range(2, (math.ceil(math.sqrt(i)))+1))  # maybe just get one sqrt??
    [j for j in list(range(2, (max_fact+1)))
    # [j for j in list(range(2, (i+1)))
      if i%j==0]  ]
    for i in factors  ]
  # no factors = prime = add to list
  t1 = time.perf_counter()
  print(t1-t0)
  t0 = time.perf_counter()  
  primes.extend([
    i for [i, j] in p if len(j)==0
  ])
  t1 = time.perf_counter()
  print(t1-t0)
  
  # list(range(2, (math.ceil(math.sqrt(i)))+1))] 
  #   for i in factors]
  
  ## ANSWER THE ACTUAL QUESTION
  t2 = time.perf_counter()
  P = [[p, [i for i in X if i%p==0]] for p in primes]
  P = [[p, sum(i)] for [p, i] in P if len(i)>0]
  t3 = time.perf_counter()
  print(t3-t2)
  
  return P


# huh?

# mine = [
#   [2, -61548], [3, -4209], [5, -28265], [23, -4209], [31, -31744], 
#   [53, -72769], [61, -4209], [1373, -72769], 
#   
#   [1403, -4209], 
#   
#   [5653, -28265], [7451, -29804], 
#   
#   [72769, -72769]]
# 
# theirs = [
#   [2, -61548], [3, -4209], [5, -28265], [23, -4209], [31, -31744], 
#   [53, -72769], [61, -4209], [1373, -72769], 
#   [5653, -28265], [7451, -29804]]
# 
# len(mine)
# len(theirs)
# 
# their_unique = [a for a in theirs if a not in mine]
# my_unique = [a for a in mine if a not in theirs]
# 
# # are these prime numbers??
# 
# p_1403 = [a for a in list(range(2, 1403)) if 1403%a==0]
# p_72769 = [a for a in list(range(2, 72769)) if 72769%a==0]
# 
# their_2 = [
#   [2, -61548], [3, -4209], [5, -28265], [23, -4209], [31, -31744], 
#   [53, -72769], [61, -4209], [1373, -72769], [5653, -28265], 
#   [7451, -29804]]
# 
# 
# 
