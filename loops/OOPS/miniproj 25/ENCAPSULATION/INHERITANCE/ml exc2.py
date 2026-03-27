class vehicle:
    def vehicle_brand(self):
        print("Car Brand: BMW")

class car(vehicle):
    def car_model(self):
        print("Car Model: 120")

class sportscar(car):
    def sportscar_speed(self):
        print("Sportscar speed: 200")
a = sportscar()
a.vehicle_brand()
a.car_model()
a.sportscar_speed()
