# if else

age = int(input("Enter your age: "))
if age>=18:
    print("You are an adult!")
    print("You can drive!")
    print("Congratulations now you can also vote!")
else:
    print("You are under the 18+ cateogory.")
    
# Else if ladder

age1 = int(input("Enter you age: "))
if age1 >= 18 :
    print("You are an adult and you are abouve the consent age.")
    print("You are also eligible to vote now and can use gun in public place!")
elif age1 < 0:
    print("You are not born yet!")
    print("if you are born then why are u entering a negative invalid age!")
elif age1 == 0:
    print("Please enter a valid age, your age shoule range between 1 to the age you are!")
else:
    print("You are under the age consent.")