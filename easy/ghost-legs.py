w, h = [int(i) for i in input().split()]
lines = []
for i in range(h):
    lines.append(input())


def make_connections(line, points):
    connections = []
    curr_point = -1
    skip = False
    for c in line:
        if c is "|":
            curr_point += 1
            skip = False
        elif c is "-" and not skip:
            connections.append([points[curr_point], points[curr_point+1]])
            skip = True
    return connections           
            

def extract_points(line):
    points = []
    for c in line:
        if c is not " ":
            points.append(c)
    return points
        


starting_points = extract_points(lines[0])
lanes = {}
for i in range(len(starting_points)):
    lanes[starting_points[i]] = extract_points(lines[len(lines)-1])[i]

for start in starting_points:
    curr_point = start
    for line in lines[1:-1]:
        connections = make_connections(line, starting_points)
        for connection in connections:
            if curr_point in connection:
                curr_point = connection[0] if curr_point is connection[1] else connection[1]
    print("%c%c" % (start, lanes[curr_point]))
