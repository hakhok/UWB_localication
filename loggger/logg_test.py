import csv

exampleData = [12, 432, 534, 234, 645, 3,4 ,56 ,756856, 345, 6,54, 3, 352, 32]

def csvWriter1():
    with open('files/test5.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
        spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])

def csvWriter():
    with open('files/test2.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(['Numbers'] + ['numbers'])
        i = 0
        for data in exampleData:
            i += 1
            spamwriter.writerow([i, data])

csvWriter()

