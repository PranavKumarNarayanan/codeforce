n = int(input())
for _ in range(0,n):
    string = input()
    if len(string) > 10:
        l = list(string)
        num = len(l[0:-2])
        print(str(l[0])+str(num)+str(l[-1]))
    else:
        print(string)