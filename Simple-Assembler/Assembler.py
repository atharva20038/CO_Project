#CO Assignment
#Atharva Mehta
#Nipun Gupta
#Shantanu Dixit


#Type-A errors 
def typeAerrors(ith_instruction) : 
    if len(ith_instruction) != 5: #checks if instruction is correct
        error_line = ith_instruction[len(ith_instruction)-1]
        return (True,"Does Not Match the Required Number Of Tokens")
                
    #check if correct register names are used
    if ith_instruction[1] not in reg_code or ith_instruction[2] not in reg_code or ith_instruction[3] not in reg_code or "FLAGS" in ith_instruction[1:]:
        error_line = ith_instruction[4]
        return(True,"Invalid Register Name Used")

    return (False,"")

#Type-B errors
def typeBerrors(ith_instruction):
    if len(ith_instruction) != 4: #checks if instruction is correct
        error_line = ith_instruction[len(ith_instruction)-1]
        return (True,"Doesnot match the required number of tokens")
                
            #check if correct register names are used
    if ith_instruction[1] not in reg_code or "FLAGS" in ith_instruction[1:]:
        error_line = ith_instruction[3]
        return (True,"Invalid register name used") 

    #check if 3rd token is a valid immediate value
    if ith_instruction[2][0] != "$" or ith_instruction[1:].isnumeric() or int(ith_instruction[2][1:]) > 255 or int(ith_instruction[2][1:]) < 0:
        error_line = ith_instruction[3]
        return (True,"Invalid Immediate Value Syntax")

    return (False,"")

#Type-C errors
def typeCerrors(ith_instruction):
    if len(ith_instruction) != 4: #checks if instruction is correct
        error_line = ith_instruction[len(ith_instruction)-1]
        return (True,"Doesnot match the required number of tokens")
                
            #check if correct register names are used
    if ith_instruction[1] not in reg_code or ith_instruction[2] not in reg_code or "FLAGS" in ith_instruction[1:]:
        error_line = ith_instruction[3]
        return (True,"Invalid register name used")

    return (False,"")

#Type-D errors     
def typeDerrors(ith_instruction):
    if len(ith_instruction) != 4:
        error_line = ith_instruction[len(ith_instruction)-1]
        return (True,"Doesnot match the required number of tokens")

    if ith_instruction[1] not in reg_code or ith_instruction[1] == "FLAGS":
        error_line = ith_instruction[len(ith_instruction)-1]
        return (True,"Invalid register name used")

    if ith_instruction[2] not in variables:
        error_line = ith_instruction[len(ith_instruction)-1]
        return (True,"Variable Not Declared")

    return (False,"")

#Type-E errors
def typeEerrors(ith_instruction):
    if len(ith_instruction) != 3:
        error_line = ith_instruction[len(ith_instruction)-1]
        return (True,"Doesnot match the required number of tokens")
    
    if ith_instruction[1] not in labels:
        error_line = ith_instruction[-1]
        return (True,"Label Not Declared")

    return (False,"")

#add function
//Type A starts
def Add(a,b,c) : 
    #complete add function keeping in mind all possibilities and add the binary code to the list and add update the values in the resgisters
    
    bin_list.append(opcode["add"][0]+"00"+reg_code[a]+reg_code[b]+reg_code[c]) #binary value of instruction 
    return bin_list

def Sub(a,b,c):
    bin_list.append(opcode["sub"][0] + "00" + reg_code[a] + reg_code[b] + reg_code[c])
    return bin_list

def Mul(a,b,c):
    bin_list.append(opcode["mul"][0] +"00"reg_code[a] + reg_code[b] + reg_code[c])
    return bin_list

def Xor(a,b,c):
    bin_list.append(opcode["xor"][0] + "00" + reg_code[a] + reg_code[b] + reg_code[c])
    return bin_list

def Or(a,b,c):
    bin_list.append(opcode["or"][0] + "00" + reg_code[a] + reg_code[b] + reg_code[c])
    return bin_list

def And(a,b,c):
    bin_list.append(opcode["and"][0] + "00" + reg_code[a] + reg_code[b] + reg_code[c])
    return bin_list

