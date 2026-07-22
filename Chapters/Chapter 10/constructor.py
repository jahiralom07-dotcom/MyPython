class employee:
    language = "python" # This is a class type
    salary = 500000

    def __init__(self, name, salary, language): # Dunder method which is automatically called

        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")

    def getInfo(self):
        print(f"The language is {self.language}. the salary is {self.salary}")

    def greed(self):
        print("Good morning")

jahir = employee("jahir", 100000, "Kotlin")
jahir.name = "jahir"
print(jahir.name, jahir.salary, jahir.language)
