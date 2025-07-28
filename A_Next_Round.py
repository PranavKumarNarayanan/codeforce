nk = list(map(str, input().split()))

n = int(nk[0])
k = int(nk[1])

scores = list(map(int, input().split()))

c = 0
for i in scores:
    if i>=scores[k-1] and i!=0:
        c+=1
    
   
    
print(c)