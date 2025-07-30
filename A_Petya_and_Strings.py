l = []
for _ in range(2):
    str = input().lower()
    l.append(str)
if l[0] == l[1]:
    print(0)
elif l[0]<l[1]:
    print(-1)
else:
    print(1)