n = int(input())
x = 0
for _ in range(n):
    exp = input()
    if '++' in exp :
        x += 1
    elif '--' in exp:
        x -= 1
print(x)