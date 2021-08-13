#CO Assignment
#Atharva Mehta
#Nipun Gupta
#Shantanu Dixit


#Type-A errors 
def typeAerrors(ith_instruction) : 
    if len(ith_instruction) != 5: #checks if instruction is correct
        
        return (True,"Does Not Match the Required Number Of Tokens at line : " + str(ith_instruction[len(ith_instruction)-1]))
                
    #check if correct register names are used
    if ith_instruction[1] not in reg_code or ith_instruction[2] not in reg_code or ith_instruction[3] not in reg_code or "FLAGS" in ith_instruction[1:]:
        
        return(True,"Invalid Register Name Used at line : " + str(ith_instruction[len(ith_instruction)-1]))

    return (False,"")

#Type-B errors
def typeBerrors(ith_instruction):
    if len(ith_instruction) != 4: #checks if instruction is correct
        
        return (True,"Doesnot match the required number of tokens at line : " + str(ith_instruction[len(ith_instruction)-1]))
                
            #check if correct register names are used
    if ith_instruction[1] not in reg_code or "FLAGS" in ith_instruction[1:]:
        
        return (True,"Invalid register name used at line : " + str(ith_instruction[len(ith_instruction)-1])) 

    #check if 3rd token is a valid immediate value
    if ith_instruction[2][0] != "$" or not ith_instruction[2][1:].isnumeric() or int(ith_instruction[2][1:]) > 255 or int(ith_instruction[2][1:]) < 0:
        
        return (True,"Invalid Immediate Value Syntax at line : " + str(ith_instruction[len(ith_instruction)-1]))

    return (False,"")

#Type-C errors
def typeCerrors(ith_instruction):
    if len(ith_instruction) != 4: #checks if instruction is correct
        
        return (True,"Doesnot match the required number of tokens at line : " + str(ith_instruction[len(ith_instruction)-1]))
                
            #check if correct register names are used
    if ith_instruction[1] not in reg_code or ith_instruction[2] not in reg_code or "FLAGS" in ith_instruction[1:]:
        
        return (True,"Invalid register name used at line : " + str(ith_instruction[len(ith_instruction)-1]))

    return (False,"")

#Type-D errors     
def typeDerrors(ith_instruction):
    if len(ith_instruction) != 4:
        
        return (True,"Doesnot match the required number of tokens at line : " + str(ith_instruction[len(ith_instruction)-1]))

    if ith_instruction[1] not in reg_code or ith_instruction[1] == "FLAGS":
        
        return (True,"Invalid register name used at line : " + str(ith_instruction[len(ith_instruction)-1]))

    if ith_instruction[2] not in variables:
        
        return (True,"Variable Not Declared at line : " + str(ith_instruction[len(ith_instruction)-1]))

    return (False,"")

#Type-E errors
def typeEerrors(ith_instruction):
    if len(ith_instruction) != 3:
        
        return (True,"Doesnot match the required number of tokens at line : " + str(ith_instruction[len(ith_instruction)-1]))
    
    if ith_instruction[1] not in labels:
        
        return (True,"Label Not Declared at line : " + str(ith_instruction[len(ith_instruction)-1]))

    return (False,"")

#add function
##Type A starts
def Add(a,b,c) : 
    #complete add function keeping in mind all possibilities and add the binary code to the list and add update the values in the resgisters
    
    bin_list.append(opcode["add"][0]+"00"+reg_code[a]+reg_code[b]+reg_code[c]) #binary value of instruction 
    return bin_list

def Sub(a,b,c):
    ## Appending the opcode of subtract instruction along with the syntax supposed for the subtract instruction
    bin_list.append(opcode["sub"][0] + "00" + reg_code[a] + reg_code[b] + reg_code[c])
    return bin_list

def Mul(a,b,c):
    ## Appending the opcode of multiply instruction along with the syntax supposed for the multiplication instruction
    bin_list.append(opcode["mul"][0] +"00"+reg_code[a] + reg_code[b] + reg_code[c])
    return bin_list

def Xor(a,b,c):
    ## Appending the opcode of xor instruction along with the syntax supposed for the xor instruction
    bin_list.append(opcode["xor"][0] + "00" + reg_code[a] + reg_code[b] + reg_code[c])
    return bin_list

