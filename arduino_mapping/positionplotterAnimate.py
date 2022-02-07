import serial
import time
from mpl_toolkits import mplot3d
import  numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random
from itertools import count

ser = serial.Serial("COM15", 115200)
xList = []
yList = []
zList = []
timeList = []

fig = plt.figure()
ax = plt.axes(projection="3d")

start_time = time.time()
print("Starting...")

ax.set(xlim=(0, 4800), ylim=(0, 4800), zlim=(0, 4800))
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")


def animate(i):
    cc=str(ser.readline())
    #print(cc[2:][:-5])
    #print(cc)
    xPos = cc.find('x(mm):')
    yPos = cc.find('y(mm):')
    zPos = cc.find('z(mm):')
    xValue = str(cc[(xPos + 7):(xPos + 11)])
    yValue = str(cc[(yPos + 7):(yPos + 11)])
    zValue = str(cc[(zPos + 7):(zPos + 11)])
    final_xValue = xValue.replace(",", "")
    final_yValue = yValue.replace(",", "")
    final_zValue = zValue.replace("\\", "")
    try:
        xInt = int(final_xValue)
        yInt = int(final_yValue)
        zInt = int(final_zValue)

        xList.append(xInt)
        yList.append(yInt)
        zList.append(zInt)

        if len(xList)>20:
            xList.pop(0)
            yList.pop(0)
            zList.pop(0)
        
        timeList.append(time.time() - start_time)
        ax.scatter3D(xList, yList, zList, c=timeList, cmap='hsv')
        plt.pause(0.05)
        
    except:
        pass





ani = FuncAnimation(plt.gcf(), animate, 10000)

plt.show()