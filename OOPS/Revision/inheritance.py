class Animal:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        
    def eat(self):
        print("I am eating")

    def sleep(self):
        print("I am sleeping")


class Dog(Animal):
    def bark(self):
        print("I am barking")
    
    def display(self):
        print(f"Age is {self.age}")

dog = Dog("cherry", 22)
dog.bark()
dog.eat()
dog.sleep()
dog.display()