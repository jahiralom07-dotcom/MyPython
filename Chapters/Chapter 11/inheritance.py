class employee:
    company = "ITC"
    def show(self):
        print(f"The name is: {self.name} and the salary is {self.salary}")

# class programmer:
#     company = "ITC Infotech"
#     def show(self):
#         print(f"The name is: {self.name} and the salary is {self.salary}")
        
#         def showLanguage(self):
#             print(f"The name is: {self.name} and the salary is {self.language}")

class programmer(employee):
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The name is: {self.name} and he is good with {self.language} language")
        
a = employee()
b = programmer()
print(a.company, b.company)