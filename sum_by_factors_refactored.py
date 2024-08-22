I1 = [12, 15]
I2 = [15, 30, -45]
X_2 = [819130, -923140, -517752, -311862, -53501, 781108, -703659, -32265, -530739, -509141, 679211, -716685, -269634]


def sum_for_list(X):
  
  import math
  
  ## FIND PRIME FACTORS
  
  # define potential prime factors based on positive versions of all nums
  max_fact = max([abs(i) for i in X])
  
  # all odds in range
  factors = [i for i in list(range(7, (max_fact+1), 2))] 
  
  # eliminate easy ones
  factors = [i for i in factors if i%3!=0]
  factors = [i for i in factors if i%5!=0]
  
  # define a container
  primes = [2, 3, 5] # we know these are prime
  # print(f'primes is {primes}')
  
  # for all potential prime factors
  for i in factors:

    a = list(range(2, (math.ceil(math.sqrt(i)))+2))
    b = [j for j in a if i%j==0]
    if len(b)==0:
      primes.append(i)
    
    # if we get through all that without finding a factor, it's prime
    
    # if is_prime:
    #   # print("append")
    #   primes.append(i)
      
  ## ANSWER THE ACTUAL QUESTION
  
  # get a container. this will be returned
  # P = []
  
  # pull out each prime and find the elements it is a factor of
  # for p in primes:
  #   # list of elements in X divided cleanly by the prime i
  #   a = [i for i in X if i%p==0]
  #   # ONLY if it finds some, add them to the return list
  #   if len(a)!=0:
  #     P.append([p, sum(a)])
  
  P = [[p, [i for i in X if i%p==0]] for p in primes]
  # P = [[p, i] for [p, i] in P if len(i)>0]
  P = [[p, sum(i)] for [p, i] in P if len(i)>0]
  
  
  
  return P


# huh?

mine = [
  [2, -61548], [3, -4209], [5, -28265], [23, -4209], [31, -31744], 
  [53, -72769], [61, -4209], [1373, -72769], 
  
  [1403, -4209], 
  
  [5653, -28265], [7451, -29804], 
  
  [72769, -72769]]

theirs = [
  [2, -61548], [3, -4209], [5, -28265], [23, -4209], [31, -31744], 
  [53, -72769], [61, -4209], [1373, -72769], 
  [5653, -28265], [7451, -29804]]

len(mine)
len(theirs)

their_unique = [a for a in theirs if a not in mine]
my_unique = [a for a in mine if a not in theirs]

# are these prime numbers??

p_1403 = [a for a in list(range(2, 1403)) if 1403%a==0]
p_72769 = [a for a in list(range(2, 72769)) if 72769%a==0]

their_2 = [
  [2, -61548], [3, -4209], [5, -28265], [23, -4209], [31, -31744], 
  [53, -72769], [61, -4209], [1373, -72769], [5653, -28265], 
  [7451, -29804]]



