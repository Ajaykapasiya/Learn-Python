# f = open("demo.txt" , "r")

# data = f.read(15)
# print(data)
# print(type(data))


# line1 = f.readline()
# print(line1)

# line2 = f.readline()
# print(line2)

# f.close()


# Write

# f = open("demo.txt" , "w")

# f.write("Learning Python is fun and rewarding.Practice a little every day to get better.Small projects help you understand concepts faster.Consistency is the key to mastering programming.")

# f.close()



 # Append

# f = open("demo.txt" , "a")

# f.write("Learning Python is fun and rewarding.Practice a little every day to get better.Small projects help you understand concepts faster. Hello everyone.\n Learn react and javascript")

# f.close()



# with open("pratice.txt" , "w") as f:
#     f.write("Hi everyone \nwe are learning File I/O\n") 
#     f.write("using Java.\nI like  programming in Java.")


# with open("pratice.txt","r") as f:
#     data = f.read()

# new_data = data.replace("Java" , "python")
# print(new_data)

word = "learning"
with open("pratice.txt","r") as f:
    data = f.read()
    if(data.find(word) != -1):
        print("Found")

    else:
        print("Not found")