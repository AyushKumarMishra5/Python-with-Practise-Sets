myname = {
    "whos is it":"Kaun hai yeh",
    "Hello" :"Namaste",
    "How are you" : "Aap kaise hain",
    "Ayush" : 27,
    "Vinay": 89.5,
    1 : "Gaurav"
}

print(type(myname))
print(myname)

print(myname.items()) #prints the items in the dictionary

print(myname.keys()) #prints the keys in the dictionary
print(myname.values()) #prints the values in the dictionary

myname.update({"Ayush": 97, "Vinay":80, 10: "Gaurav", 2:"Vinay", 3:"Ayush"})
print(myname)

print(myname.get("Ayush1")) # gets the pair the user is searching for

myname.pop(1) #deletes the key selected in the dictionary
print(myname)

myname.clear()
print(myname)



