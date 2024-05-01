import argparse # Pour récupérer le chemin du fichier avec les instructions RAM.

# Question 1

# Récupération du chemin du fichier en argument.
RAM_instructions = list() # Pour stocker chaque instruction RAM.
parser = argparse.ArgumentParser(description='Lire un fichier contenant des instructions RAM.')
parser.add_argument("filepath", help="Chemin du fichier à traiter", type=str)
args = parser.parse_args()
filepath = args.filepath
print(f"Traitement du fichier : {filepath}")

# Extraction des instructions RAM.
for line in open(filepath, 'r'):
    RAM_instructions.append(line.strip())
print(RAM_instructions)
