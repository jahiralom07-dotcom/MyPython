class complex:
    def __init__(self,r , i):
        self.r = r #real number
        self.i = i #imaginary number

    def __add__(self, c2):
        return complex(self.r + c2.r, self.i + c2.i)
    
    def __mul__(self, c2):
        real_part = self.r * c2.r - self.i * self.i
        imag_part = self.r * c2.r - self.i * self.i
        return complex(real_part, imag_part)
    
    def __str__(self):
        return f"{self.r} + {self.i}i"
    
r = int(input("Enter 1st number: "))
i = int(input("Enter 2nd number: "))
c1 = complex(r, i)
c2 = complex(r, i)

print(c1 + c2)
print(c1 * c2)