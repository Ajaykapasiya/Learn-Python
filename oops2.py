# (1) Class & Object

# class Car:
#     def __init__(self, brand, color):
#         self.brand = brand
#         self.color = color

#     def drive(self):
#         print(f"{self.brand} in {self.color} color is driving.")

# # Object creation
# car1 = Car("BMW", "Black")
# car2 = Car("Audi", "Red")

# car1.drive()
# car2.drive()



# (2) Encapsulation (🔐 Data Hiding)

# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance  # private attribute

#     def showBalance(self):
#         print("Your Balance is:", self.__balance)

# acc = BankAccount(5000)
# acc.showBalance()
# # acc.__balance  ❌ will give error (private data)


# 3) Inheritance (Parent → Child)

# class Animal:
#     def sound(self):
#         print("Some sound")

# class Dog(Animal):  # Inheriting Animal class
#     def sound(self):
#         print("Dog barks 🐶")

# d = Dog()
# d.sound()



# 4) Polymorphism (One name, many forms)

# class Bird:
#     def fly(self):
#         print("Birds can fly ✈️")

# class Penguin:
#     def fly(self):
#         print("Penguins cannot fly ❌")

# for obj in (Bird(), Penguin()):
#     obj.fly()



# Abstraction (Hide complexity)


# from abc import ABC, abstractmethod

# # Abstract Class
# class Vehicle(ABC):
#     @abstractmethod
#     def start(self):
#         pass

# # Child Class
# class Car(Vehicle):
#     def start(self):
#         print("Car started with a key 🔑")

# # Another Child Class
# class Bike(Vehicle):
#     def start(self):
#         print("Bike started with a self-start button 🚲")

# # Using the classes
# car = Car()
# bike = Bike()

# car.start()
# bike.start()
