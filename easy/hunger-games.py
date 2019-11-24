import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

nb_tributes = int(input())
tributes = []
for i in range(nb_tributes):
    tributes.append(input())
    
turns = int(input())
infos = []
for i in range(turns):
    infos.append(input())

state = {}

for tribute in tributes:
    state[tribute] = {'Killed': 'None', 'Killer': 'Winner'}

def parse_turn(turn, state):
    splitted = turn.replace(",", "").split()
    
    tribute_from = splitted[0]
    tributes_for = splitted[2:]
    for tribute_for in sorted(tributes_for):
        state[tribute_for]['Killer'] = tribute_from
        if state[tribute_from]['Killed'] is 'None':
            state[tribute_from]['Killed'] = tribute_for
        else:
            state[tribute_from]['Killed'] += ', ' + tribute_for

for turn in sorted(infos):
    parse_turn(turn, state)
first = True
for s in sorted(state):
    if not first:
        print("\n")
    else:
        first = False
    print("Name: %s\nKilled: %s\nKiller: %s" % (s, state[s]['Killed'], state[s]['Killer']), end='')
    
            
    
