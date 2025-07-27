class Tracker:
    
    
    def __init__(self, balance, budget, income):
        self.balance = balance
        self.budget = budget
        self.income = income
        print(self.balance)
    
    def update_balance(self, numerical_value):
        self.balance += numerical_value
        print("New Balance: {}".format(self.balance))
    
    def __repr__(self):
        return "Balance: {balance}\nBudget: {budget}\nIncome: {income}\nCategories: {categories}".format(income = self.income, balance = self.balance, budget = self.budget, categories = self.categories)

    def category(self):
        self.categories = {}
        while(True):
            category = input("Enter a category (or enter X to return to main menu): ")
            if category.lower() == "x":
                break
            if category in self.categories.keys():
                print("Category already exists, please enter a different category (or enter x to return to main menu)")
            else:
                self.categories[category] = 0
                print("Category added: {}".format(category))
                break

test_object = Tracker(300, 400, 120)
test_object.update_balance(-300)
test_object.category()
print(test_object)