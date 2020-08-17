
# CPU
#     Executing instructions
#     Gets them out of RAM
#     Registers (like variables)
#         Fixed names R0-R7
#         Fixed number of them -- 8 of them
#         Fixed size -- 8 bits
# Memory (RAM)
#     A big array of bytes
#     Each memory slot has an index, and a value stored at that index
#     That index into memory AKA:
#         pointer
#         location
#         address


# 0b00000000  == decimal 0
# 0b11111111  == decimal 255

# mixing data and instructions
# Main Read.me, ls8 Read.me, FAQ, LS8 -spec  all info, ignore Flags and interrupt (stretch goal)
# asm - Hello world (stretch)
import sys
memory = [
    1,
    3,  #save reg R2, 99
    2,  #        R2
    99, #            99
    4, #Print register
    2, # register number to print
    2,  # Halt
]
#43 minutes on video day 2
# TODO Error check sys.argv
filename = sys.argv[1]

with open(filename) as f:
    for address, line in enumerate(f):
        line = line.split("#")

        try:
            # 2 for base 2
            v = int(line[0], 2)
        except ValueError:
            continue

        memory[address] = v
print(memory[:15])

sys.exit(0)

register = [0] * 8

run = True

pc = 0

while run:
    inst = memory[pc]

    if inst == 1:
        print('Hello computer')
        pc += 1
    
    if inst == 2:
        run = False

    elif inst == 3:
        reg_num = memory[pc + 1]
        value = memory[pc + 2]

        register[reg_num] = value
        print(register)
        pc += 3   
    elif inst == 4:
        reg_num = memory[pc + 1]
        print(register[reg_num])

        pc += 2 
