memory = [
    1, # PRINT_BEEJ
    1, # PRINT_BEEJ
    1, # PRINT_BEEJ
    2 # HALT
]

# Start execution at address 0

# Keep track of the address of the currently-executing instruction

pc = 0 # Program counter, pointer to the instruction we're executing

halted = False

while not halted:
    instruction = memory[pc]

    if instruction == 1:
        print("Beej!")
        pc += 1
    elif instruction == 2:
        break

