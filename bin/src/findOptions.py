import databaseFunctions
import os
import csv
def find():
    file = open("mySURFS.csv")
    reader = csv.reader(file, delimiter=',')
    index = -1
    indices = []
    numbers = databaseFunctions.getAllPhones()
    for num in numbers:
        lst =  databaseFunctions.getAllKeywords(num)
        for row in reader:
            checkString = row[1] + row[2] + row[4]
            for l in lst:
                if l in checkString:
                    databaseFunctions.newOpp(row[4], "http://announcements.surf.caltech.edu/", num, row[2], "me@caltech.edu", l)
                    indices.append(index)
        index += 1