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
        self.RAM_instructions_list = [RAM_instruction(RAM_instruction_arg) for RAM_instruction_arg in RAM_instructions_list_arg]
        self.PC = PC
    
    def RAM_program_print(self):
        print("Flow d'instructions RAM :")
        for i in range(len(self.RAM_instructions_list)):
            print(f"{i} : {self.RAM_instructions_list[i].str_instruc}")
        print("\nDétails des instructions RAM :")
        for instruc in self.RAM_instructions_list:
            print(f"Instruction : {instruc.str_instruc}")
            print(f"Type : {instruc.instruc_type}")
            print(f"Arguments : {instruc.instruc_args}")

RAM_program1 = RAM_program(RAM_instructions_list)
RAM_program1.RAM_program_print()
