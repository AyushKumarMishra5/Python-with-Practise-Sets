# Lists: These are the sequence of elements which can be changed or it could be also told in a way that it is mutable.
List1 = ["Ayush", "Ankit", "Vinay", 32, 56, 87, False, True]
print(type(List1))

print(List1[0])
#As the list defines that it is mutable so ut can be changed in the following way:
List1[0] = "Nitish"

print(List1[0])
print(List1) #Thus the defintion verified!

# These are the following list methods or functions that could be used to set some properties
List2 = [23, 54, 2, 56, 9, 100]

#1 Sorting:
print(List2) #Befor sorting
List2.sort()
print("After sorting the list")
print(List2)

#2 Reverse: it actually reverses the direction of elements
#3 Append : It actually adds an element at the end of the list
#4 Insert: It actually adds the elemets at the specific position
#5 Pop: it helps deleting the element present at the specefic position
#6 Remove: It helps in deleting the element present in the list
List3 = [23, 34, 2, 56, 78, 99, 1]
print(List3) #before Reversing
print("After reversing the list the following elements are: ")
List3.reverse()
print("Adding another element in the list.")
List3.append(33)
print("Addition of list at an specific position")
List3.insert(3, 1001) #first mention the index and then the element
print("Deletion of an element through an index value.")
a = List3.pop(2)  #gives us the ided that which element has been poped out
print(a)
print("Removing of an specified element by the user or the element is predefined")
List3.remove(56)


print(List3)

print("Thus finally happy to complete this List chapter! \nThankx harry bhaiya")


