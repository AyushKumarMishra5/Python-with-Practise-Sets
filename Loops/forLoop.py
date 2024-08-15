# for loop: is a loop where we know howmuch times the code will be executed
# using for loop for the list problem
l = ["Ayush", "Ankit", "Raman", "Vinay", "Abhishek"]
for i in l:
    print(i)
    
# using for loop for the printing of tuple problem
t =("Ayush", "ANkit", "Rohit", "Vinay", "Ragda")
for i in t:
    print(i)
    
# using for loop for strings:
name = "Ayush"
for i in name:
    print(i)
    
# using for loop to print multiple of any number using the step size
for i in range(0, 100, 5):
    print(i)
    
# using for loop with else cmd
list2 = [1, 23, 76, 98]

for i in list2:
    print(i)
else:
    print("Done!") # this is printed when the loop exhausts

# using break statement in loop it helps in exiting the loop at the time when the condititon is true
print("Break Statement")
for j in range(100):
    if (j == 35):
        break
    print(j)
    
# using continue statement in loop which actually exemptes the value selected and regulates the loop till the range.
print("Continue Statement")
for j in range(100):
    if (j == 35):
        continue
    print(j)
    
    
# Pass STatement: it is a null statement which tells us to do nothing.
# it is used when we want to do nothing in a loop or if statement.
print("Pass Statement")
for i in range(100):
    pass

i = 0
while(i<45):
    print(i)
    i += 1
