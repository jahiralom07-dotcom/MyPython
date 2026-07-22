class employee:
    salary = 250
    increment = 30

    @property
    def salaryAfterincrement(self):
        return self.salary + self.salary * (self.increment / 100)

    @salaryAfterincrement.setter
    def salaryAfterincrement(self, salary):
        self.increment = ((salary / self.salary) - 1) * 100


e = employee()

e.salaryAfterincrement = 280
print(e.increment)