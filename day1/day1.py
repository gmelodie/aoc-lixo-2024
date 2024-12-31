import sys

list1 = []
list2 = []

for line in sys.stdin:
    a, b = line.strip().split()

    list1.append(int(a))
    list2.append(int(b))

list1.sort()
list2.sort()

total = 0

for a, b in zip(list1, list2):
    total += abs(a - b)

print(total)
