#CO assignment 
#Atharva Mehta
#Nipun Gupta
#Shantanu Dixit

#import matplotlib.pyplot as plt

####DOUBTS ---- To Be Addressed : 
# For which all functions do we have to reset the registers? ---- we have to reset flag register before every operation. only in jump ops we have to read value of flags and then reset.
# Invert Function would lead to a change in MSB? Or Would it lead to Overflow?
# Do we have to check for overflow in functions like division? ---- idts because it is mentioned only add sub and mul can set the overflow bit.

#------------------functions------------------

#printing function

def PRINT():
    pc_bin = bin(pc)[2:]
    #error correction
    pc_bin = str(0 * (8-len(pc_bin))) + pc_bin
    print(pc_bin, registers['000'], registers['001'], registers['010'], registers['011'], registers['100'], registers['101'], registers['110'], '0'*12 + registers['111']['V'] + registers['111']['L'] + registers['111']['G'] + registers['111']['E'])

#Type - A

def add(code):
    reg1 = code[7:10]
    reg2 = code[10:13]
    reg3 = code[13:]

    registers['111']['V'] = registers['111']['L'] = registers['111']['G'] = registers['111']['E'] = '0'  #re-setting flags register

    sum = int(registers[reg2],2) + int(registers[reg3],2)
    #checking for overflow
    if sum > pow(2,16) - 1:
        registers['111']['V'] = '1'   #overflow bit set if overflow occurs
        registers[reg1] = bin(sum)[-16:]
    else:
        temp = bin(sum)[2:]
        registers[reg1] = '0' * (16 - len(temp)) + temp 
    
  

    return (1,False)  #increment of program counter

def sub(code):
    reg1 = code[7:10]
    reg2 = code[10:13]
    reg3 = code[13:]

    registers['111']['V'] = registers['111']['L'] = registers['111']['G'] = registers['111']['E'] = '0'   #Reset
    diff = int(registers[reg2],2) - int(registers[reg3],2)


    #checking for overflow
    if diff > pow(2,16) - 1:
        registers['111']['V'] = '1'   #overflow bit set if overflow occurs
        registers[reg1] = bin(diff)[-16:]
    else:
        temp = bin(diff)[2:]
        registers[reg1] = '0' * (16 - len(temp)) + temp 
    
  

    return (1,False)  #increment of program counter

def mul(code):
    reg1 = code[7:10]
    reg2 = code[10:13]
    reg3 = code[13:]

    registers['111']['V'] = registers['111']['L'] = registers['111']['G'] = registers['111']['E'] = '0'   #Reset
    Mul = int(registers[reg2],2) * int(registers[reg3],2)


    #checking for overflow
    if Mul > pow(2,16) - 1:
        registers['111']['V'] = '1'   #overflow bit set if overflow occurs
        registers[reg1] = bin(Mul)[-16:]
    else:
        temp = bin(Mul)[2:]
        registers[reg1] = '0' * (16 - len(temp)) + temp 
    
    return (1,False)  #increment of program counter

def xor(code):
    reg1 = code[7:10]
    reg2 = code[10:13]
    reg3 = code[13:]

    registers['111']['V'] = registers['111']['L'] = registers['111']['G'] = registers['111']['E'] = '0'   #Reset
    i=0
    while(i<len(registers[reg2])):
        if((registers[reg2][i]) == registers[reg3][i]):
            registers[reg1] += '0'
        else:
            registers[reg1] += '1'
        i+=1
    registers[reg1] = '0' * (16 - len(registers[reg1])) + registers[reg1]



    if(int(registers[reg2],2) > int(registers[reg3],2)):
        registers['111']['G'] = '1'
    elif int(registers[reg2],2) < int(registers[reg3],2):
        registers['111']['L'] = '1'
    else:
        registers['111']['E'] = '1'
    
    return (1,False)

def or_fun(code):
    reg1 = code[7:10]
    reg2 = code[10:13]
    reg3 = code[13:]

    registers['111']['V'] = registers['111']['L'] = registers['111']['G'] = registers['111']['E'] = '0'   #Reset

    i=0
    while(i<len(registers[reg2])):
        if((registers[reg2][i]) == 1 or registers[reg3][i] == 1):
            registers[reg1] += '1'
        else:
            registers[reg1] += '0'
        i+=1
    registers[reg1] = '0' * (16 - len(registers[reg1])) + registers[reg1]



    if(int(registers[reg2],2) > int(registers[reg3],2)):
        registers['111']['G'] = '1'
    elif int(registers[reg2],2) < int(registers[reg3],2):
        registers['111']['L'] = '1'
    else:
        registers['111']['E'] = '1'
    
    return (1,False)

def and_fun(code):
    
    reg1 = code[7:10]
    reg2 = code[10:13]
    reg3 = code[13:]

    registers['111']['V'] = registers['111']['L'] = registers['111']['G'] = registers['111']['E'] = '0'   #Reset

    i=0
    while(i<len(registers[reg2])):
        if((registers[reg2][i]) == 1 and registers[reg3][i] == 1):
            registers[reg1] += '1'
        else:
            registers[reg1] += '0'
        i+=1
    registers[reg1] = '0' * (16 - len(registers[reg1])) + registers[reg1]



    if(int(registers[reg2],2) > int(registers[reg3],2)):
        registers['111']['G'] = '1'
    elif int(registers[reg2],2) < int(registers[reg3],2):
        registers['111']['L'] = '1'
    else:
        registers['111']['E'] = '1'
    
    return (1,False)

#Type - B

def mov_imm(code):
    reg1 = code[7:10]
    registers[reg1] = Imm      ##immediate stored in Imm

    return (1,False)

def rs(code):
    reg1 = code[7:10]
    shifter = int(Imm)
    registers[reg1] = '0'*shifter + registers[reg1][0:16-shifter]
    return (1,False)

