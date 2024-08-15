# write a program which inputs user name followed by Good Morning
name = input("Enter your name: ")
print("Good afternoon"+" "+name)

#Question 2:- Write a program which replaces the name and date in the following:
letter = '''Dear |Name| you are selected |date|'''

print(letter.replace("|Name|", "Ayush").replace("|date|", "22|08|2024"))

#question 3: Write a program which identifies the double space in the program
text = input("Enter you text  here:")
print(text.find("  "))

#question 4: Replace the double space in third problem with the 3 spaces
text = input("Enter you text  here:")
print(text.replace("  ", "   "))

#Question 5: Write a program to format this following sentence:
sent = "Hi Ayush, \nThis \"code\" you have provided is nice,\n Thanks!"

print(sent)