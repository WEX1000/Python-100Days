bill = int(input("What was the total bill? "))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
cash = bill + ( bill * ( tip / 100 ) ) / people
bill = input(f'Each person should pay: {cash}')