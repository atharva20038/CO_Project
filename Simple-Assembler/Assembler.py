#CO Assignment
#Atharva Mehta
#Nipun Gupta
#Shantanu Dixit

import fileinput
import sys

#taking the input

line_count = 0
instruction_list = []

while line_count < 256:
    line = input().strip()
    if line == '':
        continue
    
    instruction_list.append(line.split())
    line_count += 1



