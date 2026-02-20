# Reverse a string

# s = "Python"
# print(s[::-1])


# Check palindrome

# s = "madam"
# s1 = s[::-1]
# print(s == s1)


# Count characters (without len)

# s = "hello"
# count = 0
# for _ in s:
#     count += 1
# print(count)



# Count vowels
# s = "Pythonaei"
# print(sum( 1 for c in s if c.lower() in 'aeiou'))


# Reverse words in sentence
# s = "Python is easy"
# print(" ".join(s.split()[::-1]))


# Remove duplicate characters
# s = "programming"
# print("".join(dict.fromkeys(s)))


# Remove extra spaces
# s = "  Python   is   easy  "
# print(" ".join(s.split()[::-1]))


# Convert string → list
# s = "a,b,c"
# print(s.split(','))

# Convert list → string
# lst = ['a','b','c']
# print(" ".join(lst))


# Join characters with -
# s = "INTERVIEW"
# print("-".join(s))


# Count words
# s = "Python is very easy"
# print(len(s.split()))


# Longest word
# s = "Python programming is powerful"
# print(max(s.split(), key=len))

# Shortest word
# s = "Python is powerful"
# print(min(s.split(), key=len))

# Remove duplicate words
# s = "python is easy and python is powerfull"
# print(" ".join(dict.fromkeys(s.split())))


# Split by multiple spaces
# s = "a   b    c"
# print(s.split())


# Count uppercase letters
# s = "PyTHon"
# print(sum(1 for c in s if c.isupper()))
# print(sum(1 for c in "PyTHon" if c.islower()))


# Count digits
# s = "abc123"
# print(sum(1 for c in s if c.isdigit()))


#Capitalize first & last letter
# s = "python"
# print(s[0].upper() + s[1:-1] + s[-1].upper())





