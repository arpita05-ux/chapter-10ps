import random

class Train:
     
    def __init__(self, trainNo):
        self.trainNo = trainNo 



    def book(self, fro, to):
        print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to}")

    def getStatus(self):
        print(f"Train no: {self.trainNo}  is on time.")

    def getFare(self, fro, to):
        print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to} is {random.randint(222, 666)}")


t = Train(12398)
t.book("Rampur", "Delhi")
