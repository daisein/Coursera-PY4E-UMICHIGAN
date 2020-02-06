# The basic outline of this problem is to read the file, look for integers using the re.findall(), looking for a regular expression of '[0-9]+' and then converting the extracted strings to integers and summing up the integers.

numbers = list()
import re
fh = open('regex_sum_316177.txt')

for line in fh:
    line = line.rstrip()
    x = re.findall(r'\d+', line)
    if len(x)>0:
        for num in x:
            numbers.append(num)

sum = 0
for num in numbers:
    sum += int(num)

print(sum)
