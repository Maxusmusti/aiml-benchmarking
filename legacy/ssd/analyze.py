import sys

total = 0
count = 0
with open(sys.argv[1], 'r') as tocheck:
    for line in tocheck:
        data = line.split(' ')
        if len(data) >=2 and data[-2] == "sec:":
            total += float(data[-1])
            count += 1
print(total/count)