def Or(a,b,c):
    ## Appending the opcode of or instruction along with the syntax supposed for the or instruction
    bin_list.append(opcode["or"][0] + "00" + reg_code[a] + reg_code[b] + reg_code[c])
    return bin_list

def And(a,b,c):
    ## Appending the opcode of and instruction along with the syntax supposed for the and instruction
    bin_list.append(opcode["and"][0] + "00" + reg_code[a] + reg_code[b] + reg_code[c])
    return bin_list

##Type A ends
##Type B starts
def MovImm(a,b):
    Bin = bin(int(b[1:]))                              ##CHECK FOR MOV,SINCE 2 MOV ARE PRESENT IN INSTRUCTION LIST
    if(len(Bin[2:])<8):                           ##CHECKING IF LENGTH OF binary less than 8
        Zeroes = 8-len(Bin[2:])                   ##Adding appropriate number of zeroes if required
        Imm = str("0"*Zeroes) + Bin[2:]
    else:
        Imm = Bin[2:]                             ##Otherwise ignoring
    ## Appending the opcode of and instruction along with the syntax supposed for the and instruction
    bin_list.append(opcode["mov"][0][0] + reg_code[a] + Imm)
    return bin_list

def RightShift(a,b):
    Bin = bin(int(b[1:]))
    if(len(Bin[2:])<8):
        Zeroes = 8-len(Bin[2:])
        Imm = str("0"*Zeroes) + Bin[2:]
    else:
        Imm = Bin[2:]

    ## Appending the opcode of Right shift instruction along with the syntax supposed for the right shift instruction
    bin_list.append(opcode["rs"][0] + reg_code[a] + Imm)
    return bin_list

def LeftShift(a,b):
    Bin = bin(int(b[1:]))
    if(len(Bin[2:])<8):
        Zeroes = 8-len(Bin[2:])
        Imm = str("0"*Zeroes) + Bin[2:]
    else:
        Imm = Bin[2:]

    ## Appending the opcode of left shift instruction along with the syntax supposed for the left shift instruction
    bin_list.append(opcode["ls"][0] + reg_code[a] + Imm)
    return bin_list

 ##TYPE B ends

 ##TYPE C starts
def MovReg(a,b):
    bin_list.append(opcode["mov"][1][0] + "00000" + reg_code[a] + reg_code[b])
    ## Appending the opcode of move value to register instruction along with the syntax supposed for it
    return bin_list

def Div(a,b):
    bin_list.append(opcode["div"][0] + "00000" + reg_code[a] + reg_code[b])
    ## Appending the opcode of division instruction along with the syntax supposed for the division instruction
    return bin_list

def Invert(a,b):
    bin_list.append(opcode["not"][0] + "00000" + reg_code[a] + reg_code[b])
    ## Appending the opcode of invert instruction along with the syntax supposed for the division instruction
    return bin_list

def Compare(a,b):
    bin_list.append(opcode["cmp"][0] + "00000" + reg_code[a] + reg_code[b])
    ## Appending the opcode of compare instruction along with the syntax supposed for the compare instruction
    return bin_list
#TYPE C ends

#TYPE D starts
def Load(a,b):
    Bin = bin(b)
    if(len(Bin[2:])<8):
        Zeroes = 8-len(Bin[2:])
        Imm = str("0"*Zeroes) + Bin[2:]
    else:
        Imm = Bin[2:]
    bin_list.append(opcode["ld"][0] + reg_code[a] + Imm)
    return bin_list

def Store(a,b):
    Bin = bin(b)
    if(len(Bin[2:])<8):
        Zeroes = 8-len(Bin[2:])
        Imm = str("0"*Zeroes) + Bin[2:]
    else:
        Imm = Bin[2:]
    bin_list.append(opcode["st"][0] + reg_code[a] + Imm)
    return bin_list
##TYPE D ends
##TYPE E starts
def UncondJump(address):     ## Line count = -1 -> Address 00000000
    Bin = bin(address)       ## Convert the given linecount into binary and check for length and make appropriate additions
    if(len(Bin[2:])<8):      ## to convert the binary into 8 bit format
        Zeroes = 8-len(Bin[2:])
        Imm = str("0"*Zeroes) + Bin[2:]
    else:
        Imm = Bin[2:]
    bin_list.append(opcode["jmp"][0] + "000"+ Imm)
    return bin_list

