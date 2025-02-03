class Maggie_Pack:
    def __init__(self,name,price):   #cosntructor #instance 
        self.name=name
        self.price=price
    def check_budget(self,budget):
        if not isinstance(budget,(int,float)) or budget<0:
            raise ValueError("Budget cannot be strings or Negative")
        return True
    def calculate_balance(self,budget):
        return budget-self.price   #budget is a local variable so we didn't use self 
    def  suggest_packs(self,budget):
        try:
            self.check_budget(budget)
            if budget>self.price:
                print("You can buy this",self.name)
                print("Your remaining Balance:",self.calculate_balance(budget))
            elif budget==self.price:
                print("You can Buy this",self.name,"\nNo Balance is remaining")
            else:
                print("You will not be able to affors",self.name, "pack")
        except ValueError as e:
            print(e)
small=Maggie_Pack("Small",20)
regular=Maggie_Pack("Regular",30)
big=Maggie_Pack("Medium",40)
packs=[small,regular,big]
try:
    budget=float(input("Enter the Budget:"))
    print("Your budget is :",budget)
    for pack in packs:
        pack.suggest_packs(budget)
except ValueError:
    print("Enter a Numerical Value")
    
