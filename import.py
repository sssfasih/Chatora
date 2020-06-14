import sqlite3
import sys
# from sqlite3 import Error
import csv

if len(sys.argv) != 2:
    print("Usage import.py 'filename.csv' ")
    exit(1)
else:
    f = sys.argv[1]

try:
    con = sqlite3.connect("students.db")

except:
    print(sqlite3.Error)
cursor = con.cursor()

file = open(f)
infile = csv.DictReader(file)
for row in infile:
    # print(row)
    split = row['name'].split()
    if len(split) == 2:
        fir = split[0]
        mid = None
        las = split[1]
    else:
        fir = split[0]
        mid = split[1]
        las = split[2]

    con.execute("INSERT INTO students (first,middle,last,house,birth) VALUES (?, ? , ?, ? ,?);",
                (fir, mid, las, row['house'], int(row['birth'])))
    # cursor.execute("INSERT INTO students (first,middle, last, house, birth) VALUES ('{0}','{1}','{2}','{3}',{4});".format(fir,mid,las,row['house'],int(row['birth'])))

con.commit()