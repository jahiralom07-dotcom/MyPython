# import random
    # or 
from random import randint
 
class train:
    def __init__(self, trainNo):
        self.trainNo = trainNo
         
    def book(self, fro, to):
        print(f"Ticked is booked in train no: {self.trainNo} from: {fro} to {to}")
    
    def getstatus(self):
        print(f"Train no: {self.trainNo} is running on the time")

    def getfare(self, fro, to):
        print(f"Ticket fare in train no: {self.trainNo} from: {fro} to {to} is {randint(0,1000)}")

t = train(987)
t.book("dhubri", "ghy")
t.getstatus()
t.getfare("dhubri", "ghy")