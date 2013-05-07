'''
Written by Will Drevno, IEOR 180, 2013
'''
import math
 
def distance(point_A, point_B):
    lat1, lon1 = point_A
    lat2, lon2 = point_B
    radius = 3963.1676 # miles
    dlat = math.radians(lat2-lat1)
    dlon = math.radians(lon2-lon1)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    dist = radius * c
    return dist