
list =[]
temp = 0
while temp != 'QUIT':
    takin = input('Enter a number or QUIT to quit: ')
    temp = takin
    if temp != 'QUIT':
        takin = int(takin)
        if takin%2 == 0:
            list.append(takin)
print(list)