import numpy as np

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 1000]

median = np.median(data)
average = np.average(data)
mean = np.mean(data)
std = np.std(data)
var = np.var(data)
calculationsList = ["Median", "Average", "Mean", "STD", "Var"]
dataList = [median, average, mean, std, var]
returnList = []
    
for calculation, data in zip(calculationsList, dataList):
    returnList.append([calculation, data])
print(returnList)