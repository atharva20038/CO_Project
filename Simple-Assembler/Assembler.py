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
        raise Exception("Add Halt To End Program")
        break

    if line == 'hlt' :
        temp = input().strip()
        if(temp!='') :
            raise Exception("Cant add commands after Halt")
        break
    
    instruction_list.append(line.split())
    line_count += 1


if(line_count>256) :
    print("No of Instructions Exceeded")

print(instruction_list)