##Type A ends
##Type B starts
def MovImm(a,b):
    Bin = bin(b)                              ##CHECK FOR MOV , SINCE 2 MOV ARE PRESENT IN INSTRUCTION LIST
    if(len(Bin[2:])<8):
        Zeroes = 8-len(Bin[2:])
        Imm = str(0*Zeroes) + Bin[2:]
    else:
        Imm = Bin[2:]
    bin_list.append(opcode["mov"][0] + reg_code[a] + Imm)
    return bin_list

def RightShift(a,b):
    Bin = bin(b)
    if(len(Bin[2:])<8):
        Zeroes = 8-len(Bin[2:])
        Imm = str(0*Zeroes) + Bin[2:]
    else:
        Imm = Bin[2:]
    bin_list.append(opcode["rs"][0] + reg_code[a] + Imm)
    return bin_list

def LeftShift(a,b):
    Bin = bin(b)
    if(len(Bin[2:])<8):
        Zeroes = 8-len(Bin[2:])
        Imm = str(0*Zeroes) + Bin[2:]
    else:
        Imm = Bin[2:]
    bin_list.append(opcode["ls"][0] + reg_code[a] + Imm)
    return bin_list

 ##TYPE B ends

 ##TYPE C starts
def MovReg(a,b):
    bin_list.append(opcode["mov"][0] + "00000" + reg_code[a] + reg_code[b])
    return bin_list

def Div(a,b):
    bin_list.append(opcode["div"][0] + "00000" + reg_code[a] + reg_code[b])
    return bin_list

def Invert(a,b):
    bin_list.append(opcode["not"][0] + "00000" + reg_code[a] + reg_code[b])
    return bin_list

def Compare(a,b):
    bin_list.append(opcode["cmp"][0] + "00000" + reg_code[a] + reg_code[b])
    return bin_list
#TYPE C ends

#TYPE D starts
def Load(a,b):
    Bin = bin(variables[b])
    if(len(Bin[2:])<8):
        Zeroes = 8-len(Bin[2:])
        Imm = str(0*Zeroes) + Bin[2:]
    else:
        Imm = Bin[2:]
    bin_list.append(opcode["ld"][0] + reg_code[a] + Imm)
    return bin_list

def Store(a,b):
    Bin = bin(variables[b])
    if(len(Bin[2:])<8):
        Zeroes = 8-len(Bin[2:])
        Imm = str(0*Zeroes) + Bin[2:]
    else:
        Imm = Bin[2:]
    bin_list.append(opcode["st"][0] + reg_code[a] + Imm)
    return bin_list
##TYPE D ends

def UncondJump(address):     ##line_count = -1 // 00000000
    Bin = bin(address)
    if(len(Bin[2:])<8):
        Zeroes = 8-len(Bin[2:])
        Imm = str(0*Zeroes) + Bin[2:]
    else:
        Imm = Bin[2:]
    bin_list.append(opcode["jmp"][0] + "000"+ Imm)
    return bin_list

def JumpIfLess(address):
    Bin = bin(address)
    if(len(Bin[2:])<8):
        Zeroes = 8-len(Bin[2:])
        Imm = str(0*Zeroes) + Bin[2:]
    else:
        Imm = Bin[2:]
    bin_list.append(opcode["jlt"][0] "000"+ Imm)
    return bin_list

def JumpIfGreater(address):
    Bin = bin(address)
    if(len(Bin[2:])<8):
        Zeroes = 8-len(Bin[2:])
        Imm = str(0*Zeroes) + Bin[2:]
    else:
        Imm = Bin[2:]
    bin_list.append(opcode["jgt"][0] "000"+ Imm)
    return bin_list

def JumpIfEqual(address):
    Bin = bin(address)
    if(len(Bin[2:])<8):
        Zeroes = 8-len(Bin[2:])
        Imm = str(0*Zeroes) + Bin[2:]
    else:
        Imm = Bin[2:]
    bin_list.append(opcode["je"][0] "000"+ Imm)
    return bin_list
##TYPE E ends

##TYPE F starts
def Halt():
    bin_list.append(opcode["hlt"][0])
    return bin_list
##TYPE F ends


#lists and dictionaries to store codes and data
opcode = {"add":("00000","A"),"sub":("00001","A"),"mov":("00010","B"),"mov":("00011","C")
        ,"ld":("00100","D"),"st":("00101","D"),"mul":("00110","A"),"div":("00111","C"),
        "rs":("01000","B"),"ls":("01001","B"),"xor":("01010","A"),"or":("01011","A"),"and":("01100","A"),
        "not":("01101","C"),"cmp":("01110","C"),"jmp":("01111","E"),"jlt":("10000","E"),"jgt":  ("10001", 'E'),"je":("10010", 'E'),
        "hlt":("10011","F")}

