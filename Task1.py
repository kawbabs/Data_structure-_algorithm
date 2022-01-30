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
row_A = []
row_B = []

r1 = []
r2 = []
r3 = []
r4 = []

for row_A in texts:
    r1 = r1+ (row_A[0].split(','))
    r2 = r2 + (row_A[1].split(','))
    
for row_B in calls:
    r3 = r3 + (row_B[0].split(','))
    r4 = r4 + (row_B[1].split(','))
    
unique = []
unique = set(r1+r2+r3+r4)
no_telephnoe = len(unique)

print('There are', no_telephnoe, 'different telephone numbers in the records.')
