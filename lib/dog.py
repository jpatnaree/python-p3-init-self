#!/usr/bin/env python3

class Dog:

    def __init__(self, name, breed = "Mutt"):
        self.name = name
        # self.favorite_toy = favorite_toy
        self.breed = breed
        print(f"The precious {name} have been given to the world!")

    def bark(self):
        print('Woof')

    def showing_self(self):
        print(f"Name: {self.name} \nBreed: {self.breed}")
    def adopt(self, owner_name):
        self.owner = owner_name
    

# def adopt(dog, owner_name):
#         dog.owner = owner_name


scooby_doo = Dog("Scooby-Doo")

scooby_doo.adopt("Shaggy")
# print(scooby_doo is scooby_doo.showing_self())

scooby_doo.showing_self()
