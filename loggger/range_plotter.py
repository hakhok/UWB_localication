from matplotlib import pyplot as plt
import numpy as np
import csv

number_list = []
distance_list = []
rssi_list = []

number = 0
distance = 0
rssi = 0

file = 'rangeTest5.csv'

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


def movingPlot():
    plt.plot(distance_list, rssi_list, '-', lw = 1)
    plt.xlabel('Distance (mm)')
    plt.ylabel('RSSI (dBm)')
    plt.title("RSSI målinger under bevegelse")
    plt.grid = True
    plt.show()

def stillPlot():
    plt.plot(number_list, rssi_list)
    plt.xlabel('Sampel number')
    plt.ylabel('RSSI (dBm)')
    plt.title(f"{file}, average: {np.average(rssi_list).round(2)}")
    plt.grid = True
    plt.ylim(-75, -105)
    plt.show()

movingPlot()