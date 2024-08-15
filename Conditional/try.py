m1 = "Make a lot of money"
m2 = "buy now"
m3 = "subscribe this"
m4 = "click this"

spam = input("Enter the messege you have received: ")

if spam == m1 or spam == m2 or spam == m3 or spam == m4:
    print("This is a spam comment.")
else:
    print("This is not a spam comment, than this comment is real.")