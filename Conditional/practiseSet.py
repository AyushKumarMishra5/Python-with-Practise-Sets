# question1: write a program to find the greatest of 4 numbers entered by the user

n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
n3 = int(input("Enter the third number: "))
n4 = int(input("Enter the fourth number: "))

if n1>n2 and n1>n3 and n1>n4:
    print("The greatest number from all the four numbers is: ", n1)
elif n2>n1 and n2>n3 and n2>n4:
    print("The greatest number from all the four numbers is: ", n2)
elif n3>n1 and n3>n2 and n3>n4:
    print("The greatest number from all the four numbers is: ", n3)
else:
    print("The greatest number from all the four numbers is: ", n4)
    
# write a program to calculate the marks of the student from the following schema
marks = int(input("Enter your marks that you have scored: "))

if marks==100 and marks>=90:
    print("Exellent!")
elif marks<90 and marks==80:
    print("A")
elif marks<80 and marks==70:
    print("B")
elif marks<70 and marks==60:
    print("C")
elif marks<60 and marks==50:
    print("D")
else:
    print("Fail")
    

# write a program toc check weahter the student has passed in threes subjects by scoring a minimum of 40% and to pass minimum 33 % in all 3 subjects
sub1 = int(input("Enter your marks in subject 1: "))
sub2 = int(input("Enter your marks in subject 2: "))
sub3 = int(input("Enter your marks in subject 3: "))

percentage = (sub1 + sub2 +sub3)/300*100
print(percentage)

if percentage >=40 and sub1>=33 and sub2>=33 and sub3>=33:
    print("You have being passed! ")
else:
    print("You have been failed!")
    
    
# write a program to check weather the usrname contains less than 10 letter or not!
user = input("Enter your name: ")
length = user.__len__()
print(length)
if length < 10:
    print("The username containes less than 10 letters!")
else:
    print("The username conatains more than 10 letters.")
    
# write a program to detect the follwoing spam messeges
m1 = "Make a lot of money"
m2 = "Buy now"
m3 = "Subscribe this"
m4 = "click this"

mess = input("Enter the messege to check if it is spammed or not: ")

if m1 == mess or m2 == mess or m3 == mess or m4 == mess:
    print("This is a Spammed messege")
else:
    print("This is not a spammed messege.")
    
# write a program which finds out weather the given name is there in the list or not
list1 = ["Ayush", "Ankit", "Vinay", "Gaurav", "Abhishek"]

name1 = input("Enter the name to be searched: ")

if name1 in list1:
    print("The name is there in the list.")
else:
    print("The name is not there in the list.")
    

# Write a program to fund weather the given post is talking about Ayush or not
post = input("Enter the post to be checked: ")

if "Ayush" in post:
    print("This post is talking about Ayush!")
else:
    print("This post is not talking about Ayush.")
