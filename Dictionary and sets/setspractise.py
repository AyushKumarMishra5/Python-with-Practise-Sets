fab = set()
print(type(fab))

S = {"Ayush", "Vinay", "Gurav", 46, 100, True, False, 23.99, 46, 100}
print(type(S))
print(S)

#1
S.add(200)
print(S)

#2
print(S.__len__())

#3
S.remove(True)
print(S)
print(S.__len__())
# len 8

#4 
S.pop()
S.pop()
print(S)
print(S.__len__())


s1 = {1, 2, 3, 4}
s2 ={3, 4, 5, 6}

print(s1.union(s2))
print(s1.intersection(s2))


