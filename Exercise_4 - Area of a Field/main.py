fieldLength = float(input("Enter the length of the field(in feet): "))
fieldWidth = float(input("Enter the width of the field(in feet): "))

fieldArea = (fieldLength * fieldWidth)/43560
print("Area of the field(in acres) is: {}".format(fieldArea))

