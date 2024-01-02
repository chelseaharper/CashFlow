import datetime

##### Functions to define spacing of text display in console output ####
def format_head(name, symbol, length):
    """ Defines a formatting structure for the category heading """
    space_length = length - len(name)
    left_side = symbol * (space_length//2)
    right_side = symbol * (length - len(name) - len(left_side))
    formatting = left_side + name + right_side
    return formatting

def format_item(description, symbol, length, amount):
    """ Defines a formatting structure for the category entries """
    if len(description) > 23:
        descript = description[0:23]
    else:
        descript = description
    space_length = length - (len(descript) + len(amount))
    side = symbol * space_length
    formatting = descript + side + amount
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
    
    def set_target(self, amount):
        """ defines predicted spending in the category """
        # In a more complex program, this would likely be overwritten in a
        # derived class to only adjust the target under certain circumstances
        if self.expense_target == 0:
            self.expense_target = int(amount)
        else:
            self.expense_target += int(amount)
    
    def deposit(self, amount, description="", date = datetime.datetime.now()):
        self.total += amount
        self.set_target(amount)
        date_string = date.strftime("%Y-%m-%d") #ISO format
        self.ledger.append({"amount":amount,
                            "description": description,
                            "date": date_string})
    
    def withdraw(self, amount, description = "", date = datetime.datetime.now()):
        if self.check_funds(amount):
            if self.check_spending(amount):
                self.total -= amount
                self.spending += amount
                date_string = date.strftime("%Y-%m-%d") #ISO format
                self.ledger.append({"amount": -amount, "description": description, "date": date_string})
            else:
                # This else clause could be overwritten in a more complex program to allow overspending
                raise Exception(
                    "This transaction would result in spending beyond the category spending target."
                    )
        else:
            raise Exception("The account had insufficient funds for this transaction.")
    
    def transfer_expense(self, amount, other):
        try:
            self.withdraw(amount, description = f"Transfer to {other.expense_type}")
        except Exception as e:
            raise e
        self.set_target(-amount)
        other.deposit(amount, description = f"Transfer from {self.expense_type}")
    
    def check_funds(self, amount):
        return amount <= self.total
    
    def check_spending(self, amount):
        return (self.spending + amount) <= self.expense_target
    
    def __str__(self):
        """ Redefine string method to create custom print output when object is printed """
        expenses = self.ledger
        line_format = format_head(self.expense_type, "*", 30)
        line_items = [line_format]
        for expense in expenses:
            expense_amount = "{:.2f}".format(expense["amount"])
            line_item = format_item(expense["description"], " ", 30, expense_amount)
            line_items.append(line_item)
        total = format_item("Total:", " ", 30, "{:.2f}".format(self.get_balance()))
        line_items.append(total)
        display = "\n".join(line_items)
        return display
