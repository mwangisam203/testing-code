"""Topic 13: class inheritance."""


class Animal:
    def speak(self):
        # Parent classes hold behavior that many child classes may share.
        return "Some sound"


class Dog(Animal):
    def speak(self):
        # Child classes can override methods when they need specific behavior.
        return "Woof!"


pet = Dog()
print(pet.speak())

# Dog inherits from Animal, then replaces the `speak` behavior.
# Inheritance thinking:
# Use it when objects have an "is a" relationship.
# A Dog is an Animal, so inheritance makes sense here.
