def fizzbuzz(i):
    if i % 3 == 0 and i % 5 == 0:
        return 'FB'
    elif i % 3 == 0:
        return 'F'
    elif i % 5 == 0:
        return 'B'
    else:
        return str(i)

n = int(input('n = '))

data = list(range(1, n + 1))

result = map(fizzbuzz, data)

print(list(result))