import csv
from matplotlib import pyplot as plt

class Data():
    def __init__(self):
        self.x = []
        self.y = []
        self.timestamp = []

        self.mode = []
        self.mode_timestamp = []

        self.lat = []
        self.long = []
        self.lat_long_timestanp = []

data = Data()

def readPositionFile(file):
    with open(file, newline='') as csvfile:
        positionReader = csv.reader(csvfile, delimiter=',')
        for row in positionReader:
            try:
                name = str(row[0])
                if name == "BCN":
                    x = float(row[8])
                    y = float(row[9])
                    if x != 0 and y != 0 and name == "BCN":
                        data.x.append(x)
                        data.y.append(y)
                        data.timestamp.append(float(row[1]))
                elif name == "MODE":
                    data.mode.append(row[2])
                    data.mode_timestamp.append(row[1])
                elif name == "POS":
                    data.lat.append(float(row[2]))
                    data.long.append(float(row[3]))
                    data.lat_long_timestanp.append(float(row[1]))
            except:
                pass


def plotPos():
    x_list = []
    y_list = []
    x_list_other = []
    y_list_other = []
    loiter_start = 0
    loiter_end = 0
    i = 0
    for mode in data.mode:
        if mode == " Loiter":
            loiter_start = float(data.mode_timestamp[i])
            loiter_end = float(data.mode_timestamp[i+1])
        i+=1
    for x, y, timestamp in zip(data.x, data.y, data.timestamp):
        if timestamp > loiter_start and timestamp < loiter_end:
            x_list.append(x)
            y_list.append(y)
        else:
            x_list_other.append(x)
            y_list_other.append(y)

    plt.scatter(x_list, y_list, c="g")
    plt.scatter(x_list_other, y_list_other, c="pink")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Indoor loiter test")
    plt.grid()
    plt.show()

def plotLatLong():
    x_list = []
    y_list = []
    x_list_other = []
    y_list_other = []
    loiter_start = 0
    loiter_end = 0
    i = 0
    for mode in data.mode:
        if mode == " Loiter":
            loiter_start = float(data.mode_timestamp[i])
            loiter_end = float(data.mode_timestamp[i+1])
        i+=1
    for x, y, timestamp in zip(data.lat, data.long, data.lat_long_timestanp):
        if timestamp > loiter_start and timestamp < loiter_end:
            x_list.append(x)
            y_list.append(y)
        else:
            x_list_other.append(x)
            y_list_other.append(y)
    
    #plt.xlim(0, 7)
    #plt.ylim(0, 7)
    plt.scatter(y_list, x_list, c="g")
    plt.scatter(y_list_other, x_list_other, c="pink")
    plt.xlabel("Latitude")
    plt.ylabel("Longitude")
    plt.title("Indoor loiter test")
    plt.grid()
    plt.show()


#x_list, y_list, number_list = readPositionFile("C:\\Users\\Haako\dev\\source\\github_ws\\UWB_localication\\ArduPilot\\indoorLoiter\\55.log")
readPositionFile(
    "C:\\Users\Haako\\UiT Office 365\\O365-Bachelor Drone - General\\Bachelor\\Flights\\56gang\\67.log")

#plotLatLong()
plotPos()

