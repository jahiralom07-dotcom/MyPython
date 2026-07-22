class TwoDVector:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def show(self):
        print(f"The Vactor is: {self.i}i + {self.j}j")

class ThreeDVactor(TwoDVector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k 

    def show(self):
        print(f"The Vactor is: {self.i}i + {self.j}j + {self.k}k")

print("2D vactor -----")
i = int(input("Enter 1st number: "))
j =  int(input("Enter 2nd number: "))
a = TwoDVector(i, j)
a.show()

print("\n3D vactor-----")
i = int(input("Enter 1st number: "))
j =  int(input("Enter 2nd number: "))
k =  int(input("Enter 3nd number: "))
b = ThreeDVactor(i, j, k)
b.show()