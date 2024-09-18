class Bear:
    # Class attribute
    species = "Ursidae"

    # Constructor (initializer) method
    def __init__(self, name, age, bear_type):
        # Instance attributes
        self.name = name
        self.age = age
        self.bear_type = bear_type
    
    # Instance method
    def description(self):
        return f"{self.name} is a {self.age}-year-old {self.bear_type} bear."
    
    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}."

# Creating an object (instance of the class)
bear1 = Bear("Baloo", 5, "American Black")
print(bear1.description())  # Output: Baloo is a 5-year-old American Black bear.
print(bear1.speak("Roar!"))  # Output: Baloo says Roar!