reg_code = {'R0':'000', 'R1':'001', 'R2':'010', 'R3':'011', 'R4':'100', 'R5':'101', 'R6':'110', 'FLAGS':'111'}  #codes of registers
reg_data = {'R0':0, 'R1':0, 'R2':0, 'R3':0, 'R4':0, 'R5':0, 'R6':0, 'FLAGS':[0,0,0,0]}  #decimal values of R0-R6 registers and V,L,G,E bits of flags register

variables = {}  #dictionary to store memory and values of variables
labels = {}  #dictionary to store memory of labels

line_count = 0
instruction_list = []
bin_list = []
#exact line number of the code 

while True:
    try : 
        line = input().strip()
        if line == '':  
            continue
        
        instruction_list.append(line.split())
        instruction_list[line_count].append(line_count)
        line_count += 1
    except : 
        break


flag = False
error_line = 0
error_msg = ''

last_var = False
var_count = 0



#adding instructions and raising exceptions otherwise

for i in range(0,len(instruction_list)) : 
    ith_instruction = instruction_list[i]

    if i == len(instruction_list)-1 and  'hlt' not in ith_instruction:
        error_msg = 'hlt not present'
        error_line = i
        flag = True
        break

    elif 'hlt' in ith_instruction and i != len(instruction_list)-1:
        error_line = i
        error_msg = 'hlt not last statement'
        flag = True
        break

    elif 'hlt' in ith_instruction and i == len(instruction_list)-1:
        if len(ith_instruction != 2):
            error_line = 'Wrong hlt syntax'
            error_line = i
            flag = True
            break

    #check for errors in general instructon
    elif ith_instruction[0] in opcode:
        #put error checks on all the operation functions here
        if ith_instruction[0] == "add" :
            temp = typeAerrors(ith_instruction)
            flag = temp[0]
            if(flag) : break
            bin_list = add(ith_instruction[1],ith_instruction[2],ith_instruction[3])
            

    #check for errors in variables
    elif ith_instruction[0] == "var":
        if last_var:
            error_msg = 'Variable not declared at top'
            flag = True
            error_line = i
            break
        
        if not last_var and instruction_list[i+1][0] != 'var':
            last_var = True

        if len(ith_instruction) != 3:
            error_msg = 'Wrong syntax while declaring variable'
            error_line = i
            flag = True
            break

        temp = []      ##variable store
        temp.extend(ith_instruction[1])
        for e in temp:
            if (ord(e) not in range(ord('a'), ord('z')+1)) or (ord(e) not in range(ord('A'), ord('Z')+1)) or ord(e) != ord('_'):
                error_msg = 'Wrong variable name'
                error_line = i
                flag = True
                break
        if flag:
            break

        variables[ith_instruction[1]] = (0, i)
        var_count += 1

    #checks for error in label declaration
    elif ith_instruction[0][-1] == ":":
        temp = []
        temp.extend(ith_instruction[0][0:-1])
        for e in temp:
            if (ord(e) not in range(ord('a'), ord('z')+1)) or (ord(e) not in range(ord('A'), ord('Z')+1)) or ord(e) != ord('_'):
                error_msg = 'Wrong label name'
                error_line = i
                flag = True
                break
        if flag:
            break

        if ith_instruction[0][0:-1] in variables:
            error_line = 'Variable name used as label name'
            error_line = i
            flag = True
            break

        #label is followed a general instruction. So add all the error checks for instructions above here also

        if 'hlt' == ith_instruction[1]:
            if len(ith_instruction != 3):
                error_msg = 'Wrong syntax'
                error_line = i
                flag = True
                break
            
            elif i != len(instruction_list)-1:
                error_msg = 'hlt not last instruction'
                error_line = i
                flag = True
                break

        elif ith_instruction[1] in opcode:
            print()
            
        else:
            error_msg = 'Wrong command after label'
            error_line = i
            flag = True
            break


#error for checking stack limit
if(line_count+var_count>256) : 
    error = "Cant have more than 256 instructions"
    flag = True

 

#adding exception for invalid syntax
if flag : 
    #raise Exception("Invalid Syntax in Line : " ,error_line)
    print('error')
else:
    for x in bin_list:
        print(x)



                

            

