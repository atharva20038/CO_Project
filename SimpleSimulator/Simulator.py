#CO assignment 
#Atharva Mehta
#Nipun Gupta
#Shantanu Dixit

import matplotlib.pyplot as plt


#------------------functions------------------

#printing function

def PRINT():
    pc_bin = bin(pc)[2:]
    #error correction
    pc_bin = '0' * (8 - len(pc_bin)) + pc_bin
    print(pc_bin, registers['000'], registers['001'], registers['010'], registers['011'], registers['100'], registers['101'], registers['110'], '0'*12 + registers['111']['V'] + registers['111']['L'] + registers['111']['G'] + registers['111']['E'])
    return
    
#Type - A

def add(code):
    reg1 = code[7:10]
    reg2 = code[10:13]
    reg3 = code[13:]

    registers['111']['V'] = registers['111']['L'] = registers['111']['G'] = registers['111']['E'] = '0'  #Reset flags register

    sum = int(registers[reg2],2) + int(registers[reg3],2)
    #checking for overflow
    if sum > pow(2,16) - 1:
        registers['111']['V'] = '1'   #overflow bit set if overflow occurs
        registers[reg1] = bin(sum)[-16:]
    else:
        temp = bin(sum)[2:]
        registers[reg1] = '0' * (16 - len(temp)) + temp 
    PRINT()
    return (1,False)  #increment of program counter

def sub(code):
    reg1 = code[7:10]
    reg2 = code[10:13]
    reg3 = code[13:]

    registers['111']['V'] = registers['111']['L'] = registers['111']['G'] = registers['111']['E'] = '0'   #Reset Flag Registers
    diff = int(registers[reg2],2) - int(registers[reg3],2)

    #checking for overflow
    if diff < 0:
        registers['111']['V'] = '1'   #overflow bit set if overflow occurs
        registers[reg1] = '0' * 16
    else:
        temp = bin(diff)[2:]
        registers[reg1] = '0' * (16 - len(temp)) + temp 
    PRINT()
    return (1,False)  #increment of program counter

def mul(code):
    reg1 = code[7:10]
    reg2 = code[10:13]
    reg3 = code[13:]

    registers['111']['V'] = registers['111']['L'] = registers['111']['G'] = registers['111']['E'] = '0'   #Reset Flag registers
    Mul = int(registers[reg2],2) * int(registers[reg3],2)

    #checking for overflow
    if Mul > pow(2,16) - 1:
        registers['111']['V'] = '1'   #overflow bit set if overflow occurs
        registers[reg1] = bin(Mul)[-16:]
    else:
        temp = bin(Mul)[2:]
        registers[reg1] = '0' * (16 - len(temp)) + temp 
    PRINT()
    return (1,False)  #increment of program counter

def xor(code):
    reg1 = code[7:10]
    reg2 = code[10:13]
    reg3 = code[13:]

    registers['111']['V'] = registers['111']['L'] = registers['111']['G'] = registers['111']['E'] = '0'   #Reset
    temp = ''
    i=0
    while(i<len(registers[reg2])):
        if((registers[reg2][i]) == registers[reg3][i]):
            temp += '0'
        else:
            temp += '1'
        i+=1
    registers[reg1] = temp
    PRINT()
    return (1,False)

def or_fun(code):
    reg1 = code[7:10]
    reg2 = code[10:13]
    reg3 = code[13:]

    registers['111']['V'] = registers['111']['L'] = registers['111']['G'] = registers['111']['E'] = '0'   #Reset
    temp = ''
    i=0
    while(i<len(registers[reg2])):
        if((registers[reg2][i]) == 1 or registers[reg3][i] == 1):
            temp += '1'
        else:
            temp += '0'
        i+=1
    registers[reg1] = temp
    PRINT()
    return (1,False)

def and_fun(code):
    
    reg1 = code[7:10]
    reg2 = code[10:13]
    reg3 = code[13:]

    registers['111']['V'] = registers['111']['L'] = registers['111']['G'] = registers['111']['E'] = '0'   #Reset
    temp = ''
    i=0
    while(i<len(registers[reg2])):
        if((registers[reg2][i]) == 1 and registers[reg3][i] == 1):
            temp += '1'
        else:
            temp += '0'
        i+=1
    registers[reg1] = temp
    PRINT()
    return (1,False)

#Type - B

def mov_imm(code):
    registers['111']['V'] = registers['111']['L'] = registers['111']['G'] = registers['111']['E'] = '0'   #Reset
    reg1 = code[5:8]
    Imm = code[8:]
    registers[reg1] = '0' * 8 + Imm      ##immediate stored in Imm
    PRINT()
    return (1,False)

def rs(code):
    registers['111']['V'] = registers['111']['L'] = registers['111']['G'] = registers['111']['E'] = '0'   #Reset
    reg1 = code[5:8]
    reg_val = int(registers[reg1],2)
    shifter = int(code[8:],2)
    registers[reg1] = bin(reg_val >> shifter)[2:]
    PRINT()
    return (1,False)

