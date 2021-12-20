import re

fileHandle = open('regex_sum_1435615.txt')

text = fileHandle.read()

numbers = re.findall('[0-9]+', text)

total = 0

for number in numbers:
    total += int(number)

print(total)