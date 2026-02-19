"""print("Enter two number")
a = int(input())
b = int(input())

c = a+b
print("the sum is",c)"""


"""print("Enter the number")
marks = int(input())

if(marks>90):
    print("Grade A")
elif(marks>80):
    print("Grade B")
elif(marks>70):
    print("Grade C")
elif(marks>60):
    print("Grade D")
elif(marks>50):
    print("Grade E")
else:
    print("Grade F")"""

"""print("Enter the number")
x = int(input())

print("even") if (x%2 == 0) else print("Odd")"""


"""x = 1
while x <= 5:
  print("Hello")
  x = x+1"""


"""x = int(input("Enter the number: "))
i = 1
y = 0
while i<=x:
        y = y + i
        i+=1
print("the sum is:", y)"""


"""n = int(input("Enter the number: "))
i = 2
while i<=n-1:
    if n%i==0:
        break
    i+=1

if i==n:
    print("Prime")
else:
    print("Non Prime")"""



# print("Enter the Number")
# a = int(input())

# for a in range(1,a+1):
#     print(a,'=',a*a)


# l1 = [1,2,3,4,5]
# # for x in l1:
# #     print(x)
# l1.append(6)
# l1.insert(2,2.5)
# print(l1)


# i = 1
# while i<=10:
#     print(2*i-1)
#     i+=1

# for i in range(1,11):
#     print(2*i-1,end=' ')
# print()

# n = int(input())
# sum = 0

# for a in range(1,n+1):
#     sum = sum + a

# print(sum)


# l1 = [1,2,3,4,5,6]
# i = 0
# while i<=5:
#     print(l1[i],end=' ')
#     i+=1

# for x in l1:
#     print(x)


# l1 = [1,2,3,4,5,6]
# print(len(l1))
# print(max(l1))
# print(min(l1))
# print(sum(l1))
# print(sorted(l1))

# l2 = [3,4,6,3,5,2]
# del l2[3]


# print(l2)

# s1 = 'Hey my name is ajay'
# # print(type(s1))
# print(len(s1))
# print(s1.index('y'))
# print(s1.count('a '))
# print(s1.startswith('Hey'))
# print(s1.isupper())
# print(s1.replace('a','A'))
# print(s1)


# s1 = 'Hello how are you'
# s2 = s1.split(' ')
# s3 = "-".join(s2)
# print(s3)

# s1 = ['Java', 'Test']

# s1.reverse()
# print(s1)


# s1 = ['Java', 'Test']

# result = [x[::-1] for x in s1[::-1]]
# print(result)

# result.reverse()
# print(result)

# s1 = input("Enter the string: ")
# rev = s1.split(' ')[::-1]
# print(" ".join(rev))

# t = (1,2,3,4,5,6,7)
# for x in t:
#     print(x)

# t1 = ([int(e) for e in input().split(',')])
# print(t1)


# s = "Python Is Fun"
# print(" ".join(word[::-1] for word in s.split(' ')[::-1]))

# l1 =[10,20,40,10,50,20,50,60]

# l2 = list(set(l1))
# print(l2)


# s1 = {10,20,30,40,40,30,50,60}
# print(s1)

# s2 = list(s1)
# print(s2)
# print(s2[3])


# d1 ={
#     "name":"Ajay",
#     "age":23,
#     "city":"Noida"
# }

# print(d1)
# print(d1["name"])
# for k in d1:
#     print(k)

# for k in d1:
#     print(k,d1[k])

# del d1["age"]
# print(d1)



# num1 = int(input("Enter the number:"))
# num2 = int(input("Enter the number:"))

# operation = input("Enter the operation (+,-,*,/)")

# if operation == '+':
#     result = num1+num2
# elif operation == '-':
#     result = num1-num2
# elif operation == '*':
#     result = num1*num2
# elif operation == '/':
#     if num1 != 0:
#      result = num1 / num2
#     else:
#        result=("Error! Division by zero")
# else:
#    print("Operation in incorrect")

# print("result:",result)


# class Car:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model

#     def info(self):
#         print(f"The car brand is {self.brand} and its model is {self.model}.")

# my_car = Car("BMW","340i")
# # my_car.info()
# print(my_car.brand,my_car.model )


num = int(input("Enter a number: "))

if num <= 1:
    print("Not a Prime Number")
else:
    is_prime = True
    
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print("Prime Number")
    else:
        print("Not a Prime Number")
