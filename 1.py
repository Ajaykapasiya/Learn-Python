# a = 5.4
# b = 98
# c = 8989.43

# print(a,b,c)
# d = int(input("enter the value: "))
# print("The value is: ",d)



# a = 9
# b = 7 
# c = 8

# print("Sum 0f a + b is:",a+b)
# print("Diff. 0f a + b is:",a-b)
# print("Multiply 0f a + b is:",a*b)
# print("Divide 0f a + b is:",a/b)


# num = int(input("Enter the value: "))
# print("Even" if num % 2 == 0 else "odd")

# a,b,c = map(int,input().split())
# print(min(a,b,c))


# p = int(input("P: "))
# r = int(input("R: "))
# t = int(input("T: "))
# print((p*r*t)/100)


#  To check a string is palindrome or not

# n = input()
# rev = ""
# for char in n:
#     rev = char + rev

# if n == rev:
#     print("Yes it's palindrome")
# else:
#   print("It's not a palindrome")   



# num = 20 
# while num > 0:
#     print(num)
#     num = num - 2


# for num in range(20 , 0, -2)=:
#     print(num)


#  find min and max element from array

# def find(arr):
#     minn , maxx = arr[0],arr[0]

#     for num in arr[1:]:
#         if num < minn:
#             minn = num
#         elif num > maxx:
#             maxx = num   
#     return minn , maxx

# array = (12,23,56,34,3,2,5,7,9,6)
# minn , maxx = find(array)
# print(minn, maxx)


# Find HCF of two number 

# num1 = int(input("Enter the number: "))
# num2 = int(input("Enter the number: "))

# while num2 != 0:
#     num1, num2 = num2, num1 % num2 
# print("The HCF of two number:",num1)


# Find vowles in string 

# input_val = input().lower()
# vowels = ''

# if "a" in input_val:
#     vowels += 'a'
# if "e" in input_val:
#     vowels += 'e'
# if "i" in input_val:
#     vowels += 'i'
# if "o" in input_val:
#     vowels += 'o'
# if "u" in input_val:
#     vowels += 'u'

# print(vowels)


# s = input().lower()
# count = sum(1 for ch in s if ch in "aeiou")
# print(count)



# Encode decode the string 
# alpha = 'abcdefghijklmnopqrstuvwxyz'
# encode = 'defg'
# decode = ''
# for i in range(len(encode)):
#     decode += alpha[(alpha.index(encode[i])-3)%26]
# print(decode)


# Factorial

# n = int(input())
# fact = 1
# for i in range(1, n+1):
#     fact *= i
# print(fact)


# Fibonacci Series
# n = int(input())
# a, b = 0, 1
# for _ in range(n):
#     print(a, end=" ")
#     a, b = b, a + b


# s = "ajay"
# # rev = s[::-1]
# # print(rev)
# print(''.join(reversed(s)))  # yaja
