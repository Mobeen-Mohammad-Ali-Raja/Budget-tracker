class Tracker:
    
    # initialising
    def __init__(self):
        self.categories = {}

    #update methods
    def update_balance(self):
        #print(self.categories.keys())
        
        if not self.categories:
            print("\nNo category has yet been created")
            print("\nReturning back to menu")
            return
        
        for category_key, category_value in self.categories.items():
            print("{} : {} ".format(category_key, category_value))
            
        category = input("Please select a chosen category to update")
        if category in self.categories():
            amount = input("Please enter amount")
            category[category] += amount
            print("Updated {category} with {amount}".format(category, amount))
        print("New Balance: {}".format(self.balance))
    
    #printing out object string information method
    def __repr__(self):
        return "Balance: {balance}\nBudget: {budget}\nIncome: {income}\nCategories: {categories}".format(income = self.income, balance = self.balance, budget = self.budget, categories = self.categories)

    #category that allows expenses to be divided into
    def category(self):
        while(True):
            print("")
            category = input("Enter a category (or enter X to return to main menu): ")
            amount = 0
            if category.lower() == "x":
                break
            if category in self.categories.keys():
                print("")
                print("Category already exists, please enter a different category (or enter x to return to main menu)")
                continue
            amount = float(input("Enter amount: "))
            self.categories[category] = amount
            print("")
            print("Category added: {}".format(category))
            
            
    def get_total_budget(self):
        total = 0
        for value in self.categories.values():
            total += value
        print("") total
    def view_all(self):
        for key, value in self.categories:
            print("{}: {}".format(key, value))
    
    
#print("\U2708")
test_object = Tracker()
while(True):
    print("")
    print("""
          -----------------------------
          Budget Application Menu
          -----------------------------
          1. Create Category
          2. Add Income
          3. View Categories
          4. View Total Budget
          5. View All
          X. Exit
          """)
    response = input("Select an option to choose from: ")
    if response == "1":
        test_object.category()
    elif response == "2":
        test_object.update_balance()
    elif response == "3":
        print("Budget View: " + str(test_object.get_total_budget()))
    elif response == "4":
        print("Total Budget remaining: {}".format(test_object.get_total_budget()))
    elif response == "5":
        test_object.view_all()
    elif response.lower() == "x" or response == "0":
        print("----------------------------------")
        print("Ending program")
        print("----------------------------------")
        break
    else:
        print("----------------------------------")
        print("Error Incorrect Response")
        print("Please enter an appropriate response")
        print("----------------------------------")
