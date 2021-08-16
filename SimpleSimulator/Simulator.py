#CO assignment 
#Atharva Mehta
#Nipun Gupta
#Shantanu Dixit

#------------------functions------------------

#Type - A

def add(code):
    pass

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

#printing function

def PRINT():
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

# #opcodes
# opcodes = {
#     '00000': add(),
#     '00001': sub(),
#     '00010': mov_imm(),
#     '00011': mov_reg,
#     '00100': ld(),
#     '00101': st(),
#     '00110': mul(),
#     '00111': div(), 
#     '01000': rs(),
#     '01001': ls(),
#     '01010': xor(),
#     '01011': or_fun(),
#     '01100': and_fun(),
#     '01101': not_,
#     '01110': cmp',
#     '01111': jmp',
#     '10000': jlt',
#     '10001': jgt',
#     '10010': je',
#     '10011': hlt'
# }

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
