num = list(map(int, list(input())))
fours = 0
sevens = 0

for i in num:
    if i == 4:
        fours += 1
    elif i == 7:
        sevens += 1

if fours+sevens == 4 or fours+sevens == 7:
    print('YES')
else:
    print('NO')