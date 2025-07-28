weight = int(input())

for i in range(0, weight, 2):
    b = weight - i
    if (weight%2 != 0) or (weight==2):
        print('NO')
        break
    else:
        print('YES')
        break