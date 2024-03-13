# Define a superclass
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        return f"{self.name} says {self.sound}"

# Define subclasses inheriting from Animal
class Dog(Animal):
    def __init__(self, name):
        # Call the superclass's __init__ method to initialize name and sound
        super().__init__(name, "Woof")

class Cat(Animal):
    def __init__(self, name):
        # Call the superclass's __init__ method to initialize name and sound
        super().__init__(name, "Meow")

# Create instances of subclasses
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Call methods from the superclass
print(dog.make_sound()) 
print(cat.make_sound())  
