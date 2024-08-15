# create a dictionary with hindi words  to the meaning of english word and print them such that the user ask the meaning
hindi_dict = {
    "Namaste" : "Hello",
    "Khana" : "Food",
    "Dekho" : "Look",
    "Chalo" : "Let's go",
    "Kya hai" : "What is it"
}

word = input("Enter the word to be translated in English: ")
print(hindi_dict.get(word))


# take 8 inputs from the user and display all the unique language once
s = set()
print(type(s))
n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
n3 = int(input("Enter the third number: "))
n4 = int(input("Enter the fourth number: "))
n5 = int(input("Enter the fifth number: "))
n6 = int(input("Enter the sixth number: "))
n7 = int(input("Enter the seventh number: "))
n8 = int(input("Enter the eigth number: "))
s.add(n1)
s.add(n2)
s.add(n3)
s.add(n4)
s.add(n5)
s.add(n6)
s.add(n7)
s.add(n8)

print(s)

# Question 3: Check weather a set can have int 18 and string 18 values
a = set()
intn = int(input("Enter the number: "))
stringN = input("Enter the string: ")

a.add(intn)
a.add(stringN)

print(a)

# what will be the length when we add a string value a float value and int value same in the set
k = set()
intN = int(input("Enter the number: "))
stringN = input("Enter the number: ")
floatN = float(input("Enter the float value: "))

k.add(intN)
k.add(stringN)
k.add(floatN)

print(k)
print(len(k))

# s ={} what is the type of s
S = {}
print(type(S)) #dictionary

# create a empty dictionary where let the 4 students  input their langs as keys and their names as values

d = {}
key1 = input("Enter the first language: ")
key2 = input("Enter the first language: ")
key3 = input("Enter the first language: ")
key4 = input("Enter the first language: ")

value1 = input("Enter you name: ")
value2 = input("Enter you name: ")
value3 = input("Enter you name: ")
value4 = input("Enter you name: ")

d.update({key1:value1, key2:value2, key3:value3, key4:value4})
print(d)

# trying if the name of two friends in the dictionary are same:-
l = {}
n1 = input("Enter the first language: ")
n2 = input("Enter the second language: ")
n3 = input("Enter the third language: ")
n4 = input("Enter the fourth language: ")

v1 = input("Enter the name: ")
v2 = input("Enter the name: ")
v3 = input("Enter the name: ")
v4 = input("Enter the name: ")

l.update({n1:v1, n2:v2, n3:v3, n4:v4})
print(l) #checking that if 2 names are same will it work or not!
# thus it will not be taken

# question:8 if names of two friend are same then will it be taken or not
#solution it will be taken as the names are stored in values and values can be same but the key values cannot be!

# Question9:  can you change the list inside a set
# solution: no you cannot change the list inside a set as set is immutable and list is mutable
i = {1, 23, 54, 67, 98, [23,23]}
print(i)

