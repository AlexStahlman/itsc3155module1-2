import string


text = input('Type a phrase ')
mystring = ''
// to cycle through the string
odd = True
for v in text:
    if odd:
        mystring = mystring + v.upper()

    else:
        mystring = mystring + v.lower()
    if v != " ":
        //checking for spaces
        odd = not odd
print(mystring)