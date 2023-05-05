class Investment:
    def __init__(self): #this method initializez all the elements that go into calculating the roi
        self.rent = int(input('please enter the amount you charge for rent: ')) 
        self.laundry = int(input('please enter the amount you charge for laundry: '))
        self.storage = int(input('please enter the amount you charge for storage: '))
        self.property_tax = int(input('Please enter how much you spend on property tax: '))
        self.insurance = int(input('Please enter how much you will spend on Insurasnce: '))
        self.utilities = int(input('Please enter how much you will spend on Utilities: '))
        self.vacancy = int(input('Please enter how much you will save for vacancy: '))
        self.repairs = int(input('Please enter how much you will save for repairs: '))
        self.mortgage = int(input('Please enter how much you will spend on your mortgage: '))
        self.property_manager = int(input('Please enter how much you wiil spend on a property manager: '))
        self.down_payment = int(input('Please enter how much you will spend on the down payment: '))
        self.closing_cost = int(input('Please enter how much you will spend on the rehab budget: '))
    
    def income(self): #this method calculates what the tenant is going to pay you each month for living on the property
        self.total_income = self.rent + self.laundry + self.storage + self.misc
        
        return self.total_income


    def expenses(self):# this method is going to calculate the total expenses permonth as upkeep on the propery
        self.total_expenses = self.property_tax + self.insurance + self.utilities + self.repairs + self.property_manager + self.mortgage + self.vacancy

        return self.total_expenses
    
    def annual_cashflow(self): # this method calculates what your yearly income was
        self.monthly_cashflow = self.income() - self.expenses()
        self.yearly_cashflow = self.monthly_cashflow*12

        return self.yearly_cashflow
    def total_investment(self): # this method is going to get the total investment by adding what was initially spent buying the property

        self.add_up_investments = self.down_payment + self.closing_cost +self.rehab_budget

        return self.add_up_investments
    
    def return_on_investment(self):
        self.roi = (self.annual_cashflow() / self.total_investment())*100

        return self.roi
    
    def driver(self): #this method wraps everything together and calls the return on investment method to get the roi
        print(self.return_on_investment(),"%")

user = Investment()
user.driver()
    
