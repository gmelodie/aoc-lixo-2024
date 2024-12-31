import sys
from collections import Counter

list1, list2 = [], []

for line in sys.stdin:
    a, b = line.strip().split()

    list1.append(int(a))
    list2.append(int(b))

count = Counter(list2)

total = 0

for a in list1:
    total += a*count[a]

print(total)
