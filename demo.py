import calculations

food = calculations.Category("Food")
rent = calculations.Category("Rent")
gas = calculations.Category("Gas")

food.deposit(1000, "Starting money")
rent.deposit(1500, "Starting money")
gas.deposit(300, "Starting money")

food.withdraw(200, "Weekly Groceries")
rent.withdraw(1200, "Rent")
gas.withdraw(40, "Weekly Groceries")

print(food)
print(rent)
print(gas)