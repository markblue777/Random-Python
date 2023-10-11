import csv
import os

director = os.path.join("c:\\", "Users\\markd\\Downloads\\FB\\11\\")

for root, dirs, files in os.walk(director):
    for file in files:
        if not file.endswith("fixed.csv"):
            with open(director + file, 'r') as read_obj:
                cr = csv.reader(read_obj)
                newFile = open(director + file.replace(".csv", "_fixed.csv"),'w', newline='')
                cw = csv.writer(newFile)
                for row in cr:
                    cw.writerow(row[0:35])