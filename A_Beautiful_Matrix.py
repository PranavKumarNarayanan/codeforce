matrix = []
for _ in range(5):
    l = list(map(int, input().split(' ')))
    matrix.append(l)
for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            coordinates = [i+1,j+1]

dif1 = abs(coordinates[0] - 3)
dif2 = abs(coordinates[1] - 3)

print(dif1+dif2)

