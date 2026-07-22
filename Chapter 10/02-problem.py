class Calculator:
    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"The square is {self.n**2}")
    
    def cube(self):
        print(f"The square is {self.n**3}")

    def squareroot(self):
        print(f"The square is {self.n**1/2}")

num = int(input("Enter the value: "))
a = Calculator(num)
a.square()
a.cube()
a.squareroot()