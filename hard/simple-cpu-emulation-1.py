import sys
import math
import operator

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

program = input()

registers = ['0', '0', '0']

buffer_size, instruction_size = len(program), 4

instructions =  [ program[i:i+instruction_size] for i in range(0, buffer_size, instruction_size) ]
ignore = False
print("Raw instructions :\n\t%s\ninstructions :" % (program,), file=sys.stderr)
print(instructions, file=sys.stderr)

def two_registers_operations(x, y, operator): #does registers[x] operator registers[y] and stores 8 first bits of the result in registers[x] 
    res = operator(int(registers[x], 2), int(registers[y], 2))
    flag = False
    if res < 0:
        res = 256 + res
        flag = True
        
    res = format(res, 'b')
    if len(res) > 8:
        print("INTEGER OVERFLOW ON %s LIMIT IS %s" % (res, format(255, 'b')), file=sys.stderr)
    registers[2] = '1' if len(res) > 8 or flag else '0'
    registers[x] = res[-8:]
    
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
        print("LD r%d, %s" % (r, nn), file=sys.stderr)
        registers[r] = nn
    elif opcode == 2: #add
        x = int(instruction[2])
        y = int(instruction[3])
        print("ADD r%d, r%d" % (x, y), file=sys.stderr)
        two_registers_operations(x, y, operator.add)
    elif opcode == 3: #sub
        x = int(instruction[2])
        y = int(instruction[3])
        print("SUB r%d, r%d" % (x, y), file=sys.stderr)
        two_registers_operations(x, y, operator.sub)
    elif opcode == 4: #or
        x = int(instruction[2])
        y = int(instruction[3])
        print("OR r%d, r%d" % (x, y), file=sys.stderr)
        res = format(int(registers[x], 2) | int(registers[y], 2), 'b')
        registers[x] = res
    elif opcode == 5:
        x = int(instruction[2])
        y = int(instruction[3])
        print("AND r%d, r%d" % (x, y), file=sys.stderr)
        res = format(int(registers[x], 2) & int(registers[y], 2), 'b')
        registers[x] = res
    elif opcode == 6:
        x = int(instruction[2])
        y = int(instruction[3])
        print("XOR r%d, r%d" % (x, y), file=sys.stderr)
        res = format(int(registers[x], 2) ^ int(registers[y], 2), 'b')
        registers[x] = res
    elif opcode == 7:
        nn = format(int(instruction[2:], 16), 'b')
        r = int(instruction[1])
        print("SE r%d, %s" % (r, nn), file=sys.stderr)
        if(registers[r] == nn):
            ignore = True
    elif opcode == 8:
        nn = format(int(instruction[2:], 16), 'b')
        r = int(instruction[1])
        print("SNE r%d, %d" % (r, nn), file=sys.stderr)
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

        
