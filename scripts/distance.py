from math import radians, cos, sin, asin, sqrt

def distance(lat1, lat2, lon1, lon2):
    lon1 = radians(lon1)
    lon2 = radians(lon2)
    lat1 = radians(lat1)
    lat2 = radians(lat2)
      
    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
 
    c = 2 * asin(sqrt(a))
    
    # Radius of earth in kilometers. Use 3956 for miles
    r = 6371
      
    # calculate the result in meters
    return(c * r) * 1000

# Calculates speed in m/s and km/h 
def speed(distance_in_meters, delta_time):
    m_p_s = distance_in_meters / delta_time
    km_h = 3.6 * m_p_s
    return m_p_s, km_h
    

# driver code
lat1 = 59.13232333
lat2 = 59.131885

lon1 = 11.4876
lon2 = 11.48873833

#t1 = 10
#t2 = 20
#d_t = t2 - t1
d_t = 256

dist = distance(lat1, lat2, lon1, lon2) 
mps, kmh = speed(dist, d_t)
print("\n\n")
print(f"Distance: {round(dist, 2)} Meters\tSpeed: {round(mps, 2)} m/s = {round(kmh, 2)} km/h")
print("\n\n")


