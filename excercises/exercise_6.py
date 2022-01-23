# worked with James Sprague
row = int(input('Enter a row number from 1 to 5: ')) -1
column = int(input('Enter a column number from 1 to 5: ')) -1
for u in range(5):
    for i in range(5):
        if u == row and i == column:
            print('1', end='')
        else:
            print('0', end='')
    print('')
