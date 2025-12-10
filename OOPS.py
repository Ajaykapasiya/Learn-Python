# Simple class and object 

# class Car:
#     def __init__(self,brand, model):
#         self.brand = brand
#         self.model = model
    
#     def full_name(self):
#      return f"{self.brand} {self.model}"
 

# class ElectricCar(Car):
#     def __init__(self, brand, model, battery_size):
#         super().__init__(brand,model)
#         self.battery_size = battery_size
       


# my_tesla = ElectricCar('tesla','S','85kwh')
# print(my_tesla.full_name())




# Encapsulation

# class employee:
#    def __init__(self,name, salary):
#       self.name = name
#       self.__salary = salary

# emp = employee('Rick','50000')
# print(emp.name)
# print(emp.__salary)


class Bird:
    def fly(self):
        print("Birds can fly ✈️")

class Penguin:
    def fly(self):
        print("Penguins cannot fly ❌")

for obj in (Bird(), Penguin()):
    obj.fly()
