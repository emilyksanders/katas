# Started: June 28, 2024
# URL: https://www.codewars.com/kata/6638277786032a014d3e0072/train/python

# the input of the prompt will be a list like this
customers = [(6,8), (2,4), (1,5), (7,7), (1,9)]

def allocate_rooms(customers):
  
  # Import these, we need them
  import pandas as pd
  import numpy as np
    
  # Sort by arrival date
  customers.sort()

  # Get a customer number, 1-indexed
  cust_nums = list(range(1, (len(customers)+1)))
  
  # Get separate lists
  arrivals = pd.Series([x[0] for x in customers])
  departures = pd.Series([x[1] for x in customers])
  
  # Create a DF to hold the info...
  reservations = pd.DataFrame(
    data = list(range(min(arrivals), (max(departures)+1))),
    columns = ['days'])
  
  # ...and a list because that's the format they want
  res_list = []
  
  # Create the first room
  reservations['room_1'] = np.nan
  rooms = [1]
  
  # For every customer (by number)
  for n in cust_nums:
  
  # Debugging check 1 - works FINE up to here
  #   res_list.append(n)
  # return res_list
    
    # Rebase to 0 because lists are 0-indexed
    c = customers[n-1] 
    # Debugging check 1 - works FINE up to here
  #   res_list.append(c)
  # return res_list
    
    # Debugging check 7.2
    print(f'debugging check 7, customer {n}')
    
    # Extract the info
    arrive = c[0]
    depart = c[1]
    
    # Debugging check 3 - WORKS FINE TIL HERE
  #   res_list.append(arrive)
  #   res_list.append(depart)
  # return res_list
    
    # Isolate the rows
    days = list(range(arrive, depart+1))
    
    # Debugging check 4 - WORKS TIL HERE
    # print(days)
    
    # Get their index numbers
    # make a placeholder list
    days_index = []
    # start with the first day (arrival)
    d = arrive
    # add the index number of every day until they leave to the list
    while d <= depart:
      days_index.append(reservations[reservations['days']==d].index[0])
      d+=1 # move the counter!
    
    # Debugging check 5 - WORKS TIL HERE
    # print(days)
    # print(days_index) 
    
    # Create a subsetted dataframe to work with
    poss_rooms = reservations.loc[days_index, :]
    
    # Debugging check 6 - WOKRS TIL HERE
    # print(poss_rooms.index)
    # print(days_index)
    
    # Open a "ticket" to assign a room (basically a counter)
    room_assigned = False
    
    # For every possible room (skip the "days" column)
    for room in list(poss_rooms.columns)[1:]:
      # If every row (day) within that column (room) IS NA, 
      # then the sum of notna will be 0.  In that case...
      if poss_rooms[room].notna().sum()==0:
        # Match it back to the original DF and double check that those are NA too
        if reservations.loc[days_index, room].notna().sum()==0:
          # If they are, put the customer in that room,
          reservations.loc[days_index, room] = n
          
          # Debugging check 8.4.1
          print(f'    putting custumer {n}, {c}, into room {room}.')
          
          # close the ticket,
          room_assigned = True
          # add it to the list because that's the format they want,
          r = room.split('_')[-1]  # this should just be the #, i.e., room_1 -> 1
          res_list.append(r)
          
          # Debugging check 8.4.2
          print(f'    added room {r} to res_list, {res_list}.')
        
          # and move on to the next one
          continue
        # If they aren't, something's wrong
        else: 
          # Tell me
          print(f'''
          Error for customer {n}, {c}.
          {room} was NA in poss_rooms but not in reservations for days {days}.
          ''')
          # Abort the whole project
          return reservations
    
    # Debugging check 7 - WORKS TIL HERE
    # print(f'debugging check 7, customer {n}')
    print(f'  customer details: {c}')
    print(f'  ordered res list: {res_list}')
    print(f'  extant rooms: {reservations.columns}')
    
    # At the end of that loop over extant rooms, 
    # check if a room still needs to be assigned, and do so if needed.
    if room_assigned == False:
      # Debugging check 8.1
      print(' creating a new room')
      
      # Create a new room
      new_room = max(rooms)+1
      # Add it to the list of rooms
      rooms.append(new_room)
      
      # Debugging check 8.2 - WORKS TIL HERE
      print(f'  room list: {rooms}')
      
      # Add it to the dataframe
      reservations[f'rooms_{new_room}'] = np.nan
      
      # Debugging check 8.3
      print(f'  extant rooms: {reservations.columns}')
      
      # Put the customer in that room, 
      reservations.loc[days_index, f'rooms_{new_room}'] = n
      # close the ticket,
      room_assigned = True
      # add it to the list because that's the format they want,
      r = room.split('_')[-1]  # this should just be the #, i.e., room_1 -> 1
      res_list.append(r)
      # take the opportunity to sanity-check
      if r == new_room:
        print("just created a new room, it's working!")
      else: 
        print(f"just created a new room, {new_room}, it's not working!")
        return reservations, res_list
    
    # # Debugging check 8 - NOT WORKING
    # print(c)
    # print(res_list)
    # print(reservations.columns)
  
  # At the end of all that, every customer should be assigned.
  # For every customer, I either slotted them into an existing room,
  # or created a new one for them. It's time to return the results!
  return res_list, reservations

# test this
a, b = allocate_rooms(customers)



##### first take that might have been better??

# poss_rooms = reservations[reservations['days']>=arrive]
# poss_rooms = poss_rooms[poss_rooms['days']<=depart]
#
# index_by_days = 
# 
# # Slot it in
# for r in poss_rooms:
#   
#   # Not this one
#   if r = 'days':
#     continue
#   
#   # If there's already an opening...
#   elif poss_rooms[r].nunique()==0:
#     reservations.loc[]
# 
# 
# return []
  
