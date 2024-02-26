fuelEfficiency = float(input("Enter the fuel efficiency in miles-per-gallon (MPG): "))
result = (100*3.78541)/(1.60934*fuelEfficiency)
print("Fuel efficiency expressed in liters-per-hundred kilometers (L/100 km) is {}".format(round(result),4))