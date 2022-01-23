"""
import serial

ser = serial.Serial('COM15', 115200, timeout=1)
line =  ser.readline()
print(type(line))
data = line.decode()

i = 0
while i < 100:
    print(str(line))
    i+=1
ser.close()
"""
import serial
import time
from mpl_toolkits import mplot3d
import  numpy as np
import matplotlib.pyplot as plt
ser = serial.Serial("COM15", 115200)
xList = []
yList = []
zList = []
timeList = []

fig = plt.figure()
ax = plt.axes(projection="3d")

start_time = time.time()
print("Starting...")
while time.time() - start_time < 20:
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
        
        timeList.append(time.time() - start_time)
        
    except:
        pass
    #print(f"x:{final_xValue} y:{final_yValue} z:{final_zValue}")

print("Plotting...")
ax.scatter3D(xList, yList, zList, c=timeList, cmap='hsv')
ax.set(xlim=(0, 4800), ylim=(0, 4800), zlim=(0, 4800))
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")

time_elapsed = timeList[-1] - timeList[0]
number_of_items = len(timeList)
freq = number_of_items/time_elapsed

print(f"Time elapsed: {time_elapsed}  Number of items: {number_of_items}  Freq: {freq}")

plt.show()