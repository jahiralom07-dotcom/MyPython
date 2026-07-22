class Vector:
    def __init__(self, l):
        self.l = l

    # def __add__(self, other):
    #     return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    # def __mul__(self, other):
    #     return (self.x * other.x + self.y * other.y + self.z * other.z)

    # def __str__(self):
    #     return f"Vector({self.x}, {self.y}, {self.z})"
    
    def __len__(self):
        return len(self.l)


# Test the implementation
v1 = Vector([1, 2, 3])
print(len(v1))
# v2 = Vector(4, 5, 6)
# v3 = Vector(7, 8, 9)

# print(v1 + v2)   # Vector(5, 7, 9)
# print(v1 * v2)   # 32

# print(v1 + v3)   # Vector(8, 10, 12)
# print(v1 * v3)   # 50