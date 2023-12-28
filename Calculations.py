import datetime

##### Functions to define spacing of text display in console output ####
def head_spacing(name, symbol, length):
  """ Defines a formatting structure for the category heading """
  space_length = length - len(name)
  left_side = symbol * (space_length//2)
  right_side = symbol * (length - len(name) - len(left_side))
  formatting = left_side + name + right_side
  return formatting

def item_spacing(description, symbol, length, amount):
  """ Defines a formatting structure for the category entries """
  if len(description) > 23:
    descript = description[0:23]
    space_length = length - (len(descript) + len(amount))
    side = symbol * space_length
    formatting = descript + side + amount
  else:
    space_length = length - (len(description) + len(amount))
    side = symbol * space_length
    formatting = description + side + amount
  return formatting

##### Creation of categories of spending and tracking of expenses ####
class Category:
    """ A budget category which tracks spending for a particular type of expense """
    categories = []

    @classmethod
    def add_category(cls, item):
        Category.categories.append(item)
    
    def __init__(self, expense_type):
        self.expense_type = expense_type
        self.ledger = []
        self.total = 0
        self.spending = 0
        self.expense_target = 0
        self.expense_target_frequency = "Monthly"
        Category.add_category(self)
    
    def get_balance(self):
        return self.total
    
    def set_target(self, amount, frequency="Monthly"):
        """ defines predicted spending in the category """
        self.expense_target = int(amount)
        self.expense_target_frequency = frequency
    
    def deposit(self, amount, description="", date = datetime.datetime.now()):
        self.total += amount
        date_string = date.strftime("%d-%b-%Y")
        self.ledger.append({"amount":amount,
                            "description": description,
                            "date": date_string})
    def withdraw(self, amount, description = "", date = datetime.datetime.now()):
        if self.check_funds(amount):
            self.total -= amount
            self.spending += amount
            date_string = date.strftime("%d-%b-%Y")
            self.ledger.append({"amount": -amount, "description": description, "date": date_string})
            return True
        else:
            raise Exception("The account had insufficient funds for this transaction.")
    
    def transfer_expense(self, amount, other):
        transfer = self.withdraw(amount, description = f"Transfer to {other.expense_type}")
        if transfer == True:
            other.deposit(amount, description=f"Transfer from {self.expense_type}")
        return transfer
    
    def check_funds(self, amount):
        return amount <= self.total
    
    def __str__(self):
        """ Redefine string method to create custom print output when object is printed """
        expenses = self.ledger
        line_format = head_spacing(self.expense_type, "*", 30)
        line_items = [line_format]
        for i in expenses:
            index = self.ledger.index(i)
            expense = expenses[index]
            expense_desc = expense["description"]
            expense_amount = "{:.2f}".format(expense["amount"])
            line_item = item_spacing(expense_desc, " ", 30, expense_amount)
            line_items.append(line_item)
        total = item_spacing("Total:", " ", 30, str(self.get_balance()))
        line_items.append(total)
        display = "\n".join(line_items)
        return display