def ls(code):
    reg1 = code[7:10]
    shifter = int(Imm)
    registers[reg1] = registers[reg1][shifter:length(registers[reg1])] + '0'*shifter
    return (1,False)

#Type - C

def mov_reg(code):
    r1 = code[10:13]
    r2 = code[13:16]

    #moving r2 to r1 
    registers[r1] = registers[r2]

    return (1,False)

    


def div(code):
    r3 = code[10:13]
    r4 = code[13:16]

    #storing quotient in '000' and remainder in '001'

    #storing the quotient
    r0 = bin(int(int(registers[r3],2)/int(registers[r4],2)))[2:]
    registers['000'] = '0'*(16-len(r0)) + r0

    #storing the remainder
    r1 = bin(int(registers[r3],2) - int(registers['000'],2)*int(registers[r4],2))[2:]
    registers['001'] = '0'*(16-len(r1)) + r1

    return (1,False) 
    


def inv(code):
    ###need confirmation on some part ....waiting for confirmation
    r1 = code[10:13]
    r2 = code[13:16]
    
    #we store the result in register-1 
    temp = ''

    for i in range(0,len(registers[r2])) :
        if(registers[r2][i]=='0') : 
            temp += '1'
        
        else :
            temp += '0'


    registers[r1] = '0'*(16-len(temp)) + temp

    return (1,False)
        


def cmp(code):
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

    return (1,False)
    

#Type - D

def ld(code):
    reg = code[5:8]
    mem_add = code[8:]
    registers[reg] = memory[int(mem_add, 2)]
    return (1,False)

def st(code):
    reg = code[5:8]
    mem_add = code[8:]
    memory[int(mem_add, 2)] = registers[reg]
    return (1,False)

#Type - E

def jmp(code):
    address = code[8:16]
    print(int(address,2))
    return (int(address,2),True)

def jlt(code):
    if registers['L'] == '1' : 
        return (int(code[8:16],2),True)
    else : 
        return (1,False)

def jgt(code):
    if registers['G'] == '1' : 
        return (int(code[8:16],2),True)
    else : 
        return (1,False)

def je(code):
    if registers['E'] == '1' : 
        return (int(code[8:16],2),True)
    else : 
        return (1,False)

#Type - F

def hlt(code):
    return (line_counter+1,True)

#------------global variables-------------

#variables for bonus question
cycle = 1
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
        if temp[0] : 
            pc = temp[1]
        else : 
            pc += 1

   #sub 
    elif op_code == '00001':
        temp = sub(code)
        if temp[0] : 
            pc = temp[1]
        else : 
            pc += 1
    
    #mov_imm
    elif op_code == '00010':
        temp = mov_imm(code)
        if temp[0] : 
            pc = temp[1]
        else : 
            pc += 1
    
    #mov_reg
    elif op_code == '00011':
        temp = mov_reg(code)
        if temp[0] : 
            pc = temp[1]
        else : 
            pc += 1
    
    #ld
    elif op_code == '00100':
        temp = ld(code)
        if temp[0] : 
            pc = temp[1]
        else : 
            pc += 1
    
    #st
    elif op_code == '00101':
        temp = st(code)
        if temp[0] : 
            pc = temp[1]
        else : 
            pc += 1
    
    #mul
    elif op_code == '00110':
        temp = mul(code)
        if temp[0] : 
            pc = temp[1]
        else : 
            pc += 1

    #div
    elif op_code == '00111':
        temp = div(code)
        if temp[0] : 
            pc = temp[1]
        else : 
            pc += 1

    #rs
    elif op_code == '01000':
        temp = rs(code)
        if temp[0] : 
            pc = temp[1]
        else : 
            pc += 1
    
    #ls
    elif op_code == '01001':
        temp = ls(code)
        if temp[0] : 
            pc = temp[1]
        else : 
            pc += 1

    #xor
    elif op_code == '01010':
        temp = xor(code)
        if temp[0] : 
            pc = temp[1]
        else : 
            pc += 1

    #or_fun
    elif op_code == '01011':
        temp = or_fun(code)
        if temp[0] : 
            pc = temp[1]
        else : 
            pc += 1

    #and_fun
    elif op_code == '01100':
        temp = and_fun(code)
        if temp[0] : 
            pc = temp[1]
        else : 
            pc += 1

    #inv
    elif op_code == '01101':
        temp = inv(code)
        if temp[0] : 
            pc = temp[1]
        else : 
            pc += 1

    #cmp
    elif op_code == '01110':
        temp = cmp(code)
        if temp[0] : 
            pc = temp[1]
        else : 
            pc += 1

    #jmp
    elif op_code == '01111':
        temp = jmp(code)
        if temp[0] : 
            pc = temp[1]
        else : 
            pc += 1

    #jlt
    elif op_code == '10000':
        temp = jlt(code)
        if temp[0] : 
            pc = temp[1]
        else : 
            pc += 1
    
    #jgt
    elif op_code == '10001':
        temp = jgt(code)
        if temp[0] : 
            pc = temp[1]
        else : 
            pc += 1
    
    #je
    elif op_code == '10010':
        temp = je(code)
        if temp[0] : 
            pc = temp[1]
        else : 
            pc += 1
    
    #hlt
    elif op_code == '10011':
        temp = hlt(code)
        if temp[0] : 
            pc = temp[1]
        else : 
            pc += 1

    PRINT()
    cycle += 1


#printing memory dump

#####testing.... so removed this bit temporarily
# for x in memory:
#     print(x)

#bonus plot
# plt.plot(cycle_list, pc_list)
# plt.xlabel('Cycle')
# plt.ylabel('Memory address')
# plt.title('Memory address v/s cycle')
# plt.plot()