def JumpIfLess(address):
    Bin = bin(address)
    if(len(Bin[2:])<8):
        Zeroes = 8-len(Bin[2:])
        Imm = str("0"*Zeroes) + Bin[2:]
    else:
        Imm = Bin[2:]
    bin_list.append(opcode["jlt"][0]+"000"+ Imm)
    return bin_list

def JumpIfGreater(address):
    Bin = bin(address)
    if(len(Bin[2:])<8):
        Zeroes = 8-len(Bin[2:])
        Imm = str("0"*Zeroes) + Bin[2:]
    else:
        Imm = Bin[2:]
    bin_list.append(opcode["jgt"][0]+"000"+ Imm)
    return bin_list

def JumpIfEqual(address):
    Bin = bin(address)
    if(len(Bin[2:])<8):
        Zeroes = 8-len(Bin[2:])
        Imm = str("0"*Zeroes) + Bin[2:]
    else:
        Imm = Bin[2:]
    bin_list.append(opcode["je"][0]+"000"+ Imm)
    return bin_list
##TYPE E ends

##TYPE F starts
def Halt():
    bin_list.append(opcode["hlt"][0] + 11*"0")
    return bin_list
##TYPE F ends


#lists and dictionaries to store codes and data
opcode = {"add":("00000","A"),"sub":("00001","A"),"mov":(("00010","B"),("00011","C"))
        ,"ld":("00100","D"),"st":("00101","D"),"mul":("00110","A"),"div":("00111","C"),
        "rs":("01000","B"),"ls":("01001","B"),"xor":("01010","A"),"or":("01011","A"),"and":("01100","A"),
        "not":("01101","C"),"cmp":("01110","C"),"jmp":("01111","E"),"jlt":("10000","E"),"jgt":  ("10001", 'E'),"je":("10010", 'E'),
        "hlt":("10011","F")}

reg_code = {'R0':'000', 'R1':'001', 'R2':'010', 'R3':'011', 'R4':'100', 'R5':'101', 'R6':'110', 'FLAGS':'111'}  #codes of registers
reg_data = {'R0':0, 'R1':0, 'R2':0, 'R3':0, 'R4':0, 'R5':0, 'R6':0, 'FLAGS':[0,0,0,0]}  #decimal values of R0-R6 registers and V,L,G,E bits of flags register

variables = {}  # Dictionary to store memory and values of variables
labels = {}  # Dictionary to store memory of labels

##line_count contains the total number of lines excluding the blank lines including the variable declarations
line_count = 0
##inlcudes all the lines including blank spaces and variables
blank_included_count = 0

instruction_list = []
bin_list = []
#exact line number of the code 

while True:
    try : 
        line = input().strip()
        if line == '':  
            blank_included_count += 1
            continue
        
        instruction_list.append(line.split())
        #included blanks in the count
        
        blank_included_count += 1
        instruction_list[line_count].append(blank_included_count)
        line_count += 1
        
        
    except : 
        break


# while True:
#     line = input().strip()
#     if line == '':
#         break
    
#     instruction_list.append(line.split())
#     blank_included_count += 1
#     instruction_list[line_count].append(blank_included_count)
#     line_count += 1


flag = False
error_line = 0
error_msg = ''

last_var = False
##Number of variables declared
var_count = 0



#adding instructions and raising exceptions otherwise

