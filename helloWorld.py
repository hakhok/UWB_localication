fileList = [1, 2, 3, 4, 5, 6, 7]
numberOfFiles = len(fileList)
numberOfRows = int(numberOfFiles/4) + 1
axis = []
for row in range(numberOfRows):
    column = []
    for _ in range(4):
        column.append("ax")
    axis.append(column)
print(axis)