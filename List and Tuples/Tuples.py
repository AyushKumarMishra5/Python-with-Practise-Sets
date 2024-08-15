#Tuples: are the collection of elements which cannot be changed and are also called as immutable
a = (23, 34, 45, 56, -24, 24, 24, 24)

print(type(a)) #Return the class 
# checking weather tuples are really immutable by trying chage its index value
#  a[0] = 24  thus proved that we cannot change the values
print(a)

# Methods in tuples:
# 1. count() : returns the number of occurrences of the specified value in the tuple
# 2. index() : returns the index of the first occurrence of the specified value in the
# 3. Concatenation() : combines two tuples and returns the tuple
print(a.count(24))
print(a.index(24))

t1 = (23,24)
t2 = (34,35)
print(t1+t2)