for i in range(0,len(instruction_list)) : 
    ith_instruction = instruction_list[i]

    #Checking For Halt Errors

    if i == len(instruction_list)-1 and  'hlt' not in ith_instruction:
        error_msg = 'hlt not present in line : ' + str(ith_instruction[len(ith_instruction)-1])
        flag = True
        break

    elif 'hlt' in ith_instruction and i != len(instruction_list)-1:
        
        error_msg = 'hlt not last statement in line : ' + str(ith_instruction[len(ith_instruction)-1])
        flag = True
        break

    elif 'hlt' in ith_instruction and i == len(instruction_list)-1:
        if len(ith_instruction) != 2:
            error_msg = 'Wrong hlt syntax in line : ' + str(ith_instruction[len(ith_instruction)-1])
            flag = True
            break
        bin_list = Halt()

    #check for errors in general instructon
    if ith_instruction[0] in opcode:
        #put error checks on all the operation functions here
        #Type-A instructions checking
        if ith_instruction[0] == "add" :
             #checking for errors
            temp = typeAerrors(ith_instruction)
            flag = temp[0]
            #if error found
            if(flag) : 
                error_msg = temp[1]
                break
            #otherwise generating binary
            bin_list = Add(ith_instruction[1],ith_instruction[2],ith_instruction[3])

        if ith_instruction[0] == "sub" :
             #checking for errors
            temp = typeAerrors(ith_instruction)
            flag = temp[0]
            #if error found
            if(flag) : 
                error_msg = temp[1]
                break
            #otherwise generating binary
            bin_list = Sub(ith_instruction[1],ith_instruction[2],ith_instruction[3])

        if ith_instruction[0] == "mul" :
            #checking for errors
            temp = typeAerrors(ith_instruction)
            flag = temp[0]
             #if error found
            if(flag) : 
                error_msg = temp[1]
                break
            #otherwise generating binary
            bin_list = Mul(ith_instruction[1],ith_instruction[2],ith_instruction[3]) 

        if ith_instruction[0] == "xor" :
            #checking for errors
            temp = typeAerrors(ith_instruction)
            flag = temp[0]
            #if error found
            if(flag) : 
                error_msg = temp[1]
                break
            #otherwise generating binary
            bin_list = Xor(ith_instruction[1],ith_instruction[2],ith_instruction[3])

        if ith_instruction[0] == "or" :
            #checking for errors
            temp = typeAerrors(ith_instruction)
            flag = temp[0]
            #if error found
            if(flag) : 
                error_msg = temp[1]
                break
            #otherwise generating binary
            bin_list = Or(ith_instruction[1],ith_instruction[2],ith_instruction[3])

        if ith_instruction[0] == "and" :
            #checking for errors
            temp = typeAerrors(ith_instruction)
            flag = temp[0]
            #if error found
            if(flag) : 
                error_msg = temp[1]
                break
            #otherwise generating binary
            bin_list = And(ith_instruction[1],ith_instruction[2],ith_instruction[3])
        
    #Type-A ends Type-B checking begins
        if ith_instruction[0] == "mov" and ith_instruction[2] in reg_code:
            #checking for errors
            temp = typeCerrors(ith_instruction)
            flag = temp[0]
            #if error found
            if(flag) : 
                error_msg = temp[1]
                break
            #otherwise generating binary
            bin_list = MovReg(ith_instruction[1],ith_instruction[2])

        if ith_instruction[0] == "rs" :
            #checking for errors
            temp = typeBerrors(ith_instruction)
            flag = temp[0]
            #if error found
            if(flag) :
                error_msg = temp[1]
                break
            #otherwise generating binary
            bin_list = RightShift(ith_instruction[1],ith_instruction[2])
        
        if ith_instruction[0] == "ls" :
            #checking for errors
            temp = typeBerrors(ith_instruction)
            flag = temp[0]
            #if error found
            if(flag) : 
                error_msg = temp[1]
                break
            #otherwise generating binary
            bin_list = LeftShift(ith_instruction[1],ith_instruction[2])

    #Type-B ends Type-C checking begins
        if ith_instruction[0] == "mov" :
            #checking for errors
            temp = typeBerrors(ith_instruction)
            flag = temp[0]
            #if error found
            if(flag) : 
                error_msg = temp[1]
                break
            #otherwise generating binary
            bin_list = MovImm(ith_instruction[1],ith_instruction[2])
        
        if ith_instruction[0] == "div" :
            #checking for errors
            temp = typeCerrors(ith_instruction)
            flag = temp[0]
            #if error found
            if(flag) : 
                error_msg = temp[1]
                break
            #otherwise generating binary
            bin_list = Div(ith_instruction[1],ith_instruction[2])
        
        if ith_instruction[0] == "not" :
            #checking for errors
            temp = typeCerrors(ith_instruction)
            flag = temp[0]
            #if error found
            if(flag) : 
                error_msg = temp[1]
                break
            #otherwise generating binary
            bin_list = Invert(ith_instruction[1],ith_instruction[2])

        if ith_instruction[0] == "cmp" :
            #checking for errors
            temp = typeCerrors(ith_instruction)
            flag = temp[0]
            #if error found
            if(flag) : 
                error_msg = temp[1]
                break
            #otherwise generating binary
            bin_list = Compare(ith_instruction[1],ith_instruction[2])

    #Type-C ends Type-D checking begins
        if ith_instruction[0] == "st" :
                #checking for errors
                temp = typeDerrors(ith_instruction)
                flag = temp[0]
                #if error found
                if(flag) : 
                    error_msg = temp[1]
                    break
                #otherwise generating binary
                bin_list = Store(ith_instruction[1],variables[ith_instruction[2]]+line_count-var_count)
        
        if ith_instruction[0] == "ld" :
                #checking for errors
                temp = typeDerrors(ith_instruction)
                flag = temp[0]
                #if error found
                if(flag) : 
                    error_msg = temp[1]
                    break
                #otherwise generating binary
                bin_list = Load(ith_instruction[1],variables[ith_instruction[2]]+line_count-var_count)
    #Type-D ends Type-E checking begins
        if ith_instruction[0] == "je" :
                #checking for errors
                temp = typeEerrors(ith_instruction)
                flag = temp[0]
                #if error found
                if(flag) : 
                    error_msg = temp[1]
                    break
                #otherwise generating binary
                #i is given as input 0-based indexing
                bin_list = JumpIfEqual(i-var_count)

        if ith_instruction[0] == "jgt" :
                #checking for errors
                temp = typeEerrors()
                flag = temp[0]
                #if error found
                if(flag) : 
                    error_msg = temp[1]
                    break
                #otherwise generating binary
                #i is given as input 0-based indexing
                bin_list = JumpIfGreater(i-var_count)

        if ith_instruction[0] == "jlt" :
                #checking for errors
                temp = typeEerrors(ith_instruction)
                flag = temp[0]
                #if error found
                if(flag) : 
                    error_msg = temp[1]
                    break
                #otherwise generating binary
                #i is given as input 0-based indexing
                bin_list = JumpIfLess(i-var_count)

        if ith_instruction[0] == "jmp" :
                #checking for errors
                temp = typeEerrors(ith_instruction)
                flag = temp[0]
                #if error found
                if(flag) : 
                    error_msg = temp[1]
                    break
                #otherwise generating binary
                #i is given as input 0-based indexing
                bin_list = UncondJump(i-var_count)

        
        
        
        
    #check for errors in variables
    elif ith_instruction[0] == "var":
        if last_var:
            error_msg = 'Variable not declared at top at line : ' + str(ith_instruction[len(ith_instruction)-1])
            flag = True
            
            break
        
        if not last_var and instruction_list[i+1][0] != 'var':
            last_var = True

        if len(ith_instruction) != 3:
            error_msg = 'Wrong syntax while declaring variable : ' + str(ith_instruction[len(ith_instruction)-1])
            flag = True
            break

        temp = []      ##variable store
        temp.extend(ith_instruction[1])
        for e in temp:
            if (ord(e) not in range(ord('a'), ord('z')+1)) and (ord(e) not in range(ord('A'), ord('Z')+1)) and ord(e) != ord('_'):
                error_msg = 'Wrong variable name at line : ' + str(ith_instruction[len(ith_instruction)-1])
                flag = True
                break
        if flag:
            break

        if ith_instruction[1] in opcode:
            error_msg = 'Variable name Can\'t be an operation code: ' + str(ith_instruction[-1])
            flag = True
            break 

        if ith_instruction[1] in variables:
            error_msg = 'Error while declaring same variable again: ' + str(ith_instruction[-1])
            flag = True
            break

        variables[ith_instruction[1]] = i
        var_count += 1



    #checks for error in label declaration
    elif ith_instruction[0][-1] == ":":
        temp = []
        temp.extend(ith_instruction[0][0:-1])
        for e in temp:
            if (ord(e) not in range(ord('a'), ord('z')+1)) and (ord(e) not in range(ord('A'), ord('Z')+1)) and ord(e) != ord('_'):
                error_msg = 'Wrong label name at line : ' + str(ith_instruction[len(ith_instruction)-1])
                flag = True
                break
        if flag:
            break

        if ith_instruction[0][0:-1] in variables:
            error_line = 'Variable name used as label name at line : ' + str(ith_instruction[len(ith_instruction)-1])
            flag = True
            break

        #label is followed a general instruction. So add all the error checks for instructions above here also

        if 'hlt' == ith_instruction[1]:
            if len(ith_instruction) != 3:
                error_msg = 'Wrong syntax at line : ' + str(ith_instruction[len(ith_instruction)-1])
                flag = True
                break
            
            elif i != len(instruction_list)-1:
                error_msg = 'hlt not last instruction at line : ' + str(ith_instruction[len(ith_instruction)-1])
                flag = True
                break

            else : 
                bin_list = Halt()

        elif ith_instruction[1] in opcode:
            label_name = ith_instruction[0][0:-1]
            ith_instruction = ith_instruction[1:]
        #Type-A instructions checking
            if ith_instruction[0] == "add" :
                #checking for errors
                temp = typeAerrors(ith_instruction)
                flag = temp[0]
                #if error found
                if(flag) : 
                    error_msg = temp[1]
                    break
                #otherwise generating binary
                bin_list = Add(ith_instruction[1],ith_instruction[2],ith_instruction[3])

            if ith_instruction[0] == "sub" :
                #checking for errors
                temp = typeAerrors(ith_instruction)
                flag = temp[0]
                #if error found
                if(flag) : 
                    error_msg = temp[1]
                    break
                #otherwise generating binary
                bin_list = Sub(ith_instruction[1],ith_instruction[2],ith_instruction[3])

            if ith_instruction[0] == "mul" :
                #checking for errors
                temp = typeAerrors(ith_instruction)
                flag = temp[0]
                #if error found
                if(flag) : 
                    error_msg = temp[1]
                    break
                #otherwise generating binary
                bin_list = Mul(ith_instruction[1],ith_instruction[2],ith_instruction[3]) 

            if ith_instruction[0] == "xor" :
                #checking for errors
                temp = typeAerrors(ith_instruction)
                flag = temp[0]
                #if error found
                if(flag) : 
                    error_msg = temp[1]
                    break
                #otherwise generating binary
                bin_list = Xor(ith_instruction[1],ith_instruction[2],ith_instruction[3])

            if ith_instruction[0] == "or" :
                #checking for errors
                temp = typeAerrors(ith_instruction)
                flag = temp[0]
                #if error found
                if(flag) : 
                    error_msg = temp[1]
                    break
                #otherwise generating binary
                bin_list = Or(ith_instruction[1],ith_instruction[2],ith_instruction[3])

            if ith_instruction[0] == "and" :
                #checking for errors
                temp = typeAerrors(ith_instruction)
                flag = temp[0]
                #if error found
                if(flag) : 
                    error_msg = temp[1]
                    break
                #otherwise generating binary
                bin_list = And(ith_instruction[1],ith_instruction[2],ith_instruction[3])
            
        #Type-A ends Type-B checking begins
            if ith_instruction[0] == "mov" and ith_instruction[2] in reg_code:
                #checking for errors
                temp = typeCerrors(ith_instruction)
                flag = temp[0]
                #if error found
                if(flag) : 
                    error_msg = temp[1]
                    break
                #otherwise generating binary
                bin_list = MovReg(ith_instruction[1],ith_instruction[2])

            if ith_instruction[0] == "rs" :
                #checking for errors
                temp = typeBerrors(ith_instruction)
                flag = temp[0]
                #if error found
                if(flag) :
                    error_msg = temp[1]
                    break
                #otherwise generating binary
                bin_list = RightShift(ith_instruction[1],ith_instruction[2])
            
            if ith_instruction[0] == "ls" :
                #checking for errors
                temp = typeBerrors(ith_instruction)
                flag = temp[0]
                #if error found
                if(flag) : 
                    error_msg = temp[1]
                    break
                #otherwise generating binary
                bin_list = LeftShift(ith_instruction[1],ith_instruction[2])

        #Type-B ends Type-C checking begins
            if ith_instruction[0] == "mov" :
                #checking for errors
                temp = typeBerrors(ith_instruction)
                flag = temp[0]
                #if error found
                if(flag) : 
                    error_msg = temp[1]
                    break
                #otherwise generating binary
                bin_list = MovImm(ith_instruction[1],ith_instruction[2])
            
            if ith_instruction[0] == "div" :
                #checking for errors
                temp = typeCerrors(ith_instruction)
                flag = temp[0]
                #if error found
                if(flag) : 
                    error_msg = temp[1]
                    break
                #otherwise generating binary
                bin_list = Div(ith_instruction[1],ith_instruction[2])
            
            if ith_instruction[0] == "not" :
                #checking for errors
                temp = typeCerrors(ith_instruction)
                flag = temp[0]
                #if error found
                if(flag) : 
                    error_msg = temp[1]
                    break
                #otherwise generating binary
                bin_list = Invert(ith_instruction[1],ith_instruction[2])

            if ith_instruction[0] == "cmp" :
                #checking for errors
                temp = typeCerrors(ith_instruction)
                flag = temp[0]
                #if error found
                if(flag) : 
                    error_msg = temp[1]
                    break
                #otherwise generating binary
                bin_list = Compare(ith_instruction[1],ith_instruction[2])

        #Type-C ends Type-D checking begins
            if ith_instruction[0] == "st" :
                    #checking for errors
                    temp = typeDerrors(ith_instruction)
                    flag = temp[0]
                    #if error found
                    if(flag) : 
                        error_msg = temp[1]
                        break
                    #otherwise generating binary
                    bin_list = Store(ith_instruction[1],variables[ith_instruction[2]]+line_count-var_count)
            
            if ith_instruction[0] == "ld" :
                    #checking for errors
                    temp = typeDerrors(ith_instruction)
                    flag = temp[0]
                    #if error found
                    if(flag) : 
                        error_msg = temp[1]
                        break
                    #otherwise generating binary
                    bin_list = Load(ith_instruction[1],variables[ith_instruction[2]]+line_count-var_count)
        #Type-D ends Type-E checking begins
            if ith_instruction[0] == "je" :
                    #checking for errors
                    temp = typeEerrors(ith_instruction)
                    flag = temp[0]
                    #if error found
                    if(flag) : 
                        error_msg = temp[1]
                        break
                    #otherwise generating binary
                    #i is given as input 0-based indexing
                    bin_list = JumpIfEqual(i-var_count)

            if ith_instruction[0] == "jgt" :
                    #checking for errors
                    temp = typeEerrors()
                    flag = temp[0]
                    #if error found
                    if(flag) : 
                        error_msg = temp[1]
                        break
                    #otherwise generating binary
                    #i is given as input 0-based indexing
                    bin_list = JumpIfGreater(i-var_count)

            if ith_instruction[0] == "jlt" :
                    #checking for errors
                    temp = typeEerrors(ith_instruction)
                    flag = temp[0]
                    #if error found
                    if(flag) : 
                        error_msg = temp[1]
                        break
                    #otherwise generating binary
                    #i is given as input 0-based indexing
                    bin_list = JumpIfLess(i-var_count)

            if ith_instruction[0] == "jmp" :
                    #checking for errors
                    temp = typeEerrors(ith_instruction)
                    flag = temp[0]
                    #if error found
                    if(flag) : 
                        error_msg = temp[1]
                        break
                    #otherwise generating binary
                    #i is given as input 0-based indexing
                    bin_list = UncondJump(i-var_count)
            
            labels[label_name] = i
            
        else:
            error_msg = 'Wrong command after label at line : ' + str(ith_instruction[len(ith_instruction)-1])
            
            flag = True
            break

    else : 
        flag = True
        error_msg = "Syntax Error on line : " + str(ith_instruction[len(ith_instruction)-1])

    


#error for checking stack limit
#if we dont encounter any previous errors we check for stack limit
if not flag : 
    if(line_count+var_count>256) : 
        error_line = "Cant have more than 256 instructions"
        flag = True

 

#adding exception for invalid syntax
if flag : 
    #raise Exception("Invalid Syntax in Line : " ,error_line)
    print(error_msg)
else:
    for x in bin_list:
        print(x)


                

            

