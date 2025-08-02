class Tracker:
    
    # initialising
    def __init__(self, balance, budget, income):
        self.balance = balance
        self.budget = budget
        self.income = income
        self.categories = {}
        print(self.balance)

    #update methods
    def update_balance(self, numerical_value):
        self.balance += numerical_value
        print("New Balance: {}".format(self.balance))
    
    #printing out object string information method
    def __repr__(self):
        return "Balance: {balance}\nBudget: {budget}\nIncome: {income}\nCategories: {categories}".format(income = self.income, balance = self.balance, budget = self.budget, categories = self.categories)

    #category that allows expenses to be divided into
    def category(self):
        while(True):
            category = input("Enter a category (or enter X to return to main menu): ")
            amount = 0
            if category.lower() == "x":
                break
            if category in self.categories.keys():
                print("Category already exists, please enter a different category (or enter x to return to main menu)")
                continue
            amount = float(input("Enter amount: "))
            self.categories[category] = amount
            print("Category added: {}".format(category))
            
            
    def get_total_budget(self, categories):
        total = 0
        for value in categories.values():
            total += value
        return total
    
    
print("\U2708")
test_object = Tracker(300, 400, 120)
test_object.update_balance(-300)
test_object.category()
print(test_object)
print(test_object.get_total_budget(test_object.categories))