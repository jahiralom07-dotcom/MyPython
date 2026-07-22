class employee:
    def __init__(self):
        print("Constructor of Employee")
    a = 1

class programmer(employee):
    def __init__(self):
        print("Constructor of programmer")
    b = 2
        
class manager(programmer): 
    def __init__(self):
        super().__init__()
        print("Constructor of manager")
    c = 3

# o = employee()
# print(o.a)

# o = programmer()
# print(o.a, o.b)

o = manager()
print(o.a, o.b, o.c)

  