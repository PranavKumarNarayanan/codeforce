w, l = map(int, input().split(' '))
dim = w*l

if dim%2 == 0:
    print(int(dim/2))
else:
    print(int((dim-1)/2))