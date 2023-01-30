class Garage():
    def __init__(self, parkingSpaces = [*range(46)], tickets = 200, currentTicket = {"paid": False}):
        self.parkingSpaces = parkingSpaces
        self.tickets = tickets
        self.currentTicket = currentTicket

    def takeTicket(self):
        del self.parkingSpaces[-1]
        self.tickets-=1

    def leaveGarage(self):
        if self.currentTicket["paid"] != True:
            self.payForParking()
        else:
            print("Thank you, have a nice day.")
            newSpace = int(self.parkingSpaces[-1]) + 1
            self.parkingSpaces.append(newSpace)
            self.tickets += 1
            # To prove it worked
            print(self.parkingSpaces)
            print(self.tickets)

    def payForParking(self):
        while self.currentTicket["paid"] == False:
            input("Please enter your payment amount: ")
            if input:
                print("Thank you. Your ticket has been paid. You have 15 minutes to exit the garage.")
                self.currentTicket["paid"] = True
                break
        Garage.leaveGarage(self)

    

parkingGarage = Garage()

def park():
    while True:
        parkingGarage.currentTicket["paid"] = False
        response = input("What would you like to do? Park / Pay / See Availability / Quit ")
        if response.lower() == "quit":
            print("Thank you for coming.")
            # response == False
            break
        elif response.lower() == "park":
            print("Please take a ticket and proceed to a space.")
            parkingGarage.takeTicket()
        elif response.lower() == "pay":
            parkingGarage.payForParking()
        elif response.lower() == "see availability":
            print(parkingGarage.parkingSpaces)
            print(parkingGarage.tickets)
        else:
            print("Please choose one of the given options.")

park()