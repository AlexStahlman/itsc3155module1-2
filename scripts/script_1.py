#Alex Stahlman, helped by Dylan Halstead
my_list = [1, 2, 3, 2, 1, 4]
list2 = []
def get_unique_list(list):
    for c in my_list:
        if not c in list2:
            list2.append(c)
    return list2

unique_list = get_unique_list(my_list)
print(unique_list)