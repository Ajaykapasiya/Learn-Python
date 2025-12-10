# def sum(a,b):
#     sum = a + b
#     return sum


# print(sum(1,5))

# def cal_avg(a,b,c):
#     sum = a+b+c
#     avg = sum/3
#     return avg 

# print(int(cal_avg(1354323,2435,3435)))


# cites = ["Mumbai","New York","Los Angles","Pune","Noida" ]
# number = [1,2,3,4,5,6,7,8]

# def print_len(list):
#     print(len(list))
   
# print_len(cites)
# print_len(number)

# def print_list(list):
#     for city in list:
#       print(city)


# print_list(cites)
    

def cal_fact(n):
    fact = 1 
    for i in range(1, n+1):
        fact *= i
    print(fact)
cal_fact(6)     


# def converter(usd_val):
#     inr_val = usd_val * 83
#     print(usd_val,"USD =", inr_val, "INR")

# converter(2)




# Recursion

# def show(n):
#     if(n==0):
#      return
#     print(n)
#     show(n-1)

# show(5)


# def fact(n):
#     if(n == 0 or n == 1):
#         return 1
#     else:
#         return n * fact(n-1)
    
# print(fact(6))



# def sum(n):
#     if(n == 0):
#      return 0
#     return sum(n-1) + n

# cal = sum(4)
# print(cal)

# def print_list(list,idx=0):
#      if(idx == len(list)):
#           return
#      print(list[idx])
#      print_list(list, idx+1)

# city =["pune","NY", "LA" ,  "noida"]
# print_list(city)





# def cal_sum(a,b):
#  sum = a + b
#  print(sum)

# cal_sum(1,3)
 
