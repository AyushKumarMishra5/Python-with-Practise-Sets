# Question1: Multiplication of a number using user input
number = int(input("Enter the number you want to find the multiple of: "))
for i in range(0, 100, number):
    print(i)

# Question2: Write a program to greet all the person name in the list starting with Sir
names = ["Ayush", "Ankit", "Vinay", "Abhishek"]
for j in names:
    print("Sir", j)
    
# Question3: Attempt problem 1 using while loop
num1 = int(input("Enter the number to find its multiples: "))
i = 1
while (i<11):
    print(num1*i)
    i += 1
    
# Question4: Write a program to find weather the number is prime or not using loop
num = int(input("Enter the number to check weather it is prime or not: "))
for i in range(2, num):
    if num % 2 == 0:
        print(num, "is a composite number.")
        break
    else:
        print(num, "is a prime number.")
        
# Question5: write a program to find the sum of first n natural numbers
num2 = int(input("Enter the number to find the sum upto: "))
i = 1
result = 0
while i<=num2:
    result +=i
    i +=1
print("Sum of first n natural numbers is: ", result)

# Question6: write a program to find the factorial of a given number
fact = int(input("Enter the number to find the factorial of: "))
result = 1
for i in range(1, fact+1):
    result *= i
    
    print("The factorial of the given number is: ", result)
    
#Question 7: write the program to print the following star pattern
# *
# **
# ***
star = int("Enter the number of times to print the star pattern: ")

