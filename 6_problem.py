import random

class Train:
     
    def __init__(slf, trainNo):
        slf.trainNo = trainNo 



    def book(slf, fro, to):
        print(f"Ticket is booked in train no: {slf.trainNo} from {fro} to {to}")

    def getStatus(slf):
        print(f"Train no: {slf.trainNo}  is on time.")

    def getFare(slf, fro, to):
        print(f"Ticket is booked in train no: {slf.trainNo} from {fro} to {to} is {random.randint(222, 666)}")


t = Train(12398)
t.book("Rampur", "Delhi")
t.getStatus()
t.getFare("Rampur", "Delhi")
