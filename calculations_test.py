import unittest
import calculations

class TestCalculations(unittest.TestCase):

    def test_deposit(self):
        food = calculations.Category("Food")
        self.assertEqual(food.total, 0)
        self.assertEqual(food.expense_target, 0)
        food.deposit(100, "Initial Deposit")
        self.assertEqual(food.total, 100)
        self.assertEqual(food.expense_target, 100)
    
    def test_insufficient_funds(self):
        food = calculations.Category("Food")
        food.deposit(100, "Initial Deposit")
        with self.assertRaises(Exception):
            food.withdraw(200)
    
    def test_transfer(self):
        food = calculations.Category("Food")
        rent = calculations.Category("Rent")
        self.assertEqual(food.total, 0)
        self.assertEqual(food.expense_target, 0)
        self.assertEqual(rent.total, 0)
        self.assertEqual(rent.expense_target, 0)
        food.deposit(3000, "Initial Deposit")
        self.assertEqual(food.total, 3000)
        self.assertEqual(food.expense_target, 3000)
        food.transfer_expense(2000, rent)
        self.assertEqual(food.total, 1000)
        self.assertEqual(food.expense_target, 1000)
        self.assertEqual(food.spending, 0)
        self.assertEqual(rent.total, 2000)
        self.assertEqual(rent.expense_target, 2000)
        
    
    def test_overspending(self):
        food = calculations.Category("Food")
        self.assertEqual(food.expense_target, 0)
        food.deposit(100, "Initial Deposit")
        self.assertEqual(food.expense_target, 100)
        food.set_target(-50)
        self.assertEqual(food.expense_target, 50)
        with self.assertRaises(Exception):
            food.withdraw(75)

if __name__ == '__main__':
    unittest.main()