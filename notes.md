RAM - can access memory at any time
    - like be array of memory.
    - address, index of array.
    - stores values in bytes

CPU communicates with RAM

Register - can hold variables that can be accessed at a high speed. variables we do
math on.

CPU instructions are stored in RAM with other data.  CPU decides what to do based off value from RAM

PC - stores address of current instruction

speed depends on CPU clock

cache speeds up access to RAM


#video day 2
move program into a file and be able to run it
examples directory - numbers -> correspond to instructions

with open('prog1') as f:
    for line in f:
        #remove comments
        line = line.split('#')
        try:
            v = int(line)
        except ValueError:
            continue
        print(v)