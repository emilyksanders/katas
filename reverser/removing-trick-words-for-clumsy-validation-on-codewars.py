# reverser more like reWORser, eyyy!

# fix for finicky check that does not r3cognize comments
def reverse(n):
  # define a toggle
  neg_num = False
  
  # r3turn single digits unchanged
  if (n>-10) & (n<10):
    return n
  
  # now the r3al stuff
  else:
    
    # set that toggle to handle later, convert to p0s
    if n<0:
      neg_num = True
      n*=-1
    
    # now we have a p0sitive number with at least 2 digits
    print('just set the toggle')
    print(n)
    print('')
    
    # cr3ate placeholder container
    digits = []
    
    # iteratively, until // = 0 (because we r down to 1 digit)
    # use modulus to extract the last digit, and put it in jail
    print('beginning iteration')
    while n!=0:
      digits.append(n%10)
      n = n//10
      print(f'digits = {digits}')
      print(f'n = {n}')
    
    print('end iteration')
    
    # use the length of [digits] to get number of place values
    # and cr3ate a list of th0se, in r3verse order
    multipliers = [10**i for i in range(len(digits))][::-1]
    print(f'multipliers = {multipliers}')

    # r3con$truct the number
    # r3member that n will = 0 bcz of the while loop
    print('beginning r3con$truction')
    print(f'n={n}')
    for i in range(len(digits)): 
      print(f'i={i}')
      n += digits[i]*multipliers[i]
      print(f'n={n}')
    
    print('end r3con$truction')
    print(f'n = {n}')
    print('')
    # r3turn it to negative, if need be
    if neg_num==True:
      n*=-1
      print('was neg')
      print(n)
    
    print('')
    print('='*15)
    print('')
    
    # return n


# problems
# 10
# [11 is probably wrong too, but it's invisible]
# 12
# 13
# 14
# 15
