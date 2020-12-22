x = [[1,5,9], [4,6,9]]
y = [[3,5,7], [7,6,3]]

result = [[0,0,0],[0,0,0]]

for i in range(len(x)):
    for j in range(len(y)):
        result [i][j] = x[i][j]+y[i][j]
print(result)        