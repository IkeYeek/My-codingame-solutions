import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

program = input()

registers = ['0', '0', '0']

buffer_size, instruction_size = len(program), 4

instructions =  [ program[i:i+instruction_size] for i in range(0, buffer_size, instruction_size) ]
ignore = False
for instruction in instructions:
    if ignore:
        ignore = False
        continue
    
    opcode = int(instruction[0], 16)
    if opcode == 0:
        print("%s %s %s" % tuple(map(lambda x: int(x, 2), registers)))
        break
    elif opcode == 1: #load
        nn = format(int(instruction[2:], 16), 'b')
        r = int(instruction[1])
        print("LD %d, %s" % (r, nn), file=sys.stderr)
        registers[r] = nn
    elif opcode == 2: #add
        x = int(instruction[2])
        y = int(instruction[3])
        print("ADD %d, %d" % (x, y), file=sys.stderr)
        res = format(int(registers[x], 2) + int(registers[y], 2), 'b')
        registers[2] = '1' if len(res) > 8 else '0'
        registers[x] = res[-8:]
    elif opcode == 3: #sub
        x = int(instruction[2])
        y = int(instruction[3])
        print("SUB %d, %d" % (x, y), file=sys.stderr)
        res = int(registers[x], 2) - int(registers[y], 2)
        if res < 0:
            res = 256 + res
        res = format(res, 'b')
        registers[2] = '1' if int(registers[x], 2) < int(registers[y], 2) else '0'
        registers[x] = res
    elif opcode == 4: #or
        x = int(instruction[2])
        y = int(instruction[3])
        print("OR %d, %d" % (x, y), file=sys.stderr)
        res = format(int(registers[x], 2) | int(registers[y], 2), 'b')
        registers[x] = res
    elif opcode == 5:
        x = int(instruction[2])
        y = int(instruction[3])
        print("AND %d, %d" % (x, y), file=sys.stderr)
        res = format(int(registers[x], 2) & int(registers[y], 2), 'b')
        registers[x] = res
    elif opcode == 6:
        x = int(instruction[2])
        y = int(instruction[3])
        print("XOR %d, %d" % (x, y), file=sys.stderr)
        res = format(int(registers[x], 2) ^ int(registers[y], 2), 'b')
        registers[x] = res
    elif opcode == 7:
        nn = format(int(instruction[2:], 16), 'b')
        r = int(instruction[1])
        print("SE %d, %s" % (r, nn), file=sys.stderr)
        if(registers[r] == nn):
            ignore = True
    elif opcode == 8:
        nn = format(int(instruction[2:], 16), 'b')
        r = int(instruction[1])
        print("SNE %d, %d" % (r, nn), file=sys.stderr)
        if(registers[r] != nn):
            ignore = True
    elif opcode == 9:
        x = int(instruction[2])
        y = int(instruction[3])
        print("SE r%d, r%d" % (x, y), file=sys.stderr)
        if(x == y):
            ignore = True
    elif opcode == 10:
        x = int(instruction[2])
        y = int(instruction[3])
        print("SNE r%d, r%d" % (x, y), file=sys.stderr)
        if(x != y):
            ignore = True
    print("===registers values===", file=sys.stderr)
    print(registers, file=sys.stderr)
    print(list(map(lambda x: int(x, 2), registers)), file=sys.stderr, end="\n\n")

        
