from matplotlib import pyplot as plt
import csv
import os


def readCsvFile(file = 'positionAcuracy2.csv'):
    path = "loggger\\files\\"
    number_list = []
    x_list = []
    y_list = []
    z_list = []

    number = 0
    x = 0
    y = 0
    z = 0

    with open(path+file, newline='') as csvfile:
        positionReader = csv.reader(csvfile, delimiter=',')
        for row in positionReader:
            try:
                number = [int(s) for s in row[0].split() if s.isdigit()][0]
                x = [int(s) for s in row[1].split() if s.lstrip("-").isdigit()][0]
                y = [int(s) for s in row[2].split() if s.lstrip("-").isdigit()][0]
                z = [int(s) for s in row[3].split() if s.lstrip("-").isdigit()][0]
                
                if x != 0 and y != 0 and z != 0:
                    #print(f"number: {number}, distance: {distance}, rssi: {rssi}")
                    number_list.append(number)
                    x_list.append(x)
                    y_list.append(y)
                    z_list.append(z)
            except:
                pass
    return x_list,y_list, z_list, number_list, file


def position2D():
    x_list,y_list, z_list, number_list, file = readCsvFile()
    plt.scatter(x_list, z_list, c=number_list)
    plt.xlabel('X (mm)')
    plt.ylabel('Y (mm)')
    plt.title(file)
    plt.grid(True)
    plt.plot([0, 0], [0, 5000], 'k-')
    plt.plot([0, 5000], [5000, 5000], 'k-')
    plt.plot([5000, 5000], [5000, 0], 'k-')
    plt.plot([5000, 0], [0, 0], 'k-')
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()


def position3D():
    x_list,y_list, z_list, number_list, file = readCsvFile()
    fig = plt.figure()
    ax = plt.axes(projection="3d")
    ax.scatter3D(x_list, y_list, z_list, c=number_list, cmap='hsv')
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    plt.show()


def plotMultiple(grid = True):
    x_list,y_list, z_list, number_list, file = readCsvFile()
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3)

    ax1.scatter(x_list, y_list, c=number_list)
    ax1.set(xlabel='X (mm)')
    ax1.set(ylabel='Y (mm)')
    ax1.grid(True)
    
    ax1.set_aspect(1)
    draw_circle = plt.Circle((1070, 725), 100,fill=False)
    ax1.add_artist(draw_circle)

    ax2.scatter(x_list, z_list, c=number_list)
    ax2.set(xlabel='X (mm)')
    ax2.set(ylabel='Z (mm)')
    ax2.grid(True)
    
    ax2.set_aspect(1)
    draw_circle = plt.Circle((1070, 1125), 100,fill=False)
    ax2.add_artist(draw_circle)

    ax3.scatter(y_list, z_list, c=number_list)
    ax3.set(xlabel='Y (mm)')
    ax3.set(ylabel='Z (mm)')
    ax3.grid(True)
    
    ax3.set_aspect(1)
    draw_circle = plt.Circle((725, 1125), 100,fill=False)
    ax3.add_artist(draw_circle)

    if grid:
        ax1.plot([0, 0], [0, 5000], 'k-')
        ax1.plot([0, 5000], [5000, 5000], 'k-')
        ax1.plot([5000, 5000], [5000, 0], 'k-')
        ax1.plot([5000, 0], [0, 0], 'k-')
        ax2.plot([0, 0], [0, 2500], 'k-')
        ax2.plot([5000, 5000], [0, 2500], 'k-')
        ax2.plot([0, 5000], [2500, 2500], 'k-')
        ax2.plot([5000, 0], [0, 0], 'k-')
        ax3.plot([0, 0], [0, 2500], 'k-')
        ax3.plot([5000, 5000], [0, 2500], 'k-')
        ax3.plot([0, 5000], [2500, 2500], 'k-')
        ax3.plot([5000, 0], [0, 0], 'k-')


def plotXY(file, ax):
    x_list,y_list, z_list, number_list, file = readCsvFile(file)
    ax.scatter(x_list, y_list, c=number_list)
    ax.set(title=file)
    ax.grid(True)
    ax.plot([0, 0], [0, 5000], 'k-')
    ax.plot([0, 5000], [5000, 5000], 'k-')
    ax.plot([5000, 5000], [5000, 0], 'k-')
    ax.plot([5000, 0], [0, 0], 'k-')
    ax.set_aspect(1)


def findFilesByName(fileName):
    path = "loggger\\files\\"
    fileType = '.csv'
    fileList = []
    fileNumber = 1
    while os.path.isfile(path + fileName + str(fileNumber) + fileType):
            fileList.append(fileName + str(fileNumber) + fileType)
            fileNumber += 1
    return fileList


def plotMultipleFiles(filename):
    fileList = findFilesByName(filename)
    numberOfFiles = len(fileList)

    numberOfRows = int(numberOfFiles/6) + 1
    numberOfColumns = 6

    fig, axs = plt.subplots(nrows=numberOfRows, ncols=numberOfColumns)
    fig.suptitle("Position plots", fontsize=18, y=0.95)

    for file, ax in zip(fileList, axs.ravel()):
        plotXY(file, ax)
    
    plt.show()


if __name__ == '__main__':

    plotMultipleFiles('positionAcuracy')
    