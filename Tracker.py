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
        return "Balance: {balance}\nBudget: {budget}\nIncome: {income}".format(income = self.income, balance = self.balance, budget = self.budget)
        
test_object = Tracker(300, 400, 120)
test_object.update_balance(-300)
print(test_object)