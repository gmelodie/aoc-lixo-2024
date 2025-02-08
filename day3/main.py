import re


line = input()

mul_pattern = r"mul\((\d+),(\d+)\)"
do_pattern = r"(don't\(\))"
dont_pattern = r"(do\(\))"

pattern = '|'.join([mul_pattern, do_pattern, dont_pattern])

matches = re.findall(pattern, line)

s = 0
mut_disabled = False
for match in matches:
    if (match[0] and match[1]) and not mut_disabled:
        s += int(match[0]) * int(match[1])
    elif match[2]: # dont
        mut_disabled = True
    elif match[3]: # do
        mut_disabled = False

print(s)
