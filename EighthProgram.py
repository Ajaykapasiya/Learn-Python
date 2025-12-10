# class student:
#     college_name = "ABC clg."

#     def __init__(self , name, marks):
#         self.name = name
#         self.marks = marks
        

# # Method
#     def welcome(self):
#      print("Welcome student")



# s1 = student("Alok",78)
# s1.welcome()
# print(s1.name, s1.marks)

# s2 = student("Om",78)
# print(s2.name, s2.marks, s2.college_name)




# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def __str__(self):
#     return f"{self.name}({self.age})"

# p1 = Person("John", 36)

# print(p1)


# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def myfunc(self):
#     print("Hello my name is " + self.name)

# p1 = Person("John", 36)
# p1.myfunc()





# Inheritance

# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname)

# class Student(Person):
#   def __init__(self, fname, lname, year):
#     super().__init__(fname, lname)
#     self.graduationyear = year

#   def welcome(self):
#     print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

# x = Student("Mike", "Olsen", 2024)
# x.welcome()


# Encapsulation

# Wrapping data (variables) and methods (functions) together.

# Can make variables private to protect data.

# class BankAccount:
#  def __init__(self, balance):
#         self.__balance = balance   # private variable

#  def deposit(self, amount):
#         self.__balance += amount

#  def get_balance(self):
#         return self.__balance

# account = BankAccount(1000)
# account.deposit(500)
# print(account.get_balance()) 




# . Class and Object

# Class → Blueprint/template (like a car design).

# Object → Real entity created from a class (like an actual car).

# class Car:
#     def __init__(self, brand, color):
#         self.brand = brand
#         self.color = color

#     def show(self):
#         print(f"{self.color} {self.brand}")

# # Creating objects
# car1 = Car("BMW", "Black")
# car2 = Car("Tesla", "White")

# car1.show()  # Output: Black BMW
# car2.show()  # Output: White Tesla


# Polymorphism

# Same function name, but different behaviors (many forms).

# class Bird:
#     def fly(self):
#         print("Some birds can fly")

# class Sparrow(Bird):
#     def fly(self):
#         print("Sparrow flies high")

# class Ostrich(Bird):
#     def fly(self):
#         print("Ostrich cannot fly")

# b1 = Sparrow()
# b2 = Ostrich()

# b1.fly()   # Output: Sparrow flies high
# b2.fly()   # Output: Ostrich cannot fly



# from abc import ABC, abstractmethod

# # Abstract class
# class Vehicle(ABC):
    
#     @abstractmethod
#     def start(self):   # Abstract method (no implementation here)
#         pass

#     @abstractmethod
#     def stop(self):
#         pass


# # Concrete class
# class Car(Vehicle):
#     def start(self):
#         print("Car starts with a key.")

#     def stop(self):
#         print("Car stops with brakes.")


# class Bike(Vehicle):
#     def start(self):
#         print("Bike starts with a kick.")

#     def stop(self):
#         print("Bike stops with hand brakes.")


# # Using objects
# v1 = Car()
# v1.start()   # Output: Car starts with a key.
# v1.stop()    # Output: Car stops with brakes.

# v2 = Bike()
# v2.start()   # Output: Bike starts with a kick.
# v2.stop()    # Output: Bike stops with hand brakes.


# Creating class
# class student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#         print("Welcome")
  
# s1 = student("Ajay", 89)
# print(s1.name, s1.marks)


class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

f
    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hi", self.name, "Your avg. score is:",sum/3)

s1 = student("Ajay",[89,90,98])     
s1.get_avg()        f
