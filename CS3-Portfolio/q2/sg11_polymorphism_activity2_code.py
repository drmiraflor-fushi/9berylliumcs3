# Creating the three classes (Car, Boat, and Drone) with each having its own move() method
class Car:
  def move(self):
    print("The car drives on the road.")

class Boat:
  def move(self):
    print("The boat sails on water.")

class Drone:
  def move(self):
    print("The drone flies in the sky.")

def start_trip(vehicle):  # This function will take a vehicle parameter and call its move() method
  vehicle.move()

# Create individual objects for each class
caryo = Car()
boatyo = Boat()
droneyo = Drone()

# Call the start_trip() method for each object
start_trip(caryo)
start_trip(boatyo)
start_trip(droneyo)

