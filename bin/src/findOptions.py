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
            for col in row:
                for l in lst:
                    if l.lower() in col.lower():
                        databaseFunctions.newOpp(row[4], "http://announcements.surf.caltech.edu/", num, row[2], "me@caltech.edu", l)
                        indices.append(index)
        index += 1