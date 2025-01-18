# Python Practice
# December 4, 2024

# Snail Sort - 4 kyu
# https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1/train/python

# INSTRUCTIONS
# Given an n x n array, return the array elements 
# arranged from outermost elements to the middle 
# element, traveling clockwise.
# 
# array = [[1,2,3],
#          [4,5,6],
#          [7,8,9]]
# snail(array) #=> [1,2,3,6,9,8,7,4,5]
# 
# For better understanding, please follow the 
# numbers of the next array consecutively:
# 
# array = [[1,2,3],
#          [8,9,4],
#          [7,6,5]]
# snail(array) #=> [1,2,3,4,5,6,7,8,9]


# MY STUFF

# imports
import numpy as np

# test array
r = [[1,2,3],
    [4,5,6],
    [7,8,9]]

# convert to array
r = np.array(r)

# get the shape
s = r.shape

# how long should the resulting list be?
d = s[0]*s[1]

# # start pulling elements out
# 
# # entire first row
# e = list(r[0,:])
# 
# # entire first far column, without duplicates
# for i in list(r[1:, -1]):
#   e.append(i)
# 
# 
# for i in list(range(1, s[1])):
#   print(i)


# what if we try chopping up the array?

# make a backup
# b = r.copy()

# restore from backup while I'm testing
r = b.copy()

# initialize a list
e = []

while r.shape != (0, 0):
  
  print('')
  
  # append the top row
  for i in list(r[0,:]):
    print(i)
    e.append(i)
    
  print(e)
  
  # drop the top row
  r = r[1:, :]
  
  print(r)
  print(r.shape)
  print('')
  
  # bail out?
  if r.shape == (0, 0):
    break
  
  
  # append the last column
  for i in list(r[:, -1]):
    print(i)
    e.append(i)
    
  print(e)
  
  # drop the last column
  r = r[:, :-1]
  
  print(r)
  print(r.shape)
  print('')
  
  # bail out?
  if r.shape == (0, 0):
    break


  # append the bottom row, reversed
  for i in (list(r[-1,:])[::-1]):
    print(i)
    e.append(i)
    
  print(e)
  
  # drop the bottom row, reversed
  r = r[0:-1, :]
  
  print(r)
  print(r.shape)
  print('')
  
  # bail out?
  if r.shape == (0, 0):
    break


  # append the first column, reversed
  for i in (list(r[:,0])[::-1]):
    print(i)
    e.append(i)
    
  print(e)

  # drop the first column, reversed
  r = r[:, 1:]
  
  print(r)
  print(r.shape)
  print('')
  
  # bail out?
  if r.shape == (0, 0):
    break


# functionize

def snail(r):

  # convert to array
  r = np.array(r)
  
  # initialize a list
  e = []
  
  while r.shape != (0, 0):

    # append the top row
    for i in list(r[0,:]):
      e.append(i)
    
    # drop the top row
    r = r[1:, :]
    
    # bail out?
    if r.shape == (0, 0):
      break
    
    
    # append the last column
    for i in list(r[:, -1]):
      e.append(i)
    
    # drop the last column
    r = r[:, :-1]
    
    # bail out?
    if r.shape == (0, 0):
      break
  
  
    # append the bottom row, reversed
    for i in (list(r[-1,:])[::-1]):
      e.append(i)
    
    # drop the bottom row, reversed
    r = r[0:-1, :]
    
    # bail out?
    if r.shape == (0, 0):
      break
  
  
    # append the first column, reversed
    for i in (list(r[:,0])[::-1]):
      e.append(i)

    # drop the first column, reversed
    r = r[:, 1:]
    
    # bail out?
    if r.shape == (0, 0):
      break
  
  return e


# test

a = [[1,2,3],
    [4,5,6],
    [7,8,9]]
    
# snail(array) #=> [1,2,3,6,9,8,7,4,5]

For better understanding, please follow the
numbers of the next array consecutively:

b = [[1,2,3],
    [8,9,4],
    [7,6,5]]

# snail(array) #=> [1,2,3,4,5,6,7,8,9]
