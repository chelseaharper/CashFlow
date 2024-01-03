import calculations

food = calculations.Category("Food")
rent = calculations.Category("Rent")
gas = calculations.Category("Gas")

food.deposit(3000, "Starting money")

rent.deposit(1500, "Starting money")
gas.deposit(300, "Starting money")

food.transfer_expense(1500, rent)
food.set_target(-500)

food.withdraw(200, "Weekly Groceries")
rent.withdraw(1200, "Rent")
gas.withdraw(40, "Gas to store and back")

print(food)
print(rent)
print(gas)