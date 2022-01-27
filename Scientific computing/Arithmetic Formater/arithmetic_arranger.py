def arithmetic_arranger(problems: list, calculate=False):
    problemObjects = list()
    for items in problems:
        problemObjects.append(problem(list(items.split())[0], list(items.split())[1], list(items.split())[2]))
    
    formatedProblems = list()

    for i in range(len(problems)):
        formatedProblems.append(problemObjects[i].MakeFormat())
    
    brokenLines = list()
    for formatedProblem in formatedProblems:
        brokenLines.append(formatedProblem.split("\n"))
    
    ans = ""
    for i in range(3):
        for brokenLine in brokenLines:
            ans += brokenLine[i]+"    "
        ans += "\n"
    return ans
       
    

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

        
        return Oneformated

