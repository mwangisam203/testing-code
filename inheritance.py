"""Topic 13: class inheritance."""


class Animal:
    def speak(self):
        return "Some sound"


class Dog(Animal):
    def speak(self):
        return "Woof!"


pet = Dog()
print(pet.speak())

# Dog inherits from Animal, then replaces the `speak` behavior.
