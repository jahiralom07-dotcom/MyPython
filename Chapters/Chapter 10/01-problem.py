class programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin

p = programmer("jahir", 120000, 786786)
print(p.name, p.salary, p.pin, p.company)

h = programmer("harry", 120000, 786786)
print(h.name, h.salary, h.pin, h.company)


