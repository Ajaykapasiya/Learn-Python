# info = {
#     "name" : "Ajay",
#     "age" : 24,
#     "Subject" : ["Python","Cpp" ,"React"],
#     "Marks" : [87,85,76]
# }

# print(info)
# print(info["name"])
# print(info['age'])
# print(info["Subject"])

# info["name"] = "Bill bsdka"
# info["Surname"] = "Gandu"
# print(info)


# Nested Dictionaries
# student = {
# "name": "Ajay",
# "score":
# {
# "chem": 98,
# "phy": 97,
# "math":95
# }
# }
# print(student)
# print(student["score"])



# Dictionary Methods
# myDict.keys( ) #returns all keys
# myDict.values( ) #returns all values
# myDict.items( ) #returns all (key, val) pairs as tuples
# myDict.get( “key““ ) #return the key according to value
# myDict.update( newDict ) #inserts the specified items to the dictionary

# print(info.keys())
# print(info.values())
# print(info.items())
# print(info.get("Marks"))
# print(info.update({"city" : "Delhi"}))
# print(info)





# Sets

# collection = {1,2,3,4,2,4,"hello","world","hello"}
# print(collection)
# print(len(collection))

# coll2 = {} #empty set
# print(coll2)

# coll3 = set()
# coll3.add(1)
# coll3.add(2)
# coll3.add(3)
# coll3.add(2)
# print(coll3)


# coll3.remove(1)

# print(coll3)
# # coll3.clear()
# # print((coll3))

# print(coll3.pop())
# print(coll3.pop())


set1 = {1,2,3}
set2 = {3,4,5}

print(set1.union(set2))
print(set1.intersection(set2))