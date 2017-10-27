'''
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
'''

import datetime
import string

start_time = datetime.datetime.now()

# Actual code
names = list()
rating = dict()
for i, c in enumerate(string.ascii_uppercase):
    rating[c] = i + 1

with open('Names_22.txt') as file:
    for line in file:
        names.extend([n.split('"')[1] for n in line.split(',')])

names = sorted(names)


def value_name(name: str):
    m = map(lambda x: rating[x], name)
    return sum(m)


total = sum(map(lambda x, y: value_name(x) * y, names, range(1, len(names) + 1)))

# End actual code
end_time = datetime.datetime.now()
print(f'The total of all the name scores is {total} ({(end_time - start_time)})')
# The total of all the name scores is 871198282 (0:00:00.017000)
