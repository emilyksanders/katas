# function to solve multiple equations with multiple variables

def solve_lin_eq(constants):
  '''
  A function to solve systems of linear equations.
  None of the terms may have exponents.  There must 
  be exactly as many equations as there are variables.
  
  Arg:
    constants: an array of lists of numbers (int or float).
    All but the last of these numbers should be coefficients, 
    including sign, of the variables being sought.  The order 
    of these coefficients, relative to their respective 
    variables, must be consistent in each list.
    e.g., 2x + 3y - 4z = 10 -> [2, 3, -4, 10]
    10z + 7y - 6x = 67 -> [-6, 7, 10, 67]
  
  Raise:
    Insufficient constants: 
      Each array in {constants} must contain exactly one
      more number than the total number of lists in array.
      e.g., [[1, 2], [3, 4]] is not valid, but this is:
      [[1, 2, 3], [4, 5, 6]]
    Incorrect types:
      Each value in {constants} must be an int or float
      
  Return:
    Tuple (x, y, z), OR string, "Unsolvable"
  '''
  
  # imports
  import numpy as np
  
  
  ## MAKE SURE YOU HAVE ENOUGH ##
  
  # calculate the length of each entry
  ns = [len(i) for i in constants]
  
  # make sure you have the right number of coefficients versus equations
  for i in ns:
    if i > (len(constants) + 1):
      raise insufficient_terms('too many coefficients')
    elif < (len(constants) + 1):
      raise insufficient_terms('too few coefficients')
  
  # make sure they're all the same length
  # which will also ensure they're all nums
  try:
    ns = [i-ns[0] for i in ns] # can't subtract = not nums
  except:
    raise wrong_type('wrong_type Error: non-numerical input')
  # line in the try block will give all 0s if lens are equal
  
  # redudant, but not hurting anything
  if np.sum(ns) != 0:
    raise insufficient_terms('lists within {constants} are of unequal lengths')
  
  
  ## MAKE ALL X COEFFICIENTS = 1 ##
  
  # create a holding array
  x_is_1 = []
  
  # manipulate each equation so the x coefficient is 1
  for equation in constants:
    x_to_1 = [i/equation[0] for i in equation]
    x_is_1.append(x_to_1)
  
  
  #### FROM HERE ON IT ONLY WORKS FOR 3 VARIABLES ####
  #### MAKE RECURSIVE LATER ###
  
  
  ## SUBTRACT X OUT ##
  
  #create a holding array
  x_is_0 = []
  
  # subtract all X out from the normalized equations
  for i in x_is_1[1:]:
    x_to_0 = [i - j for i, j in list(zip(x_is_1[0], i))]
    x_to_0 = x_to_0[1:] # drop the 0 term
    x_is_0.append(x_to_0)
  
  
  ## MAKE ALL Y COEFFICIENTS = 1 ##
  
  # create a holding array
  y_is_1 = []
  
  # manipulate each equation so the x coefficient is 1
  for equation in x_is_0:
    y_to_1 = [i/equation[0] for i in equation]
    y_is_1.append(y_to_1)
  
  
  ## SUBTRACT Y OUT ##
  
  # create a holding array
  y_is_0 = []
  
  # subtract all Y out from the normalized equations
  for i in y_is_1[1:]:
    y_to_0 = [i - j for i, j in list(zip(y_is_1[0], i))]
    y_to_0 = y_to_0[1:] # drop the 0 term
    y_is_0.append(y_to_0)
    
  
  ## SOLVE FOR Z ##
  eq = y_is_0[0]
  z = eq[1]/eq[0]
  
  
  ## SOLVE FOR Y ##
  eq = x_is_0[0]
  y = (eq[2] - (eq[1]*z))/eq[0]
  
  
  ## SOLVE FOR X ##
  eq = constants[0]
  x = (eq[3] - eq[2]*z - (eq[1]*y))/eq[0]
  
  return (x, y, z)
  
    
    
    
  
class wrong_type(Exception):
  '''Custom error for non-number inputs.'''
  
  def __init__(self, message):
    self.message = message
    super().__init__(self.message) 


class insufficient_terms(Exception):
  '''Custom error for insufficient inputs.'''
  
  def __init__(self, message):
    self.message = message
    super().__init__(self.message)   
  
  
  
  
