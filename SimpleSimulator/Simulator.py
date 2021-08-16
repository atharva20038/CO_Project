#CO assignment 
#Atharva Mehta
#Nipun Gupta
#Shantanu Dixit


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

#opcodes
opcodes = {
    '00000': 'add',
    '00001': 'sub',
    '00010': 'mov_imm',
    '00011': 'mov_reg',
    '00100': 'ld',
    '00101': 'st',
    '00110': 'mul',
    '00111': 'div', 
    '01000': 'rs',
    '01001': 'ls',
    '01010': 'xor',
    '01011': 'or',
    '01100': 'and',
    '01101': 'not',
    '01110': 'cmp',
    '01111': 'jmp',
    '10000': 'jlt',
    '10001': 'jgt',
    '10010': 'je',
    '10011': 'hlt'
}

#------------------functions------------------


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

    

