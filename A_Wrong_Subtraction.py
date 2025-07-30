num, k = map(int, input().split(' '))
for i in range(1, k+1):
    numlist = list(map(int, list(str(num))))
    if numlist[-1] != 0:
        num = num-1
    elif numlist[-1] == 0:
        num = int(num/10)
print(num)