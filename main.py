class Roi:

    def __init__(self):
        self.possible_income = {}
        self.income_sum = 0
        self.initial_cost = {}
        self.monthly_cost = {}
        self.monthly_cost_sum = 0
        self.investment_sum = 0

    # keep track of all income
    def income(self):
        count = int(input('How many sources of income are there? 💸 : '))
        for i in range(count):
            a = input('What is the source of income?(This includes rent): ')
            b = int(input('How much will the source of income make?: '))
            self.income_sum += b
            self.possible_income[a] = b
            print("\033c")
        print(f'Here are your sources of income: {self.possible_income}')

    
    #Keep track of all expenses
    def cost(self):
        count = int(input('How many costs are there? 💸 : '))
        for i in range(count):
            c = input('What is the cost? (This Mortage Paymen,Bills,ETC...): ')
            d = int(input('How much will the cost be?: '))
            self.monthly_cost_sum += d
            self.monthly_cost[c] = d
            print("\033c")
        print(f'Here are your costs: {self.monthly_cost}')
    

    #Keep track of Initial costs
    def investment(self):
        count = int(input('How many initial costs are there? 💸 : '))
        for i in range(count):
            e = input('What is the cost? (Downpayment, Closing Cost, ETC.....): ')
            f = int(input('How much will the cost be?: '))
            self.investment_sum += f
            self.initial_cost[e] = f
            print("\033c")
        print(f'Here are your costs: {self.initial_cost}')
    

    #Get ROI
    def roi(self):
        if self.income_sum > self.monthly_cost_sum:
            f = self.income_sum - self.monthly_cost_sum
            g = ((f*12) / self.investment_sum)*100
            print(f'Your monthly income is {f}')
            print (f'Your Roi is: {g}')
        else:
            print('Your Spending more than your earning! Your Roi is negative')



    #Run the program
    def run(self):
        print("""
        WHAT WOULD YOU LIKE TO DO?
        -------------------------
        Run- Run the program
        Quit- Exit the program
        """) 
        user = input('What would you like to do? : ').lower().strip()
        
        if user == 'run':
            self.income()
            self.cost()
            self.investment()
            self.roi()
house =  Roi()
house.run()
