#Worked with Austin Hadinger
total = 0
c =5
i = 0
while i < c:
    integ = input("Put in an Integer: ")
    x = integ.isnumeric()
    
    if x is False:
        print("Not a valid integer... try again ")
    else:
        total += int(integ)
        c = c- 1
print(total)
