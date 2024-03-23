#!/usr/bin/python3

from model_car import Car


class Specs(Car):
    def __init__(self, make, model, year, doors, trim, color, price):
        super().__init__(make, model, year)
        self.doors = doors
        self.trim = trim
        self.color = color
        self.price = price

    def print_specs(self):
        print(f"I am a {self.year} {self.make} {self.model}")
        print(f"I have {self.doors} doors")
        print(f"My trim color is {self.trim}")
        print(f"My color is {self.color}")
        print(f"My price is ${self.price}")


if __name__ == "__main__":
    Specs1 = Specs("Ford", "Fusion", 2018, 5, "Premium", "Black", 80000)
    Specs2 = Specs("Toyota", "Corolla", 2019, 5, "Premium", "Black", 30000)
    Specs.print_specs(Specs1)
    Car.make_sound(Specs1)
    Specs.print_specs(Specs2)
    Car.make_sound(Specs2)
