list=[]
for i in range(10):
    grab = int(input('Enter a number: '))
    if grab not in list:
        list.append(grab)
print(list)