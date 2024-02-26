import cmath
import math
latitude = (input("Enter Latitude values separated by commas: "))
latitudeList = []
for i in latitude.split(","):
    latitudeList.append(math.radians(float(i)))

longitude = (input("Enter Longitude values separated by commas: "))
longitudeList = []
for i in longitude.split(","):
    longitudeList.append(math.radians(float(i)))


distance = 6371.01 * math.acos(math.sin(latitudeList[0]) * math.sin(longitudeList[0]) + math.cos(latitudeList[0]) * math.cos(longitudeList[0]) * math.cos(latitudeList[1] - longitudeList[1]))
print(f"With the given latitude values {latitudeList[0],latitudeList[1]} and longitude values {longitudeList[0],longitudeList[1]} distance between them is {distance}")

