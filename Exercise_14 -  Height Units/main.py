number_of_foot = float(input("Enter number of foot: "))
number_of_inches = float(input("Enter number of inches: "))

result_centimeters = (number_of_foot * 12 * 2.54) + (number_of_inches * 2.54)
print(f"\nThe data provided in centimeters is : {round(result_centimeters,4)}")