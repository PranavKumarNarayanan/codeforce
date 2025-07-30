inp = input()
upper = 0
lower = 0

for i in inp:
    if i.isupper():
        upper+=1
    elif i.islower():
        lower+=1
if upper>lower:
    print(inp.upper())
else:
    print(inp.lower())