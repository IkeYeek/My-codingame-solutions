import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
isbns = []
for i in range(n):
    isbns.append(input())

invalids = []

for isbn in isbns:
    valid = True
    check = -1
    if len(isbn) == 10:
        summed = 0
        for i in range(9):
            if not isbn[i].isnumeric():
                valid = False
            else:
                k = int(isbn[i])
                summed += (10 - i) * k
                remainder = summed % 11
                check = (11 - remainder) 
                if check == 10:
                    check = 'X'
                elif check == 11:
                    check = 0
    elif len(isbn) == 13:
        summed = 0
        for i in range(12):
            if not isbn[i].isnumeric():
                valid = False
            else:
                k = int(isbn[i])
                summed += k if i%2 == 0 else 3*k
                remainder = summed % 10
                check = (10 - remainder) 
                if check == 10:
                    check = 0
            
    if str(check) != str(isbn[-1]) or not valid:
        invalids.append(isbn)

print("%d invalid:" % (len(invalids), ))
for invalid in invalids:
    print(invalid)
