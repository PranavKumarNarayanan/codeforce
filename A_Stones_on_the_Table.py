n = int(input())
col = list(input())
c = 0
i = 0
while i<n-1:
    if col[i] == col[i+1]:
        c+=1
    i+=1
print(c)