class animal:
    def __init__(self):
        pass

class pets(animal):
    pass

class dog(pets):
    @staticmethod
    def bark():
        print("Baw Baw!!")

d = dog()
d.bark()