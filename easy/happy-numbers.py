n = int(input())
x = []
for i in range(n):
    x.append(input())

#wanted to do this recursively but codingame's python interpreter acted weird
def is_happy(n):
    seen = []
    n = str(n)
    while(True):
        seen.append(n)
        sum = 0
        for c in n:
            sum += (int(c) ** 2)   
        
        if sum == 1:
            return True
        elif str(sum) in seen:
            return False
        else:
            n = str(sum)

for line in x:
    print("%s :)" % line if is_happy(line) else "%s :(" % line)