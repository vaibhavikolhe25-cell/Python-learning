# can u change a self parameter inside a class to something else (say harry) try changing self to slf  or harry and see the effects
from random import randint

class Train:


    def __init__(slf,TrainNo):
        slf.TrainNo = TrainNo


    def book_ticket(tanu, fro, to):
        print(f"the ticket is booked in Train No : {tanu.TrainNo} from {fro} to {to} ")


    def get_status(self):
        print(f"train no : {self.TrainNo} has {randint(2,100)} seats available")


    def get_fair(self,fro,to):
        print(f"Ticket fair on train no: {self.TrainNo} from {fro} to {to} is ₹{randint(444,5000)} ")     


T = Train(1125) 
T.book_ticket("pune", "banglore")
T.get_status()
T.get_fair("pune", "banglore")        