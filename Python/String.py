class Student:
    def __init__(self, name ,age):
        self.name = name
        self.age = age

    def Student_details(self):
        print(f"My name is {self.name} and my age is {self.age} ")

s1 = Student("Ajay",22)
print(s1.name)
print(s1.age)
s1.Student_details()

class gard_Student(Student):
    def __init__(self, name, age , year):
        super().__init__(name, age)
        self.year=year

    def Student_details(self):
        print(f"My name is {self.name} and my age is {self.age} and i complete my gard. in{self.year}")

s2 = gard_Student("Sam",22,2025)
print(s2.name)
print(s2.age)
print(s2.year)
s2.Student_details()




