class employe:
    language = "java" # This is the class attributs
    salary = 13000

jahir = employe()
jahir.name = "jahir" # This is an object/instance attributes
print(jahir.name, jahir.language, jahir.salary)

rohan = employe()
rohan.name = "rohan"
print(rohan.name, rohan.language, rohan.salary) 

# Here name is object/instance attribute and salary and language are class 
# attributes as they direct belong to the class