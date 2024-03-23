#!/usr/bin/python3

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def make_sound(self):
        print("Vroom, vroom, I go quick")

    def print_car(self):
        print(f"I am a {self.year} {self.make} {self.model}")


if __name__ == "__main__":
    Car_1 = Car("Ford", "Fusion", 2018)
    Car_2 = Car("Toyota", "Corolla", 2019)
    Car.print_car(Car_1)
    Car.make_sound(Car_1)
    Car.print_car(Car_2)
    Car.make_sound(Car_2)
