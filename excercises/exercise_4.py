sho = int(input("Enter list size "))
list = []

i=0
while i<sho:
    noot = input("Enter number "+i)
    list[i] = noot
    i+=1
print(list)
sum_num = 0
for v in list:
    sum_num = sum_num+v
avg = sum_num/len(list)
print('Average is '+avg)