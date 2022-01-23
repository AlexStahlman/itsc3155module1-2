# Worked with James Sprague
list1=[]
list2=[]
for i in range(5):
    list1.append(int(input('Enter a number for the first list ')))
for v in range(5):
    list2.append(int(input('Enter a number for the second list ')))
list3=[]
for i in list1:
    for h in list2:
        if i==h:
            if i not in list3:
                list3.append(i)
print(list3)