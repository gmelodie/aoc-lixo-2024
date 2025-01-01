import sys


def check_pair(first, sec, inc):
    if inc:
        return 1 <= (sec-first) <= 3
    else:
        return 1 <= (first-sec) <= 3


def check_line(line, inc):
    removed = False

    if not check_pair(line[0], line[1], inc):
        if check_pair(line[0], line[2], inc):
            line.pop(1)
            removed = True

        elif check_pair(line[1], line[2], inc):
            line.pop(0)
            removed = True

        else:
            print("no inicio")
            return False

    for i in range(len(line)-1):
        a = line[i]
        b = line[i+1]

        if not check_pair(a,b, inc) and removed:
            return False

        if not check_pair(a,b, inc):
            new_list = line[i:]
            new_list.pop(1)

            return all(check_pair(x, y, inc) for x, y in zip(new_list[:-1], new_list[1:]))

    return True


count = 0
for line in sys.stdin:
    line = [int(x) for x in line.split()]
    if not check_line(line.copy(), True) and not check_line(line.copy(), False):
        print("Error")
        print(line)
    else:
        count += 1

print(count)
