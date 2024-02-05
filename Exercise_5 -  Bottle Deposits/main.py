while True:
    firstConatinerNumber = input("Enter number of drink containers holding one liter or less ")
    if firstConatinerNumber.isdigit():
        firstConatinerNumber = int(firstConatinerNumber) 
        if firstConatinerNumber >= 0:
            break
        else:
            print("Please enter some valid number of drink containers ")
    else:
        print("Please enter a valid number of drink containers")

while True:
    secondConatinerNumber = input("\nEnter number of drink containers holding more than one liter " )
    if secondConatinerNumber.isdigit():
        secondConatinerNumber = int(secondConatinerNumber)
        if secondConatinerNumber >= 0:
            break
        else:
            print("Please enter some valid number of drink containers ")
    
    print("Please enter a valid number of drink containers")


refundAmount = (firstConatinerNumber * 0.10) + (secondConatinerNumber * 0.25)
print("\nThank you for returning these conatiners. You will receive ${}".format(refundAmount))

