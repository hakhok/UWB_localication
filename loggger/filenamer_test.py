import os

folder = 'files/'
i = 0
mybool = True
while mybool == True:
    i += 1
    mybool = os.path.isfile(folder + 'test' + str(i) + '.csv')
    print(str(i) + str(mybool))

print(f"Next filenumber is: {i}")