# Python Practice
# 2026-10-30

# Nesting Structure Comparison - 4 kyu
# URL: https://www.codewars.com/kata/520446778469526ec0000001/train/python

# INSTRUCTIONS
# Complete the function to return True when its argument is an array 
# that has the same nesting structures and same corresponding length 
# of nested arrays as the first array.

# For example:
# 
# # should return True
# same_structure_as([ 1, 1, 1 ], [ 2, 2, 2 ] )
# same_structure_as([ 1, [ 1, 1 ] ], [ 2, [ 2, 2 ] ] )
# 
# # should return False 
# same_structure_as([ 1, [ 1, 1 ] ], [ [ 2, 2 ], 2 ] )
# same_structure_as([ 1, [ 1, 1 ] ], [ [ 2 ], 2 ] )
# 
# # should return True
# same_structure_as([ [ [ ], [ ] ] ], [ [ [ ], [ ] ] ] )
# 
# # should return False
# same_structure_as([ [ [ ], [ ] ] ], [ [ 1, 1 ] ] )


# MY STUFF
x = [ 1, [ 1, 1 ] ]
y = [ 2, [ 2, 2 ] ]
z = [ 'cat', [ 'dog', 'frog' ] ]

import itertools

itertools.chain(x).items

type(x[0])==type(y[0])
type(x[1])==type(y[2])
type(x[0])==type(y[1])

y.extend([{'cat': 1}])
x.extend(['cat'])

def same_structure_as(list_1, list_2):
  # Arg
    # list_1: should be an array.  this is the one to compare TO
    # list_2: should be an array.  this is the one we're TESTING
  
  if (type(list_1)!=list) or (type(list_2)!=list):
    return False
  
  elif len(list_1)!=len(list_2):
    return False
  
  z = list(zip(list_1, list_2))
  
  # stuff from Daddy
  def reset_scalars_new(nested_list):
    return [
    reset_scalars_new(item) if isinstance(item, list)
    else 1
    for item in nested_list
    ]
  
  if reset_scalars_new(list_1)==reset_scalars_new(list_2):
    return True
  
  else:
    return False

def reset_scalars_new(nested_list):
  return [
  reset_scalars_new(item) if isinstance(item, list)
  else 1
  for item in nested_list
  ]



# back to me
same_structure_as(x, z)

def same_structure_as(list_1, list_2):
  # Arg
    # list_1: should be an array.  this is the one to compare TO
    # list_2: should be an array.  this is the one we're TESTING
  
  if (type(list_1)!=list) or (type(list_2)!=list):
    return False
  
  elif len(list_1)!=len(list_2):
    return False
  
  z = list(zip(list_1, list_2))
  
  for i in z:
    n = (((type(i[0])==list)*1) + ((type(i[1])==list)*1))
    
    if n==1:
      return False
    
    if n==2:
      
    
    if ((type(i[0])!=list) and (type(i[1])!=list)):
      continue
    if len(i[0])!=len(i[1]):
      return False
    
    














