text = input('Type a phrase ')
mystring = ''
odd = True
for v in text:
    if odd:
        mystring = mystring + v.upper()

    else:
        mystring = mystring + v.lower()
    if v != " ":
        odd = not odd
print(mystring)