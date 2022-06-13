import csv
import time
from collections import Counter

# with open("example.csv") as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)

# with open("example.tsv") as f:
#     reader = csv.reader(f,delimiter="\t")
#     for row in reader:
#         print(row)

# students = [
#     ["Greg", "Dean", 70, 80, 90, "Food job, Greg"],
#     ["Wirt", "Wood", 80, 80.2, 80, "Nicely done"]
# ]

# with open("example.csv", "w", newline='') as f:
#     writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
#     writer.writerows(students)

crimes_2015 = []

with open(r"./Crimes.csv") as f:
    dr = csv.DictReader(f)
    for row in dr:

        s_t = None
        for fmt in ("%m-%d-%y %H:%M", "%m/%d/%Y %I:%M:%S %p"):
            try:
                s_t = time.strptime(row["Date"], fmt)
            except ValueError:
                pass

        if s_t is None:
            raise ValueError('Roman, you did not provide a valid date format')

        if s_t[0] == 2015:
            crimes_2015.append(row['Primary Type'])

c = Counter(crimes_2015)
print(c.most_common(3))     # print 3 most common crimes committed in 2015
