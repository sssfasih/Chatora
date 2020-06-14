import sqlite3
import sys

if len(sys.argv) != 2:
    print("Usage roaster.py 'House' ")
    exit(1)
else:
    roast = sys.argv[1]

try:
    con = sqlite3.connect("students.db")

except:
    print(sqlite3.Error)

cursor = con.cursor()

extraction = cursor.execute("SELECT first,middle, last, birth FROM students WHERE house= (:val) ORDER BY last,first;",
                            {"val": roast})

for rows in extraction:
    for EveryField in rows:
        if EveryField == None:
            pass
        elif EveryField == rows[2]:
            print(EveryField, end="")

        elif type(EveryField) == int:
            print(", born " + str(EveryField), end="")
        else:
            print(EveryField, end=" ")

    print()
