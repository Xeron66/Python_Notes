class Animal:
    def __init__(self):
        # creating empty class variables else it will throw and exception
        # since we dont want to use the constructor to set values!
        self.__name = ""
        self.__type = ""
        self.__color = ""
    
    # Here we are using decorators to simplify the code
    # and also makes it easy to understand and write!

    # Getters!
    @property
    def name(self) -> str:
        return self.__name
    @property
    def type(self) -> str:
        return self.__type
    @property
    def color(self) -> str:
        return self.__color
    
    # Setters!
    @name.setter
    def name(self, name: str) -> None:
        self.__name = name
    @type.setter
    def type(self, type: str) -> None:
        self.__type = type
    @color.setter
    def color(self, color: str) -> None:
        self.__color = color
    
    # This will later be overriden by Dog or Cat class sound() method
    def sound(self) -> str:
        return f'Some Sound!'
    
    # This is to just get overall detes!
    def getDetails(self) -> str:
        return f'Animal is a {self.type}, Name: {self.name}, has Color: {self.color}'

# Two New classes that inherits Animal Class!
class Dog(Animal):
    def sound(self) -> str:
        return f'{self.name} is a dog and it barks!'

class Cat(Animal):
    def sound(self) -> str:
        return f'{self.name} is a cat and it meows!'

# Code Execution Starts from here!
animal1: Dog = Dog()
animal2: Cat = Cat()

animal1.name = "Buck"
animal1.type = "Dog"
animal1.color = "Yellow"
print(animal1.getDetails())
print(animal1.sound())

animal2.name = "Oreo"
animal2.type = "Cat"
animal2.color = "Balck and White"
print(animal2.getDetails())
print(animal2.sound())



    