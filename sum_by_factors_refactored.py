I1 = [12, 15]
I2 = [15, 30, -45]


def sum_for_list(X):
  
  ## FIND PRIME FACTORS
  
  # define potential prime factors based on positive versions of all nums
  max_fact = max([abs(i) for i in X])
    # square root of the largest odd number in range, no cap
  
  factors = [i for i in list(range(7, (max_fact+1), 2))] # all odds in range
  # print(f'factors is {factors}')
  
  # easy ones
  factors = [i for i in factors if i%3!=0]
  factors = [i for i in factors if i%5!=0]
  
  # define a container
  primes = [2, 3, 5] # we know these are prime
  # print(f'primes is {primes}')
  
  # for all potential prime factors
  for i in factors:
    # print(f'i is {i}. this is a potential factor OF the numbers in the list')
    
    for j in list(range(2, (int(round((i**(1/2)), 0))+1))):
      if i%j==0:
        cont
      
    # something like that.
    
    
    
    # mults = [j for j in list(range(2, (int(round((i**(1/2)), 0))+1))) if i%j==0] # skip 1 and the num itself
    # print(f'mults = {mults}')
    if (len(mults)==0) and (i not in primes):
      primes.append(i)
    # print(f'primes is {primes}')
    
  ## ARE THEY ACTUALLY FACTORS THO?
  
  # get a container
  P = []
  
  # pull them out
  for p in primes:
    a = [i for i in X if i%p==0]
    if len(a)!=0:
      P.append([p, sum(a)])
  
  return P
