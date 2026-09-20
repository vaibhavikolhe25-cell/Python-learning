# write a class train which has methods to book a ticket,get status(no of seats) and get fair information of a train runing under indian railways 
from random import randint

class train:


    def __init__(self,trainno):
        self.trainno = trainno

    def book_ticket(self, fro,to):
        print(f"the ticket is booked in train no :{self.trainno} from {fro} to {to}")

    def getstatus(self):
        print(f"train no : {self.trainno}  is running on time")

    def get_fair(self, fro, to):
        print(f"ticket fare on trainno : {self.trainno} from {fro} to {to}  is {randint(234,7665)}")


t = train(1125)
t.book_ticket("pune","mumbai")
t.getstatus()
t.get_fair("pune","mumbai")

from random import randint

class Train:

    def __init__(self, trainno):
        self.trainno = trainno

    def book_ticket(self, fro, to):
        print(f"Ticket booked in train no: {self.trainno} from {fro} to {to}")

    def get_status(self):
        print(f"Train no: {self.trainno} has {randint(1, 100)} seats available")

    def get_fare(self, fro, to):
        print(f"Ticket fair train no: {self.trainno} from {fro} to {to} is ₹{randint(234, 7665)}")


t = Train(1125)

t.book_ticket("Pune", "Mumbai")
t.get_status()
t.get_fare("Pune", "Mumbai")