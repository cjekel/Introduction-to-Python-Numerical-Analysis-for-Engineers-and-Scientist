x = [1,2,3,4,5]
y = [11,8,2,3,4,81,66]
z = []
for i in x:
    for j in y:
        z.append(i + 2*j)

def innerLoop(i,y):
    for j in y:
        z.append(i + 2*j)
z = []
for i in x:
    innerLoop(i,y)