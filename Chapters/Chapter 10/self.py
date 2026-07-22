class employee:
    language = "python" # This is a class type
    salary = 500000

    def getInfo(self):
        print(f"The language is {self.language}. the salary is {self.salary}")

    def greed(self):
        print("Good morning")

jahir = employee()
jahir.language = "java" # this is an instance attribute
jahir.greed()
jahir.getInfo()
# Emplpoyee.getInfo(jahir) 