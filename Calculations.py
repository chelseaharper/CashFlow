import datetime

#### Function to create an account ####
def create_account():
    pass

##### Functions to define spacing of text display in console ####
def head_spacing(name, symbol, length):
  space_length = length - len(name)
  left_side = symbol * (space_length//2)
  right_side = symbol * (length - len(name) - len(left_side))
  formatting = left_side + name + right_side
  return formatting

def item_spacing(description, symbol, length, amount):
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

#### Function to calculate spending by expense category ####
def spending(categories):
    total_sum = sum(i.spending for i in categories)
    result = []
    for i in categories:
      result.append((i.expense_type, (i.spending * 100) // total_sum))
    return result

##### Creation of categories of spending and tracking of expenses ####
class Category:
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
        self.expense_target = int(amount)
        self.expense_target_frequency = frequency
    
    def deposit(self, amount, description="", date = datetime.datetime.now()):
        self.total += amount
        date_string = date.strftime("%d-%b-%Y")
        self.ledger.append({"amount: ":amount,
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
        if amount > self.total:
            over_target = abs(self.total - amount)
            return over_target
        else:
            return True
    
    def __str__(self):
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


if __name__ == "__main__":
    create_account()

