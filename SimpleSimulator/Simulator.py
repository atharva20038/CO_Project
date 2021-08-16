#CO assignment 
#Atharva Mehta
#Nipun Gupta
#Shantanu Dixit

#------------------functions------------------

#printing function

def PRINT():
    pc_bin = bin(pc)[2:]
    pc_bin = 0 * (8-len(pc_bin)) + pc_bin
    print(pc_bin, registers['000'], registers['001'], registers['010'], registers['011'], registers['100'], registers['101'], registers['110'], 0*12 + registers['111']['V'] + registers['111']['L'] + registers['111']['G'] + registers['111']['E'])

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
        registers[reg1] = 0 * (16 - len(temp)) + temp 
    
    PRINT()

    return 1  #increment of program counter

def sub(code):
    pass

def mul(code):
    pass

def xor(code):
    pass

def or_fun(code):
    pass

def and_fun(code):
    pass

#Type - B

def mov_imm(code):
    pass

def rs(code):
    pass

def ls(code):
    pass

#Type - C

def mov_reg(code):
    pass

def div(code):
    pass

def inv(code):
    pass

def cmp(code):
    pass

#Type - D

def ld(code):
    pass

def st(code):
    pass

#Type - E

def jmp(code):
    pass

def jlt(code):
    pass

def jgt(code):
    pass

def je(code):
    pass

#Type - F

def hlt(code):
    pass

#------------global variables-------------

#memory
memory = ['0000000000000000']*256

#program counter
pc = 0

#register values
registers = {
    '000': '00000000',
    '001': '00000000', 
    '010': '00000000',
    '011': '00000000',
    '100': '00000000',
    '101': '00000000',
    '110': '00000000',
    '111': {'V':'0', 'L': '0', 'G': '0', 'E': '0'}
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


while pc<line_counter:
    code = memory[pc]
    op_code = code[0:5]

    if op_code == '000':
        pc += add(code)


#printing memory dump

for x in memory:
    print(x)