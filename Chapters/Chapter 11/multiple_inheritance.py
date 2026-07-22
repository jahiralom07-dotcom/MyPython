class employee:
    company = "ITC"
    name = "dedfault name"
    def show(self):
        print(f"The name is: {self.name} and the salary is {self.company}")

class coder:
    language = "python"
    def printlanguage(self):
        print(f"Out of all the language here is your language: {self.language}")
    

class programmer(employee, coder):
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The name is: {self.company} and he is good with {self.language} language")
        
a = employee()
b = programmer()

b.show()
b.printlanguage()
b.showLanguage()
# print(a.company, b.company)