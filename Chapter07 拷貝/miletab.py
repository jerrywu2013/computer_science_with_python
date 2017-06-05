# L-7 MCS 260 : mileage table as nested dictionary
"""
We use a dictionary of dictionaries to encode the distance in miles
between four cities.  If the user does not make any typing errors when
entering the city names, the distance between the two cities is shown.
"""
DISTANCE = { \
  'Chicago' : {'Los Angeles' : 2047, 'Miami' : 1237, 'New York' : 807},  \
  'Los Angeles' : {'Chicago' : 2047, 'Miami' : 2780, 'New York' : 2787}, \
  'Miami' : {'Chicago' : 1237, 'Los Angeles' : 2780, 'New York' : 1346}, \
  'New York' : {'Chicago' : 807, 'Los Angeles' : 2787, 'Miami' : 1346} \
}
CITY1 = input('Give first city : ')
CITY2 = input('Give second city : ')
print(CITY1, '-', CITY2, ':', DISTANCE[CITY1][CITY2], 'miles')
