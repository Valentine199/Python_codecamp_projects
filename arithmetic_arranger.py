def arithmetic_arranger(problems: list, calculate=False):
    # I turn the strings into more handleable classes
    if CheckProblemsLength(problems):
        return "Error: Too many problems."
    problemObjects = list()
    for items in problems:
        problemObjects.append(problem(list(items.split())[0], list(items.split())[1], list(items.split())[2], calculate))
    
    # creates a list of lists which contains the list of the numbers and opperator for each object
    brokenLines = BreakObjectsToLines(problemObjects)
      
    # We go through the broken lines as many times as many lines we need and always get the string needed for that specific line
    # since we can only have a maximum of four lines we should be able to even mic things up if neccessary
    ans = ""
    for i in range(4):
        for brokenLine in brokenLines:
            if(len(brokenLine)>=i):
                ans += brokenLine[i]+"    "
        ans += "\n"
    return ans

def CheckProblemsLength(problems: list):
    return len(problems)>5  
def BreakObjectsToLines(problemObjects: list):
    formatedProblems = list()

    for i in range(len(problemObjects)):
        formatedProblems.append(problemObjects[i].MakeFormat())
    
    brokenLines = list()
    for formatedProblem in formatedProblems:
        brokenLines.append(formatedProblem.split("\n"))
    
    return brokenLines

class problem:
    
    def __init__(self, firstNum:str, opp: str, secondNum:str, calculate=False):
        assert opp =="+" or opp =="-", "Error: Operator must be '+' or '-'."
        assert len(firstNum)< 5 and len(secondNum)< 5, "Error: Numbers cannot be more than four digits."
        assert firstNum.isnumeric() == True and secondNum.isnumeric() ==True, "Error: Numbers must only contain digits."

        self.FirstNum = firstNum
        self.Opp = opp
        self.SecondNum = secondNum
        self.calc = calculate
        self.difference =  problem.GetLengthDifference(self)


    def GetLengthDifference(self):
        dif = len(self.FirstNum) - len(self.SecondNum)
        if dif <0:
            self.Bigger = self.SecondNum
        else:
            self.Bigger = self.FirstNum
        return abs(dif)

    def MakeFormat(self):
        Oneformated = ""
        if(self.Bigger == self.FirstNum):
            Oneformated += f"  {self.FirstNum}\n{self.Opp}"
            for i in range (len(self.Bigger) - len(self.SecondNum) + 1):
                Oneformated += " "
            Oneformated += f"{self.SecondNum}\n"
            for i in range (len(self.Bigger)+2):
                Oneformated += "-"
        else:
            for i in range(len(self.Bigger)-len(self.FirstNum)+2):
                Oneformated += " "
            Oneformated += f"{self.FirstNum}\n{self.Opp} {self.SecondNum}\n"
            for i in range (len(self.Bigger)+2):
                Oneformated += "-"
        if self.calc == True:
            result = str(problem.DoCalculation(self))
            Oneformated += "\n"
            for i in range(len(self.Bigger)-len(result)+2):
                Oneformated += " "
            Oneformated +=f"{result}"

        
        return Oneformated
    
    def DoCalculation(self):
        if(self.Opp == "+"):
            return int(self.FirstNum) + int(self.SecondNum)
        else:
            return int(self.FirstNum) - int(self.SecondNum)



