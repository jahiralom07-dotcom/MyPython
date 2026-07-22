class employee:
    a = 1
    @classmethod 
    def show(cls): #When we use the class decorator the output will show class value(a = 1)
                    #and when wo don't use it then the output will carry instance value(e.a = 45)
        print(f"The class attribute of a is:{cls.a}")

e = employee()
e.a = 45
e.show()