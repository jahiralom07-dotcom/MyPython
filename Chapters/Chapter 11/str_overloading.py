class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return f"Student name: {self.name} and age: {self.age}"
    

s = student("jahir", 20)
print(s)