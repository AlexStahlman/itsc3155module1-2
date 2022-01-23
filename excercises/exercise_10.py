#worked with james 
grab = str(input('Enter a string: '))
arrlist = []
size = len(grab)
while size >0:
    if size<3:
        new_arr = grab[0:size]
        size = 0
    else:
        new_arr = grab[0:3]
        size = size -3
    new_arr = list(new_arr)
    arrlist.append(new_arr)
    grab=grab[3:]
print(arrlist)
