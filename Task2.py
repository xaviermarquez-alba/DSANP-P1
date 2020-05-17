"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds,
on the phone during
September 2016.".
"""


call_duration = {}

for call in calls:
    # check if key exists
    if str(call[0]) in call_duration:
        call_duration[str(call[0])] += int(call[3])
    else:
        call_duration[str(call[0])] = int(call[3])

    # check if key exists
    if str(call[1]) in call_duration:
        call_duration[str(call[1])] += int(call[3])
    else:
        call_duration[str(call[1])] = int(call[3])

max_time_key = max(call_duration, key=call_duration.get)

print(max_time_key + ' spent the longest time, '
      + str(call_duration[max_time_key])
      + ' seconds, on the phone during September 2016.')
