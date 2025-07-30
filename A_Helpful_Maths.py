inp = list(input())
num = []
for i in inp:
    if i != '+':
        num.append(i)
num.sort()
inp[::2] = num

print(''.join(inp))
