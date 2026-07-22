class Demo:
    a = 4

o = Demo
print(o.a) #Print the class attribute beacuse instance attribute is not present
o.a = 0 #instance attribute is set
print(o.a) #print the instance attribute because instance attribute is present 
print(Demo.a) #Print the class attribute