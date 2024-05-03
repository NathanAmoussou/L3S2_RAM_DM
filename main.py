import argparse # Pour récupérer le chemin du fichier avec les instructions RAM.

# Question 1

# Récupération du chemin du fichier en argument.
RAM_instructions_list = list() # Pour stocker chaque instruction RAM.
parser = argparse.ArgumentParser(description='Lire un fichier contenant des instructions RAM.')
parser.add_argument("filepath", help="Chemin du fichier à traiter", type=str)
args = parser.parse_args()
filepath = args.filepath
print(f"Traitement du fichier : {filepath}")
for line in open(filepath, 'r'):
    RAM_instructions_list.append(line.strip())

# Création de la classe pour les instructions RAM.
class RAM_instruction:
    def __init__(self, instruction: str):
        self.str_instruc = instruction # Instruction sous la forme 'ADD(r1,r2,r3)'
        self.instruc_elements = self.parse() # Instruction sous la forme ('ADD', ['r1', 'r2', 'r3'])
        self.instruc_type = self.instruc_elements[0] # Type de l'instruction (ADD, SUB, ...)
        self.instruc_args = self.instruc_elements[1] # Arguments de l'instruction (['r1', 'r2', 'r3'])
        
    def parse(self):
        # On récupère l'instruction et les arguments.
        instruction, arguments = self.str_instruc.split("(")
        arguments = arguments[:-1]
        arguments = arguments.split(",")
        return instruction, arguments

# Création de la classe pour le programme RAM.
class RAM_program:
    def __init__(self, RAM_instructions_list_arg, PC: int = 0):
        self.supported_operations = {"ADD": self.ADD_instruction, 
                                     "SUB": self.SUB_instruction, 
                                     "MUL": self.MULT_instruction, 
                                     "DIV": self.DIV_instruction}
        if RAM_instructions_list_arg[0][0:3]  not in self.supported_operations.keys():
            self.RAM_input_list = RAM_instructions_list_arg[0].split(" ")
            self.RAM_instructions_list = [RAM_instruction(RAM_instruction_arg) for RAM_instruction_arg in RAM_instructions_list_arg[1:]]
        else:
            self.RAM_input_list = list()
            self.RAM_instructions_list = [RAM_instruction(RAM_instruction_arg) for RAM_instruction_arg in RAM_instructions_list_arg]
        self.PC = PC
        self.in_registers = list() # Registres d'entrée.
        self.out_registers = list() # Registres de sortie.
        self.working_registers = dict() # Registres de travail.
        if len(self.RAM_input_list) > 0:
            self.in_registers = self.RAM_input_list
            self.in_registers.insert(0, len(self.RAM_input_list))

    def RAM_program_print(self):
        print("Flow d'instructions RAM :")
        if len(self.RAM_input_list) > 0:
            print(f"Entrées : {self.in_registers}")
        else:
            print("Pas d'entrées.")
        for i in range(len(self.RAM_instructions_list)):
            print(f"{i} : {self.RAM_instructions_list[i].str_instruc}")
        print("\nDétails des instructions RAM :")
        for instruc in self.RAM_instructions_list:
            print(f"Instruction : {instruc.str_instruc}")
            print(f"Type : {instruc.instruc_type}")
            print(f"Arguments : {instruc.instruc_args}")

    def acces_register(self, register_input):
        if register_input[0] == "r":
            return int(self.working_registers[register_input])
        elif register_input[0] == "i":
            return int(self.in_registers[int(register_input[1:])])
        elif register_input[0:2] == "@r":
            return int(self.working_registers[register_input[1:]])
        elif register_input[0:2] == "@i":
            return int(self.in_registers[int(register_input[2:])])
        else:
            return int(register_input)

    def RAM_program_execute(self, nb_of_cycles: int = 1):
        for _ in range(nb_of_cycles):
            if self.PC >= len(self.RAM_instructions_list):
                print("Fin du programme RAM.")
                break
            self.supported_operations[self.RAM_instructions_list[self.PC].instruc_type](self.RAM_instructions_list[self.PC])
            self.PC += 1
            for key, value in self.working_registers.items():
                print(f"Registre {key} : {value}")

    def ADD_instruction(self, RAM_instruction_arg: RAM_instruction):
        self.working_registers[RAM_instruction_arg.instruc_args[2]] = self.acces_register(RAM_instruction_arg.instruc_args[0]) + self.acces_register(RAM_instruction_arg.instruc_args[1])

    def SUB_instruction(self, RAM_instruction_arg: RAM_instruction):
        self.working_registers[RAM_instruction_arg.instruc_args[2]] = self.acces_register(RAM_instruction_arg.instruc_args[0]) - self.acces_register(RAM_instruction_arg.instruc_args[1])

    def MULT_instruction(self, RAM_instruction_arg: RAM_instruction):
        self.working_registers[RAM_instruction_arg.instruc_args[2]] = self.acces_register(RAM_instruction_arg.instruc_args[0]) * self.acces_register(RAM_instruction_arg.instruc_args[1])

    def DIV_instruction(self, RAM_instruction_arg: RAM_instruction):
        self.working_registers[RAM_instruction_arg.instruc_args[2]] = self.acces_register(RAM_instruction_arg.instruc_args[0]) / self.acces_register(RAM_instruction_arg.instruc_args[1])


RAM_program1 = RAM_program(RAM_instructions_list)
RAM_program1.RAM_program_execute(7)
#RAM_program1.RAM_program_print()
