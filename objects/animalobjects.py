# animalobjects.py
# practice object-oriented programming in the context of animals

class Animal(): # class uses cap first letter
    # constructor
    def __init__(self):
        self.name = "Unnamed"
        self.legs = 0
        # print("I'm in the constructor")
    # method
    def talk(self):
        if self.name != "Unnamed":
            print(f"Hello, my name is {self.name}!")
        else:
            print("Hello.")

# creating an animal object
some_animal = Animal()
# access properties
print(some_animal.name)
some_animal.name = "Rex"
some_animal.legs = 2
print(some_animal.name)

# TODO: Create a new object
#   * name it whatever you like
#   * give it 20 legs
#   * print out the name and legs

some_other_animal = Animal()
some_other_animal.name = "Roland"
some_other_animal.legs = 20
print(f"{some_other_animal.name}\n{some_other_animal.legs}")
print(type(some_other_animal))
some_other_animal.talk()

another_animal = Animal()
another_animal.talk()
