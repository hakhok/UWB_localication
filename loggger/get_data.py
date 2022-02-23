import numpy as np
import csv
import os

def findFilesByName(fileName):
    path = "loggger\\files\\"
    fileType = '.csv'
    fileList = []
    fileNumber = 1
    while os.path.isfile(path+fileName + str(fileNumber) + fileType):
            fileList.append(fileName + str(fileNumber) + fileType)
            fileNumber += 1
    return fileList

def readPositionFile(file):
    number_list = []
    x_list = []
    y_list = []
    z_list = []

    number = 0
    x = 0
    y = 0
    z = 0

    path = "loggger\\files\\"

    with open(path + file, newline='') as csvfile:
        positionReader = csv.reader(csvfile, delimiter=',')
        for row in positionReader:
            try:
                number = [int(s) for s in row[0].split() if s.isdigit()][0]
                x = [int(s) for s in row[1].split() if s.lstrip("-").isdigit()][0]
                y = [int(s) for s in row[2].split() if s.lstrip("-").isdigit()][0]
                z = [int(s) for s in row[3].split() if s.lstrip("-").isdigit()][0]
                
                if x != 0 and y != 0 and z != 0:
                    number_list.append(number)
                    x_list.append(x)
                    y_list.append(y)
                    z_list.append(z)
            except:
                pass
    return [x_list,y_list, z_list]

def readRangeFile(file):
    number_list = []
    ms_list = []
    distance_list = []
    rssi_list = []

    number = 0
    ms = 0
    distance = 0
    rssi = 0

    path = "loggger\\files\\"

    with open(path + file, newline='') as csvfile:
        rangeReader = csv.reader(csvfile, delimiter=',')
        for row in rangeReader:
            try:
                number = [int(s) for s in row[0].split() if s.isdigit()][0]
                ms = [int(s) for s in row[1].split() if s.lstrip("-").isdigit()][0]
                distance = [int(s) for s in row[2].split() if s.lstrip("-").isdigit()][0]
                rssi = [int(s) for s in row[3].split() if s.lstrip("-").isdigit()][0]
                
                if ms != 0 and distance != 0 and rssi != 0:
                    number_list.append(number)
                    ms_list.append(ms)
                    distance_list.append(distance)
                    rssi_list.append(rssi)
            except:
                pass
    return [distance_list, rssi_list]

def makeCalculations(data):
    median = (np.median(data)).round(2)
    average = (np.average(data)).round(2)
    mean = (np.mean(data)).round(2)
    std = (np.std(data)).round(2)
    var = (np.var(data)).round(2)
    calculatedData = [median, average, mean, std, var]
    
    return calculatedData

def writePositionCsvFile(dataList, fileName):
    headerList = [
        "Filename","x-median", "y-median", "z-median", 
        "x-average", "y-average", "z-average",
        "x-mean", "y-mean", "z-mean",
        "x-std", "y-std", "z-std",
        "x-var", "y-var", "z-var",]
    
    with open("loggger\\calculated\\Calculated_"+fileName+".csv", 'w', newline='') as csvfile:
        dataWriter = csv.writer(csvfile, delimiter=',',
                                quotechar=' ', quoting=csv.QUOTE_MINIMAL)
        dataWriter.writerow(headerList)
        for list in dataList:
            dataWriter.writerow(list)

def writeRangeCsvFile(dataList, fileName):
    headerList = [
        "Filename","distance-median", "rssi-median", 
        "distance-average", "rssi-average",
        "distance-mean", "rssi-mean",
        "distance-std", "rssi-std",
        "distance-var", "rssi-var"]
    
    with open("loggger\\calculated\\Calculated_"+fileName+".csv", 'w', newline='') as csvfile:
        dataWriter = csv.writer(csvfile, delimiter=',',
                                quotechar=' ', quoting=csv.QUOTE_MINIMAL)
        dataWriter.writerow(headerList)
        for list in dataList:
            dataWriter.writerow(list)

def runPositionFiles(fileName):
    if not os.path.isfile("loggger\\calculated\\Calculated_"+fileName+".csv"):
        fileList = findFilesByName(fileName)
        allDataList = []
        for file in fileList:
            thisDataList = []
            thisDataList.append(file)
            fileData = readPositionFile(file)
            for data in fileData:
                calculatedData = makeCalculations(data)
                for calc in calculatedData:
                    thisDataList.append(calc)
            allDataList.append(thisDataList)
        writePositionCsvFile(allDataList, fileName)
    else:
        print("Position file already exists")
        ans = input("Delete file? (y/n): ")
        if ans=="y" or ans == "yes":
            try:
                os.remove("loggger\\calculated\\Calculated_"+fileName+".csv")
                print("File deleted")
            except:
                print("Could not delete file")

def runRangeFiles(fileName):
    if not os.path.isfile("loggger\\calculated\\Calculated_"+fileName+".csv"):
        fileList = findFilesByName(fileName)
        allDataList = []
        for file in fileList:
            thisDataList = []
            thisDataList.append(file)
            fileData = readRangeFile(file)
            for data in fileData:
                calculatedData = makeCalculations(data)
                for calc in calculatedData:
                    thisDataList.append(calc)
            allDataList.append(thisDataList)
        writeRangeCsvFile(allDataList, fileName)
    else:
        print("Range file already exists")
        ans = input("Delete file? (y/n): ")
        if ans=="y" or ans == "yes":
            try:
                os.remove("loggger\\calculated\\Calculated_"+fileName+".csv")
                print("File deleted")
            except:
                print("Could not delete file")

if __name__ == '__main__':

    runPositionFiles("positionAcuracy")
    runRangeFiles("rangeAcuracy")
