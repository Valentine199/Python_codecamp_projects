def arithmetic_arranger(problems: list, calculate=False):
    problemObjects = list()
    for items in problems:
        problemObjects.append(problem(list(items.split())[0], list(items.split())[1], list(items.split())[2]))
       
    FirstSpaces = problemObjects
    print("Hello")

class problem:
    
    def __init__(self, firstNum, opp, secondNum):
        self.FirstNum = firstNum
        self.Opp = opp
        self.SecondNum = secondNum
        self.difference =  problem.GetLengthDifference(self)


    def GetLengthDifference(self):
        dif = len(self.FirstNum) - len(self.SecondNum)
        if dif <0:
            self.Bigger = self.SecondNum
        else:
            self.Bigger = self.FirstNum
        return abs(dif)

