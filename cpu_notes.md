Class CPU:
    init
        - ram storage - 256 zeros
        - reg = 8 zeros
        - starts pc at 0
        - flags at 0

    ram_read 
        returns value stored in RAM at the index

    ram_write  ????
        holds value to write or just read

    Load 
        - loads instructions to RAM

    alu 
        - add reg[b] to reg[a], and stores at reg[a]

    trace(self)
        - prints CPU state

    get_int

    prn

    ldi
        - converts binary number to integer and uses for value of reg

    run - runs instructions, stops at HLT 