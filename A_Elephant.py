import math as m
dist = int(input())
movements = [1,2,3,4,5]
steps = []
for i in movements:
    steps.append(m.ceil(dist/i))
print(min(steps))
