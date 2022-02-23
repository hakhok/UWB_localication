from distutils import filelist
from matplotlib import pyplot as plt
import numpy as np
import csv
import os



fileName = 'rangeAcuracy'
fileType = '.csv'
fileList = []
avrgDistList = []

fileNumber = 1
while os.path.isfile(fileName + str(fileNumber) + fileType):
        fileList.append(fileName + str(fileNumber) + fileType)
        fileNumber += 1

plotRssiList = []
plotDistanceList = []

fig, (ax1, ax2) = plt.subplots(2)

for file in fileList:
    number_list = []
    distance_list = []
    rssi_list = []

    with open(file, newline='') as csvfile:
        rangeReader = csv.reader(csvfile, delimiter=',')
        for row in rangeReader:
            try:
                number = [int(s) for s in row[0].split() if s.isdigit()][0]
                distance = [int(s) for s in row[2].split() if s.isdigit()][0]
                rssi = [int(s) for s in row[3].split() if s.lstrip("-").isdigit()][0]
                
                if (distance != 0) and rssi != 0:
                    #print(f"number: {number}, distance: {distance}, rssi: {rssi}")
                    number_list.append(number)
                    distance_list.append(distance)
                    rssi_list.append(rssi)
            except:
                pass
    plotDistanceList.append(np.average(distance_list))
    plotRssiList.append((np.average(rssi_list)))
    #plt.plot(np.average(distance_list), np.average(rssi_list), '-', lw = 2)
    avrgDistList.append(f"{(np.average(distance_list)/1000).round(2)} m, average: {(np.average(rssi_list)).round(2)}")
    ax2.plot(number_list, rssi_list)
ax1.plot(plotDistanceList, plotRssiList)
ax1.set(xlabel="Distance (mm)")
ax1.set(ylabel="RSSI (dBm)")
ax2.set(xlabel="Samples")
ax2.set(ylabel="RSSI (dBm)")
ax2.legend(avrgDistList)
fig.suptitle('RSSI målt over ulike distanser')
plt.show()
