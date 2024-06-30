# Started: June 28, 2024
# URL: https://www.codewars.com/kata/6638277786032a014d3e0072/train/python

import pandas as pd
import numpy as np

customers = [(6,8), (2,4), (1,5), (7,7), (1,9)]

#def allocate_rooms(customers):
    
# sort
customers.sort()

# get separate lists
arrivals = pd.Series([x[0] for x in customers])
departures = pd.Series([x[1] for x in customers])

# Create a DF to hold the info
reservations = pd.DataFrame(
  data = list(range(min(arrivals), (max(departures)+1))),
  columns = ['days'])

# Create the first room
reservations['room_1'] = np.nan
rooms = [1]

##for c in customers:
c = customers[0]
# Extract the info
arrive = c[0]
depart = c[1]

# Isolate the rows
days = list(range(arrive, depart+1))

days_index = []
d = arrive
while d <= depart:
  days_index.append(reservations[reservations['days']==d].index[0][0])
  d+=1
days_index

poss_rooms = reservations[reservations['days']>=arrive]
poss_rooms = poss_rooms[poss_rooms['days']<=depart]



index_by_days = 

# Slot it in
for r in poss_rooms:
  
  # Not this one
  if r = 'days':
    continue
  
  # If there's already an opening...
  elif poss_rooms[r].nunique()==0:
    reservations.loc[]


return []
  