def ls(code):
    registers['111']['V'] = registers['111']['L'] = registers['111']['G'] = registers['111']['E'] = '0'   #Reset
    reg1 = code[5:8]
    reg_val = int(registers[reg1],2)
    shifter = int(code[8:],2)
    registers[reg1] = bin(reg_val << shifter)[2:]
    PRINT()
    return (1,False)

#Type - C

def mov_reg(code):

    r1 = code[10:13]
    r2 = code[13:16]

    #moving r2 to r1 
    if r2 != '111':
        registers['111']['V'] = registers['111']['L'] = registers['111']['G'] = registers['111']['E'] = '0'  #re-setting flags register
        registers[r1] = registers[r2]
        PRINT()
    else:
        registers[r1] = '0'*12 + registers['111']['V'] + registers['111']['L'] + registers['111']['G'] + registers['111']['E']
        registers['111']['V'] = registers['111']['L'] = registers['111']['G'] = registers['111']['E'] = '0'  #re-setting flags register
        PRINT()
    return (1,False)


def div(code):

    registers['111']['V'] = registers['111']['L'] = registers['111']['G'] = registers['111']['E'] = '0'  #re-setting flags register

    r3 = code[10:13]
    r4 = code[13:16]

    #storing quotient in '000' and remainder in '001'

    #storing the quotient
    r0 = bin(int(int(registers[r3],2)/int(registers[r4],2)))[2:]
    registers['000'] = '0'*(16-len(r0)) + r0

    #storing the remainder
    r1 = bin(int(registers[r3],2) - int(registers['000'],2)*int(registers[r4],2))[2:]
    registers['001'] = '0'*(16-len(r1)) + r1
    PRINT()
    return (1,False) 
    

def inv(code):
    ###need confirmation on some part ....waiting for confirmation
    r1 = code[10:13]
    r2 = code[13:16]

    registers['111']['V'] = registers['111']['L'] = registers['111']['G'] = registers['111']['E'] = '0'  #re-setting flags register
    
    #we store the result in register-1 
    temp = ''

    for i in range(0,len(registers[r2])) :
        if(registers[r2][i]=='0') : 
            temp += '1'
        
        else :
            temp += '0'


    registers[r1] = '0'*(16-len(temp)) + temp
    PRINT()
    return (1,False)
        


def cmp(code):

    registers['111']['V'] = registers['111']['L'] = registers['111']['G'] = registers['111']['E'] = '0'  #re-setting flags register

    r1 = code[10:13]
    r2 = code[13:16]
    value1 = int(registers[r1],2)
    value2 = int(registers[r2],2)

    if(value2<value1) : 
        registers['111']['G'] = '1'
    elif value2>value1 :
        registers['111']['L'] = '1'
    else : 
        registers['111']['E'] = '1'
    PRINT()
    return (1,False)
    

#Type - D

def ld(code):

    registers['111']['V'] = registers['111']['L'] = registers['111']['G'] = registers['111']['E'] = '0'  #re-setting flags register

    reg = code[5:8]
    mem_add = code[8:]
    mem_int = int(mem_add, 2)
    registers[reg] = memory[int(mem_add, 2)]
    PRINT()
    return (1,False,mem_int)

def st(code):

    registers['111']['V'] = registers['111']['L'] = registers['111']['G'] = registers['111']['E'] = '0'  #re-setting flags register

    reg = code[5:8]
    mem_add = code[8:]
    memory[int(mem_add, 2)] = registers[reg]
    mem_int = int(mem_add, 2)
    PRINT()
    return (1,False,mem_int)

#Type - E

def jmp(code):
    address = code[8:16]
    
    registers['111']['V'] = registers['111']['L'] = registers['111']['G'] = registers['111']['E'] = '0'  #re-setting flags register
    PRINT()
    return (int(address,2),True)

def jlt(code):
    if registers['111']['L'] == '1' : 
        registers['111']['V'] = registers['111']['L'] = registers['111']['G'] = registers['111']['E'] = '0'  #re-setting flags register
        PRINT()
        return (int(code[8:16],2),True)
    else : 
        registers['111']['V'] = registers['111']['L'] = registers['111']['G'] = registers['111']['E'] = '0'  #re-setting flags register
        PRINT()
        return (1,False)

def jgt(code):
    if registers['111']['G'] == '1' : 
        registers['111']['V'] = registers['111']['L'] = registers['111']['G'] = registers['111']['E'] = '0'  #re-setting flags register
        PRINT()
        return (int(code[8:16],2),True)
    else : 
        registers['111']['V'] = registers['111']['L'] = registers['111']['G'] = registers['111']['E'] = '0'  #re-setting flags register
        PRINT()
        return (1,False)

def je(code):
    if registers['111']['E'] == '1' : 
        registers['111']['V'] = registers['111']['L'] = registers['111']['G'] = registers['111']['E'] = '0'  #re-setting flags registe0r
        PRINT()
        return (int(code[8:16],2),True)
    else : 
        registers['111']['V'] = registers['111']['L'] = registers['111']['G'] = registers['111']['E'] = '0'  #re-setting flags register
        PRINT()
        return (1,False)

#Type - F

