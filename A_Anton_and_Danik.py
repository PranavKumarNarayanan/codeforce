n = int(input())
wins = list(input())
a = 0
d = 0
for i in wins:
    if i == 'A':
        a+=1
    elif i== 'D':
        d+=1
if a>d:
    print('Anton')
elif a == d:
    print('Friendship')
else:
    print('Danik')