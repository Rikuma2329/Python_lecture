fizz = 3        #3の倍数かを判断する変数fizz（初期値3）
buzz = 5        #5の倍数かを判断する変数buzz（初期値5）
fizzbuzz = 15       #15の倍数かを判断する変数fizzbuzz（初期値15）

n = int(input('n = '))

for i in range(1, n + 1):
    if i == fizzbuzz:
        fizzbuzz += 15
        fizz += 3
        buzz += 5
        print('FB', end = ' ')
    elif i == fizz:
        fizz += 3
        print('F', end = ' ')
    elif i == buzz:
        buzz += 5
        print('B', end = ' ')
    else:
        print(i, end = ' ')