#CO Assignment
#Atharva Mehta
#Nipun Gupta
#Shantanu Dixit

import fileinput
import sys
#add function
def add(a,b,c,r,bin_list) : 
    #complete add function keeping in mind all possibilities and add the binary code to the list and add update the values in the resgisters
    return (r,bin_list)

#taking the input
opcode = {"add":("00000","A"),"sub":("00001","A"),"mov":("00010","B"),"mov":("00011","C")
        ,"ld":("00100","D"),"st":("00101","D"),"mul":("00110","A"),"div":("00111","C"),
        "rs":("01000","B"),"ls":("01001","B"),"xor":("01010","A"),"or":("01011","A"),"and":("01100","A"),
        "not":("01101","C"),"cmp":("01110","C"),"jmp":("01111","E"),"jlt":("10000","E"),"jgt":  ("10001", 'E'),"je":("10010", 'E'),
        "hlt":("10011","F")}

r = [0,0,0,0,0,0,0,True]
line_count = 0
instruction_list = []
bin_list = []

while line_count < 256:
    line = input().strip()
    if line == '':
        continue
        

    if line == 'hlt' :
        temp = input().strip()
        if(temp!='') :
            #Exception for adding commands after halt
            raise Exception("Cant add commands after Halt")
        break
    
    instruction_list.append(line.split())
    line_count += 1

#Exception for instructions exceeding 256 instructions
if(line_count>256) :
    raise Exception("No of Instructions Exceeded")



print(instruction_list)

flag = True

for i in range(0,instruction_list.length) : 
    for j in dict.keys() : 
        if(instruction_list[0][0]==j) :
            flag = False 
            if(j=="add") :
                x = add(instruction_list[0][1],instruction_list[0][2],instruction_list[0][3],r,bin_list)
                r = x[0]
                bin_list = x[1]







                

            

