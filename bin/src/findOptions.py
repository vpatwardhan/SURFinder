import databaseFunctions
import os
import csv
file = open("mySURFS.csv")
reader = csv.reader(file, delimiter=',')
index = -1
indices = []
numbers = databaseFunctions.getAllPhones()
for num in numbers:
    lst =  databaseFunctions.getAllKeywords(num)
    for row in reader:
        checkString = row[1] + row[2] + row[3]
        for l in lst:
            if l in checkString:
                indices.append(index)
    index += 1