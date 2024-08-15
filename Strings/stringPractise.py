#string: a text entiled with double inverted commas stored in a data type.
#Strings are immutable so some changes cannot be done suppose changig of a lteer in the name
name = "vinay"
name2 = "VINAY"
print(name)

#prints the lenght of the text
print(len(name))

#splits the value
print(name[0:3])
print(name[0:2])
print(name[0:5])

# string functions: 

#Changes the first letter and makes it capitalize
#it changes only first letter in the word and doesn't changes with all
print(name.capitalize())

#endswith and startswith
#endswith check weather the names ends with the identation you have put and the same occurs with the statwith
print(name.endswith("nay")) #endswith
print(name.startswith("Bi")) #startswith

#upper and to lower: it changes thw whole text to the function being called in the python string
print(name.upper())
print(name2.lower())

# escape sequence: it is an code when added provides some identation to text

text = "Vinay is a good boy and \nhe will remain good boy!" #next line
text2 = "Vinay is a good boy and \t\nhe will remain good boy!" #tab space
print(text)
print(text2)

#replace: it replaces the chosen word with the newly added word

text3 = "Vinay Loves flower"
replace = text3.replace("flower", "Banana")
print(replace)

