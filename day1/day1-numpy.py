from collections import Counter
import numpy as np

data = np.loadtxt("big.txt", delimiter=",", dtype=int)
col1, col2 = data[:, 0], data[:, 1]

print(np.abs(np.sort(col1) - np.sort(col2)).sum())

# part 2
counts = Counter(col2)
print(sum(x*counts[x] for x in col1))
