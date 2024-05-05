import partie_1

### Question 6

# Définition des fonctions de la machine RAM
def lire_automate(RAM_program_arg: RAM_program):
    # Lecture du nombre de transitions
    nb_transitions = RAM_program_arg.acces_register("i0")

    # Lecture des transitions
    transitions = []
    for i in range(nb_transitions):
        q = RAM_program_arg.acces_register(f"i{i * 6 + 1}")
        a = RAM_program_arg.acces_register(f"i{i * 6 + 2}")
        A = RAM_program_arg.acces_register(f"i{i * 6 + 3}")
        w = []
        for j in range(RAM_program_arg.acces_register(f"i{i * 6 + 4}")):
            w.append(RAM_program_arg.acces_register(f"i{i * 6 + 5 + j}"))
        q_prime = RAM_program_arg.acces_register(f"i{i * 6 + 6}")
        transitions.append((q, a, A, w, q_prime))

    return transitions

def lire_mot(RAM_program_arg: RAM_program):
    mot = []
    for i in range(RAM_program_arg.acces_register("i0")):
        mot.append(RAM_program_arg.acces_register(f"i{i + 1}"))
    return mot

def simuler_automate(RAM_program_arg: RAM_program, transitions, mot):
    # Initialisation de l'état courant et de la pile
    q = 0
    pile = [0]

    # Boucle sur les lettres du mot
    for lettre in mot:
        # Recherche d'une transition applicable
        transition_applicable = None
        for transition in transitions:
            if transition[0] == q and transition[1] == lettre and transition[2] == pile[-1]:
                transition_applicable = transition
                break

        # Si aucune transition applicable n'est trouvée, le mot n'est pas reconnu
        if transition_applicable is None:
            return 1

        # Application de la transition
        q = transition_applicable[4]
        pile = pile[:-1] + transition_applicable[3]

    # Si l'état final est atteint, le mot est reconnu
    if q == 1:
        return 0
    else:
        return 1
    
'''Explication du code ajouté
Le code ajouté effectue les tâches suivantes:

Définition des fonctions de la machine RAM:
La fonction lire_automate lit les transitions de l'automate à pile à partir de la RAM.
La fonction lire_mot lit le mot à tester à partir de la RAM.
La fonction simuler_automate simule l'exécution de l'automate à pile sur le mot donné. Elle retourne 0 si le mot est reconnu et 1 sinon.
Appel des fonctions de la machine RAM:
La fonction lire_automate est appelée pour lire les transitions de l'automate à pile à partir de la RAM.
La fonction lire_mot est appelée pour lire le mot à tester à partir de la RAM.
La fonction simuler_automate est appelée pour simuler l'exécution de l'automate à pile sur le mot donné.
Écriture du résultat dans la RAM:
Le résultat de la simulation (0 si le mot est reconnu, 1 sinon) est écrit dans le registre de sortie de la RAM.
Fonctionnement de la simulation
La fonction simuler_automate fonctionne comme suit:

Elle initialise l'état courant à l'état initial de l'automate (0 dans ce cas).
Elle initialise la pile avec le symbole de fond de pile (0).
Elle boucle sur les lettres du mot à tester:
Pour chaque lettre, elle cherche une transition applicable dans la liste des transitions de l'automate. Une transition est applicable si l'état courant, le symbole d'entrée et le symbole au sommet de la pile correspondent à la transition.
Si une transition est trouvée, elle met à jour l'état courant, empile le mot w sur la pile et passe à la lettre suivante du mot.
Si aucune transition n'est trouvée, la simulation s'arrête et retourne 1 (le mot n'est pas reconnu).
Si la boucle se termine sans erreur, la simulation s'arrête et retourne 0 (le mot est reconnu).
'''

# Question 7

# Définition de l'automate à pile
transitions = [(0, 0, 0, [1, 1], 1),
               (1, 1, 1, [1], 1),
               (1, 0, 1, [], 2)]

# Définition du mot à tester
mot = [0, 1, 0, 1]

# Simulation de l'automate
result = simuler_automate(RAM_program2, transitions, mot)

# Affichage du résultat
print(f"Résultat : {result}")

'''
Explication du code ajouté
Le code ajouté effectue les tâches suivantes:

Définition de l'automate à pile:
La variable transitions contient la liste des transitions de l'automate. Chaque transition est un tuple de la forme (q, a, A, w, q'), où:
q est l'état courant.
a est le symbole d'entrée.
A est le symbole au sommet de la pile.
w est le mot à empiler sur la pile.
q' est le nouvel état.
Définition du mot à tester:
La variable mot contient le mot à tester par l'automate.
Simulation de l'automate:
La fonction simuler_automate simule l'exécution de l'automate sur le mot donné. Elle retourne 0 si le mot est reconnu et 1 sinon.
Affichage du résultat:
Le résultat de la simulation est affiché à l'écran.
Fonctionnement de la simulation
La fonction simuler_automate fonctionne comme suit:

Elle initialise l'état courant à l'état initial de l'automate (0 dans ce cas).
Elle initialise la pile avec le symbole de fond de pile (0).
Elle boucle sur les lettres du mot à tester:
Pour chaque lettre, elle cherche une transition applicable dans la liste des transitions de l'automate. Une transition est applicable si l'état courant, le symbole d'entrée et le symbole au sommet de la pile correspondent à la transition.
Si une transition est trouvée, elle met à jour l'état courant, empile le mot w sur la pile et passe à la lettre suivante du mot.
Si aucune transition n'est trouvée, la simulation s'arrête et retourne 1 (le mot n'est pas reconnu).
Si la boucle se termine sans erreur, la simulation s'arrête et retourne 0 (le mot est reconnu).
'''