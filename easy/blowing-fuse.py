import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def calc(status, all_nx):
    total = 0
    for i in range(len(status)):
        if status[i]:
            total += int(all_nx[i])
    return total

n, m, c = [int(i) for i in input().split()]
all_nx = []
status = []
all_mx = []
for i in input().split():
    all_nx.append(i)
    status.append(False)
for i in input().split():
    all_mx.append(int(i))

max = -1

for mx in all_mx:
    status[mx-1] = not status[mx-1]
    curr = calc(status, all_nx)
    if curr > max:
        max = curr


if max > c:
    print("Fuse was blown.")
else:
    print("Fuse was not blown.")
    print("Maximal consumed current was %d A." % (max,))