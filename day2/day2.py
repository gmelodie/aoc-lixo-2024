import sys
import numpy as np

count = 0
for line in sys.stdin:
    line = np.array([int(x) for x in line.split()])
    offset_line = line[1:]
    diff = line[:-1]-offset_line

    if ( (1 <= diff) & (diff <= 3) ).all():
        count += 1
    elif ( (-1 >= diff) & (diff >= -3)).all():
        count += 1

print(count)
