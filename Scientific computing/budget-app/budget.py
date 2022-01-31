from optparse import Values


class Category:
    funds = 0
    def __init__(self, name: str):
        self.category = name
        self.ledger = list()

    def deposit(self, amount: float, description =""):
        assert amount >= 0, f"The deposit can't be negative"
        self.ledger.append({"amount": amount, "description": description})
        self.funds += amount

    def withdraw(self, amount:float, description=""):
        assert amount >= 0, f"The withdraw can't be negative"
        if Category.check_funds(self, amount):
            self.ledger.append({"amount": amount * -1, "description": description})
            self.funds -= amount
            return True
        else:
            return False
    
    def transfer(self, amount: float, other: object):
        assert amount >= 0, f"The transfer can't be negative"
        if Category.check_funds(self, amount):
            self.withdraw(amount, f"Transfer to {other.category}")
            other.deposit(amount, f"Transfer from {self.category}")        
        else:
            return False
    
    def check_funds(self, amount:float):
        return self.funds >= amount

    def get_balance(self):
        return self.funds

    def __str__(self) -> str:
        amountOfAsterisk = 30- len(self.category)
        printMe = ""
        
        for i in range(amountOfAsterisk//2):
            printMe += "*"
        printMe +=self.category
        for i in range(amountOfAsterisk//2):
            printMe += "*"
        
        printMe += "\n"

        for i in range(len(self.ledger)):
            line = list(self.ledger[i].values())

            line[0] = "{:.2f}".format(line[0])
            
            printMe += line[1][:23]

            for i in range(30 -(len(line[1][:23]) + len(line[0][:7]))):
                printMe += " "

            printMe += line[0][:7]
            printMe += "\n"

        printMe += f"Total: {self.funds}"
        return printMe



def create_spend_chart(categories):
    percentages = get_percentages(categories)
    
    
    pass

def get_percentages(categories: list):
    allSpent = 0
    categorySpent = list()
    for category in categories:
        categorySpentIterator = 0
        for transfers in category.ledger:
            if transfers["amount"] < 0:
                allSpent -= transfers["amount"]
                categorySpentIterator -= transfers["amount"]
        categorySpent.append(categorySpentIterator)
    percentages = list()
    for parts in categorySpent:
        percentages.append(round((parts / allSpent*10),0))
    
    return percentages
