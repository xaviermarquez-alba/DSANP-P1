"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
"""

#
numbers_set = set()
for t in texts:
    numbers_set.add(t[0])
    numbers_set.add(t[1])
for c in calls:
    numbers_set.add(c[0])
    numbers_set.add(c[1])

count = len(set(numbers_set))
print('There are ' + str(count) + ' different telephone numbers in the records.')
