I1 = [12, 15]
I2 = [15, 30, -45]
X_2 = [819130, -923140, -517752, -311862, -53501, 781108, -703659, -32265, -530739, -509141, 679211, -716685, -269634]

import time

# test cases
a1 = [15,21,24,30,45]
b1 = [[2, 54], [3, 135], [5, 90], [7, 21]]

a2 = [15,21,24,30,-45]
b2 = [[2, 54], [3, 45], [5, 0], [7, 21]]

a3 = [107, 158, 204, 100, 118, 123, 126, 110, 116, 100]
b3 = [[2, 1032], [3, 453], [5, 310], [7, 126], 
  [11, 110], [17, 204], [29, 116], [41, 123], 
  [59, 118], [79, 158], [107, 107]]

a4 = [-29804, -4209, -28265, -72769, -31744]
b4 = [[2, -61548], [3, -4209], [5, -28265], 
  [23, -4209], [31, -31744], [53, -72769], [61, -4209], 
  [1373, -72769], [5653, -28265], [7451, -29804]]






def sum_for_list(X):
  
  import math
  
  ## FIND PRIME FACTORS
  
  # define potential prime factors based on positive versions of all nums
  max_fact = max([abs(i) for i in X])
  max_fact_sqrt = math.ceil(math.sqrt(max_fact))
  print(max_fact, max_fact_sqrt)
  
  # all odds in range
  t0 = time.perf_counter()
  
  factors = [
    i for i in list(range(7, (max_fact+1), 2))
    if ((i%3!=0) and (i%5!=0))]
  factors
  
  t1 = time.perf_counter()
  print(t1-t0)

  # define a container
  primes = [2, 3, 5] # we know these are prime
  
  ### for all potential prime factors
  # [factor, ITS factors]
  t2 = time.perf_counter()
  
  p = [
    [i, 
    [j for j in list(range(2, ((math.ceil(i/2))+1))) 
    # [j for j in list(range(2, max_fact)) 
    if ((i%j==0) and (i!=j))]
    ] for i in factors]
  
  t3 = time.perf_counter()
  print(t3-t2)
  t4 = time.perf_counter()
  
  ### no factors = prime = add to list
  primes.extend([i for [i, j] in p if len(j)==0])
  
  t5 = time.perf_counter()
  print(t5-t4)

  ## ANSWER THE ACTUAL QUESTION
  t6 = time.perf_counter()
  
  P = [[p, [i for i in X if i%p==0]] for p in primes]
  P = [[p, sum(i)] for [p, i] in P if len(i)>0]
  
  t7 = time.perf_counter()
  print(t7-t6)
  # print(P)
  
  return P
