# function: is a group of statements performing a specefic task
# it can be reused by the programmer multiple times insted of writing the same logic again
# function can take arguments and return values
# function can be reused by calling the function name with the required arguments
def plus(): # creating a function
    a = int(input("Enter the number: "))
    b = int(input("Enter the number: "))
    c = int(input("Enter the number: "))
    
    result = (a+b+c)
    print("The sum of three numbers is: ", result)
    
plus()# method to call the function
# plus()
# plus()
# plus()
# plus()

# Quiz1: write a program to greet the user using functions:
def greet():
    name = input("Enter the name of the user: ")
    print("Hello!", name)
    
# greet()
# greet()
# greet()

'''
Types of functions: 
#1 Built in functions: are the function which are provided by the python, such as 
print(), len(), max(), min(), etc.
#2 User defined functions: are the function which are created by the user, and defined such to implementing
logic and calling it to show an output.
'''

#function arguments: return and defualt argument
# defualt argument : it is basically used when in case there is no valye given to the argument inside the function

def retur(name):
    a=input("Enter the name: ")
    b=input("Enter the name: ")
    c=input("Enter the name: ")
    
    return "Ayush is a good boy"

a = retur("Ayush")
print(a)


#defualt argument:
def defult(name, great="Thank You!"):
    print(f"Hello! {name}")
    print(great)
    
defult("Ayush") # as you can see when the agrument was not given the value while calling the function then it took the default value given while intializeing the argument!
# defult("Ayush", "Thank You!") # if you want to give the value.

#recursion: is a function which calls itself
def factorial(n):
    if(n==1 or n==0):
        return 1
    return n*factorial(n-1)

n = int(input("Enter any number: "))
print(f"The factorial of the number is: {factorial(n)}")

# fabiconna series 
def fabiconna(a):
    if(a==0):
        return 0
    elif(a==1):
        return 1
    else:
        return fabiconna(a-1) + fabiconna(a-2)

a = int(input("Enter the number to find the fabiconna series upto: "))
print(f"The fabiconna series is as follows: {fabiconna(a)}")