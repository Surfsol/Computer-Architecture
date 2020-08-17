"""CPU functionality."""

import sys

class CPU:
    """Main CPU class."""

    def __init__(self, current):
        """Construct a new CPU."""
        # 256 bytes of memory 
        self.ram = [0] * 256
        #  8 general-purpose registers.
        self.reg = [0] * 8
        #PC address of current executing instructions
        self.pc = 0
        # FL Flags
        self.fl = 0
        
        
    #should accept the address to read and return the value stored there.
    # returns value stored in RAM at that index
    def ram_read(self, MAR):
        # MAR holds memory address reading or writing MAR = self.pc
        return self.ram[MAR]

    #should accept a value to write, and the address to write it to.
    def ram_write(self, MAR, MDR):
        # MDR Memory Data Register, holds the value to write or the value just read
        #value to write or read MDR
        self.ram[MAR] = MDR

    def load(self, program = None):
        """Load a program into memory."""

        address = 0

        # For now, we've just hardcoded a program:

        program = [
            # From print8.ls8
            0b10000010, # LDI R0,8
            0b00000000,
            0b00001000,
            0b01000111, # PRN R0
            0b00000000,
            0b00000001, # HLT
        ]

        #put instructions into RAM
        for instruction in program:
            self.ram[address] = instruction
            address += 1


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""
        #adding operation, add a + b
        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def get_int(self, binary):
        binStr = str(binary)
        return int(binStr,2)

    def prn(self, reg_num):
        #get integer of binary and print
        integer = self.get_int(reg_num)
        # print the integer
        print(integer)
        print(self.reg[integer])

    #set value of a register to an interger
    def ldi(self, a, b):
        #find variable that is a binary that can be 
        #converted to a value
        if self.get_int(a):
            value = self.get_int(a)
            idx = b
        else: 
            value = self.get_int(b)
            idx = a
        self.reg[idx] = value

    def run(self):
        """Run the CPU."""
        HLT = 0b00000001
        LDI = 0b10000010 
        PRN = 0b01000111

        #It needs to read the memory address that's stored in register `PC`
        self.ir = self.ram_read(self.pc)

        while self.ir != HLT:
            if self.ir == LDI:
                #Using `ram_read()`,read the bytes at `PC+1` and `PC+2` from RAM into
                #  variables `operand_a` and `operand_b` in case the instruction needs them.
                self.operand_a = self.ram_read(self.pc + 1)
                self.operand_b = self.ram_read(self.pc + 2)
                #should do if else statements  on the operands
                self.ldi(self.operand_a, self.operand_b)
                self.pc += 3
            elif self.ir == PRN:
                #print next line
                # take next value in ram and put it in prn
                self.prn(self.ram[self.pc+1])
                self.pc += 2
            elif self.ir != HLT and self.ir != PRN:
                self.pc += 1
            # go to next instructions.
            self.ir = self.ram_read(self.pc)


