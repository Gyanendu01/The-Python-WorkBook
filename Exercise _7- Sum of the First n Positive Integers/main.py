while True:
    userData = input("Enter a number: ")
    if userData.isdigit():
        userData = int(userData)
        if userData > 0:
            break
        else:
            print("Enter any number greater than zero.")
    print("Numbers only allowed")

print("Sum of numbers from {} to {} is {}".format(1,userData,int((userData*(userData+1))/2)))