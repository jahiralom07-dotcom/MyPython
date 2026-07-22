class employee:
    a = 1

class programmer(employee):
    b = 2
        
class manager(programmer): 
    c = 3

o = employee()
print(o.a) #prints the a attribute
# print(o.b) # Shows an erroe as there is no b attribute in employee class

o = programmer()
print(o.a, o.b)

o = manager()
print(o.a, o.b, o.c)

