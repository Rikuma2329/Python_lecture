n = int(input('n = '))                  

for i in range(1, n + 1):
    if i % 3 == 0:
        if i % 5 == 0:  
            print('FB', end = ' ')
        else:
            print('F', end = ' ')
    elif i % 5 == 0:
        print('B', end = ' ')
    else:
        print(i, end = ' ')