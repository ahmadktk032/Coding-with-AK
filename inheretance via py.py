# Function approach gets messy with inheritance
def animal_speak(animal_type, name):
    if animal_type == "dog":
        return f"{name} says woof!"
    elif animal_type == "cat":
        return f"{name} says meow!"
    elif animal_type == "bird":
        return f"{name} says chirp!"
    # What if we add 20 more animals?

# Class approach - clean and extensible
class Animal:
    def speak(self):
        raise NotImplementedError

class Dog(Animal):
    def speak(self):
        return f"{self.name} says woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says meow!"

class Bird(Animal):
    def speak(self):
        return f"{self.name} says chirp!"

# Now adding a new animal type is easy
class Fish(Animal):
    def speak(self):
        return f"{self.name} says blub!"

# Usage
animals = [Dog("Buddy"), Cat("Whiskers"), Bird("Tweety")]
for animal in animals:
    print(animal.speak())  # Same interface, different behavior
