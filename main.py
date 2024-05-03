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
            self.RAM_input_list = [RAM_instructions_list_arg[0]]
            self.RAM_instructions_list = [RAM_instruction(RAM_instruction_arg) for RAM_instruction_arg in RAM_instructions_list_arg[1:]]
        else:
            self.RAM_input_list = list()
            self.RAM_instructions_list = [RAM_instruction(RAM_instruction_arg) for RAM_instruction_arg in RAM_instructions_list_arg]
        self.PC = PC
        self.in_registers = list() # Registres d'entrée.
        self.out_registers = list() # Registres de sortie.
        self.working_registers = dict() # Registres de travail.

    def RAM_program_print(self):
        print("Flow d'instructions RAM :")
        if len(self.RAM_input_list) > 0:
            print(f"Entrées : {self.RAM_input_list}")
        else:
            print("Pas d'entrées.")
        for i in range(len(self.RAM_instructions_list)):
            print(f"{i} : {self.RAM_instructions_list[i].str_instruc}")
        print("\nDétails des instructions RAM :")
        for instruc in self.RAM_instructions_list:
            print(f"Instruction : {instruc.str_instruc}")
            print(f"Type : {instruc.instruc_type}")
            print(f"Arguments : {instruc.instruc_args}")

    def RAM_program_execute(self, nb_of_cycles: int = 1):
        if self.PC > len(self.RAM_instructions_list):
            print("PC hors des limites du programme.")
            return
        for _ in range(nb_of_cycles):
            self.supported_operations[self.RAM_instructions_list[self.PC].instruc_type](self.RAM_instructions_list[self.PC])
            self.PC += 1
            for key, value in self.working_registers.items():
                print(f"Registre {key} : {value}")

    def ADD_instruction(self, RAM_instruction_arg: RAM_instruction):
        buff = 0
        for arg in RAM_instruction_arg.instruc_args[0:2]:
            if arg[0] == "r":
                buff += self.working_registers[arg]
            else:
                buff += int(arg)
        self.working_registers[RAM_instruction_arg.instruc_args[2]] = buff

    def SUB_instruction(self, RAM_instruction_arg: RAM_instruction):
        buff = 0
        for arg in RAM_instruction_arg.instruc_args[0:2]:
            if arg[0] == "r":
                buff += self.working_registers[arg]
            else:
                buff -= int(arg)
        self.working_registers[RAM_instruction_arg.instruc_args[2]] = buff

    def MULT_instruction(self, RAM_instruction_arg: RAM_instruction):
        buff = 1
        for arg in RAM_instruction_arg.instruc_args[0:2]:
            if arg[0] == "r":
                buff *= self.working_registers[arg]
            else:
                buff *= int(arg)
        self.working_registers[RAM_instruction_arg.instruc_args[2]] = buff

    def DIV_instruction(self, RAM_instruction_arg: RAM_instruction):
        # Récupère la première valeur (dividende)
        if RAM_instruction_arg.instruc_args[0][0] == 'r':
            dividend = self.working_registers[RAM_instruction_arg.instruc_args[0]]
        else:
            dividend = int(RAM_instruction_arg.instruc_args[0])

        # Récupère la deuxième valeur (diviseur)
        if RAM_instruction_arg.instruc_args[1][0] == 'r':
            divisor = self.working_registers[RAM_instruction_arg.instruc_args[1]]
        else:
            divisor = int(RAM_instruction_arg.instruc_args[1])

        # Effectue la division et stocke le résultat dans le registre de destination
        if divisor != 0:  # Assurez-vous que le diviseur n'est pas zéro pour éviter une division par zéro
            self.working_registers[RAM_instruction_arg.instruc_args[2]] = dividend / divisor
        else:
            print("Erreur de division par zéro")


RAM_program1 = RAM_program(RAM_instructions_list)
RAM_program1.RAM_program_execute(4)