def hlt(code):
    registers['111']['V'] = registers['111']['L'] = registers['111']['G'] = registers['111']['E'] = '0'  #re-setting flags register
    PRINT()
    return (line_counter+1,True)

#------------global variables-------------

#variables for bonus question
cycle = 0
cycle_list = []
pc_list = []

#memory
memory = ['0000000000000000']*256

#program counter
pc = 0

#register values
registers = {
    '000': '0' * 16,
    '001': '0' * 16, 
    '010': '0' * 16,
    '011': '0' * 16,
    '100': '0' * 16,
    '101': '0' * 16,
    '110': '0' * 16,
    '111': {'V':'0', 'L': '0', 'G': '0', 'E': '0'}

    # ####TESTING.....

    # '000': '0000000000001111',
    # '001': '0' * 16, 
    # '010': '0' * 16,
    # '011': '0000000000001111',
    # '100': '0000000000000111',
    # '101': '0' * 16,
    # '110': '0' * 16,
    # '111': {'V':'0', 'L': '0', 'G': '0', 'E': '0'}
}

#input - block

#counter
line_counter = 0

while True:
    try:
        instruction = input().strip()
        memory[line_counter] = instruction
        line_counter += 1
    
    except:
        break

# while True:
#     line = input().strip()
#     if line == '':
#         break
#     memory[line_counter] = line
#     line_counter += 1

# #####Testing......
# jmp('0111100000001111')
# PRINT()


while pc<line_counter:

    #updating bonus variables
    cycle_list.append(cycle)
    
    pc_list.append(pc)

    code = memory[pc]
    op_code = code[0:5]

    #add
    if op_code == '00000':
        temp = add(code)
        if temp[1] : 
            pc = temp[0]
        else : 
            pc += 1

   #sub 
    elif op_code == '00001':
        temp = sub(code)
        if temp[1] : 
            pc = temp[0]
        else : 
            pc += 1
    
    #mov_imm
    elif op_code == '00010':
        temp = mov_imm(code)
        if temp[1] : 
            pc = temp[0]
        else : 
            pc += 1
    
    #mov_reg
    elif op_code == '00011':
        temp = mov_reg(code)
        if temp[1] : 
            pc = temp[0]
        else : 
            pc += 1
    
    #ld
    elif op_code == '00100':
        temp = ld(code)
        if temp[1] : 
            pc = temp[0]
        else : 
            pc += 1

        pc_list.append(temp[2])
        cycle_list.append(cycle)
    
    #st
    elif op_code == '00101':
        temp = st(code)
        if temp[1] : 
            pc = temp[0]
        else : 
            pc += 1

        pc_list.append(temp[2])
        cycle_list.append(cycle)
    
    #mul
    elif op_code == '00110':
        temp = mul(code)
        if temp[1] : 
            pc = temp[0]
        else : 
            pc += 1

    #div
    elif op_code == '00111':
        temp = div(code)
        if temp[1] : 
            pc = temp[0]
        else : 
            pc += 1

    #rs
    elif op_code == '01000':
        temp = rs(code)
        if temp[1] : 
            pc = temp[0]
        else : 
            pc += 1
    
    #ls
    elif op_code == '01001':
        temp = ls(code)
        if temp[1] : 
            pc = temp[0]
        else : 
            pc += 1

    #xor
    elif op_code == '01010':
        temp = xor(code)
        if temp[1] : 
            pc = temp[0]
        else : 
            pc += 1

    #or_fun
    elif op_code == '01011':
        temp = or_fun(code)
        if temp[1] : 
            pc = temp[0]
        else : 
            pc += 1

    #and_fun
    elif op_code == '01100':
        temp = and_fun(code)
        if temp[1] : 
            pc = temp[0]
        else : 
            pc += 1

    #inv
    elif op_code == '01101':
        temp = inv(code)
        if temp[1] : 
            pc = temp[0]
        else : 
            pc += 1

    #cmp
    elif op_code == '01110':
        temp = cmp(code)
        if temp[1] : 
            pc = temp[0]
        else : 
            pc += 1

    #jmp
    elif op_code == '01111':
        temp = jmp(code)
        if temp[1] : 
            pc = temp[0]
        else : 
            pc += 1

    #jlt
    elif op_code == '10000':
        temp = jlt(code)
        if temp[1] : 
            pc = temp[0]
        else : 
            pc += 1
    
    #jgt
    elif op_code == '10001':
        temp = jgt(code)
        if temp[1] : 
            pc = temp[0]
        else : 
            pc += 1
    
    #je
    elif op_code == '10010':
        temp = je(code)
        if temp[1] : 
            pc = temp[0]
        else : 
            pc += 1
    
    #hlt
    elif op_code == '10011':
        temp = hlt(code)
        if temp[1] : 
            pc = temp[0]
        else : 
            pc += 1

    #PRINT()
    cycle += 1


#printing memory dump

#####testing.... so removed this bit temporarily
for x in memory:
    print(x)

#bonus plot

plt.xlabel('Cycle')
plt.ylabel('Memory address')
plt.title('Memory address v/s cycle')
plt.scatter(cycle_list, pc_list)
plt.savefig("abc.png")