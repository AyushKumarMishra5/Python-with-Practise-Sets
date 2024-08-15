# Sets: is a collection of non repetative items
'''
#1 sets are unordered
#2 sets are unindexed
#3 There is no way to change items in sets
#4 Sets cannot contain duplicate values.
'''
#define a null set:
my_set = set()
print(my_set)

s = {1, 23, 54, 23, 54, 67, 100, 67, "Ayush", "Ayush", "Ankit"}
print(s) #thus proves that sets dosen't contain repetative items

#methods:
#1 add(): adds on item in the set
s.add(566)
print(s)

#2 len(): prints the length of the set
print(len(s))

#3 remove(): deletes the value choose from the set
s.remove(100)
print(s)

#4 pop(): deletes the random elemnet from the set
s.pop()
print(s)

#5 clear(): this method clears the whole elements in the set
s.clear()
print(s)

# IMP #6 union(): prints the values in both the sets which are common
s1 = {1, 2, 45, 68}
s2 = {23, 45, 67, 76}

print(s1.union(s2))
print(s1.intersection(s2)) #actually take the common values in the both the sets