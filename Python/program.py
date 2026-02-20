# num = int(input("Enter a number: "))

# if num <= 1:
#     print("Not a Prime Number")
# else:
#     is_prime = True
    
#     for i in range(2, num):
#         if num % i == 0:
#             is_prime = False
#             break
    
#     if is_prime:
#         print("Prime Number")
#     else:
#         print("Not a Prime Number")


# num = int(input("Enter a number: "))
# fact = 1
# for i in range(1,num+1):
#     fact *= i
# print(fact)


# num = int(input("Enter a number: "))
# sum = 0

# while num > 0:
#     sum += num % 10
#     num //= 10
# print(sum)


# n = int(input("Enter a number: "))
# for i in range(1, n + 1):
#     print("*" * i)


# s = "hello"
# count = 0
# for _ in s:
#     count += 1
# print(count)



# n1 = int(input("enter the number: "))
# n2 = int(input("enter the number: "))
# print(n1,n2)
# n1,n2 = n2,n1
# print(n1,n2)


# num = (input("enter the 3 number: "))

# sum = int(num[0]) + int(num[1]) + int(num[2])

# print(sum)


# num = input("Enter a 3-digit number: ")

# sum_digits = int(num[0]) + int(num[1]) + int(num[2])

# print("Sum of digits:", sum_digits)


# num = input("Enter a 3-digit number: ")
# sum = 0
# for x in num:
#     sum += int(x)

# print(sum)

# x = input()
# rev = x[::-1]
# if x==rev:
#     print(True)
# else:
#     print(False)


# n1 = int(input("Enter the leap year "))

# if n1%400 == 0 or n1%4 == 0 and n1!=0:
#     print("it is leap year")
# else:
#     print("it is not leap year")

# import math

# x1 = float(input("Enter x1: "))
# y1 = float(input("Enter y1: "))
# x2 = float(input("Enter x2: "))
# y2 = float(input("Enter y2: "))

# distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)

# print(distance)


# a = int(input("Enter first angle: "))
# b = int(input("Enter second angle: "))
# c = int(input("Enter third angle: "))

# if a>0 and b>0 and c>0 and ( a + b + c == 180 ):
#      print("Yes, these angles can form a triangle")
# else:
#     print("No, these angles cannot form a triangle")



# a = int(input("Enter first  Number: "))
# b = int(input("Enter second Number: "))
# c = int(input("Enter third  Number: "))

# a1 = a**2
# b1 = b**2
# c1 = c**2

# print(a1+b1+c1)


# x = int(input("Enter the number"))

# fact = 1
# for i in range(1,x+1):
#     fact *= i
# print(fact)


# for i in range (1,50,2):
#     print(i)

# count = 0
# num = 1

# while count < 25:
#     print(num)
#     num += 2
#     count += 1


# x = int(input("Enter the number: "))
# if x <= 1:
#     print("not prime")
# else:
#  is_prime = True

# for i in range(2,x):
#    if x%i==0:
#       is_prime =False
#       break
# if is_prime:
#    print("Prime")

# else:
#    print("Not prime")


# x = int(input("Enter the number "))
# a,b = 0,1

# for i in range(x):
#     print(a,end=" ")
#     a,b = b, a+b

# x = (input("Enter the number: "))
# print(len(x))

# n= 5

# for i in range(1,n+1):
#     print(" "*(n-i) + "*" *(2*i-1))
# for i in range(n,0,-1):
#     print(" "*(n-i) + "*" *(2*i-1))

# n=4
# for i in range(1, n):
#     print("*" * i)
# for i in range(n, 0, -1):
#     print("*" * i)


# n=11

# for i in range(1,n+1):
#     print(" "*(n-i),end="")
#     for j in range(1,i+1):
#       print(j,end="")
#     for j in range(i-1,0,-1):
#       print(j,end="")
#     print()

# n = 4
# num = 1

# for i in range(1,n+1):
#     for j in range(i):
#         print(num,end=" ")
#         num += 1
#     print()



# old_list = [1, 2, 3, 4, 5]
# new =[]

# for num in old_list:
#     new.append(num**2)
# print(new)

# s1 = "Hello how are you"

# print(" ".join(s1.split()[::-1]))


# s1 = ["Java","Test"]

# r = [word[::-1] for word in s1[::-1]]
# print(r)

# s1 = "hello"
# print(s1[-1].upper()+s1[-2:-6:-1])

# s1 = "Hello how are you"
# print(len(s1.split()))

# l1 = [1,2,3,4,5,6,7,8,9,10]
# l2 = []
# l3 = []

# for x in l1:
#     if x %2 == 0:
#         l2.append(x)
#     else:
#         l3.append(x)
# print(l2)
# print(l3)




# x = int(input("Enter the number: "))
# s = str(x)


# print("String value:", s)
# print("Type:", type(s))





