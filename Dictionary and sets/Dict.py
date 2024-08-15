#Dictionary: is a collection of key value pairs
# it is unordered, mutable, indexed and cannot contain duplicate keys

#creating a dictionary where it has two parameters: keys and value
marks = {
    "Ayush" : 78,
    "Vinay" : 100,
    "Gaurav": 1
}
print(marks, type(marks)) #prints the dictionary as it is
print(marks["Ayush"]) # prints the value of the key called

#mtehods:
#items: returns the list of key and values
print("Using the first methods which is Items")
print(marks.items())

#2 keys: returns a list containing the dictionary set keys.
print(marks.keys())

#3 Values: return the values associated with keys in the dictionary
print(marks.values())

#4 Update: it either updates the value selcted or add the values in the dictionary created
marks.update({"Ayush":80, "Guarav":100, "Harsh":90})
print(marks)

#5 Get: this method allows the user to get the value of the key he is entering or provide none in the case if the key dosen't exists.
print(marks.get("Ayush"))
print(marks.get("Ankit")) # checking for a random name.

#the differnce between marks.get("Ayush") and marks["Ayush"] is that if the key appears in the
# dictionary then the dictionary then the value will be returned otherwise for the get 
# method it will return none and for the second method it will throw and error.

#6 pop: it removes the key and return the value of the key been poped out.
print(marks.pop("Harsh"))

#7 clear: it clears the whole dictonary
print(marks.clear())
print(marks) # checking if the dictionary is empty or not.


