import partie_1
#Question 8

def create_graph(self):
    """Crée un graphe orienté représentant le code de la RAM."""

    graph = {}  # Le graphe est représenté par un dictionnaire
    for i, instruction in enumerate(self.RAM_instructions_list):
        graph[i] = []  # Chaque instruction est un sommet du graphe
        if instruction.instruc_type in ("ADD", "SUB", "MUL", "DIV", "JUMP"):
            graph[i].append(i + 1)  # Les instructions arithmétiques et JUMP ont un degré sortant de 1
        elif instruction.instruc_type == "JE":
            graph[i].append(i + 1)  # La première branche du JE a un degré sortant de 1
            graph[i].append(self.acces_register(instruction.instruc_args[2]))  # La deuxième branche a un degré sortant de 1
        elif instruction.instruc_type == "JL":
            graph[i].append(i + 1)  # La première branche du JL a un degré sortant de 1
            graph[i].append(self.acces_register(instruction.instruc_args[2]))  # La deuxième branche a un degré sortant de 1

    return graph

# Test
RAM_program1 = RAM_program(RAM_instructions_list)
graph = RAM_program1.create_graph()
print(graph)

# Question 9

def remove_unreachable_code(self):
        """Supprime le code mort du programme."""

        graph = self.create_graph()

        # Effectuer une recherche en profondeur à partir de la première instruction
        visited = set()
        stack = [0]
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                stack.extend(graph[node])

        # Supprimer les instructions non visitées
        self.RAM_instructions_list = [
            instruction
            for i, instruction in enumerate(self.RAM_instructions_list)
            if i in visited
        ]

        # Mettre à jour le PC
        if self.PC not in visited:
            self.PC = 0
# Question 10 : (Bonus) Proposer une m ́ethode pour combiner plusieurs instructions en une seule. Par
# exemple, les deux instructions cons ́ecutives ADD(4,0,r1), ADD(r1,9,r1) peuvent ˆetre remplac ́ees par
# ADD(13,0,r1), si dans le graphe le sommet ADD(r1,9,r1) n’a comme pr ́ed ́ecesseur que ADD(4,0,r1).

def combine_instructions(self):
    """Combine les instructions consécutives du même type."""

    combined_instructions = []
    i = 0
    while i < len(self.RAM_instructions_list):
        current_instruction = self.RAM_instructions_list[i]
        combined_instruction = current_instruction

        # Combiner les instructions ADD consécutives
        if current_instruction.instruc_type == "ADD":
            while (
                i + 1 < len(self.RAM_instructions_list)
                and self.RAM_instructions_list[i + 1].instruc_type == "ADD"
                and self.RAM_instructions_list[i + 1].instruc_args[0]
                == combined_instruction.instruc_args[2]
            ):
                combined_instruction.instruc_args[1] = self.RAM_instructions_list[
                    i + 1
                ].instruc_args[1]
                i += 1

        # Combiner les instructions SUB consécutives
        elif current_instruction.instruc_type == "SUB":
            while (
                i + 1 < len(self.RAM_instructions_list)
                and self.RAM_instructions_list[i + 1].instruc_type == "SUB"
                and self.RAM_instructions_list[i + 1].instruc_args[0]
                == combined_instruction.instruc_args[2]
            ):
                combined_instruction.instruc_args[1] = self.RAM_instructions_list[
                    i + 1
                ].instruc_args[1]
                i += 1

        # Combiner les instructions MUL consécutives
        elif current_instruction.instruc_type == "MUL":
            while (
                i + 1 < len(self.RAM_instructions_list)
                and self.RAM_instructions_list[i + 1].instruc_type == "MUL"
                and self.RAM_instructions_list[i + 1].instruc_args[0]
                == combined_instruction.instruc_args[2]
            ):
                combined_instruction.instruc_args[1] = self.RAM_instructions_list[
                    i + 1
                ].instruc_args[1]
                i += 1

        # Combiner les instructions DIV consécutives
        elif current_instruction.instruc_type == "DIV":
            while (
                i + 1 < len(self.RAM_instructions_list)
                and self.RAM_instructions_list[i + 1].instruc_type == "DIV"
                and self.RAM_instructions_list[i + 1].instruc_args[0]
                == combined_instruction.instruc_args[2]
            ):
                combined_instruction.instruc_args[1] = self.RAM_instructions_list[
                    i + 1
                ].instruc_args[1]
                i += 1

        combined_instructions.append(combined_instruction)
        i += 1

    self.RAM_instructions_list = combined_instructions

def optimize_program(self):
    """Optimise le programme RAM en supprimant le code mort et en combinant les instructions."""

    self.remove_unreachable_code()
    self.combine_instructions()


import tkinter as tk

def draw_graph(graph, canvas):
    position = {}
    step_x = 400 // (len(graph) + 1)
    current_x = step_x
    current_y = 200  # Centre vertical du canvas

    # Dessiner les nœuds
    for node in graph:
        position[node] = (current_x, current_y)
        canvas.create_oval(current_x - 20, current_y - 20, current_x + 20, current_y + 20, fill='skyblue')
        canvas.create_text(current_x, current_y, text=str(node))
        current_x += step_x  # Déplacement horizontal

    # Dessiner les arêtes
    for node in graph:
        for dest in graph[node]:
            start_x, start_y = position[node]
            end_x, end_y = position[dest]
            canvas.create_line(start_x, start_y, end_x, end_y, arrow=tk.LAST)
def setup_and_run():
    root = tk.Tk()
    root.title("Visualisation du Graphe de la RAM")
    canvas = tk.Canvas(root, height=400, width=400, bg='white')
    canvas.pack()

    # Utiliser une instance et une méthode pour créer le graphe (supposant que RAM_program1 est déjà définie)
    graph = RAM_program1.create_graph()
    draw_graph(graph, canvas)

    root.mainloop()

setup_and_run()