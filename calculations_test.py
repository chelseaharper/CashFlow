import unittest
import calculations

class TestCalculations(unittest.TestCase):

    def test_deposit(self):
        food = calculations.Category("Food")
        self.assertEqual(food.total, 0)
        food.deposit(100, "Initial Deposit")
        self.assertEqual(food.total, 100)
    
    def test_insufficient_funds(self):
        food = calculations.Category("Food")
        food.deposit(100, "Initial Deposit")
        with self.assertRaises(Exception):
            food.withdraw(200)

if __name__ == '__main__':
    unittest.main()