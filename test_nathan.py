instruction_RAM = "ADD(r1,r2,r3)"

def destructuration(instruction):
    # On récupère l'instruction et les arguments.
    instruction, arguments = instruction.split("(")
    arguments = arguments[:-1]
    arguments = arguments.split(",")
    return instruction, arguments

instruction_RAM_destruct = destructuration(instruction_RAM)
print(instruction_RAM_destruct)
for element in instruction_RAM_destruct:
    print(element)
for args in instruction_RAM_destruct[1]:
    print(args)