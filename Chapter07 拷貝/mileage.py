# L-7 MCS 260 : a mileage table
"""
A dictionary records the distance from Chicago
to 3 other cities.  The result of a raw input
is key to query the distances in the dictionary.
"""
CHICAGO = {'Los Angeles' : 2047, 'Miami' : 1237, 'New York' : 807}
CITY = input('Give a city : ')
print('Chicago -', CITY, ':', CHICAGO[CITY], 'miles')
