while True:
    NumberOfWidget = input("Enter the number of widgets: ")
    if NumberOfWidget.isdigit():
        NumberOfWidget = int(NumberOfWidget)
        if NumberOfWidget >= 0:
            break
        else:
            print("Widget number cannot be negative.")
    else:
        print("please enter a number.")

while True:
    NumberOfgizmo = input("Enter the number of gizmo: ")
    if NumberOfgizmo.isdigit():
        NumberOfgizmo = int(NumberOfgizmo)
        if NumberOfgizmo >= 0:
            break
        else:
            print("gizmo number cannot be negative.")
    else:
        print("please enter a number.")

totalWeight = ((NumberOfWidget*75)+(NumberOfgizmo*112))/1000

print("Total weight of all widgets and gizmo is: {}kg".format(totalWeight))