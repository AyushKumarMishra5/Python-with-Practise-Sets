# Question1: write a program using functions to find the greatest of three numbers
def great(a, b, c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

print(f"The greatest number from the three numbers {a}, {b} and {c} is: ", great(a, b, c))

# Question 2: write a program to convert celcius to farenhite using functions
'''
celcius to farenhite
farehnite = celcius*9/5 + 32
'''

def celToFaranite(celcius):
    farenhite = (celcius*9/5) + 32
    return farenhite
celcius = int(input("Enter the current celcius of the room: "))
print(f"The conversion from {celcius}deg to farenhite is: ", celToFaranite(celcius))

# Question 3: How do you prevent a python print() function to print a new line at the end
# using the defalut aregument and keeping it blank
print("Hello!")
print("Ayush")
print("Ankit", end=" ")
print("Mishra",)

# Question 4: Pyhton program to find the dum og n natural numbers using recursive fucntion
# while True: but while adding this remember to add the identation to avoid error!
def sumN(n):
    if n == 1:
        return 1
    else:
        return n * (n+1)//2
    # return n + sumN(n-1) even this logic will work
n = int(input("Enter the number to find the sum upto the numbers: "))
recursive = sumN(n)
print(f"The sum of the first {n} natural numbers is: ", recursive)


# Question 5: Python function which converts inches to cm
'''
1 inch = 2.54 cm
'''
def inchConverter(inch):
    if inch <= 0:
        return False
    else:
        cm = inch * 2.54
        return cm
    
inch = int(input("Enter the height in inches: "))
print(f"The conversion from{inch} to centimeter is: ", inchConverter(inch))

# Question 6: write a python function to remove a given word from list and stip it at the same time.
list = ["Ayush", "Ankit", "Shivam", "Abhishek"]
print(list)
def listRemover(word):
    if word in list:
        list.remove(word)
    else:
        print(f"{word} is not there in the list!")

word = input("Enter the word you want to remove from the list: ")
remove = listRemover(word)
print(remove)
print("The updated list is as follows: ")
print(list)

# Question 7: Python program to find the multiplication table of a given number
def tablesOfNumber(num):
    i = 1
    while i<=10:
        print(f"The product of {num} X {i} is: ", num * i)
        i = i+1

num = int(input("Tell the number you want to find the multiplication table of: "))
tablesOfNumber(num)
        
        
    

