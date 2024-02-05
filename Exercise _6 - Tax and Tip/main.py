while True:
    mealCost = input("Enter the cost of the meal: ")
    if mealCost.isdigit():
        mealCost = int(mealCost)
        if mealCost > 0.0:
            break
        else:
            print("Enter a valid price")
    else:
        print("Cost of the meal should be a whole number")

taxAmount = 0.05 * mealCost
tipAmount = 0.18 * mealCost
totalAmount = taxAmount + tipAmount

print("\nTax amount: {}".format(round(taxAmount,2)))
print("Tip amount: {}".format(round(tipAmount,2)))
print("Total amount: {}".format(round(totalAmount,2)))