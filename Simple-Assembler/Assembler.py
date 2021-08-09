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
#exact line number of the code 
line_no = 0

while line_count < 256:
    line = input().strip()
    line_no +=1
    if line == '':
        continue
        

    if line == 'hlt' :
        temp = input().strip()
        if(temp!='') :
            #Exception for adding commands after halt
            raise Exception("Cant add commands after Halt")
        break
    
    instruction_list.append(line.split())
    instruction_list[line_count].append(line_no)
    line_count += 1

#Exception for instructions exceeding 256 instructions
if(line_count>256) :
    raise Exception("No of Instructions Exceeded")



print(instruction_list)

flag = False
error_line = 0

#adding instructions and raising exceptions otherwise

for i in range(0,len(instruction_list)) : 
    for j in opcode.keys() : 
        if(instruction_list[i][0]==j) :
            if(j=="add") :
                x = add(instruction_list[i][1],instruction_list[i][2],instruction_list[i][3],r,bin_list)
                r = x[0]
                bin_list = x[1]

    #add remaining instructions
    else : 
        flag = True
        error_line = instruction_list[i][len(instruction_list[i])-1]
        break

#adding exception for invalid syntax
if flag : 
    raise Exception("Invalid Syntax in Line : " ,error_line)



                

            

