moneyDeposited = float(input("Enter the amount that you want to deposit: "))
annualInterestRate = 0.04
numberOfTimesCompounded = 1
for timeInYears in range(1,4):
    print("Amount of money in savings account in year {} is: {}".format(timeInYears,round((moneyDeposited * (1+(annualInterestRate/numberOfTimesCompounded))**(numberOfTimesCompounded*timeInYears)) - moneyDeposited,2)))


