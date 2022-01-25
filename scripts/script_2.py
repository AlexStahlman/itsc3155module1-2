my_dict_1 = {'a': 5, 'b': 12, 'c': 3, 'd': 9}
my_dict_2 = {'b': 4, 'c': 9, 'd': 10, 'e': 16}
third_dict ={}
def get_combined_dict(dict, dict1):
    for c in my_dict_1:
        for v in my_dict_2:
            if v in c:
                third_dict[c] = my_dict_1[c] +my_dict_2[v]
    return third_dict

combined_dict = get_combined_dict(my_dict_1, my_dict_2)
print(combined_dict)