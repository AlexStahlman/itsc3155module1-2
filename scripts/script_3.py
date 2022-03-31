#Worked with James Sprague
impu = input("Enter a String: ")

def get_string_letter(impu):
    dict1 = {}
    for c in impu.lower():
        if c.isalpha():
            if c in dict1:
                dict1[c] += 1
            else:
                dict1[c] = 1
    return dict1
print(get_string_letter(impu))